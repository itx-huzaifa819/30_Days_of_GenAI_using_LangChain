from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """Space exploration is a multi-generational effort...
It involves robots and humans working together.

Mars is the next big goal for NASA and SpaceX."""


recursive_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

recursive_chunks = recursive_splitter.split_text(text)

for i, chunk in enumerate(recursive_chunks):
    print(f"Chunk {i+1}: {chunk}")