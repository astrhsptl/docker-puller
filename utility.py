import json
from typing import Dict

from schemas import ConfigSchema


def load_config() -> ConfigSchema:
    with open("config.json") as config_file:
        dict_from_json: Dict = json.load(config_file)

        hooks = dict_from_json.get("hooks")
        token = dict_from_json.get("token")

        if not hooks or not token:
            return None

        return ConfigSchema(token=token, hooks=hooks)


async def processing_hook(hooks: Dict[str, str], hook: str):
    print(hooks, hook)
    script = hooks.get(hook)

    if not script:
        print("invalid script")
        return
    try:
        # subprocess.call(script)
        print("successful start!!!")
    except OSError as e:
        print(e)
