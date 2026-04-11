from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
import os
from dotenv import load_dotenv
load_dotenv()
groq_api_key=os.getenv("GROQ_API_KEY")
groq=ChatGroq(model="openai/gpt-oss-120b",groq_api_key=groq_api_key)
prompts=ChatPromptTemplate([
    ("system","Convert the message into {language}"),
    ("user","{text}")
])
parser=StrOutputParser()
chain=prompts| groq|parser

app=FastAPI(
    title="langchain server",
    version="1.0",
    description="A simple API server using the langchain runnables"
)
add_routes(
    app,
    chain,
    path="/chain"
)
if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)

