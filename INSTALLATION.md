# Installation Guide for Jarvis Voice AI Agent

This guide will help you set up Jarvis Voice AI Agent on your system.

## Prerequisites

- Python 3.7 or higher
- OpenAI API key
- Microphone and speakers (for voice mode)
- Internet connection

## Step 1: Install Python

### Windows
1. Download Python from [python.org](https://www.python.org/downloads/)
2. During installation, make sure to check "Add Python to PATH"
3. Verify installation: `python --version`

### macOS
```bash
# Using Homebrew
brew install python

# Or download from python.org
```

### Linux
```bash
sudo apt update
sudo apt install python3 python3-pip
```

## Step 2: Clone or Download the Project

```bash
git clone <repository-url>
cd Jarvis-Voice-AI-Agent
```

Or download and extract the ZIP file.

## Step 3: Install Dependencies

### Automatic Installation (Recommended)
```bash
python setup.py
```

### Manual Installation
```bash
pip install -r requirements.txt
```

### Windows Users - Audio Dependencies
If you encounter issues with PyAudio on Windows:

1. **Option 1: Use pipwin**
   ```bash
   pip install pipwin
   pipwin install pyaudio
   ```

2. **Option 2: Download from Unofficial Binaries**
   - Go to [Unofficial Windows Binaries for Python](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
   - Download the appropriate version for your Python
   - Install with: `pip install PyAudio-0.2.11-cp312-cp312-win_amd64.whl`

3. **Option 3: Use Text Mode**
   - If audio setup fails, use the text-based version: `python jarvis_text_mode.py`

## Step 4: Get OpenAI API Key

1. Go to [OpenAI Platform](https://platform.openai.com/api-keys)
2. Sign up or log in
3. Create a new API key
4. Copy the key (it starts with `sk-`)

## Step 5: Configure API Key

1. Copy the example environment file:
   ```bash
   # Windows
   copy env_example.txt .env
   
   # macOS/Linux
   cp env_example.txt .env
   ```

2. Edit the `.env` file and replace `your_openai_api_key_here` with your actual API key:
   ```
   OPENAI_API_KEY=sk-your-actual-api-key-here
   ```

## Step 6: Test Your Setup

```bash
python test_setup.py
```

This will verify that all components are working correctly.

## Step 7: Run Jarvis

### Voice Mode (Full Experience)
```bash
python jarvis_agent.py
```

### Text Mode (If Audio Issues)
```bash
python jarvis_text_mode.py
```

### Demo Mode (See Examples)
```bash
python demo.py
```

## Troubleshooting

### Common Issues

#### 1. "No module named 'pyaudio'"
**Solution**: Install PyAudio using one of the methods above.

#### 2. "OpenAI API key not configured"
**Solution**: Make sure you've created the `.env` file with your API key.

#### 3. "Microphone not working"
**Solutions**:
- Check microphone permissions in your OS
- Ensure microphone is set as default input device
- Try running as administrator (Windows)

#### 4. "Could not understand audio"
**Solutions**:
- Speak clearly and at normal pace
- Reduce background noise
- Move closer to microphone
- Check microphone volume

#### 5. "Rate limit exceeded"
**Solution**: Wait a moment and try again. Consider upgrading your OpenAI plan.

### Platform-Specific Issues

#### Windows
- Use `run_jarvis.bat` or `run_jarvis.ps1` for easy launching
- If PyAudio fails, use text mode: `python jarvis_text_mode.py`

#### macOS
- Grant microphone permissions in System Preferences
- Install PortAudio: `brew install portaudio`

#### Linux
- Install system dependencies: `sudo apt-get install python3-pyaudio portaudio19-dev`

## Alternative Setup Methods

### Using Virtual Environment
```bash
# Create virtual environment
python -m venv jarvis_env

# Activate (Windows)
jarvis_env\Scripts\activate

# Activate (macOS/Linux)
source jarvis_env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Using Conda
```bash
conda create -n jarvis python=3.9
conda activate jarvis
pip install -r requirements.txt
```

## Next Steps

Once installed, you can:
1. Start with the demo: `python demo.py`
2. Try text mode: `python jarvis_text_mode.py`
3. Use voice mode: `python jarvis_agent.py`
4. Customize settings in `config.py`

## Support

If you encounter issues:
1. Check the troubleshooting section above
2. Run `python test_setup.py` to diagnose problems
3. Check the logs in `jarvis.log`
4. Review the README.md for additional information 