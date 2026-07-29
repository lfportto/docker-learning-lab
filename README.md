# Docker Learning Lab

📄 [English version](README_English.md)

## Descrição do Projeto
O **Docker Learning Lab** é um projeto de estudos desenvolvido para praticar a criação de APIs com FastAPI, containerização de aplicações Python com Docker, orquestração com Docker Compose e persistência de dados utilizando PostgreSQL.

A ideia principal foi construir uma API REST simples para gerenciamento de livros, utilizando boas práticas de desenvolvimento e executando toda a aplicação em containers Docker.

Embora seja um projeto pequeno, ele reproduz uma arquitetura muito próxima da utilizada em aplicações reais:

- API em um container
- Banco PostgreSQL em outro container
- Comunicação entre containers via Docker Compose
- Persistência de dados utilizando volumes
- Inicialização automática do banco utilizando init.sql

O projeto serviu como um laboratório para compreender conceitos que posteriormente serão utilizados em projetos maiores.

---

## Tecnologias Utilizadas
- Python 3.13
- FastAPI
- Uvicorn
- PostgreSQL 15
- Docker
- Docker Compose
- Bibliotecas Python: Pydantic, psycopg2, python-dotenv

---

## Arquitetura do Projeto
A figura abaixo mostra como foi estruturada a arquitetura por trás desse projeto:  
![architecture](https://github.com/user-attachments/assets/eeb1b7fe-9be1-46c7-8dc3-dbf62a55fd71)

## 📁 Estrutura do Projeto
```text
docker-learning-lab/
│
├── main.py
├── Dockerfile
├── compose.yaml
├── requirements.txt
├── init.sql
├── .env.example
├── README.md
└── ...
```

---

## Como executar

### 1. Clonar o repositório

```bash
git clone <url-do-repositório>
```

### 2. Criar o arquivo `.env`

Utilize o arquivo `.env.example` como base.

### 3. Executar os containers

```bash
docker compose up --build -d
```

Após alguns segundos, a API estará disponível em:

```
http://localhost:8000
```

Documentação automática:

```
http://localhost:8000/docs
```

---

## Endpoints

| Método | Endpoint | Descrição |
|---------|----------|-----------|
| GET | `/` | Informações da API |
| GET | `/books` | Lista todos os livros |
| POST | `/books` | Cria um novo livro |
| DELETE | `/books/{id}` | Remove um livro |
| GET | `/health` | Health Check |

---

## Estrutura da Tabela

Tabela **books**

| Campo | Tipo |
|--------|------|
| id | SERIAL |
| title | VARCHAR |
| author | VARCHAR |
| genre | VARCHAR |
| year | INTEGER |

---

## Documentação da API
![api_docs](https://github.com/user-attachments/assets/e607b37a-6824-41f0-be0e-3af4e74dc02c)

---

## Principais Aprendizados

Durante este projeto foram praticados conceitos importantes como:

- criação de APIs REST;
- utilização de variáveis de ambiente;
- criação de imagens Docker;
- execução de containers;
- comunicação entre containers;
- Docker Compose;
- Docker Networks;
- Docker Volumes e Persistência de dados
- inicialização automática do PostgreSQL utilizando scripts SQL;
- conexão entre FastAPI e PostgreSQL;
- documentação automática utilizando Swagger/OpenAPI.

---

## 🚀 Possíveis Melhorias Futuras
- Utilização de SQLAlchemy
- Conexão assíncrona com PostgreSQL
- Tratamento centralizado de exceções
- Testes automatizados
- CI/CD com GitHub Actions
- Paginação dos endpoints
- Atualização de livros (PUT/PATCH)
- Autenticação utilizando JWT

---

## Licença
Este projeto está licenciado sob a [Licença MIT](LICENSE).

---

## Tags
`#Docker` `#DockerCompose` `#FastAPI` `#Python` `#PostgreSQL` `#RESTAPI` `#Backend` `#API` `#Containerization` `#DevOps` `#SQL` `#Database` `#Microservices` `#OpenSource` `#SoftwareEngineering` `#SoftwareDevelopment` `#BackendDevelopment` `#PythonDeveloper` `#LearningProject` `#PortfolioProject` `#Programming` `#Tech` `#DockerLearningLab`