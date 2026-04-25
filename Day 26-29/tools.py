from langchain_community.tools import DuckDuckGoSearchRun, ShellTool
from langchain_core.tools import tool, StructuredTool, BaseTool
from pydantic import BaseModel, Field
from typing import Type

# ==========================================
# SECTION 1: BUILT-IN TOOLS
# ==========================================
print("--- Built-in Tools ---")

# DuckDuckGo Search
search_tool = DuckDuckGoSearchRun()
# print(search_tool.invoke("Current weather in Lahore"))

# Shell Tool (Requires langchain-experimental)
shell_tool = ShellTool()
# print(shell_tool.invoke("echo Hello from Shell"))


# ==========================================
# SECTION 2: CUSTOM TOOLS (3 METHODS)
# ==========================================
print("\n--- Custom Tools ---")

# --- METHOD A: @tool Decorator (Simple) ---
@tool
def multiply_simple(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

print(f"Method A Result: {multiply_simple.invoke({'a': 5, 'b': 3})}")


# --- METHOD B: StructuredTool & Pydantic (Strict) ---
class MultiplyInput(BaseModel):
    a: int = Field(description="First number")
    b: int = Field(description="Second number")

def multiply_func(a: int, b: int) -> int:
    return a * b

multiply_structured = StructuredTool.from_function(
    func=multiply_func,
    name="multiply_structured",
    description="Multiply two numbers precisely",
    args_schema=MultiplyInput
)

print(f"Method B Result: {multiply_structured.invoke({'a': 10, 'b': 4})}")


# --- METHOD C: BaseTool Class (Highly Customizable) ---
class MultiplyClassTool(BaseTool):
    name: str = "multiply_class"
    description: str = "Multiply two numbers using a class-based tool"
    args_schema: Type[BaseModel] = MultiplyInput

    def _run(self, a: int, b: int) -> int:
        return a * b

multiply_class = MultiplyClassTool()
print(f"Method C Result: {multiply_class.invoke({'a': 2, 'b': 50})}")


# ==========================================
# SECTION 3: TOOLKITS
# ==========================================
print("\n--- Toolkits ---")

@tool
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

class MathToolkit:
    def __init__(self):
        self.tools = [add, multiply_simple]

    def get_tools(self):
        return self.tools


toolkit = MathToolkit()
my_math_tools = toolkit.get_tools()

for t in my_math_tools:
    print(f"Toolkit Tool: {t.name} | Description: {t.description}")


# ==========================================
# SECTION 4: TOOL SCHEMA (JSON for LLM)
# ==========================================
import json
print("\n--- Tool Schema (JSON for LLM) ---")
print(json.dumps(multiply_simple.args, indent=2))