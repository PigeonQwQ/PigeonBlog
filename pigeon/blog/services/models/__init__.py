import functools
import os

from sqlmodel import create_engine

from . import user
from ..configurations import env


@functools.cache
def get_engine():
    return create_engine(env.SQL_DSN, echo=(os.environ['DEBUG'].lower() == "true"))


__all__ = ["get_engine", "user", ]
