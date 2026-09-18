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

Send username and password as form data to receive a JWT access token.

```text
username=Bhargav
password=any

## Response:

{
  "access_token": "<JWT_TOKEN>",
  "token_type": "bearer"
}
🧮 Calculate
POST /calculate

Requires a valid JWT Bearer token.

Request:

{
  "a": 10,
  "b": 5,
  "operation": "add"
}

Response:

{
  "user": "Bhargav",
  "result": 15
}
🌐 Live Demo

Swagger API Documentation:

https://token-calculator-api.onrender.com/docs

Use /login to obtain a JWT token, then click Authorize in Swagger to test the protected /calculate endpoint.

📁 Project Structure
token-calculator-api/
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md

## 🔐 How to Test

1. Open the [Swagger Docs](https://token-calculator-api.onrender.com/docs).
2. Use `POST /login` with a username and password.
3. Copy the returned `access_token`.
4. Click **Authorize** 🔒 in Swagger.
5. Enter:
   `Bearer <JWT_TOKEN>`
6. Click **Authorize** and then test `POST /calculate`.

The `/calculate` endpoint requires a valid JWT token.
