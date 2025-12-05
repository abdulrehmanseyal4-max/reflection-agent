from dotenv import load_dotenv
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END, StateGraph
from langgraph.graph import add_messages
from chains import reflect_chain, generate_chain

load_dotenv()


class MessageGraphevolution(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


REFLECT = "reflect"
GENERATE = "generate"


def generation_node(state: MessageGraphevolution):
    return {"messages": [generate_chain.invoke({"messages": state["messages"]})]}


def reflection_node(state: MessageGraphevolution):
    res = reflect_chain.invoke({"messages": state["messages"]})
    return {"messages": [HumanMessage(role="user", content=res.content)]}

builder = StateGraph(state_schema=MessageGraphevolution)
builder.add_node(GENERATE, generation_node)
builder.add_node(REFLECT, reflection_node)
builder.set_entry_point(GENERATE)


def should_continue(state: MessageGraphevolution):
    if len(state["messages"]) >= 4:
        return END
    return REFLECT


builder.add_conditional_edges(
    GENERATE, should_continue, path_map={END: END, REFLECT: REFLECT}
)
builder.add_edge(REFLECT, GENERATE)

graph = builder.compile()


def run_agent(user_input: str) -> str:
    """Flask will call this function."""
    msg = HumanMessage(content=user_input)
    response = graph.invoke({"messages": [msg]})
    final_msg = response["messages"][-1].content
    return final_msg
