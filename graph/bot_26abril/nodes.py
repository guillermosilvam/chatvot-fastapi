from langgraph.graph import MessagesState
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage
from core.models import model

# Historial del chat
prompt_template_1 = ChatPromptTemplate(
    [
        SystemMessage(content="Eres un experto en finanzas y contabilidad."),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

# Nodes
def call_model(state:MessagesState):
    prompt_to = prompt_template_1.invoke(state['messages'])
    response = model.invoke(prompt_to)
    return {'messages' : response}


