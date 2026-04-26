# 🦜🔗 30_Days_of_GenAI_using_LangChain

> **A 30-day learning challenge exploring Generative AI concepts using LangChain, including LLM applications, prompt engineering, agents, RAG pipelines, and AI-powered tools.**
---

## 🎯 What I Learned

- Fundamentals and architecture of LangChain
- Working with prompts, structured output, and output parsers
- Building and chaining LLM workflows using Chains and Runnables
- Document loaders, text splitters, vector stores, and retrievers
- Retrieval Augmented Generation (RAG) — theory and implementation
- Building functional chatbots and AI tools
- Tool calling and agent creation with LangChain
- Developing end-to-end AI systems

---

## 📅 30-Day Progress Log

| Day | Topic |
|-----|-------|
| Day 01 | Introduction to LangChain |
| Day 02 | LangChain Components & NLP Concepts |
| Day 03 | Understanding Language Models and Embeddings |
| Day 04 | Deep Dive into LangChain Models |
| Day 05 | Prompts in Language Models |
| Day 06 | Structured Output in LangChain |
| Day 07 | LangChain Output Parsers |
| Day 08 | Chains in LangChain |
| Day 09 | Sequential Chains in LangChain (practice) |
| Day 10 | Conditional & Parallel Chains in LangChain (practice) |
| Day 11 | Simple Chains in LangChain (practice) |
| Day 12 | Complex Chains in LangChain (practice) |
| Day 13 | What are Runnables in LangChain |
| Day 14 | Runnables in LangChain — Part 2 |
| Day 15-19 | Document Loaders in LangChain |
| Day 20 | Vector Stores in LangChain |
| Day 21-24 | Retrievers in LangChain & Retrieval Augmented Generation (RAG) |
| Day 25 | YouTube Chatbot - Building a RAG System |
| Day 26-29 | Tools & Tool Calling in LangChain  |
| Day 30 | Building an End-to-End AI Agent & Final Review, Recap & Portfolio Polish |

---

## 📚 Curriculum Breakdown

### 🔰 Foundation (Days 1–7)
Getting started with LangChain's ecosystem and understanding its core building blocks.

| Video | Title | Key Concepts |
|-------|-------|-------------|
| Intro | GenAI Roadmap for Beginners | GenAI landscape, learning path, tools overview |
| 00 | Generative AI using LangChain | What is LangChain, why use it, course overview |
| 01 | Introduction to LangChain | Architecture, installation, first LLM call |
| 02 | LangChain Components | Models, Prompts, Chains, Memory, Agents, Tools overview |
| 03 | LangChain Models | LLMs vs Chat Models, embeddings, model wrappers |

### 🔧 Prompts & Output Handling (Days 8–13)
Mastering how to communicate with and structure responses from LLMs.

| Video | Title | Key Concepts |
|-------|-------|-------------|
| 04 | Prompts in LangChain | PromptTemplate, ChatPromptTemplate, few-shot prompting |
| 05 | Structured Output in LangChain | `.with_structured_output()`, Pydantic models, JSON output |
| 06 | Output Parsers in LangChain | StrOutputParser, PydanticOutputParser, CommaSeparatedParser |

### ⛓️ Chains & Runnables (Days 14–17)
Building composable workflows and understanding the LCEL (LangChain Expression Language).

| Video | Title | Key Concepts |
|-------|-------|-------------|
| 07 | Chains in LangChain | `LLMChain`, `SequentialChain`, chain composition |
| 08 | What are Runnables in LangChain | LCEL, `RunnableSequence`, `RunnablePassthrough`, pipe operator |
| 09 | LangChain Runnables — Part 2 | `RunnableParallel`, `RunnableLambda`, branching logic |

### 📄 Data & Retrieval (Days 18–24)
Working with real-world documents — loading, splitting, storing, and retrieving them.

| Video | Title | Key Concepts |
|-------|-------|-------------|
| 10 | Document Loaders in LangChain | PDF, CSV, web, YouTube loaders |
| 11 | Text Splitters in LangChain | `RecursiveCharacterTextSplitter`, chunk size & overlap |
| 12 | Vector Stores in LangChain | FAISS, Chroma, embedding storage & similarity search |
| 13 | Retrievers in LangChain | `VectorStoreRetriever`, MMR, contextual compression |
| 14 | Retrieval Augmented Generation (RAG) | What is RAG, RAG pipeline, retrieval + generation flow |

### 🤖 Projects & Agents (Days 25–30)
Applying everything to build real AI applications and autonomous agents.

| Video | Title | Key Concepts |
|-------|-------|-------------|
| 15 | YouTube Chatbot — Building a RAG System | End-to-end RAG chatbot powered by YouTube transcripts |
| 16 | Tools in LangChain | Built-in tools, custom tools, tool schema |
| 17 | Tool Calling in LangChain | Function calling, tool binding to LLMs |
| 18 | Building End-to-End AI Agent | `AgentExecutor`, ReAct agent, multi-step reasoning |

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-0.3.x-1C3C3C?style=flat&logo=langchain&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-412991?style=flat&logo=openai&logoColor=white)
![FAISS](https://img.shields.io/badge/FAISS-Vector%20Store-0055FF?style=flat)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat&logo=jupyter&logoColor=white)

- **Language:** Python 3.10+
- **Framework:** LangChain (LCEL)
- **LLMs:** OpenAI GPT-4o / GPT-3.5-turbo
- **Vector Stores:** FAISS, Chroma
- **Notebooks:** Jupyter / Google Colab
- **Version Control:** Git + GitHub

---

## 🚀 Key Projects Built

### 1. 🎥 YouTube RAG Chatbot (Day 25)
A retrieval-augmented chatbot that answers questions from any YouTube video's transcript.
- Loads transcripts using `YoutubeLoader`
- Chunks and embeds them with FAISS
- Answers queries using a RAG chain

### 2. 🤖 End-to-End AI Agent (Day 30)
An autonomous ReAct agent capable of multi-step reasoning and tool use.
- Uses `AgentExecutor` with custom + built-in tools
- Demonstrates tool calling and dynamic decision making
- Follows the Thought → Action → Observation loop

---

## 📖 Resources

| Resource | Link |
|----------|------|
| 📺 Playlist | [YouTube — CampusX](https://www.youtube.com/playlist?list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0) |
| 📚 Official LangChain Docs | [python.langchain.com](https://python.langchain.com) |

---



