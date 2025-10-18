import importlib
import os

def setup_middlewares(app):
    middlewares_dir = os.path.join(os.path.dirname(__file__), "../middlewares")

    for filename in os.listdir(middlewares_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = f"app.middlewares.{filename[:-3]}"  # Remove '.py'
            module = importlib.import_module(module_name)
            
            # Assuming each middleware module has a 'setup' function
            if hasattr(module, "setup"):
                module.setup(app)
