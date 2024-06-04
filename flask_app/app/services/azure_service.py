from llama_index.llms.azure_openai import AzureOpenAI
from llama_index.embeddings.azure_openai import AzureOpenAIEmbedding
from llama_index.core import Settings
from app.config import Config  # Assuming settings are in the config module

def initialize_azure_openai():
    llm = AzureOpenAI(
        engine=Config.OPENAI_DEPLOYMENT,
        model=Config.OPENAI_MODEL,
        temperature=0.0,
        azure_endpoint=Config.OPENAI_API_ENDPOINT,
        api_key=Config.OPENAI_API_KEY,
        api_version=Config.OPENAI_API_VERSION,
    )
    Settings.llm = llm
    return llm

def initialize_azure_embedding():
    embed_model = AzureOpenAIEmbedding(
        model=Config.EMBEDDING_MODEL,
        deployment_name=Config.EMBEDDING_DEPLOYMENT,
        azure_endpoint=Config.OPENAI_API_ENDPOINT,
        api_key=Config.OPENAI_API_KEY,
        api_version=Config.OPENAI_API_VERSION,
    )
    Settings.embed_model = embed_model
    return embed_model
