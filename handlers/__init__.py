from aiogram import Router

from . import common, games, weather

routers: tuple[Router] = (
    common.router, games.router, weather.router,
)