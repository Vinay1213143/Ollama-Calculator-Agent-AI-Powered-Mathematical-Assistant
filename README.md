# 🤖 Ollama Calculator Agent

An AI-powered mathematical assistant built using **Python, LangChain, and Ollama (Llama 3.2)**. This project uses an intelligent AI agent that understands mathematical questions and selects appropriate calculator tools to perform accurate arithmetic operations.

## 🚀 Project Overview

The Ollama Calculator Agent allows users to ask mathematical questions in natural language. Instead of calculating everything directly through the language model, the agent uses custom Python tools to perform calculations.

It intelligently selects the required tools and provides clear answers to mathematical queries.

## ✨ Features

- Addition of two numbers
- Subtraction of two numbers
- Multiplication of two numbers
- Division with zero-division handling
- Percentage calculation
- Natural language mathematical queries
- Intelligent tool selection using LangChain Agents
- Local LLM integration using Ollama
- Interactive command-line interface

## 🛠️ Technologies Used

- **Python** – Core programming language
- **LangChain** – Agent creation and tool integration
- **LangChain Core** – Custom tool development
- **LangChain Ollama** – Ollama model integration
- **Ollama** – Local Large Language Model
- **Llama 3.2** – AI language model


## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Ollama-Calculator-Agent.git
```

### 2. Navigate to the Project Directory

```bash
cd Ollama-Calculator-Agent
```

### 3. Install Required Libraries

```bash
pip install langchain langchain-core langchain-ollama
```

### 4. Install Ollama

Download Ollama from:

https://ollama.com/

### 5. Download the Llama 3.2 Model

```bash
ollama pull llama3.2
```

### 6. Run the Application

```bash
python main.py
```

## 💻 Available Calculator Tools

| Tool | Description |
|---|---|
| `add()` | Adds two numbers |
| `subtract()` | Subtracts the second number from the first |
| `multiply()` | Multiplies two numbers |
| `divide()` | Divides two numbers |
| `percentage()` | Calculates a percentage of a value |

## 🧪 Example Usage

```text
======================================
       OLLAMA CALCULATOR AGENT
======================================
Model : llama2:latest
Type 'exit' to stop

Enter your question: What is 25% of 800?

Agent: 25% of 800 is 200.

Enter your question: Add 150 and 250

Agent: 150 + 250 = 400.

Enter your question: Multiply 25 by 10

Agent: 25 multiplied by 10 is 250.
```

## 🧠 How It Works

1. The user enters a mathematical question.
2. LangChain Agent receives the question.
3. The Llama 3.2 model understands the mathematical requirement.
4. The agent selects the appropriate calculator tool.
5. The Python function performs the calculation.
6. The agent returns the result with a clear explanation.

## 🎯 Learning Outcomes

Through this project, I explored:

- Building AI agents using LangChain.
- Creating custom tools with `@tool`.
- Integrating local LLMs using Ollama.
- Understanding AI tool calling.
- Using multiple tools to solve mathematical problems.
- Building interactive AI applications with Python.

## 🔮 Future Enhancements

- Add square root and power operations.
- Add scientific calculator functions.
- Build a Streamlit-based user interface.
- Maintain calculation history.
- Improve mathematical expression handling.

## 👨‍💻 Author

**Vinay Awari**

Computer Science Engineering Graduate | Python | AI | Generative AI | LangChain

[GitHub](https://github.com/Vinay1213143)

---

⭐ If you find this project useful, feel free to star the repository!
