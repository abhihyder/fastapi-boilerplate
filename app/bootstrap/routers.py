import importlib
import os

def setup_routers(app):
    routes_dir = os.path.join(os.path.dirname(__file__), "../routes")

    for filename in os.listdir(routes_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = f"app.routes.{filename[:-3]}"
            module = importlib.import_module(module_name)

            router = getattr(module, "router", None)
            config = getattr(module, "route_config", {})

            if router:
                app.include_router(
                    router,
                    prefix=config.get("prefix", ""),
                    tags=config.get("tags", None),
                    dependencies=config.get("dependencies", None),
                    responses=config.get("responses", None),
                )
