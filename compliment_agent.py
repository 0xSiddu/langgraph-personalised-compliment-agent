from typing import TypedDict
from langgraph.graph import StateGraph, END


# 1. Define the State
class AgentState(TypedDict):
    name: str
    compliment: str


# 2. Define the Node (concatenates, doesn't replace)
def compliment_node(state: AgentState) -> AgentState:
    name = state["name"]
    compliment = f"{name}, you're doing an amazing job learning LangGraph!"
    return {**state, "compliment": compliment}  # concatenate state, not replace


# 3. Build the Graph
def build_graph():
    graph = StateGraph(AgentState)

    # Add node
    graph.add_node("compliment_node", compliment_node)

    # Set entry point and edge to END
    graph.set_entry_point("compliment_node")
    graph.add_edge("compliment_node", END)

    return graph.compile()


# 4. Run the Agent
if __name__ == "__main__":
    app = build_graph()

    # Test with "Bob"
    input_state = {"name": "Bob", "compliment": ""}
    result = app.invoke(input_state)

    print("Input : {'name': 'Bob'}")
    print(f"Output: \"{result['compliment']}\"")

    # Test with a few more names
    print("\n--- More examples ---")
    for name in ["Alice", "Charlie", "Diana"]:
        out = app.invoke({"name": name, "compliment": ""})
        print(f"Output: \"{out['compliment']}\"")
