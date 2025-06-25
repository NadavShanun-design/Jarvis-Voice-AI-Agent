"""
Configuration file for Jarvis Voice AI Agent
Customize these settings to personalize your Jarvis experience
"""

# Voice Settings
VOICE_RATE = 150  # Speed of speech (words per minute)
VOICE_VOLUME = 0.9  # Volume level (0.0 to 1.0)
PREFER_MALE_VOICE = True  # Try to use a male voice if available

# Speech Recognition Settings
ENERGY_THRESHOLD = 4000  # Minimum audio energy to consider as speech
DYNAMIC_ENERGY_THRESHOLD = True  # Automatically adjust energy threshold
PAUSE_THRESHOLD = 0.8  # Seconds of silence to mark end of speech
LISTEN_TIMEOUT = 5  # Seconds to wait for speech to start
PHRASE_TIME_LIMIT = 15  # Maximum seconds for a single phrase

# AI Settings
AI_MODEL = "gpt-3.5-turbo"  # OpenAI model to use
MAX_TOKENS = 200  # Maximum response length
TEMPERATURE = 0.7  # Response creativity (0.0 to 1.0)
MAX_CONVERSATION_HISTORY = 10  # Number of messages to keep in context

# System Prompt Customization
SYSTEM_PROMPT = """You are Jarvis, a helpful AI assistant that provides practical advice and feedback for everyday situations. 
When someone asks you a question or describes a situation, provide:
1. Clear, actionable advice
2. Relevant information or context
3. Encouraging and supportive feedback
4. Practical steps they can take

Keep responses concise but helpful (2-3 sentences). Be friendly, wise, and practical in your guidance.
If someone asks for specific information, provide accurate and helpful answers."""

# Wake Words (optional - set to None to disable)
WAKE_WORDS = ["hey jarvis", "jarvis"]

# Exit Commands
EXIT_COMMANDS = ["goodbye", "exit", "quit", "stop", "bye", "end"]

# Special Commands
CLEAR_COMMANDS = ["clear", "reset", "start over"]
HELP_COMMANDS = ["help", "what can you do", "commands"]

# Logging Settings
LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_FILE = "jarvis.log"

# UI Settings
SHOW_EMOJIS = True  # Display emojis in console output
SHOW_TIMESTAMPS = True  # Show timestamps in logs 