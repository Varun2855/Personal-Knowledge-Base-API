# Personal Knowledge Base API

A FastAPI backend application that allows users to securely create, manage, and retrieve personal notes with user-based authorization. The project is designed as a scalable backend foundation for an AI-powered personal knowledge assistant using Retrieval-Augmented Generation (RAG).

## Overview

This API provides authenticated users with isolated note storage. Each user can perform CRUD operations on their own notes while access from other users is restricted through JWT-based authentication.

The system follows a modular backend architecture using FastAPI dependencies, SQLAlchemy ORM models, and PostgreSQL persistence. The backend also includes an AI endpoint that allows users to ask questions about their stored notes using an external large language model.

## Features

- JWT authentication (register and login)
- User-scoped authorization
- Create, read, update, and delete notes
- AI-powered question answering over user notes
- PostgreSQL database integration
- Structured router-based architecture
- Pydantic schema validation
- API documentation via Swagger UI

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- OAuth2 + JWT
- External LLM API (OpenRouter compatible)
- Uvicorn

## Architecture

The application follows a modular backend architecture where each domain is separated into its own router and service layer.

Request Flow:

Client Request
→ FastAPI Router
→ Dependency Injection (Authentication / Database Session)
→ SQLAlchemy ORM (Database Interaction)
→ Business Logic Layer
→ Response Serialization (Pydantic)

For AI queries, the flow is extended:

User Question
→ Authentication Validation
→ Retrieve User Notes from Database
→ Construct Context from Notes
→ Send Prompt to External LLM API
→ Return Generated Answer


## Authentication
1. Register a new user.
2. Login to obtain an access token.
3. Authorize requests using the token in Swagger UI.
4. Access protected endpoints.

All notes are accessible only to their owner.


## AI Setup

To enable the AI endpoint:

1. Create an account with a compatible LLM provider (e.g., OpenRouter).
2. Generate an API key.
3. Add the following variables to a `.env` file:

OPENROUTER_API_KEY=your_api_key  
OPENROUTER_MODEL=your_model_name  

4. Restart the server.

Model availability depends on the provider and account credits.

## Future Work

- Embedding-based semantic search for notes
- Vector database integration (FAISS or PGVector)
- True Retrieval-Augmented Generation with chunked note retrieval
- Background task processing for embedding generation
- Rate limiting and request throttling
- Docker containerization for deployment
- Pagination and advanced filtering for notes
- Tagging and categorization system
- API usage analytics
- Frontend interface for interacting with the knowledge base