from pydantic import BaseModel
from typing import Optional


class MailRequest(BaseModel):
    mail_content: str
    mail_tone: str
    model_name: Optional[str] = None
