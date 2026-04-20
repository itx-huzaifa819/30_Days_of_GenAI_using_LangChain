# 🔍 LangChain Output Parsers

> Notes and explanations covering output parsers in LangChain — their definitions, types, and practical usage.

---

## Table of Contents

1. [Definition of Output Parsers](#1-definition-of-output-parsers)
2. [Types of Output Parsers](#2-types-of-output-parsers)
3. [Summary](#3-summary)
4. [References](#references)

---

## 1. Definition of Output Parsers

**Output parsers** in LangChain help convert LLM (Large Language Model) responses into structured formats such as:

- JSON
- CSV
- Pydantic models
- And more

### Why Use Output Parsers?

| Benefit | Description |
|---------|-------------|
| ✅ **Consistency** | Ensure uniform structure across LLM responses |
| 🛡️ **Validation** | Verify that outputs conform to expected formats |
| ⚙️ **Usability** | Make responses easier to consume in downstream applications |

---

## 2. Types of Output Parsers

LangChain provides **four main types** of output parsers:

### 🔤 1. String Output Parser
- The simplest type of output parser
- Parses LLM output and returns it as a **plain string**

### 🗂️ 2. JSON Output Parser
- Forces the LLM to return output in **JSON format**
- Does **not enforce a schema** — only ensures valid JSON structure

### 🧱 3. Structured Output Parser
- Extracts **strictly structured JSON data** from LLM responses
- Uses **pre-defined field schemas** to guarantee correct structure

### 🧬 4. Pydantic Output Parser
- Uses **Pydantic models** to enforce schema validation
- Validates LLM responses according to the model definition
- Provides the highest level of consistency and type safety

#### Key Benefits of Pydantic Output Parser

| Benefit | Description |
|---------|-------------|
| 🔒 **Strict Schema Enforcement** | Guarantees LLM output matches the exact structure defined in the Pydantic model |
| 🛡️ **Type Safety** | Ensures every field has the correct data type, catching errors before they reach your app |
| ✅ **Easy Validation** | Built-in Pydantic validation automatically rejects malformed or incomplete responses |
| 🔗 **Seamless Integration** | Works natively with Python type hints and integrates smoothly into LangChain pipelines |

---

## 3. Summary

| Parser Type | Output Format | Schema Enforcement |
|-------------|---------------|:-----------------:|
| **String** | Plain string | ❌ |
| **JSON** | JSON (unvalidated) | ❌ |
| **Structured** | JSON with pre-defined fields | ✅ |
| **Pydantic** | JSON validated by Pydantic model | ✅ |

---

## References

- Concepts derived from lecture notes on **LangChain Output Parsers**
- Application of parsers ensures **validation, consistency, and ease of use** in LLM-powered applications
