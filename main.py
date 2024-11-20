import os
import traceback
import google.generativeai as genai
from fastapi import FastAPI, APIRouter
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from utils import (
    get_logger,
    get_prompt,
    get_llm_response,
    MailRequest
)

load_dotenv(override=True)
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

logger = get_logger("Mail AI", "app.log")

app = FastAPI()

router = APIRouter(
    prefix="/api/v1",
    responses={404: {"description": "Not found"}},
)


@app.get("/", tags=["HealthCheck"])
async def root_endpoint():
    logger.info("Root endpoint accessed.")
    return {"status": "healthy"}


@router.post("/ai-response/", tags=["GenAI API"])
async def get_genai_response(request: MailRequest):
    try:
        mail_tone = "Clear and Appreciative"
        prompt = get_prompt(request.mail_content, mail_tone)
        response = get_llm_response(os.getenv("GEMINI_MODEL"), prompt)
        return {"message": "ok", "response": response}
    except Exception as ex:
        logger.critical(traceback.format_exc())
        return JSONResponse(status_code=400, content={"message": str(ex)})

app.include_router(router)
