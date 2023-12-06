# Project Launch Guide

This guide provides step-by-step instructions on how to set up and launch the project, which includes managing books, authors, and clients using FastAPI, PostgreSQL, and Docker.

## Prerequisites

Ensure you have the following installed on your machine:

- **Docker:** Download and install Docker from the [official website](https://www.docker.com/get-started).

## Project Setup

1. **Clone the Repository:**  
   Clone the project repository using Git.

   ```bash
   git clone <repository_url>
   cd <project_directory>
   
2. **Configuration:**  
   Review and update configuration files if necessary, such as database connection details or any environment-specific settings.

## Launching the project

1. **Build and Start containers:**  
   Run Docker Compose to build and start the application containers.

   ```bash
   docker-compose up --build
  This command will orchestrate the setup and launch the entire infrastructure, including the FastAPI application, PostgreSQL database, and any associated services defined in the `docker-compose.yml` file.
   
2. **Migrate the Database:**  
   Once the containers are up and running, open a new terminal window (or use a separate terminal tab) and navigate to the project directory.

   Run the database migrations to set up the initial database schema.

   ```bash
   docker-compose exec app alembic upgrade head
This command applies the database migrations using Alembic, ensuring the database is properly configured according to the defined models.

3. **Access the API:**  
   Once the containers and migrations are successfully completed, you can access the API endpoints using an API client like Postman or cURL.

   -- API Endpoint: `http://localhost:8000`
   
4. **Testing with Postman:**  
   Utilize the provided Postman collection (`books_api_postman_collection.json`) to test various API functionalities.

   - Import the collection into Postman.
   - Use the collection's requests to test adding books, managing authors, creating clients, and linking/unlinking clients with books.
   - Verify the retrieval of book lists based on filtering options.
  
## Stopping the project

To stop and remove the containers while keeping the data intact:

   ```bash
   docker-compose down
```
This command stops and removes the containers, networks, and volumes defined in the `docker-compose.yml` file.
