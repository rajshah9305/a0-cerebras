# 🤖 Agent Zero with Cerebras AI

A powerful autonomous AI agent powered by Cerebras AI's Wafer-Scale Engine, providing ultra-low latency responses and advanced reasoning capabilities.

![Agent Zero](https://img.shields.io/badge/Agent-Zero-blue)
![Cerebras AI](https://img.shields.io/badge/Powered%20by-Cerebras%20AI-green)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## 🚀 Quick Start

### Prerequisites
- **Python 3.8+**
- **Cerebras API Key** - Get yours at [Cerebras AI](https://cerebras.ai)
- **Git**

### Installation

```bash
# Clone the repository
git clone https://github.com/rajshah9305/a0-cerebras.git
cd a0-cerebras

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file with your API key
echo "CEREBRAS_API_KEY=your_cerebras_api_key_here" > .env

# Run the application
python main.py
```

### Access
Open your browser and go to: `http://localhost:7861`

## 🎯 Features

### Core Capabilities
- **🤖 Autonomous AI Agent**: Self-directed task execution and problem solving
- **⚡ Ultra-Low Latency**: Powered by Cerebras Wafer-Scale Engine
- **🧠 Advanced Reasoning**: Access to cutting-edge LLM models
- **💻 Code Execution**: Run Python, Node.js, and terminal commands
- **🌐 Web Browsing**: Interactive web automation and data extraction
- **📁 File Operations**: Complete file system access and management
- **🔍 Web Search**: Real-time information retrieval
- **💾 Memory System**: Persistent conversation and solution memory
- **🛠️ Extensible Tools**: Custom tool development framework

### Cerebras AI Integration
- **Supported Models**:
  - `llama3.1-8b` - Fast, efficient for most tasks
  - `llama3.1-70b` - Advanced reasoning and complex tasks
  - `mixtral-8x7b` - Mixture of experts model
  - `llama-4-scout-17b-16e-instruct` - Current default model

- **Performance Benefits**:
  - **Millisecond responses** - No cold starts
  - **High throughput** - Handle multiple agents simultaneously
  - **Consistent performance** - No variable response times
  - **Advanced reasoning** - Complex problem-solving capabilities

## 📁 Project Structure

```
a0-cerebras/
├── README.md                    # This file
├── main.py                      # Main application entry point
├── agent.py                     # Agent Zero core logic
├── cerebras_provider.py         # Cerebras AI integration
├── models.py                    # AI model configurations
├── config.yaml                  # Application configuration
├── requirements.txt             # Python dependencies
├── example.env                  # Environment variables template
├── config/
│   └── cerebras_config.yaml     # Cerebras-specific configuration
├── python/                      # Core Python modules
│   ├── api/                     # REST API endpoints
│   ├── helpers/                 # Utility functions
│   ├── tools/                   # Agent tools
│   └── extensions/              # System extensions
├── webui/                       # Gradio web interface
│   ├── css/                     # Stylesheets
│   ├── js/                      # JavaScript files
│   └── public/                  # Static assets
├── work_dir/                    # Working directory for file operations
└── logs/                        # Application logs
```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the root directory:

```bash
# Required: Your Cerebras API key
CEREBRAS_API_KEY=your_cerebras_api_key_here

# Optional: Custom configuration
WEB_UI_PORT=7861
USE_CLOUDFLARE=false
TOKENIZERS_PARALLELISM=true
PYDEVD_DISABLE_FILE_VALIDATION=1
```

### Cerebras Configuration

Edit `config/cerebras_config.yaml` for advanced settings:

```yaml
cerebras:
  api_key: "${CEREBRAS_API_KEY}"
  model: "llama3.1-8b"
  max_tokens: 4096
  temperature: 0.7
  stream: true
  base_url: "https://api.cerebras.ai/v1"
  
agent:
  max_iterations: 10
  memory_enabled: true
  tools_enabled: true
  conversation_memory_limit: 10
```

## 🛠️ Usage Examples

### 1. Development Project
```
"Create a React dashboard with real-time data visualization using D3.js"
```

**Agent Zero will:**
- Set up a new React project
- Install necessary dependencies (D3.js, etc.)
- Create component structure
- Implement real-time data fetching
- Add interactive visualizations
- Test and debug the application

### 2. Data Analysis
```
"Analyze the uploaded sales data CSV and create trend reports with predictions"
```

**Agent Zero will:**
- Read and examine the CSV structure
- Perform statistical analysis
- Create visualizations
- Generate trend predictions
- Export results to PDF/HTML

### 3. System Administration
```
"Set up monitoring for my web servers with alerts"
```

**Expected actions:**
- Install monitoring tools (Prometheus, Grafana, etc.)
- Configure server metrics collection
- Set up alerting rules
- Create dashboards
- Test alert notifications

### 4. Content Creation
```
"Write a technical blog post about microservices architecture with code examples"
```

**Agent Zero process:**
- Research current microservices best practices
- Structure the blog post outline
- Write detailed content with examples
- Create code snippets and diagrams
- Format for publication

## 🔧 Advanced Features

### Multi-Agent Workflows
Agent Zero can create subordinate agents for complex tasks:

```
"Create a project manager agent and three developer agents to build a web application"
```

**Result:**
- Manager agent coordinates the project
- Developer agents handle: Backend, Frontend, Database
- Agents communicate and report progress
- Automatic task delegation and coordination

### Memory and Learning
**Memory Types:**
- **Episodic**: Remembers specific conversations and solutions
- **Semantic**: Learns general patterns and best practices
- **Procedural**: Remembers how to perform complex tasks

**Memory Management:**
```python
# Access agent memory
agent.memory.store("project_setup", solution_code)
previous_solution = agent.memory.retrieve("similar_project")
```

### Real-time Interaction
**Terminal Commands:**
- `Ctrl+C`: Stop current agent execution
- Type messages anytime to redirect or provide feedback
- Agents will acknowledge and adapt in real-time

## 🌐 Web Interface

### Features
- **Modern UI**: Clean, responsive Gradio-based interface
- **Real-time Chat**: Live conversation with the agent
- **File Browser**: Upload, download, and manage files
- **Settings Panel**: Configure models and preferences
- **Task Scheduler**: Schedule recurring tasks
- **Memory Viewer**: Browse and manage agent memory
- **History Export**: Export conversation history

### Navigation
- **Chat Tab**: Main conversation interface
- **Files Tab**: File management and browser
- **Settings Tab**: Configuration and model settings
- **Scheduler Tab**: Task scheduling and management
- **History Tab**: Conversation history and export

## 🔒 Security & Safety

### Important Warnings
⚠️ **Agent Zero Can Be Dangerous!**

- Agents can execute system commands and modify files
- Always run in isolated environment for production use
- Never run on production systems without proper sandboxing
- Review agent actions before execution in sensitive environments

### Safety Features
**Built-in Protections:**
- File system access controls
- Network access limitations
- Command execution monitoring
- Memory usage limits

**Recommended Practices:**
```bash
# Use isolated environment
python -m venv venv
source venv/bin/activate

# Limit resource usage
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
python main.py --sandbox-mode
```

## 🐛 Troubleshooting

### Common Issues

**Issue**: Cerebras API authentication fails
```bash
# Check your API key in .env file
echo $CEREBRAS_API_KEY
# Verify key validity at Cerebras dashboard
```

**Issue**: Port already in use
```bash
# Use a different port
export WEB_UI_PORT=7862
python main.py
```

**Issue**: Agent gets stuck in loops
- **Solution**: Interrupt with Ctrl+C and provide clearer instructions
- **Prevention**: Use more specific prompts with clear success criteria

**Issue**: Memory usage too high
```bash
# Clear agent memory
python -c "from python.helpers.memory import reload; reload()"
```

### Debug Mode
**Enable verbose logging:**
```bash
# Set environment variable
export DEBUG_MODE=true

# Or modify config
debug:
  enabled: true
  log_level: "DEBUG"
  save_logs: true
```

### Getting Help
- **Log Files**: Check `logs/` folder for detailed execution logs
- **Issues**: Report bugs on [GitHub Issues](https://github.com/rajshah9305/a0-cerebras/issues)
- **Documentation**: See the [docs folder](docs/) for detailed guides

## 🔧 Customization

### System Prompts
**Location**: `prompts/default/agent.system.md`

Modify to change agent behavior:
- Change personality and communication style
- Add domain-specific expertise
- Set task priorities and workflows
- Define safety boundaries

**Example Customization:**
```markdown
# Your Custom Agent Prompt

You are a senior software engineer specializing in Python and machine learning.

## Core Behaviors:
- Always write clean, well-documented code
- Prefer industry best practices
- Ask clarifying questions before starting complex tasks
- Provide testing strategies for all code

## Specializations:
- Machine Learning: TensorFlow, PyTorch, Scikit-learn
- Web Development: FastAPI, Django, React
- Data Science: Pandas, NumPy, Matplotlib
```

### Custom Tools
**Location**: `python/tools/`

Create new tools by adding Python files:

**File**: `python/tools/my_custom_tool.py`
```python
from python.helpers.tool import Tool, Response

class MyCustomTool(Tool):
    def execute(self, **kwargs):
        # Your custom tool logic here
        result = "Custom tool executed successfully"
        return Response(message=result, break_loop=False)
```

### Environment Variables
**File**: `.env`

```bash
# Cerebras Configuration
CEREBRAS_API_KEY=your_key_here
CEREBRAS_MODEL=llama3.1-8b

# Agent Configuration  
AGENT_NAME=MyAgent
MAX_ITERATIONS=15
ENABLE_MEMORY=true
ENABLE_TOOLS=true

# Security
SAFE_MODE=true
DOCKER_ISOLATION=true
```

## 📊 Performance

### Benchmarks
- **Response Time**: < 100ms average (Cerebras WSE)
- **Throughput**: 1000+ requests/second
- **Memory Usage**: < 2GB RAM
- **Context Window**: Up to 32K tokens

### Optimization Tips
- Use appropriate model size for your task
- Enable streaming for long responses
- Configure memory limits based on usage
- Use Docker for production deployments

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Setup
```bash
# Clone and setup development environment
git clone https://github.com/rajshah9305/a0-cerebras.git
cd a0-cerebras
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/

# Run linting
flake8 python/
black python/
```

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Agent Zero Framework**: Built on the excellent [frdel/agent-zero](https://github.com/frdel/agent-zero) foundation
- **Cerebras AI**: Powered by Cerebras Wafer-Scale Engine technology
- **Community**: Thanks to all contributors and users providing feedback

## 📞 Support

- **GitHub Issues**: [Report bugs and request features](https://github.com/rajshah9305/a0-cerebras/issues)
- **Discussions**: [Join community discussions](https://github.com/rajshah9305/a0-cerebras/discussions)
- **Documentation**: [Browse detailed docs](docs/)

## 🔗 Links

- **Repository**: https://github.com/rajshah9305/a0-cerebras
- **Cerebras AI**: https://cerebras.ai
- **Agent Zero**: https://github.com/frdel/agent-zero
- **Documentation**: [docs/](docs/)

---

**Ready to unleash the power of autonomous AI agents with Cerebras speed? Let's get started! 🚀**

<div align="center">

[![Star on GitHub](https://img.shields.io/github/stars/rajshah9305/a0-cerebras?style=social)](https://github.com/rajshah9305/a0-cerebras/stargazers)
[![Fork on GitHub](https://img.shields.io/github/forks/rajshah9305/a0-cerebras?style=social)](https://github.com/rajshah9305/a0-cerebras/network/members)
[![Issues](https://img.shields.io/github/issues/rajshah9305/a0-cerebras)](https://github.com/rajshah9305/a0-cerebras/issues)
[![License](https://img.shields.io/github/license/rajshah9305/a0-cerebras)](https://github.com/rajshah9305/a0-cerebras/blob/main/LICENSE)

</div> 