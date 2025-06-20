import os
import sys
import asyncio
import gradio as gr
from gradio.themes import Soft
import json
import requests
from typing import Optional, Dict, Any, List
from datetime import datetime

# Add the project root to Python path to fix import issues
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

class CerebrasProvider:
    """Enhanced Cerebras API Provider with real API integration"""
    
    def __init__(self, api_key: str, base_url: str = 'https://api.cerebras.ai/v1'):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        self.model = 'llama-4-scout-17b-16e-instruct'
        self.max_tokens = 1000
        self.temperature = 0.7
    
    def generate_response(self, messages: List[Dict[str, str]], stream: bool = False) -> str:
        """
        Generate response using Cerebras API
        """
        try:
            payload = {
                "model": self.model,
                "messages": messages,
                "max_tokens": self.max_tokens,
                "temperature": self.temperature,
                "stream": stream
            }
            
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=self.headers,
                json=payload,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                return result['choices'][0]['message']['content']
            else:
                return f"❌ API Error {response.status_code}: {response.text}"
                
        except requests.exceptions.Timeout:
            return "❌ Request timed out. Please try again."
        except requests.exceptions.ConnectionError:
            return "❌ Connection error. Please check your internet connection."
        except Exception as e:
            return f"❌ Error calling Cerebras API: {str(e)}"
    
    def test_connection(self) -> bool:
        """Test if the API key and connection work"""
        try:
            test_messages = [{"role": "user", "content": "Hello"}]
            response = self.generate_response(test_messages)
            return not response.startswith("❌")
        except:
            return False

class Agent:
    """Enhanced Agent class with conversation memory and context management"""
    
    def __init__(self, llm_provider=None, config=None):
        self.llm_provider = llm_provider
        self.config = config
        self.conversation_memory = []
        self.system_prompt = self._get_system_prompt()
        self.max_memory_length = 10  # Keep last 10 exchanges
    
    def _get_system_prompt(self) -> str:
        """Define the agent's personality and capabilities"""
        return """You are Agent Zero, an advanced AI assistant powered by Cerebras AI. You are:

🤖 **Capabilities:**
- Helpful, knowledgeable, and friendly
- Able to assist with coding, writing, analysis, and general questions
- Equipped with reasoning and problem-solving abilities
- Capable of maintaining context throughout our conversation

🎯 **Your Goals:**
- Provide accurate and helpful responses
- Be clear and concise in your explanations
- Ask clarifying questions when needed
- Maintain a professional yet approachable tone

💡 **Special Instructions:**
- Always strive to be helpful and constructive
- If you're unsure about something, say so
- Provide examples when helpful
- Break down complex topics into understandable parts

How can I assist you today?"""
    
    def _prepare_messages(self, user_message: str) -> List[Dict[str, str]]:
        """Prepare messages for the API call including system prompt and conversation history"""
        messages = [{"role": "system", "content": self.system_prompt}]
        
        # Add conversation history (limited to prevent token overflow)
        for exchange in self.conversation_memory[-self.max_memory_length:]:
            messages.append({"role": "user", "content": exchange["user"]})
            messages.append({"role": "assistant", "content": exchange["assistant"]})
        
        # Add current user message
        messages.append({"role": "user", "content": user_message})
        
        return messages
    
    def chat(self, message: str) -> str:
        """Main chat method with enhanced context and memory management"""
        if not self.llm_provider:
            return "❌ Agent not properly initialized. Please check your API key."
        
        if not message.strip():
            return "Please enter a message to continue our conversation."
        
        try:
            # Prepare messages with context
            messages = self._prepare_messages(message)
            
            # Get response from Cerebras
            response = self.llm_provider.generate_response(messages)
            
            # Store in conversation memory
            if not response.startswith("❌"):
                self.conversation_memory.append({
                    "user": message,
                    "assistant": response,
                    "timestamp": datetime.now().isoformat()
                })
            
            return response
            
        except Exception as e:
            return f"❌ Error processing your message: {str(e)}"
    
    def clear_memory(self):
        """Clear conversation memory"""
        self.conversation_memory = []
        return "🧹 Conversation memory cleared."
    
    def get_memory_summary(self) -> str:
        """Get a summary of conversation memory"""
        if not self.conversation_memory:
            return "No conversation history available."
        
        return f"💭 Conversation history: {len(self.conversation_memory)} exchanges"

class Config:
    """Enhanced configuration class"""
    
    def __init__(self):
        self.cerebras_api_key = os.getenv('CEREBRAS_API_KEY', '')
        self.cerebras_model = 'llama3.1-8b'
        self.cerebras_base_url = 'https://api.cerebras.ai/v1'
        self.max_tokens = 1000
        self.temperature = 0.7
        self.conversation_memory_limit = 10

class AgentZeroMain:
    def __init__(self):
        self.agent = None
        self.cerebras_provider = None
        self.config = None
        self.setup_config()
    
    def setup_config(self):
        """Initialize configuration"""
        try:
            self.config = Config()
        except Exception as e:
            print(f"Error loading config: {e}")
            self.config = Config()  # Use default config
    
    def initialize_cerebras_provider(self, api_key: str) -> tuple[bool, str]:
        """
        Initialize the Cerebras provider with proper error handling
        Returns: (success: bool, message: str)
        """
        try:
            if not api_key or api_key.strip() == '':
                return False, "❌ Error: Cerebras API key is required"
            
            # Extract API key if it's passed as a dict
            if isinstance(api_key, dict):
                api_key = api_key.get('api_key', '') or api_key.get('key', '')
            
            if not isinstance(api_key, str):
                return False, "❌ Error: API key must be a string"
            
            # Initialize provider
            self.cerebras_provider = CerebrasProvider(
                api_key=api_key.strip(),
                base_url=getattr(self.config, 'cerebras_base_url', 'https://api.cerebras.ai/v1')
            )
            
            # Test the connection
            print("🔄 Testing Cerebras API connection...")
            if self.cerebras_provider.test_connection():
                print("✅ Cerebras provider initialized and tested successfully")
                return True, "✅ Cerebras API connection verified"
            else:
                return False, "❌ Failed to connect to Cerebras API. Please check your API key."
            
        except Exception as e:
            error_msg = f"❌ Error initializing Cerebras provider: {str(e)}"
            print(error_msg)
            return False, error_msg
    
    def initialize_agent(self, api_key: str) -> tuple[bool, str]:
        """
        Initialize the agent with Cerebras provider
        Returns: (success: bool, message: str)
        """
        try:
            success, message = self.initialize_cerebras_provider(api_key)
            if not success:
                return False, message
            
            # Initialize agent with the Cerebras provider
            self.agent = Agent(
                llm_provider=self.cerebras_provider,
                config=self.config
            )
            
            print("✅ Agent initialized successfully")
            return True, "✅ Agent Zero is ready! You can now start chatting."
            
        except Exception as e:
            error_msg = f"❌ Error initializing agent: {str(e)}"
            print(error_msg)
            return False, error_msg
    
    def chat_with_agent(self, message: str, history: list) -> tuple:
        """
        Handle chat interaction with proper error handling
        """
        try:
            if not self.agent:
                error_msg = "❌ Agent not initialized. Please set your API key first."
                history.append({"role": "user", "content": message})
                history.append({"role": "assistant", "content": error_msg})
                return history, ""
            
            if not message.strip():
                return history, ""
            
            # Get response from agent
            try:
                print(f"🤖 Processing: {message[:50]}...")
                response = self.agent.chat(message)
                
                # Add to history using the new messages format
                history.append({"role": "user", "content": message})
                history.append({"role": "assistant", "content": response})
                
                print(f"✅ Response generated successfully")
                    
            except Exception as e:
                error_response = f"❌ Error getting response: {str(e)}"
                history.append({"role": "user", "content": message})
                history.append({"role": "assistant", "content": error_response})
                print(f"❌ Chat error: {e}")
            
            return history, ""
            
        except Exception as e:
            error_msg = f"❌ Chat error: {str(e)}"
            history.append({"role": "user", "content": message})
            history.append({"role": "assistant", "content": error_msg})
            print(f"❌ Unexpected error: {e}")
            return history, ""
    
    def setup_api_key(self, api_key: str) -> str:
        """
        Setup API key and initialize the system
        """
        try:
            print(f"🔄 Setting up API key...")
            success, message = self.initialize_agent(api_key)
            return message
        except Exception as e:
            error_msg = f"❌ Error setting up API key: {str(e)}"
            print(error_msg)
            return error_msg
    
    def clear_conversation(self, history: list) -> tuple:
        """Clear the conversation history"""
        if self.agent:
            self.agent.clear_memory()
        return [], "🧹 Conversation cleared!"
    
    def create_gradio_interface(self):
        """
        Create the enhanced Gradio interface
        """
        # Custom CSS for better styling
        custom_css = """
        .container { max-width: 1400px; margin: auto; }
        .header { text-align: center; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; margin-bottom: 20px; }
        .header h1 { color: white; margin: 0; }
        .header p { color: rgba(255,255,255,0.9); margin: 5px 0 0 0; }
        .status-box { padding: 15px; border-radius: 8px; margin: 10px 0; }
        .chat-container { border-radius: 10px; }
        .input-group { background: #f8f9fa; padding: 15px; border-radius: 10px; margin: 10px 0; }
        """
        
        with gr.Blocks(
            title="Agent Zero with Cerebras AI",
            css=custom_css,
            theme=Soft(
                primary_hue="blue",
                secondary_hue="gray",
                neutral_hue="gray"
            )
        ) as interface:
            
            # Header
            gr.HTML("""
            <div class="header">
                <h1>🤖 Agent Zero with Cerebras AI</h1>
                <p>Your intelligent AI assistant powered by cutting-edge Cerebras technology</p>
            </div>
            """)
            
            # API Key Setup Section
            with gr.Row():
                with gr.Column(scale=2):
                    gr.Markdown("### 🔑 **Step 1: Initialize Your Agent**")
                    with gr.Group(elem_classes="input-group"):
                        api_key_input = gr.Textbox(
                            label="Cerebras API Key",
                            placeholder="Enter your Cerebras API key here (e.g., csk-...)",
                            type="password",
                            lines=1,
                            info="Your API key is securely handled and not stored."
                        )
                        
                        with gr.Row():
                            setup_btn = gr.Button("🚀 Initialize Agent", variant="primary", scale=2)
                            clear_btn = gr.Button("🧹 Clear Chat", variant="secondary", scale=1)
                        
                        status_output = gr.Textbox(
                            label="Status",
                            interactive=False,
                            lines=2,
                            elem_classes="status-box"
                        )
            
            # Chat Section
            gr.Markdown("### 💬 **Step 2: Chat with Your Agent**")
            
            with gr.Row():
                with gr.Column():
                    chatbot = gr.Chatbot(
                        label="Agent Zero Conversation",
                        height=500,
                        type="messages",  # Use new messages format
                        elem_classes="chat-container",
                        show_label=True,
                        avatar_images=("🧑‍💻", "🤖"),
                        bubble_full_width=False
                    )
                    
                    with gr.Row():
                        msg_input = gr.Textbox(
                            label="Your Message",
                            placeholder="Ask me anything! I can help with coding, writing, analysis, and more...",
                            lines=2,
                            scale=4,
                            show_label=False
                        )
                        send_btn = gr.Button("📤 Send", variant="primary", scale=1, size="lg")
            
            # Footer with instructions
            gr.Markdown("""
            ---
            ### 💡 **Tips for Better Conversations:**
            - Be specific in your questions for more accurate responses
            - I can help with coding, writing, analysis, problem-solving, and general questions
            - Feel free to ask follow-up questions - I maintain conversation context
            - Use the "Clear Chat" button to start fresh conversations
            
            ### 🔧 **Features:**
            - **Real-time AI responses** powered by Cerebras
            - **Conversation memory** for contextual discussions
            - **Error handling** with helpful feedback
            - **Secure API key handling**
            """)
            
            # Event handlers
            def handle_setup(api_key):
                return self.setup_api_key(api_key)
            
            def handle_send(message, history):
                return self.chat_with_agent(message, history)
            
            def handle_clear(history):
                return self.clear_conversation(history)
            
            # Button click events
            setup_btn.click(
                fn=handle_setup,
                inputs=[api_key_input],
                outputs=[status_output]
            )
            
            send_btn.click(
                fn=handle_send,
                inputs=[msg_input, chatbot],
                outputs=[chatbot, msg_input]
            )
            
            clear_btn.click(
                fn=handle_clear,
                inputs=[chatbot],
                outputs=[chatbot, status_output]
            )
            
            # Enter key support
            msg_input.submit(
                fn=handle_send,
                inputs=[msg_input, chatbot],
                outputs=[chatbot, msg_input]
            )
        
        return interface

def main():
    """
    Main function to run the application
    """
    print("🚀 Starting Agent Zero with Cerebras...")
    print("📋 Features: Real Cerebras API • Conversation Memory • Enhanced UI")
    print("=" * 60)
    
    try:
        app = AgentZeroMain()
        interface = app.create_gradio_interface()
        
        print("✅ Application ready!")
        print("🌐 Opening web interface...")
        print("📱 The interface will automatically open in your browser")
        print("=" * 60)
        
        # Launch the interface
        interface.launch(
            server_name="127.0.0.1",
            server_port=7861,
            share=False,
            inbrowser=True,
            show_error=True,
            favicon_path=None,
            app_kwargs={"docs_url": None, "redoc_url": None}
        )
        
    except KeyboardInterrupt:
        print("\n👋 Shutting down gracefully...")
        print("Thanks for using Agent Zero!")
    except Exception as e:
        print(f"❌ Application error: {e}")
        import traceback
        traceback.print_exc()
        print("\n🔧 Troubleshooting:")
        print("1. Make sure you have all required packages installed:")
        print("   pip install gradio requests")
        print("2. Check your internet connection")
        print("3. Verify your Cerebras API key is valid")

if __name__ == "__main__":
    main()
