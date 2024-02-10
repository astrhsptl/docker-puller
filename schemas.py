from enum import Enum
from typing import Dict, Optional

from pydantic import BaseModel


class RePullState(str, Enum):
    success = "success"
    failure = "failure"
    error = "error"


class ConfigSchema(BaseModel):
    token: str
    hooks: Dict[str, str]


class WebhookCallback(BaseModel):
    state: RePullState
    description: str


class WebhookPushData(BaseModel):
    pushed_at: int | float
    pusher: str
    tag: str


class WebhookRepository(BaseModel):
    comment_count: int | float
    date_created: int | float
    description: Optional[str]
    dockerfile: Optional[str]
    full_description: Optional[str]
    is_official: bool
    is_private: bool
    is_trusted: bool
    name: str
    namespace: str
    owner: str
    repo_name: str
    repo_url: str
    star_count: int
    status: str


class WebhookPayload(BaseModel):
    callback_url: str
    push_data: WebhookPushData
    repository: WebhookRepository
