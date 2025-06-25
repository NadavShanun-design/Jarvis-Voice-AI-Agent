# Jarvis Voice AI Agent 🤖

A conversational AI assistant that understands voice commands and provides helpful feedback for everyday situations. Think of it as your personal AI companion that gives you practical advice, answers questions, and helps you navigate life's challenges.

## 🌟 Features

- **Voice Recognition**: Speak naturally to interact with Jarvis
- **Text Mode**: Type your questions if voice isn't available
- **AI-Powered Responses**: Uses OpenAI's ChatGPT for intelligent, contextual responses
- **Text-to-Speech**: Jarvis speaks back to you with clear, natural-sounding voice
- **Practical Advice**: Get helpful feedback for real-life situations
- **Question Answering**: Ask anything and get informative responses
- **Easy to Use**: Simple voice commands, no complex setup required

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- OpenAI API key
- Microphone and speakers (for voice mode)
- Internet connection

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Jarvis-Voice-AI-Agent
   ```

2. **Run the setup script**
   ```bash
   python setup.py
   ```

3. **Configure your OpenAI API key**
   - Copy `env_example.txt` to `.env`
   - Replace `your_openai_api_key_here` with your actual OpenAI API key
   - Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys)

4. **Test your setup**
   ```bash
   python test_setup.py
   ```

5. **Run Jarvis**
   ```bash
   # Voice mode (full experience)
   python jarvis_agent.py
   
   # Text mode (if audio issues)
   python jarvis_text_mode.py
   
   # Demo mode (see examples)
   python demo.py
   ```

## 🎯 How to Use

### Voice Mode
- **Start a conversation**: Say "Hey Jarvis" or just speak your question
- **Ask for advice**: Describe a situation and get helpful feedback
- **Ask questions**: Get answers to any question you have
- **Exit**: Say "Goodbye", "Exit", or "Stop"

### Text Mode
- **Type your questions**: Simply type what you want to ask
- **Get instant responses**: Jarvis responds with helpful advice
- **Same functionality**: All features work except voice input/output

### Example Interactions

**You**: "I'm feeling stressed about my upcoming presentation"
**Jarvis**: "I understand that feeling. Here are some practical steps to help: First, practice your presentation out loud several times. Break it down into smaller sections and focus on one at a time. Remember to breathe deeply and visualize success. You've got this!"

**You**: "What should I do if I'm running late for an important meeting?"
**Jarvis**: "When running late for an important meeting, immediately contact the meeting organizer to let them know. Provide an estimated arrival time and apologize for the inconvenience. Consider if you can join remotely while traveling. For future meetings, set multiple alarms and plan to arrive 10-15 minutes early."

## 🛠️ Technical Details

### Architecture

- **Voice Recognition**: Uses Google's Speech Recognition API via `speech_recognition`
- **AI Processing**: OpenAI's GPT-3.5-turbo for intelligent responses
- **Text-to-Speech**: `pyttsx3` for natural voice output
- **Audio Processing**: `pyaudio` for microphone input (voice mode only)

### Key Components

- `jarvis_agent.py`: Main voice-enabled application
- `jarvis_text_mode.py`: Text-based version (no microphone required)
- `demo.py`: Demo script showing Jarvis capabilities
- `requirements.txt`: Python dependencies
- `setup.py`: Automated setup and configuration script
- `test_setup.py`: Verifies all components are working
- `config.py`: Customizable settings
- `env_example.txt`: Template for environment variables

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_actual_api_key_here
```

### Customizing Jarvis

You can modify the system prompt in `jarvis_agent.py` or `jarvis_text_mode.py` to change Jarvis's personality or response style:

```python
self.system_prompt = """Your custom prompt here..."""
```

Or edit `config.py` for other settings.

## 📋 Requirements

- Python 3.7+
- OpenAI API key
- Microphone (for voice mode)
- Speakers or headphones (for voice mode)
- Internet connection

## 🐛 Troubleshooting

### Common Issues

1. **"No module named 'pyaudio'"**
   - **Windows**: `pip install pipwin` then `pipwin install pyaudio`
   - **macOS**: `brew install portaudio` then `pip install pyaudio`
   - **Linux**: `sudo apt-get install python3-pyaudio`
   - **Alternative**: Use text mode: `python jarvis_text_mode.py`

2. **"OpenAI API key not configured"**
   - Verify your API key is correct in the `.env` file
   - Check your OpenAI account has sufficient credits
   - Ensure you have access to GPT-3.5-turbo

3. **"Microphone not working"**
   - Check your system's microphone permissions
   - Ensure microphone is set as default input device
   - Try running with administrator privileges
   - Use text mode as alternative: `python jarvis_text_mode.py`

4. **"Could not understand audio"**
   - Speak clearly and at a normal pace
   - Minimize background noise
   - Keep the microphone close to your mouth
   - Use headphones for better audio quality

### Performance Tips

- Speak clearly and at a normal pace
- Minimize background noise
- Keep the microphone close to your mouth
- Use headphones for better audio quality
- If voice recognition fails, try text mode

## 🎮 Running Options

### Windows Users
- Double-click `run_jarvis.bat` for easy launching
- Or run `run_jarvis.ps1` in PowerShell

### All Platforms
```bash
# Voice mode (requires microphone)
python jarvis_agent.py

# Text mode (no microphone needed)
python jarvis_text_mode.py

# Demo mode (see examples)
python demo.py

# Test setup
python test_setup.py
```

## 📖 Documentation

- **[Installation Guide](INSTALLATION.md)**: Detailed setup instructions
- **[Configuration](config.py)**: Customizable settings
- **[Troubleshooting](README.md#troubleshooting)**: Common issues and solutions

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- OpenAI for providing the ChatGPT API
- Google for Speech Recognition services
- The open-source community for the various Python libraries used

---


