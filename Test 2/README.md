# Project Outlines


## Project Structure

The project structure follows the given outline:

- **app/**
  - Contains the core FastAPI application files.
  - **api/**
    - Modules for handling API endpoints for managing books, authors, and clients.
  - **crud/**
    - Implements CRUD operations for books, authors, and clients.
  - **database/**
    - Database-related files (connection, models, session).
  - **schemas/**
    - Defines Pydantic schemas for entities (books, authors, clients).
  - **dependencies.py**
    - Lists project dependencies.
  - **main.py**
    - Entry point of the FastAPI application.

- **migrations/**
  - Database migration scripts.

- **books_api_postman_collection.json**
  - Postman collection file containing API request samples.

- **docker-compose.yml**
  - Docker Compose configuration for deployment.

- **Dockerfile**
  - Configuration for building the Docker image.

- **requirements.txt**
  - List of Python dependencies.

- **startup.sh**
  - Initialization script for the application.

## Implementation Steps

### 1. Entity Definition and CRUD Operations

- **Books, Authors, and Clients Entities:**
  - Defined entity attributes according to the requirements.
  - Implemented CRUD operations for managing books, authors, and clients in respective `crud/` modules.

### 2. API Endpoints

- **API Methods Implementation:**
  - Added API endpoints as per the required functionality using FastAPI in `api/` modules.
  - Endpoints for adding/editing books, managing authors, creating clients, linking/unlinking clients with books, and retrieving book lists based on filtering options.

### 3. Database Setup

- **PostgreSQL Integration:**
  - Established connection and setup models for books, authors, and clients in the `database/` directory.
  - Wrote migration scripts for database versioning in the `migrations/` directory.

### 4. Security and Authentication

- **Bearer Authentication:**
  - Secured the API using Bearer authentication with a static token list.

### 5. Client-Book Association

- **Client Identification and Book Borrowing:**
  - Implemented client-book association and retrieval based on access token without transmitting client identifiers.

### 6. Docker Deployment

- **Containerization:**
  - Configured Docker Compose for deploying the entire infrastructure.
  - Created Dockerfile for building the FastAPI application image.

### 7. Project Launch Guide

- **Launching the Project:**
  - Provided a detailed guide on how to launch the project in the `Project Launch Guide` file.
  - Included steps for setting up Docker, running migrations, and starting the FastAPI application.
  

## Contribution
- Contributions and suggestions for improvement are welcome.
- Fork the repository, make changes, and submit pull requests for review.
