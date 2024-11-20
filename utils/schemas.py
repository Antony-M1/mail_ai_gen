from pydantic import BaseModel


class MailRequest(BaseModel):
    mail_content: str
    # mail_tone: Optional[str] = "Clear and Appreciative"
    # model_name: Optional[str] = os.getenv('GEMINI_MODEL')
