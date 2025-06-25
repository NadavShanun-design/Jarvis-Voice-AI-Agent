#!/usr/bin/env python3
"""
Setup script for Jarvis Voice AI Agent
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ All packages installed successfully!")
    except subprocess.CalledProcessError:
        print("❌ Error installing packages. Please try running: pip install -r requirements.txt")
        return False
    return True

def check_api_key():
    """Check if OpenAI API key is configured"""
    if os.path.exists('.env'):
        with open('.env', 'r') as f:
            content = f.read()
            if 'OPENAI_API_KEY=' in content and 'your_openai_api_key_here' not in content:
                print("✅ OpenAI API key found in .env file")
                return True
    
    print("⚠️  OpenAI API key not configured")
    print("Please create a .env file with your OpenAI API key:")
    print("1. Copy env_example.txt to .env")
    print("2. Replace 'your_openai_api_key_here' with your actual API key")
    print("3. Get your API key from: https://platform.openai.com/api-keys")
    return False

def main():
    """Main setup function"""
    print("🚀 Setting up Jarvis Voice AI Agent...")
    print("=" * 50)
    
    # Install requirements
    if not install_requirements():
        return
    
    print("\n" + "=" * 50)
    
    # Check API key
    check_api_key()
    
    print("\n" + "=" * 50)
    print("🎉 Setup complete!")
    print("\nTo run Jarvis:")
    print("python jarvis_agent.py")
    print("\nMake sure to configure your OpenAI API key first!")

if __name__ == "__main__":
    main() 