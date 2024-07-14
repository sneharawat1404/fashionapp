import os
open_api_key="sk-proj-PZvGLUQRh0XiyFtBKZJrT3BlbkFJEw5Tivt3VE0Y30iY7hO0"
os.environ["OPENAI_API_KEY"] = open_api_key
## Basic Prompt Summarization
from langchain.chat_models import ChatOpenAI
from langchain.schema import(
    AIMessage,
    HumanMessage,
    SystemMessage
)
