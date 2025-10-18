from fastapi import FastAPI
from app.bootstrap.routers import setup_routers
from app.bootstrap.middlewares import setup_middlewares

app = FastAPI()

# Apply middlewares
setup_middlewares(app)

# Set up routers
setup_routers(app)
