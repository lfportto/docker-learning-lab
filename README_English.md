# Docker Learning Lab

📄 [Versão em português](README.md)

## Project Description
**Docker Learning Lab** is a study project developed to practice building APIs with FastAPI, containerizing Python applications with Docker, orchestrating services with Docker Compose, and persisting data using PostgreSQL.

The main goal was to build a simple REST API for book management while following development best practices and running the entire application inside Docker containers. This project is designed to run entirely with Docker Compose. As long as Docker is installed, PostgreSQL is automatically created and configured, eliminating the need to install it—or any other dependencies—locally.

Although it is a small project, it reproduces an architecture very similar to what is commonly found in real-world applications:

* API running in its own container
* PostgreSQL database running in a separate container
* Communication between containers through Docker Compose
* Data persistence using Docker Volumes
* Automatic database initialization using init.sql

This project served as a hands-on laboratory to better understand concepts that will later be applied in larger projects.

---

## Technologies Used
* Python 3.13
* FastAPI
* Uvicorn
* PostgreSQL 15
* Docker
* Docker Compose
* Python libraries: Pydantic, psycopg2, python-dotenv

---

## Project Architecture
The diagram below illustrates the architecture implemented in this project:
![architecture](https://github.com/user-attachments/assets/eeb1b7fe-9be1-46c7-8dc3-dbf62a55fd71)

## 📁 Project Structure
```text
docker-learning-lab/
    ├── assets/
    │   ├── FastAPI_docs.jpeg
    │   └── project_architecture.png
    ├── .dockerignore
    ├── .env.example
    ├── .gitignore
    ├── compose.yaml
    ├── Dockerfile
    ├── init.sql
    ├── LICENSE
    ├── main.py
    ├── README_English.md
    ├── README.md
    └── requirements.txt
```

---

## How to Run
> **Prerequisites:** Docker Desktop (or Docker Engine + Docker Compose)  
> No additional installation is required. PostgreSQL runs inside a container and is automatically configured when the project starts.

### 1. Clone the repository
```bash
git clone https://github.com/lfportto/docker-learning-lab
```

### 2. Create the `.env` file
Use the `.env.example` file as a template.

### 3. Start the containers
```bash
docker compose up --build -d
```

After a few seconds, the API will be available at:

```
http://localhost:8000
```

Automatic API documentation:

```
http://localhost:8000/docs
```

---

## Endpoints
| Method | Endpoint      | Description       |
| ------ | ------------- | ----------------- |
| GET    | `/`           | API information   |
| GET    | `/books`      | List all books    |
| POST   | `/books`      | Create a new book |
| DELETE | `/books/{id}` | Delete a book     |
| GET    | `/health`     | Health check      |

---

## Database Table Structure
**books** table
| Column | Type    |
| ------ | ------- |
| id     | SERIAL  |
| title  | VARCHAR |
| author | VARCHAR |
| genre  | VARCHAR |
| year   | INTEGER |

---

## API Documentation
![api\_docs](https://github.com/user-attachments/assets/e607b37a-6824-41f0-be0e-3af4e74dc02c)

---

## Key Learnings
Throughout this project, the following concepts were explored and practiced:
* Building REST APIs;
* Using environment variables;
* Creating Docker images;
* Running containers;
* Communication between containers;
* Docker Compose;
* Docker Networks;
* Docker Volumes and data persistence;
* Automatic PostgreSQL initialization using SQL scripts;
* Connecting FastAPI to PostgreSQL;
* Automatic API documentation with Swagger/OpenAPI.

---

## 🚀 Possible Future Improvements
* Migrate to SQLAlchemy
* Asynchronous PostgreSQL connection
* Centralized exception handling
* Automated testing
* CI/CD with GitHub Actions
* Endpoint pagination
* Book update endpoints (PUT/PATCH)
* JWT-based authentication

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Tags
`#Docker` `#DockerCompose` `#FastAPI` `#Python` `#PostgreSQL` `#RESTAPI` `#Backend` `#API` `#Containerization` `#DevOps` `#SQL` `#Database` `#Microservices` `#OpenSource` `#SoftwareEngineering` `#SoftwareDevelopment` `#BackendDevelopment` `#PythonDeveloper` `#LearningProject` `#PortfolioProject` `#Programming` `#Tech` `#DockerLearningLab`
