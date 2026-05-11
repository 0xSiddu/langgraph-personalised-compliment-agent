# 🤖 LangGraph Personalized Compliment Agent

A simple LangGraph agent that generates a personalized compliment based on a given name. Built as part of the **LangGraph Complete Course for Beginners – Complex AI Agents with Python**.

---

## 📋 Exercise Overview

| Field | Details |
|-------|---------|
| **Exercise** | Graph I — Personalized Compliment Agent |
| **Input** | `{"name": "Bob"}` |
| **Output** | `"Bob, you're doing an amazing job learning LangGraph!"` |
| **Key Hint** | Concatenate the state, don't replace it |

---

## 🗂️ Project Structure

```
compliment-agent/
│
├── compliment_agent.py   # Main agent code
└── README.md             # This file
```

---

## ⚙️ Requirements

- Python 3.9+
- LangGraph

Install dependencies:

```bash
pip install langgraph
```

---

## 🚀 How to Run

```bash
python compliment_agent.py
```

### Expected Output

```
Input : {'name': 'Bob'}
Output: "Bob, you're doing an amazing job learning LangGraph!"

--- More examples ---
Output: "Alice, you're doing an amazing job learning LangGraph!"
Output: "Charlie, you're doing an amazing job learning LangGraph!"
Output: "Diana, you're doing an amazing job learning LangGraph!"
```

---

## 🧠 Concepts Explained

### 1. `AgentState` (TypedDict)

Defines the shape of the graph's state. Every node reads from and writes to this state.

```python
class AgentState(TypedDict):
    name: str        # Input: the person's name
    compliment: str  # Output: the generated compliment
```

### 2. Node — `compliment_node`

A node is just a Python function that takes the current state and returns an updated state.

> ⚠️ **Key**: Use `{**state, "compliment": ...}` to **merge** the new value into the existing state — don't return a brand new dict with only one key!

```python
def compliment_node(state: AgentState) -> AgentState:
    name = state["name"]
    compliment = f"{name}, you're doing an amazing job learning LangGraph!"
    return {**state, "compliment": compliment}  # ✅ concatenate, not replace
```

### 3. Graph Wiring

```
START → compliment_node → END
```

```python
graph = StateGraph(AgentState)
graph.add_node("compliment_node", compliment_node)
graph.set_entry_point("compliment_node")
graph.add_edge("compliment_node", END)
app = graph.compile()
```

### 4. Invocation

```python
result = app.invoke({"name": "Bob", "compliment": ""})
print(result["compliment"])
# Bob, you're doing an amazing job learning LangGraph!
```

---

## 🔁 Graph Flow Diagram

```
┌─────────┐       ┌──────────────────┐       ┌─────┐
│  START  │──────▶│  compliment_node │──────▶│ END │
└─────────┘       └──────────────────┘       └─────┘
```

---

## ❌ Common Mistake — Replacing State Instead of Merging

```python
# ❌ WRONG — loses all other state keys
return {"compliment": compliment}

# ✅ CORRECT — merges into existing state
return {**state, "compliment": compliment}
```

---

## 📚 Resources

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LangGraph GitHub](https://github.com/langchain-ai/langgraph)
- [LangChain Python Docs](https://python.langchain.com/)

---

## 📝 License

This project is for educational purposes as part of the LangGraph Beginners Course.
