import uvicorn
import os
from dotenv import load_dotenv
load_dotenv()

APP_PORT = int(os.getenv("APP_PORT", 8000))

def main(reload: bool = True):
    uvicorn.run("app.main:app", host="0.0.0.0", port=APP_PORT, reload=reload)

def dev():
    main(reload=True)

def start():
    main(reload=False)
