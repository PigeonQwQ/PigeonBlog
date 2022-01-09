import os

from fastapi import FastAPI
from sqlmodel import create_engine, SQLModel

from .configurations import env
from .models import *  # init models package


class AppFactory(object):
    def __init__(self):
        self._app = None

    @staticmethod
    def _get_all_router():
        from pigeon.blog.services.routers import __all_routers__
        return __all_routers__

    def _apply_router(self):
        if not isinstance(self._app, FastAPI):
            raise RuntimeError("self._app isn't initialized.")
        routers = AppFactory._get_all_router()
        for r in routers:
            self._app.include_router(r)

    def _ensure_sql(self):
        if not isinstance(self._app, FastAPI):
            return

        @self._app.on_event("startup")
        def sql_startup():
            engine = get_engine()
            SQLModel.metadata.create_all(engine)

        @self._app.on_event("shutdown")
        def sql_shutdown():
            pass

    def __call__(self, *args, **kwargs):
        self._app = FastAPI(
            title="Pigeon Blog",
        )
        self._apply_router()
        self._ensure_sql()
        return self._app
