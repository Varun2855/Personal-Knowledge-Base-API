# Personal Knowledge Base API

A FastAPI backend application that allows users to securely create, manage, and retrieve personal notes with user-based authorization. The project is designed as a scalable backend foundation for an AI-powered personal knowledge assistant using Retrieval-Augmented Generation (RAG).

## Overview

This API provides authenticated users with isolated note storage. Each user can perform CRUD operations on their own notes while access from other users is restricted through JWT-based authentication.

The system follows a modular backend architecture using FastAPI dependencies, SQLAlchemy ORM models, and PostgreSQL persistence.

## Features

- JWT authentication (register and login)
- User-scoped authorization
- Create, read, update, and delete notes
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
- Uvicorn


## Authentication

1. Register a new user.
2. Login to obtain an access token.
3. Authorize requests using the token in Swagger UI.
4. Access protected note endpoints.

All notes are accessible only to their owner.

## API Endpoints

Auth:
- POST /auth/register
- POST /auth/login

Notes:
- POST /notes/
- GET /notes/
- GET /notes/{note_id}
- PUT /notes/{note_id}
- DELETE /notes/{note_id}

To enable the AI endpoint:

1. Create an account at https://openrouter.ai
2. Generate an API key
3. Add the following to your .env file:

OPENROUTER_API_KEY=your_key_here
OPENROUTER_MODEL=any_model_from_openrouter

4. Restart the server.

Note: Model availability depends on your OpenRouter account and credits.
