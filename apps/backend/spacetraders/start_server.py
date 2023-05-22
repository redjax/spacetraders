from __future__ import annotations

import stackprinter

stackprinter.set_excepthook(style="darkbg2")

from pathlib import Path

from pydantic import BaseModel
import uvicorn


class UvicornCustomServer(BaseModel):
    """Customize a Uvicorn server by passing a dict
    to UvicornCustomServer.parse_obj(dict).

    Run server with instance's .run_server(). This function
    builds a Uvicorn server with the config on the instance,
    then runs it.
    """

    app: str = "main:app"
    host: str = "0.0.0.0"
    port: int = 8000
    reload: bool = False
    root_path: str = "/"

    def run_server(self) -> None:
        uvicorn.run(
            app=self.app,
            host=self.host,
            port=self.port,
            reload=self.reload,
            root_path=self.root_path,
        )


_uvi_dev_conf = {
    "app": "main:app",
    "host": "0.0.0.0",
    "port": 8122,
    "reload": True,
    "root_path": "/api/v1",
}

dev_server = UvicornCustomServer.parse_obj(_uvi_dev_conf)
prod_server = UvicornCustomServer()


if __name__ == "__main__":
    # print(f"[DEBUG] Uvicorn config: {dev_server}")
    print(f"[DEBUG] Uvicorn config: {prod_server}")

    # print(
    #     f"[DEBUG] Starting Uvicorn server, serving app {dev_server.app} on port {dev_server.port}"
    # )
    print(
        f"[DEBUG] Starting Uvicorn server, serving app {prod_server.app} on port {prod_server.port}"
    )
    # dev_server.run_server()
    prod_server.run_server()
