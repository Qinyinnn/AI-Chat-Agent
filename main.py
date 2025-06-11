# LangChain is a Python (and JS) framework that helps developers build applications powered by large language models (LLMs)
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv # Loads environment variables
from requests import get # lets you fetch data from a URL, like calling an API or loading a webpage
from datetime import datetime # accesses date and time information
import pytz # lets you work with time zones
import pyshorteners # lets you shorten URLs
from sympy import symbols, diff, integrate, simplify, parse_expr
import sympy

load_dotenv() # Load environment variables

@tool
def identify_assistant(question: str = "") -> str:
    """Responds to questions about identity, name, introduction, or role. Use this for any questions about who the assistant is."""
    responses = {
        "name": "My name is Youri",
        "role": "I'm your personal assistant",
        "full": "My name is Youri. I'm your personal assistant."
    }    
    
    if "name" in question.lower():
        return responses["name"]
    elif "role" in question.lower() or "what do you do" in question.lower():
        return responses["role"]
    else:
        return responses["full"]

@tool
def calculator(expression: str) -> str:
    """Performs calculus operations including derivatives, integrals, and simplification.
    Examples:
    - Derivative: 'derivative of x^2'
    - Integral: 'integrate 2x + 1'
    - Simplify: 'simplify x^2 + 2*x^2'
    - Basic math: '2 + 3*x'"""
    
    print("Calculus tool called.")
    try:
        x = symbols('x')
        
        # Handle different types of calculations
        if 'derivative' in expression.lower():
            expr = expression.lower().replace('derivative of', '').strip()
            parsed_expr = parse_expr(expr)
            result = diff(parsed_expr, x)
            return f"The derivative of {expr} with respect to x is {result}"
            
        elif 'integrate' in expression.lower():
            expr = expression.lower().replace('integrate', '').strip()
            parsed_expr = parse_expr(expr)
            result = integrate(parsed_expr, x)
            return f"The integral of {expr} with respect to x is {result} + C, where C is the constant of integration"

        elif 'simplify' in expression.lower():
            expr = expression.lower().replace('simplify', '').strip()
            parsed_expr = parse_expr(expr)
            result = simplify(parsed_expr)
            return f"The simplified expression of {expr} is {result}"

        else:
            # Handle basic arithmetic
            result = parse_expr(expression)
            return f"The result is {result}"

    except Exception as e:
        return f"Error: {str(e)}. Please check your expression format."
    
@tool
def calculator(a: float, b: float) -> str:
    # LLM will use this description to understand what the tool does and decide when to call it
    """Useful for performing basic arithmetic calculations with numbers"""
    
    print("Tool has been called.")
    return f"The sum of {a} and {b} is {a + b}"

@tool
def get_time(timezone: str) -> str:
    """Gets the current time in the specified timezone"""
    print("Tool has been called.")
    try:
        tz = pytz.timezone(timezone)
        current_time = datetime.now(tz)
        return f"Current time in {timezone} is {current_time.strftime('%Y-%m-%d %H:%M:%S')}"
    except pytz.UnknownTimeZoneError:
        return f"Unknown timezone: {timezone}. Please provide a valid timezone."
    
@tool
def shorten_url(url: str) -> str:
    """Shortens a URL using an online URL shortening service"""
    print("Tool has been called.")
    s = pyshorteners.Shortener() # Create a Shortener object
    short_url = s.tinyurl.short(url) # Use the TinyURL service to shorten the URL
    return f"Here's your shortened URL: {short_url}"


def main():
    model = ChatOpenAI(temperature=0) # temperature=0: Deterministic (always the same output for the same input), use for maths

    tools = [calculator, get_time, shorten_url, identify_assistant] # List of tools that the agent can use
    agent_executor = create_react_agent(model, tools)

    print("Welcome! I'm Youri, your personal AI Assistant. How can I help you today? Type 'quit' to exit.")

    while True:
        user_input = input("\nYou: ").strip()
        if user_input == "quit":
            break

        print("\nYouri: ", end="") # The AI's name is Youri
        for chunk in agent_executor.stream( # Sends your input to the AI agent (streams the output of the agent as it generates it, instead of waiting for the whole answer to finish)
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]: # Checks if this chunk contains a message from the agent (not just internal thoughts or logs).
                for message in chunk["agent"]["messages"]:
                     print(message.content, end="") # Prints the AI's response without a new line, so it looks like it's typing
        print()

if __name__ == "__main__":
    main()