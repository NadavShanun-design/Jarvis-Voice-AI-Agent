#!/usr/bin/env python3
"""
Test script for Jarvis Voice AI Agent
Verifies that all components are working correctly
"""

import sys
import os
import subprocess

def test_imports():
    """Test if all required packages can be imported"""
    print("Testing package imports...")
    
    packages = [
        ('openai', 'OpenAI API client'),
        ('speech_recognition', 'Speech recognition'),
        ('pyttsx3', 'Text-to-speech'),
        ('pyaudio', 'Audio processing'),
        ('dotenv', 'Environment variables'),
        ('numpy', 'Numerical computing')
    ]
    
    failed_imports = []
    
    for package, description in packages:
        try:
            __import__(package)
            print(f"✅ {package} - {description}")
        except ImportError as e:
            print(f"❌ {package} - {description}: {e}")
            failed_imports.append(package)
    
    return len(failed_imports) == 0

def test_openai_api():
    """Test OpenAI API connection"""
    print("\nTesting OpenAI API...")
    
    try:
        from dotenv import load_dotenv
        load_dotenv()
        
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key or api_key == 'your_openai_api_key_here':
            print("❌ OpenAI API key not configured")
            print("Please set your API key in the .env file")
            return False
        
        import openai
        client = openai.OpenAI(api_key=api_key)
        
        # Test with a simple request
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Hello"}],
            max_tokens=10
        )
        
        print("✅ OpenAI API connection successful")
        return True
        
    except Exception as e:
        print(f"❌ OpenAI API test failed: {e}")
        return False

def test_microphone():
    """Test microphone access"""
    print("\nTesting microphone...")
    
    try:
        import speech_recognition as sr
        
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
        
        print("✅ Microphone access successful")
        return True
        
    except Exception as e:
        print(f"❌ Microphone test failed: {e}")
        return False

def test_text_to_speech():
    """Test text-to-speech functionality"""
    print("\nTesting text-to-speech...")
    
    try:
        import pyttsx3
        
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        
        if voices:
            print(f"✅ Text-to-speech initialized with {len(voices)} voice(s)")
            return True
        else:
            print("⚠️  No voices found for text-to-speech")
            return False
            
    except Exception as e:
        print(f"❌ Text-to-speech test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Testing Jarvis Voice AI Agent Setup")
    print("=" * 50)
    
    tests = [
        ("Package Imports", test_imports),
        ("OpenAI API", test_openai_api),
        ("Microphone", test_microphone),
        ("Text-to-Speech", test_text_to_speech)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} test crashed: {e}")
            results.append((test_name, False))
    
    print("\n" + "=" * 50)
    print("📊 Test Results Summary:")
    
    passed = 0
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\nOverall: {passed}/{len(results)} tests passed")
    
    if passed == len(results):
        print("🎉 All tests passed! Jarvis is ready to use.")
        print("Run 'python jarvis_agent.py' to start Jarvis.")
    else:
        print("⚠️  Some tests failed. Please check the issues above.")
        print("Refer to the README.md for troubleshooting tips.")

if __name__ == "__main__":
    main() 