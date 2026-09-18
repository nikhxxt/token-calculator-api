# 🔐 Token-Based Calculator API

A FastAPI backend with JWT-based authentication and protected arithmetic operations.

## 🚀 Features

- JWT-based authentication
- Protected `/calculate` endpoint
- Supports `add`, `sub`, `mul`, and `div`
- Token expiration
- Interactive Swagger API documentation
- Deployed on Render

## 🛠 Tech Stack

- Python
- FastAPI
- PyJWT
- OAuth2 Password Flow
- HTTPBearer

## 🔑 Authentication

### `POST /login`

Send a username and password as form data to receive a JWT access token.

**Request:**

```text
username=Bhargav
password=any
```

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

1. Open the [Swagger Docs](https://token-calculator-api.onrender.com/docs).
2. Use `POST /login` with a username and password.
3. Copy the returned `access_token`.
4. Click **Authorize 🔒** in Swagger.
5. Enter `Bearer <JWT_TOKEN>`.
6. Click **Authorize** and test `POST /calculate`.

The `/calculate` endpoint requires a valid JWT token.

## 🌐 Live Demo

**Swagger API Documentation:**  
https://token-calculator-api.onrender.com/docs

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
