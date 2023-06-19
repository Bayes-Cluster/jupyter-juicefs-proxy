import logging
import os
import shutil
from typing import Any, Dict

logger = logging.getLogger(__name__)
logger.setLevel("INFO")


def setup_gateway():
    """Setup commands and icon paths and return a dictionary compatible
    with jupyter-server-proxy.
    """

    def _get_icon_path():
        return os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "icons", "juicefs.svg"
        )

    def _juicefs_command(port):
        full_path = shutil.which("juicefs")
        if not full_path:
            raise FileNotFoundError("Can not find juicefs in $PATH")
        # lstrip is used as a hack to deal with using paths in environments
        # when using git-bash on windows
        os.environ["MINIO_ROOT_USER"] = "admin"
        os.environ["MINIO_ROOT_PASSWORD"] = "12345678"
        return [
            full_path,
            "gateway",
            "sqlite3://myjfs.db",
            "localhost:9000"
        ]

    return {
        "command": _juicefs_command,
        "timeout": 20,
        "new_browser_tab": True,
        "launcher_entry": {"title": "JuiceFS GW", "icon_path": _get_icon_path()},
    }
