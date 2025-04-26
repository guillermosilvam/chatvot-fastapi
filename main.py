from fastapi import FastAPI
from langchain_core.messages import HumanMessage
from graph.bot_26abril.main_graph import graph
from schemas.schemas import Bot

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "Hello, World!"}


@app.post("/chat")
def chat(prompt: Bot):
    config = {"configurable": {"thread_id": prompt.id}}
    input_messages = [HumanMessage(content=prompt.prompt)]
    init_state = {"messages" : input_messages}
    response = graph.invoke(init_state, config)    
    return {"message": response['messages'][-1].content}
