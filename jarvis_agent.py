import speech_recognition as sr
import pyttsx3
import openai
import os
import time
import logging
from dotenv import load_dotenv
import json
import sys

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('jarvis.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

class JarvisAgent:
    def __init__(self):
        # Load environment variables
        load_dotenv()
        
        # Initialize OpenAI client
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key or api_key == 'your_openai_api_key_here':
            raise ValueError("OpenAI API key not found. Please set OPENAI_API_KEY in your .env file")
        
        self.client = openai.OpenAI(api_key=api_key)
        
        # Initialize speech recognition
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # Adjust recognition settings for better accuracy
        self.recognizer.energy_threshold = 4000
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.pause_threshold = 0.8
        
        # Initialize text-to-speech engine
        self.tts_engine = pyttsx3.init()
        self.tts_engine.setProperty('rate', 150)
        self.tts_engine.setProperty('volume', 0.9)
        
        # Get available voices and set a good one
        voices = self.tts_engine.getProperty('voices')
        if voices:
            # Prefer a male voice if available
            for voice in voices:
                if 'male' in voice.name.lower() or 'david' in voice.name.lower():
                    self.tts_engine.setProperty('voice', voice.id)
                    break
            else:
                self.tts_engine.setProperty('voice', voices[0].id)
        
        # System prompt for the AI
        self.system_prompt = """You are Jarvis, a helpful AI assistant that provides practical advice and feedback for everyday situations. 
        When someone asks you a question or describes a situation, provide:
        1. Clear, actionable advice
        2. Relevant information or context
        3. Encouraging and supportive feedback
        4. Practical steps they can take
        
        Keep responses concise but helpful (2-3 sentences). Be friendly, wise, and practical in your guidance.
        If someone asks for specific information, provide accurate and helpful answers."""
        
        # Conversation history for context
        self.conversation_history = []
        
        logging.info("Jarvis AI Agent initialized successfully")
        print("🤖 Jarvis AI Agent initialized and ready!")
        print("💡 Say 'Hey Jarvis' to activate, or just speak your question/situation.")
        print("🔴 Say 'Goodbye' to exit.")
        print("=" * 50)
    
    def speak(self, text):
        """Convert text to speech"""
        try:
            print(f"🤖 Jarvis: {text}")
            logging.info(f"Speaking: {text}")
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
        except Exception as e:
            logging.error(f"Error in text-to-speech: {e}")
            print(f"🤖 Jarvis: {text}")
    
    def listen(self):
        """Listen for voice input with improved error handling"""
        try:
            with self.microphone as source:
                print("🎤 Listening...")
                logging.info("Listening for voice input")
                
                # Adjust for ambient noise
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                
                # Listen with timeout and phrase time limit
                audio = self.recognizer.listen(
                    source, 
                    timeout=5, 
                    phrase_time_limit=15,
                    snowboy_configuration=None
                )
            
            print("🔄 Processing speech...")
            text = self.recognizer.recognize_google(audio)
            print(f"👤 You said: {text}")
            logging.info(f"Recognized speech: {text}")
            return text.lower()
        
        except sr.WaitTimeoutError:
            print("⏰ No speech detected within timeout")
            logging.info("No speech detected - timeout")
            return None
        except sr.UnknownValueError:
            print("❓ Could not understand audio")
            logging.info("Speech not understood")
            return None
        except sr.RequestError as e:
            print(f"🌐 Could not request results; {e}")
            logging.error(f"Speech recognition request error: {e}")
            return None
        except Exception as e:
            print(f"❌ Error in speech recognition: {e}")
            logging.error(f"Speech recognition error: {e}")
            return None
    
    def get_ai_response(self, user_input):
        """Get response from ChatGPT with conversation history"""
        try:
            # Add user input to conversation history
            self.conversation_history.append({"role": "user", "content": user_input})
            
            # Keep only last 10 messages to avoid token limits
            if len(self.conversation_history) > 10:
                self.conversation_history = self.conversation_history[-10:]
            
            # Prepare messages for API call
            messages = [{"role": "system", "content": self.system_prompt}] + self.conversation_history
            
            logging.info(f"Requesting AI response for: {user_input}")
            
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=200,
                temperature=0.7
            )
            
            ai_response = response.choices[0].message.content
            
            # Add AI response to conversation history
            self.conversation_history.append({"role": "assistant", "content": ai_response})
            
            logging.info(f"AI response: {ai_response}")
            return ai_response
            
        except openai.RateLimitError:
            error_msg = "I'm getting too many requests right now. Please wait a moment and try again."
            logging.error("OpenAI rate limit exceeded")
            return error_msg
        except openai.AuthenticationError:
            error_msg = "There's an issue with my authentication. Please check your API key."
            logging.error("OpenAI authentication error")
            return error_msg
        except Exception as e:
            error_msg = f"I'm sorry, I'm having trouble processing your request right now. Error: {str(e)}"
            logging.error(f"OpenAI API error: {e}")
            return error_msg
    
    def handle_command(self, user_input):
        """Handle special commands"""
        if any(word in user_input for word in ['goodbye', 'exit', 'quit', 'stop', 'bye', 'end']):
            return "EXIT"
        elif any(word in user_input for word in ['clear', 'reset', 'start over']):
            self.conversation_history = []
            return "Conversation history cleared. How can I help you?"
        elif any(word in user_input for word in ['help', 'what can you do', 'commands']):
            return "I can help you with advice, answer questions, and provide guidance for everyday situations. Just tell me what's on your mind or ask me anything!"
        return None
    
    def run(self):
        """Main loop for the Jarvis agent with improved error handling"""
        try:
            self.speak("Hello! I'm Jarvis, your AI assistant. How can I help you today?")
            
            while True:
                try:
                    # Listen for voice input
                    user_input = self.listen()
                    
                    if user_input is None:
                        continue
                    
                    # Handle special commands
                    command_result = self.handle_command(user_input)
                    if command_result == "EXIT":
                        self.speak("Goodbye! Have a great day!")
                        logging.info("User requested exit")
                        break
                    elif command_result:
                        self.speak(command_result)
                        continue
                    
                    # Check for wake word (optional)
                    if 'hey jarvis' in user_input or 'jarvis' in user_input:
                        # Remove wake word from input
                        user_input = user_input.replace('hey jarvis', '').replace('jarvis', '').strip()
                        if not user_input:
                            self.speak("Yes, I'm listening. How can I help you?")
                            continue
                    
                    # Get AI response
                    response = self.get_ai_response(user_input)
                    
                    # Speak the response
                    self.speak(response)
                    
                    # Small pause before listening again
                    time.sleep(1)
                    
                except KeyboardInterrupt:
                    print("\n🛑 Shutting down Jarvis...")
                    self.speak("Goodbye!")
                    logging.info("Keyboard interrupt - shutting down")
                    break
                except Exception as e:
                    logging.error(f"Error in main loop: {e}")
                    print(f"❌ Error: {e}")
                    self.speak("I encountered an error. Please try again.")
                    time.sleep(2)
                    
        except Exception as e:
            logging.error(f"Critical error in Jarvis: {e}")
            print(f"❌ Critical error: {e}")
            print("Please check your setup and try again.")

def main():
    """Main function to run the Jarvis agent"""
    print("🚀 Starting Jarvis Voice AI Agent...")
    logging.info("Starting Jarvis Voice AI Agent")
    
    try:
        # Check if OpenAI API key is set
        load_dotenv()
        if not os.getenv('OPENAI_API_KEY') or os.getenv('OPENAI_API_KEY') == 'your_openai_api_key_here':
            print("❌ Error: OPENAI_API_KEY not found or not configured.")
            print("Please create a .env file with your OpenAI API key:")
            print("OPENAI_API_KEY=your_api_key_here")
            print("\nGet your API key from: https://platform.openai.com/api-keys")
            return
        
        # Create and run the agent
        jarvis = JarvisAgent()
        jarvis.run()
        
    except Exception as e:
        logging.error(f"Failed to start Jarvis: {e}")
        print(f"❌ Failed to start Jarvis: {e}")
        print("Please check your setup and try again.")

if __name__ == "__main__":
    main() 