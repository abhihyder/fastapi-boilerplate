# 🚀 FastAPI Boilerplate

A clean, modular FastAPI boilerplate with auto-discovery of routes and middlewares, providing a solid foundation for building scalable REST APIs.

---

## ✨ Features

- **Auto-discovery of routes** - Automatically loads all routes from the `app/routes` directory
- **Auto-discovery of middlewares** - Automatically applies all middlewares from the `app/middlewares` directory
- **Modular architecture** - Clean separation of concerns with organized folder structure
- **Request/Response validation** - Built-in Pydantic models for data validation
- **CORS enabled** - Pre-configured CORS middleware
- **Environment-based configuration** - Easy configuration via `.env` files
- **Poetry dependency management** - Modern Python dependency management
- **Hot-reload support** - Development mode with auto-reload

---

## 🔧 Prerequisites

Before running the project, ensure the following are installed on your system:

- **Python 3.10+**
- **Poetry** for dependency management  
  👉 Install it via:  
  ```bash
  curl -sSL https://install.python-poetry.org | python3 -
  ```

---

## 📁 Project Structure

```
.
├── app/
│   ├── main.py                 # FastAPI application entry point
│   ├── bootstrap/
│   │   ├── middlewares.py      # Auto-loads middlewares
│   │   └── routers.py          # Auto-loads routes
│   ├── controllers/
│   │   └── test_controller.py  # Test controller
│   ├── middlewares/
│   │   └── cors.py             # CORS middleware configuration
│   ├── routes/
│   │   └── api.py              # API routes (auto-discovered)
│   ├── requests/
│   │   └── hashtag.py          # Request schemas
│   ├── responses/
│   │   └── hashtag.py          # Response schemas
│   └── services/
│       └── test.py             # Business logic services
├── run.py                      # Application runner
├── pyproject.toml              # Poetry configuration
├── .env.example                # Example environment variables
├── .gitignore                  # Git ignore rules
└── README.md                   # This file
```

---

## 🧑‍💻 Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd fastapi-boilerplate
```

### 2. Install dependencies

```bash
poetry install
```

### 3. Configure environment variables

Copy the example environment file and configure it:

```bash
cp .env.example .env
```

Edit `.env` with your settings:

```env
APP_PORT=8080
```

### 4. Run the application

#### Development mode (with hot-reload):
```bash
poetry run dev
```

#### Production mode:
```bash
poetry run start
```

The API will be available at: `http://localhost:8080`

---

## 📖 API Documentation

Once the server is running, you can access:

- **Swagger UI**: `http://localhost:8080/docs`
- **ReDoc**: `http://localhost:8080/redoc`


---

## 🛠️ Adding New Features

### Adding a new route

1. Create a new file in `app/routes/` (e.g., `user.py`)
2. Define your router with configuration:

```python
from fastapi import APIRouter

route_config = {
    "prefix": "/users",
    "tags": ["Users"]
}

router = APIRouter()

@router.get("/")
def get_users():
    return {"users": []}
```

The route will be automatically discovered and registered!

### Adding a new middleware

1. Create a new file in `app/middlewares/` (e.g., `auth.py`)
2. Define a `setup` function:

```python
from fastapi import FastAPI

def setup(app: FastAPI):
    # Your middleware logic
    pass
```

The middleware will be automatically applied!

### Adding request/response schemas

- Add request schemas in `app/requests/`
- Add response schemas in `app/responses/`

Use Pydantic's `BaseModel` for validation:

```python
from pydantic import BaseModel

class UserRequest(BaseModel):
    name: str
    email: str
```

---

## 📦 Dependencies

Core dependencies defined in [pyproject.toml](pyproject.toml):

- `fastapi` - Modern web framework for building APIs
- `uvicorn[standard]` - ASGI server
- `python-dotenv` - Environment variable management
- `requests` - HTTP client library

---

## 🗂️ Key Files

- [`run.py`](run.py) - Application entry point with dev/prod modes
- [`app/main.py`](app/main.py) - FastAPI application initialization
- [`app/bootstrap/routers.py`](app/bootstrap/routers.py) - Auto-discovery logic for routes
- [`app/bootstrap/middlewares.py`](app/bootstrap/middlewares.py) - Auto-discovery logic for middlewares

---

## 🔒 Security Notes

- Update CORS origins in [`app/middlewares/cors.py`](app/middlewares/cors.py) for production
- Add authentication middleware as needed
- Keep sensitive data in `.env` file (never commit it!)

---

## 📝 License

This project is open source and available under the MIT License.

---

## 👤 Author

**Tofayel Hyder Abhi**
- Email: abhihyder7@gmail.com

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

---

## ⭐ Show your support

Give a ⭐️ if this project helped you!