#!/usr/bin/env python3
"""
Smart Launcher for Jarvis Voice AI Agent
Automatically detects the best available mode and launches Jarvis
"""

import sys
import os
import subprocess

def check_voice_capabilities():
    """Check if voice mode is available"""
    try:
        import speech_recognition as sr
        import pyttsx3
        
        # Test microphone access
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.1)
        
        # Test text-to-speech
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        
        return True, "Voice mode available"
        
    except ImportError as e:
        return False, f"Missing voice dependencies: {e}"
    except Exception as e:
        return False, f"Voice mode not available: {e}"

def check_openai_api():
    """Check if OpenAI API is configured"""
    try:
        from dotenv import load_dotenv
        load_dotenv()
        
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key or api_key == 'your_openai_api_key_here':
            return False, "OpenAI API key not configured"
        
        return True, "OpenAI API configured"
        
    except Exception as e:
        return False, f"Error checking API: {e}"

def main():
    """Main launcher function"""
    print("🚀 Jarvis AI Agent Launcher")
    print("=" * 40)
    
    # Check OpenAI API
    api_ok, api_msg = check_openai_api()
    print(f"🔑 OpenAI API: {'✅' if api_ok else '❌'} {api_msg}")
    
    if not api_ok:
        print("\n❌ Cannot launch Jarvis without OpenAI API key.")
        print("Please configure your API key in the .env file.")
        print("See INSTALLATION.md for instructions.")
        return
    
    # Check voice capabilities
    voice_ok, voice_msg = check_voice_capabilities()
    print(f"🎤 Voice Mode: {'✅' if voice_ok else '❌'} {voice_msg}")
    
    print("\n" + "=" * 40)
    
    if voice_ok:
        print("🎉 Launching Jarvis in VOICE mode!")
        print("💡 You can speak to Jarvis naturally.")
        print("🔴 Say 'goodbye' to exit.")
        print("\nStarting...")
        
        try:
            subprocess.run([sys.executable, "jarvis_agent.py"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"❌ Error launching voice mode: {e}")
            print("Falling back to text mode...")
            launch_text_mode()
        except KeyboardInterrupt:
            print("\n👋 Jarvis stopped by user.")
    else:
        print("📝 Launching Jarvis in TEXT mode!")
        print("💡 Type your questions to Jarvis.")
        print("🔴 Type 'goodbye' to exit.")
        print("\nStarting...")
        launch_text_mode()

def launch_text_mode():
    """Launch Jarvis in text mode"""
    try:
        subprocess.run([sys.executable, "jarvis_text_mode.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error launching text mode: {e}")
        print("Please check your setup and try again.")
    except KeyboardInterrupt:
        print("\n👋 Jarvis stopped by user.")

if __name__ == "__main__":
    main() 