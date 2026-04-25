from langchain_text_splitters import CharacterTextSplitter


text = "Exploration of space has always fascinated humanity. From the moon landing to Mars rovers..."

splitter = CharacterTextSplitter(
    chunk_size=100,      
    chunk_overlap=20,    
    separator=""         
)

chunks = splitter.split_text(text)

print(f"Total Chunks: {len(chunks)}")
print(f"First Chunk: {chunks[0]}")