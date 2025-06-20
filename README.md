# 🤖 Agent Zero with Cerebras AI - Clean Version

A streamlined version of Agent Zero powered by Cerebras AI, with only essential files.

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Cerebras API key

### Installation
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file with your API key
echo "CEREBRAS_API_KEY=your_api_key_here" > .env

# Run the application
python main.py
```

### Access
Open your browser and go to: `http://localhost:7861`

## 📁 Essential Files

### Core Application
- `main.py` - Main application entry point
- `agent.py` - Agent Zero core logic
- `cerebras_provider.py` - Cerebras AI integration
- `models.py` - AI model configurations
- `config.yaml` - Application configuration
- `initialize.py` - Initialization utilities

### Configuration
- `config/` - Configuration files
- `requirements.txt` - Python dependencies
- `.env` - Environment variables (create this)

### Web Interface
- `webui/` - Gradio web interface files

### Runtime Directories
- `work_dir/` - Working directory for file operations
- `logs/` - Application logs
- `python/` - Python helper modules

## 🔧 Features

- **AI Chat**: Powered by Cerebras models
- **File Operations**: Read, write, and edit files
- **Web Interface**: Modern Gradio-based UI
- **Memory**: Conversation context retention
- **Secure**: API key handling

## 🗂️ Removed Components

The following components were removed to streamline the application:
- Docker configuration
- Documentation files
- Additional tools and instruments
- CLI and tunnel runners
- Development configurations
- Backup files

## 🔄 Restore Full Version

If you need the full version with all features:
```bash
# Restore from backup
cp -r backup_before_cleanup/* .
```

## 📝 License

See LICENSE file for details. 