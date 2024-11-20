import os
from pydantic import BaseModel
from typing import Optional
from dotenv import load_dotenv

load_dotenv(override=True)


class MailRequest(BaseModel):
    mail_content: str
    mail_tone: Optional[str] = "Clear and Appreciative"
    model_name: Optional[str] = os.getenv('GEMINI_MODEL')
