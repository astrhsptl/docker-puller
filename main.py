from fastapi import BackgroundTasks, FastAPI, HTTPException, Response

from schemas import ConfigSchema, RePullState, WebhookCallback, WebhookPayload
from utility import load_config, processing_hook

app = FastAPI()


config: ConfigSchema = load_config()


@app.post("/")
async def hook_api(
    background: BackgroundTasks,
    payload: WebhookPayload,
) -> Response:
    hook = payload.repository.name

    if not config:
        print("Invalid config")
        return Response(
            WebhookCallback(
                state=RePullState.error, description="Invalid server config"
            ).model_dump(),
            200,
        )

    if not hook:
        raise HTTPException(
            400,
            WebhookCallback(
                state=RePullState.error, description="Invalid request: missing hook"
            ).model_dump(),
        )

    background.add_task(processing_hook, hooks=config.hooks, hook=hook)

    return Response(
        WebhookCallback(
            state=RePullState.success, description="Process has been started"
        ).model_dump_json(),
        200,
    )
