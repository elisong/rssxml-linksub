from starlette.applications import Starlette
from starlette.config import Config
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles
from .api import Api
from .home import home
from .schema import schema


config = Config(".env")
DEBUG = config('DEBUG', cast=bool, default=False)


routes = [Route('/', endpoint=home, name="Home Page"),
          Route('/api', endpoint=Api, name="Core API"),
          Route('/schema', endpoint=schema,
                include_in_schema=False, name="API Schema"),
          Mount('/static',
                app=StaticFiles(directory='static'), name="static")]

app = Starlette(debug=DEBUG, routes=routes)
