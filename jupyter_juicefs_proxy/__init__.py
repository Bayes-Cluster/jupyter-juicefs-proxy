import logging
import os
import shutil
from typing import Any, Dict

logger = logging.getLogger(__name__)
logger.setLevel("INFO")

def setup_gatewaye():

    def _get_juicefs_cmd(port):
        executable = "juicefs"
        if not shutil.which(executable):
            raise FileNotFoundError("Can not find juicefs in PATH")
        
        # Start vscode in CODE_WORKINGDIR env variable if set
        # If not, start in 'current directory', which is $REPO_DIR in mybinder
        # but /home/jovyan (or equivalent) in JupyterHubs
        os.environ["MINIO_ROOT_USER"] = "admin"
        os.environ["MINIO_ROOT_PASSWORD"] = "12345678"
        cmd = [
            executable,
            "gateway",
            "sqlite3://myjfs.db",
            "localhost:"+str(port)
        ]

        return cmd

    return {
        "command": _get_juicefs_cmd,
        "timeout": 300,
        "new_browser_tab": True,
        "launcher_entry": {
            "title": "JuiceFS GW",
            "icon_path": os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "icons", "juicefs.svg"
            ),
        },
    }
