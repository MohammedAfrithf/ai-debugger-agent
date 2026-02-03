# AI Debugger Agent 🧠

An AI-powered debugger agent built using LangGraph and Groq LLM.
The agent dynamically detects programming languages, identifies errors,
and suggests fixes using tool-based reasoning.

## Tech Stack
- Python
- Flask
- LangGraph
- LangChain
- Groq LLM
- HTML, CSS, JavaScript

## Features
- Dynamic tool selection (no if-else)
- Multi-language code debugging
- Agent-based reasoning
- Simple frontend UI

## How it works
1. User submits code and query
2. LLM reasons over the input
3. Agent decides which tool to use
4. Tool executes and returns results
5. LLM explains the outcome
