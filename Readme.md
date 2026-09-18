# 🔐 Token-Based Calculator API

A FastAPI backend that demonstrates JWT-based authentication and protected arithmetic operations through REST APIs.

## 🚀 Features

- JWT-based authentication
- Protected `/calculate` endpoint
- Supports `add`, `sub`, `mul`, and `div` operations
- Token expiration
- OAuth2 Password Flow
- HTTP Bearer authentication
- Interactive Swagger API documentation
- Deployed on Render

## 🛠️ Tech Stack

- **Python**
- **FastAPI**
- **PyJWT**
- **OAuth2 Password Flow**
- **HTTPBearer**
- **Uvicorn**
- **Render**

## 🔑 Authentication

### `POST /login`

Send a username and password as form data to receive a JWT access token.

**Request:**

```text
username=Bhargav
password=any
````

**Response:**

```json
{
  "access_token": "<JWT_TOKEN>",
  "token_type": "bearer"
}
```

## 🧮 Calculate

### `POST /calculate`

Requires a valid JWT Bearer token.

**Request:**

```json
{
  "a": 10,
  "b": 5,
  "operation": "add"
}
```

**Response:**

```json
{
  "user": "Bhargav",
  "result": 15
}
```

## 🔐 How to Test

1. Open the live Swagger documentation.
2. Use `POST /login` with a username and password.
3. Copy the returned `access_token`.
4. Click **Authorize 🔒** in Swagger.
5. Enter `Bearer <JWT_TOKEN>`.
6. Click **Authorize**.
7. Test `POST /calculate`.

The `/calculate` endpoint requires a valid JWT token.

## 🌐 Live Demo

**Swagger API Documentation:**
[https://token-calculator-api.onrender.com/docs](https://token-calculator-api.onrender.com/docs)

Use Swagger UI to authenticate and test the API endpoints interactively.

## 📁 Project Structure

```text
token-calculator-api/
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 📄 License

This project is licensed under the MIT License.

