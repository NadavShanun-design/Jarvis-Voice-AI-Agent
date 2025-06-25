#!/usr/bin/env python3
"""
Demo script for Jarvis Voice AI Agent
This script demonstrates Jarvis capabilities without requiring voice input
"""

import os
import sys
from dotenv import load_dotenv
import openai

def demo_jarvis_responses():
    """Demonstrate Jarvis responses to common scenarios"""
    
    # Load environment variables
    load_dotenv()
    
    # Check API key
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key or api_key == 'your_openai_api_key_here':
        print("❌ Error: OpenAI API key not configured.")
        print("Please set your API key in the .env file first.")
        return
    
    # Initialize OpenAI client
    client = openai.OpenAI(api_key=api_key)
    
    # System prompt
    system_prompt = """You are Jarvis, a helpful AI assistant that provides practical advice and feedback for everyday situations. 
    When someone asks you a question or describes a situation, provide:
    1. Clear, actionable advice
    2. Relevant information or context
    3. Encouraging and supportive feedback
    4. Practical steps they can take
    
    Keep responses concise but helpful (2-3 sentences). Be friendly, wise, and practical in your guidance.
    If someone asks for specific information, provide accurate and helpful answers."""
    
    # Demo scenarios
    scenarios = [
        "I'm feeling overwhelmed with work and don't know where to start",
        "I have a job interview tomorrow and I'm really nervous",
        "My friend is going through a tough time. How can I help?",
        "I want to start exercising but I don't have much time",
        "I'm having trouble sleeping lately",
        "What should I do if I'm running late for an important meeting?",
        "I'm trying to save money but I keep spending too much",
        "How can I improve my public speaking skills?",
        "I'm feeling lonely and don't know how to make new friends",
        "What's the best way to handle a difficult conversation with a coworker?"
    ]
    
    print("🤖 Jarvis Voice AI Agent - Demo Mode")
    print("=" * 50)
    print("This demo shows how Jarvis would respond to common situations.")
    print("In the full version, you can speak these questions to Jarvis!\n")
    
    for i, scenario in enumerate(scenarios, 1):
        print(f"📝 Scenario {i}: {scenario}")
        print("-" * 40)
        
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": scenario}
                ],
                max_tokens=200,
                temperature=0.7
            )
            
            jarvis_response = response.choices[0].message.content
            print(f"🤖 Jarvis: {jarvis_response}")
            
        except Exception as e:
            print(f"❌ Error getting response: {e}")
        
        print("\n" + "=" * 50 + "\n")
    
    print("🎉 Demo complete!")
    print("To use Jarvis with voice commands, run: python jarvis_agent.py")

def main():
    """Main demo function"""
    print("🚀 Starting Jarvis Demo...")
    demo_jarvis_responses()

if __name__ == "__main__":
    main() 