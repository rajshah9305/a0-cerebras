import openai
from typing import Optional, Dict, Any, Iterator
import json

class CerebrasProvider:
    def __init__(self, api_key: str, base_url: str = "https://api.cerebras.ai/v1"):
        self.client = openai.OpenAI(
            api_key=api_key,
            base_url=base_url
        )
    
    def chat_completion(self, messages: list, model: str = "llama3.1-8b", stream: bool = False, **kwargs):
        """
        Handle both streaming and non-streaming responses properly
        """
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                stream=stream,
                **kwargs
            )
            
            if stream:
                return self._handle_streaming_response(response)
            else:
                return self._handle_non_streaming_response(response)
                
        except Exception as e:
            print(f"Error in chat completion: {e}")
            return None
    
    def _handle_streaming_response(self, stream):
        """
        Properly handle streaming responses
        """
        full_content = ""
        usage_info = None
        
        try:
            for chunk in stream:
                if hasattr(chunk, 'choices') and len(chunk.choices) > 0:
                    choice = chunk.choices[0]
                    if hasattr(choice, 'delta') and hasattr(choice.delta, 'content'):
                        if choice.delta.content:
                            full_content += choice.delta.content
                
                # Check for usage information in the final chunk
                if hasattr(chunk, 'usage') and chunk.usage:
                    usage_info = chunk.usage
            
            # Create a response object similar to non-streaming format
            return {
                "choices": [{
                    "message": {
                        "content": full_content,
                        "role": "assistant"
                    },
                    "finish_reason": "stop"
                }],
                "usage": {
                    "prompt_tokens": getattr(usage_info, 'prompt_tokens', 0) if usage_info else 0,
                    "completion_tokens": getattr(usage_info, 'completion_tokens', 0) if usage_info else 0,
                    "total_tokens": getattr(usage_info, 'total_tokens', 0) if usage_info else 0
                }
            }
            
        except Exception as e:
            print(f"Error handling streaming response: {e}")
            return None
    
    def _handle_non_streaming_response(self, response):
        """
        Handle regular non-streaming responses
        """
        try:
            if hasattr(response, 'choices') and len(response.choices) > 0:
                return {
                    "choices": [{
                        "message": {
                            "content": response.choices[0].message.content,
                            "role": response.choices[0].message.role
                        },
                        "finish_reason": response.choices[0].finish_reason
                    }],
                    "usage": {
                        "prompt_tokens": getattr(response.usage, 'prompt_tokens', 0) if response.usage else 0,
                        "completion_tokens": getattr(response.usage, 'completion_tokens', 0) if response.usage else 0,
                        "total_tokens": getattr(response.usage, 'total_tokens', 0) if response.usage else 0
                    }
                }
        except Exception as e:
            print(f"Error handling non-streaming response: {e}")
            return None
    
    def generate_streaming_response(self, messages: list, model: str = "llama3.1-8b", **kwargs):
        """
        Generator function for streaming responses
        """
        try:
            stream = self.client.chat.completions.create(
                model=model,
                messages=messages,
                stream=True,
                **kwargs
            )
            
            for chunk in stream:
                if hasattr(chunk, 'choices') and len(chunk.choices) > 0:
                    choice = chunk.choices[0]
                    if hasattr(choice, 'delta') and hasattr(choice.delta, 'content'):
                        if choice.delta.content:
                            yield choice.delta.content
                            
        except Exception as e:
            print(f"Error in streaming response: {e}")
            yield f"Error: {str(e)}"

# Example usage function
def example_usage():
    """
    Example of how to use the fixed provider
    """
    # Initialize the provider
    provider = CerebrasProvider(api_key="your-api-key-here")
    
    # Example messages
    messages = [
        {"role": "user", "content": "Hello, how are you?"}
    ]
    
    # Non-streaming example
    print("=== Non-streaming Response ===")
    response = provider.chat_completion(messages, stream=False)
    if response and response.get('choices'):
        print(response['choices'][0]['message']['content'])
    
    # Streaming example
    print("\n=== Streaming Response ===")
    response = provider.chat_completion(messages, stream=True)
    if response and response.get('choices'):
        print(response['choices'][0]['message']['content'])
    
    # Generator streaming example
    print("\n=== Generator Streaming ===")
    for chunk in provider.generate_streaming_response(messages):
        print(chunk, end='', flush=True)
    print()  # New line at the end