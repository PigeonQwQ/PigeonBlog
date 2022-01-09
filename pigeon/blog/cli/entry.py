import functools
import os
from typing import Optional

import typer
import uvicorn

from pigeon.blog.services import AppFactory

_app = typer.Typer()


@functools.cache
def web_app():
    return AppFactory()()


_web_app = web_app()


@_app.command("start", help="Start blog server")
def start(
        host: Optional[str] = "0.0.0.0",
        port: Optional[int] = 25096,
        debug: Optional[bool] = True,
        workers: Optional[int] = 1,
):
    if debug:
        os.environ['DEBUG'] = "true"
    uvicorn.run("pigeon.blog.cli.entry:_web_app", host=host, port=port, reload=debug, workers=workers)


if __name__ == '__main__':
    _app()
