from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings

text = """
Your long document content goes here. 
This is the text that the SemanticChunker will analyze 
to find meaningful breaks based on the embeddings.
"""

embeddings = OpenAIEmbeddings()

semantic_splitter = SemanticChunker(
    embeddings, 
    breakpoint_threshold_type="standard_deviation"
)


semantic_chunks = semantic_splitter.split_text(text)

print(f"Semantic Chunks found: {len(semantic_chunks)}")