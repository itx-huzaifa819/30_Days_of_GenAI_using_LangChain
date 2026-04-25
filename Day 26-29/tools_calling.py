import os
import json
import requests
from typing import Annotated
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool, InjectedToolArg
from langchain_core.messages import HumanMessage, ToolMessage

# API Keys set karein
os.environ["OPENAI_API_KEY"] = "openai_key"
EXCHANGE_RATE_API_KEY = "api_key"

# ==========================================
# 1. DEFINE TOOLS
# ==========================================

@tool
def get_conversion_factor(base_currency: str, target_currency: str) -> float:
    """Fetches the real-time currency conversion factor between base and target currency."""
    url = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_RATE_API_KEY}/pair/{base_currency}/{target_currency}"
    response = requests.get(url).json()
    return response.get('conversion_rate')

@tool
def convert_amount(amount: float, rate: Annotated[float, InjectedToolArg]) -> float:
    """Calculates the target currency value using the amount and conversion rate."""
    return amount * rate

# ==========================================
# 2. BIND TOOLS TO LLM
# ==========================================

llm = ChatOpenAI(model="gpt-4o")
llm_with_tools = llm.bind_tools([get_conversion_factor, convert_amount])

# ==========================================
# 3. EXECUTION FLOW (The Logic)
# ==========================================

def run_currency_app(user_query):
    # Step 1: Initialize Messages
    messages = [HumanMessage(content=user_query)]
    print(f"\nUser: {user_query}")

    # Step 2: First LLM Call (Tool Calling)
    ai_msg = llm_with_tools.invoke(messages)
    messages.append(ai_msg)

    # Step 3: Handle Tool Execution
    current_rate = None
    
    # Loop through tool calls suggested by LLM
    for tool_call in ai_msg.tool_calls:
        print(f"\n[LLM suggests calling tool: {tool_call['name']}]")
        
        # Scenario 1: Fetching Rate
        if tool_call['name'] == 'get_conversion_factor':
            res = get_conversion_factor.invoke(tool_call)
            current_rate = json.loads(res.content) # Rate store kar liya
            messages.append(res)
            
        # Scenario 2: Calculation (Injection)
        elif tool_call['name'] == 'convert_amount':
            tool_call['args']['rate'] = current_rate 
            res = convert_amount.invoke(tool_call)
            messages.append(res)
    final_response = llm_with_tools.invoke(messages)
    print(f"\nAI: {final_response.content}")

# ==========================================
# 5. TEST IT
# ==========================================
run_currency_app("What is the conversion rate between USD and PKR, and how much is 50 USD in PKR?")