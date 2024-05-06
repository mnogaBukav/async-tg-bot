from . import common, games, weather

routers = (
    common.router, games.router, weather.router,
)