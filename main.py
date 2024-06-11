from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import  ChatPromptTemplate
from langchain_community.chat_models.ollama import ChatOllama
from fastapi import FastAPI
from langserve import add_routes

import uvicorn
import argparse

parser = argparse.ArgumentParser(description="Translate text from one language to another using Langchain and LLaMA3.")

parser.add_argument('--model_name', default="llama3", type=str, help='Name of the Ollama Model')
parser.add_argument('--model_host', default="localhost", type=str, help='Host on which Ollama server is up')

args = parser.parse_args()
    
model = ChatOllama(model=args.model_name, base_url=f"http://{args.model_host}:11434", temperature=0.1)
parser = StrOutputParser()

system_template = "Translate the following from English to {language}"
prompt_template = ChatPromptTemplate.from_messages(
        [
            ('system', system_template),
            ('user', "{text}")
         ]
        )

chain = prompt_template | model | parser

app = FastAPI(
  title="Text Translation",
  description="Translate text from English to any other language",
)

add_routes(
    app,
    chain,
    path="/chain",
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
