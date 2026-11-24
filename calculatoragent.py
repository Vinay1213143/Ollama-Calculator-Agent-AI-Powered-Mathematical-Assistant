from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from langchain.agents import create_agent


@tool
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


@tool
def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


@tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


@tool
def divide(a: float, b: float) -> float:
    """Divide a by b."""

    if b == 0:
        return "Error: Cannot divide by zero"

    return a / b


@tool
def percentage(value: float, percent: float) -> float:
    """Calculate percentage of a value."""

    return (value * percent) / 100


tools = [
    add,
    subtract,
    multiply,
    divide,
    percentage
]



llm = ChatOllama(
    model="llama3.2:latest",
    temperature=0
)


agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="""
You are a helpful calculator agent.

Your job is to solve mathematical problems.

Rules:

1. Always use the available calculator tools
   for arithmetic calculations.

2. Select the appropriate tool.

3. You can use multiple tools if required.

4. Explain the final answer clearly.

5. Never guess the result of a calculation.
"""
)



def ask_calculator(question):

    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": question
                }
            ]
        }
    )

    return result["messages"][-1].content


if __name__ == "__main__":

    print("======================================")
    print("       OLLAMA CALCULATOR AGENT")
    print("======================================")
    print("Model : llama2:latest")
    print("Type 'exit' to stop")

    while True:

        question = input("\nEnter your question: ")

        if question.lower() in ["exit", "quit", "bye"]:
            print("Goodbye!")
            break

        try:

            answer = ask_calculator(question)

            print("\nAgent:", answer)

        except Exception as e:

            print("\nError:", e)