# 🤖 LangGraph Personalized Compliment Agent

A simple LangGraph workflow that generates personalized compliments based on a given name.  
Built to understand the fundamentals of graph-based workflows, state management, and node execution in LangGraph using Python.

---

## 📋 Project Overview

| Field | Details |
|-------|---------|
| **Project** | Personalized Compliment Agent |
| **Framework** | LangGraph |
| **Language** | Python |
| **Input** | `{"name": "Bob"}` |
| **Output** | `"Bob, you're doing an amazing job learning LangGraph!"` |
| **Core Concept** | State management and graph execution |
| **Workflow Type** | Single-node graph |

---

## 🗂️ Project Structure

```bash
compliment-agent/
│
├── compliment_agent.py    # Main LangGraph workflow
├── requirements.txt       # Project dependencies
├── .gitignore             # Ignore unnecessary files
└── README.md              # Project documentation
```

---

## ⚙️ Requirements

- Python 3.9+
- LangGraph
- LangChain Core

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 📦 requirements.txt

```txt
langgraph>=0.2.0
langchain-core>=0.2.0
typing-extensions>=4.5.0
```

---

## 🚀 Running the Project

```bash
python compliment_agent.py
```

---

## ✅ Example Output

```python
Input : {'name': 'Bob'}

Output:
"Bob, you're doing an amazing job learning LangGraph!"
```

### Additional Examples

```python
Output:
"Alice, you're doing an amazing job learning LangGraph!"

Output:
"Charlie, you're doing an amazing job learning LangGraph!"

Output:
"Diana, you're doing an amazing job learning LangGraph!"
```

---

# 🧠 Core Concepts

## 1. Agent State (`TypedDict`)

The graph state defines the data shared between nodes during execution.

```python
class AgentState(TypedDict):
    name: str
    compliment: str
```

### Fields

| Field | Purpose |
|------|---------|
| `name` | Stores the user's name |
| `compliment` | Stores the generated compliment |

---

## 2. Node Function — `compliment_node`

Each node receives the current graph state, processes it, and returns an updated state.

```python
def compliment_node(state: AgentState) -> AgentState:
    name = state["name"]

    compliment = (
        f"{name}, you're doing an amazing job learning LangGraph!"
    )

    return {
        **state,
        "compliment": compliment
    }
```

### Important

Always merge the existing state instead of replacing it completely.

✅ Correct:

```python
return {
    **state,
    "compliment": compliment
}
```

❌ Incorrect:

```python
return {
    "compliment": compliment
}
```

The incorrect approach removes all previously stored state values.

---

## 3. Graph Construction

The workflow is built using `StateGraph`.

```python
graph = StateGraph(AgentState)

graph.add_node(
    "compliment_node",
    compliment_node
)

graph.set_entry_point("compliment_node")

graph.add_edge(
    "compliment_node",
    END
)

app = graph.compile()
```

---

## 🔁 Workflow Execution

```text
START
   │
   ▼
compliment_node
   │
   ▼
  END
```

---

## 📊 Graph Flow Diagram

```text
┌─────────┐       ┌──────────────────┐       ┌─────┐
│  START  │──────▶│  compliment_node │──────▶│ END │
└─────────┘       └──────────────────┘       └─────┘
```

---

## ▶️ Invoking the Workflow

```python
result = app.invoke({
    "name": "Bob",
    "compliment": ""
})

print(result["compliment"])
```

### Output

```python
Bob, you're doing an amazing job learning LangGraph!
```

---

# 🛠️ .gitignore

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log

# Environment
.env
```

---

# ⚠️ Troubleshooting

## ModuleNotFoundError

Install the dependencies again:

```bash
pip install -r requirements.txt
```

---

## Python Version Check

```bash
python --version
```

Use Python 3.9 or higher.

---

## Virtual Environment Activation

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

# 📚 Resources

- LangGraph Documentation  
- LangGraph GitHub Repository  
- LangChain Python Documentation  

---

# 🚀 Possible Improvements

Some ideas for extending the project:

- Multiple graph nodes
- Conditional routing
- Memory persistence
- LLM-based compliment generation
- API integration
- Logging and monitoring

---

# 📝 License

MIT License

---

# 🤝 Contributing

Contributions and improvements are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Open a pull request

---

# 📌 Notes

This project focuses on understanding:
- Graph workflows
- Stateful execution
- Node transitions
- LangGraph fundamentals

It serves as a clean starting point for building more advanced LangGraph-based systems.
