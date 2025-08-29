"""
Global configuration for all AI bots
Place this file in your Python path or import it from bot directories
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class BotConfig:
    # API Keys
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    SERPAPI_KEY = os.getenv("SERPAPI_KEY")
    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    COHERE_API_KEY = os.getenv("COHERE_API_KEY")
    AGNO_API_KEY = os.getenv("AGNO_API_KEY")
    
    # Database configs
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
    WEAVIATE_URL = os.getenv("WEAVIATE_URL")
    
    # Default model settings
    DEFAULT_MODEL = "gpt-4o-mini"
    DEFAULT_TEMPERATURE = 0.7
    
    # Common paths
    DATA_DIR = os.path.expanduser("~/bot_data")
    LOGS_DIR = os.path.expanduser("~/bot_logs")
    
    @classmethod
    def validate_keys(cls):
        """Check if essential API keys are set"""
        missing = []
        if not cls.OPENAI_API_KEY:
            missing.append("OPENAI_API_KEY")
        
        if missing:
            print(f"Warning: Missing API keys: {', '.join(missing)}")
            print("Add them to your .env file to enable full functionality")
        else:
            print("[SUCCESS] Core API keys are configured!")
        
        return len(missing) == 0

# Create data directories if they don't exist
os.makedirs(BotConfig.DATA_DIR, exist_ok=True)
os.makedirs(BotConfig.LOGS_DIR, exist_ok=True)