# Day 3 – Understanding Language Models and Embeddings

 **Day 3** of my Generative AI and LangChain learning journey! On this day, I focused on understanding **Language Models (LMs)** and **Embedding Models**, their types, differences, and applications.  

---

## 1. What are Language Models?

Language Models are **crucial components of AI frameworks** designed to facilitate interactions with various LMs and embedding models. They allow us to process and generate text in meaningful ways.  

### Key Points:
- Language Models are a core part of AI model frameworks.  
- They help convert text input into meaningful outputs.  
- Models are broadly categorized into:
  1. **Language Models (LMs)**
  2. **Embedding Models**

---

## 2. Types of Models

### 2.1 Language Models (LMs)
- **Input:** Text  
- **Output:** Generated Text  

**Types of LMs**:
- **LLMs (Large Language Models)**  
  - General-purpose models  
  - No built-in memory  
  - Used for text generation  
  - **Examples:** GPT-3, LLaMA-2-7B  

- **Chat Models**  
  - Designed for conversational tasks and multi-turn conversations  
  - Support conversation history  
  - Allow assignment of roles (user, assistant, system)  
  - **Examples:** GPT-4, GPT-3.5 Turbo, LLaMA 2-Chat  

### 2.2 Embedding Models
- **Input:** Text  
- **Output:** Numeric vectors (representing semantics)  
- **Applications:** Semantic search, similarity comparisons, and other vector-based tasks  

---

## 3. Open Source vs Closed Source Models

| Model Type           | Closed Source Examples       | Open Source Examples |
|---------------------|----------------------------|--------------------|
| Language Models      | OpenAI Cloud, Gemini        | Hugging Face       |
| Embedding Models     | OpenAI Embeddings           | Hugging Face       |

---

## 4. Differences Between LLMs and Chat Models

| Feature                  | LLMs                                | Chat Models                          |
|--------------------------|------------------------------------|-------------------------------------|
| Purpose                  | General text generation            | Conversational/multi-turn tasks     |
| Built-in memory          | No                                  | Yes (conversation history)          |
| Role assignment          | Cannot assign user/assistant roles | Supports role assignments            |
| Examples                 | GPT-3, LLaMA 2 7B                  | GPT-4, GPT-3.5 Turbo, LLaMA 2 Chat |

---

## 5. Summary

On Day 3, I learned about:  
- The definition and purpose of Language Models  
- Types of models: LMs vs Embeddings  
- Differences between LLMs and Chat Models  
- Closed source vs Open source examples for both LMs and embeddings  

This foundational knowledge will help me in building **AI-powered applications** using LangChain and other frameworks.  

---

## 📚 References
- [OpenAI API](https://platform.openai.com/docs)  
- [Hugging Face Models](https://huggingface.co/models)  
- [LLaMA 2 Documentation](https://ai.meta.com/llama/)
