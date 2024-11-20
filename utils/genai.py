import google.generativeai as genai


def get_prompt(context: str, tone: str) -> str:
    prompt = """
    You are an AI email replier. You need to generate a polite and respectful response based on the context of the email provided. If the tone of the email is not specified, always generate a calm and positive reply. Your reply should avoid any negative language or offensive terms. If the email content is in HTML markdown, string, or any other format, extract the context and craft a thoughtful response. Please use a calm, positive, and professional tone when replying.

    ### Here is the mail context:
    {context}

    ### Here is the mail tone:
    {tone}
    
    Note: provide content like I saying, The response going from me.
    """.format(context=context, tone=tone) # noqa
    return prompt


def get_llm_response(model_name: str, prompt: str) -> str:
    model = genai.GenerativeModel(model_name)
    response = model.generate_content(prompt)
    return response.text
