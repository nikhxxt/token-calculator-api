# 🔐 Token-Based Calculator API
A secure, stateless FastAPI backend that performs basic arithmetic operations using JWT-based authorization. Designed for cloud deployment and professional portfolio presentation.

![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-green?logo=fastapi)
![JWT Auth](https://img.shields.io/badge/Auth-JWT-blue)
![Deploy-Render](https://img.shields.io/badge/Deploy-Render-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![Status](https://img.shields.io/badge/Status-Production--ready-brightgreen)


---

## 📚 Table of Contents

- [Features](#-features)
- [Authentication Flow](#-authentication-flow)
- [Calculation Endpoint](#-calculation-endpoint)
- [Why JWT Instead of Credentials](#-why-jwt-instead-of-credentials)
- [Tech Stack](#-tech-stack)
- [Deployment](#-deployment)
- [File Structure](#-file-structure)
- [Sample Curl Commands](#-sample-curl-commands)
- [License](#-license)

---

## 🚀 Features

- ✅ Token-based authentication (JWT)
- 🔐 Protected `/calculate` endpoint
- 🧮 Supports `add`, `sub`, `mul`, `div`
- ⏱️ Tokens expire after 15 minutes
- 📦 Ready for Render/Railway deployment

---

## 📬 Authentication Flow

### `POST /login`

Simulates form-based login using `OAuth2PasswordRequestForm`.

**Request (form data):**
```bash
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

---

## 🧮 Calculation Endpoint

### `POST /calculate`

Requires a valid Bearer token in the header.

**Headers:**
```http
Authorization: Bearer <JWT_TOKEN>
```

**Body:**
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
  "result": 15.0
}
```

---

## 🌐 Live Demo

You can test the API interactively using Swagger UI:

🔗 [Token Calculator API – Swagger Docs](https://token-calculator-api.onrender.com/docs#/default/calculate_calculate_post)

Use the `/login` endpoint to get a JWT token, then authorize and access `/calculate` securely.

---


## 🔐 Why JWT Instead of Credentials?

- **Stateless**: No session storage required
- **Secure**: Tokens are signed and expire
- **Scalable**: Ideal for cloud-native APIs
- **Decoupled**: Auth logic separated from resource access

---

## 🛠 Tech Stack

- FastAPI
- PyJWT
- OAuth2PasswordRequestForm
- HTTPBearer

---

## 🌐 Deployment

### Render Setup

- **Build Command**:
  ```bash
  pip install -r requirements.txt
  ```
- **Start Command**:
  ```bash
  uvicorn main:app --host 0.0.0.0 --port 10000
  ```
- **Environment Variable**:
  ```
  SECRET_KEY=SUREProED
  ```

---

## 📁 File Structure

```
token-calculator-api/
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## 🧪 Sample Curl Commands

```bash
# Login
curl -X POST -F "username=Bhargav" -F "password=any" https://your-app-url.onrender.com/login

# Calculate
curl -X POST https://your-app-url.onrender.com/calculate \
  -H "Authorization: Bearer <JWT_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"a": 10, "b": 5, "operation": "add"}'
```

---

## 📜 License


This project is licensed under the [MIT License](LICENSE).  

---
