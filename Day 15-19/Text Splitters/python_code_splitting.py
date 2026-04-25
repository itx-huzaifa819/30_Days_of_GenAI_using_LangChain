from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

python_code = """
class Calculator:
    def add(self, a, b):
        return a + b
    
    def multiply(self, a, b):
        return a * b
"""

python_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, 
    chunk_size=50, 
    chunk_overlap=0
)

code_chunks = python_splitter.split_text(python_code)
print(f"Code Chunks: {len(code_chunks)}")