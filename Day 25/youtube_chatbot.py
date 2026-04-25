import os
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

os.environ["OPENAI_API_KEY"] = "OPENAI_API_KEY"

def fetch_transcript_safe(video_id):
    """
    YouTube se transcript nikalne ka sabse safe tarika.
    """
    try:
       
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
  
        try:
            transcript = transcript_list.find_transcript(['en', 'hi'])
        except NoTranscriptFound:
           
            transcript = next(iter(transcript_list))
            
        data = transcript.fetch()
        full_text = " ".join([item['text'] for item in data])
        return full_text
    
    except TranscriptsDisabled:
        return "ERROR: Is video par Subtitles/Captions band (disabled) hain."
    except NoTranscriptFound:
        return "ERROR: Is video ki transcript nahi mil saki."
    except Exception as e:
        return f"ERROR: Kuch technical masla hai: {str(e)}"

def build_rag_system(video_id):
   
    transcript_text = fetch_transcript_safe(video_id)
    
    if "ERROR" in transcript_text:
        return transcript_text

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_text(transcript_text)

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(chunks, embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

    template = """
    You are a YouTube video assistant. Answer the question based ONLY on the transcript provided.
    Transcript Context: {context}
    
    Question: {question}
    
    Answer clearly:
    """
    prompt = ChatPromptTemplate.from_template(template)
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    # Modular Chain
    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    return chain

# --- CHATBOT START ---

VIDEO_ID = "pJdMxwXBsk0" 


result = build_rag_system(VIDEO_ID)

if isinstance(result, str):
   
    print(result)
else:

    user_query = "What are the main concepts discussed in this video?"
    response = result.invoke(user_query)
    print("\n--- Chatbot Response ---\n")
    print(response)