
# Week 3 Books API

## DESCRIPTION

A Books API for managing book information using FastAPI and a database.

## TECHNOLOGIES USED

- FastAPI for the API
- Uvicorn for running the API
- SQLAlchemy for interacting with the database using Python
- SQLite for the database

## INSTRUCTIONS

### Create the Virtual Environment

**MacOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install Packages

Inside terminal command:

```bash
python -m pip install -r requirements.txt
```

### Activate the API

Inside terminal command:

```bash
uvicorn main:app --reload
```

API URL: http://127.0.0.1:8000

FastAPI Docs: http://127.0.0.1:8000/docs

## TESTING

The API can be tested using FastAPI Docs or Postman.

### Get All Books

**Endpoint:** `GET /books`

Retrieves the books stored in the database.

### Create a Book

**Endpoint:** `POST /books`

Creates a new book using the information provided in the request body.

### Get One Book

**Endpoint:** `GET /books/{book_id}`

Retrieves a book using its ID.

## STATUS CODE DEFINITIONS

| Status Code | Meaning |
|---|---|
| 200 | Successful request |
| 201 | Resource created successfully |
| 404 | Requested resource not found |
| 422 | Invalid or missing required information |

