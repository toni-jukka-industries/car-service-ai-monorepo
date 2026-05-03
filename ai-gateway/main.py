from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Car Service AI Gateway")

class AIRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"status": "AI Gateway running"}

@app.post("/ask")
def ask_ai(request: AIRequest):
    user_message = request.message

    if "vika" in user_message.lower():
        response = "Mahdollinen vika: tarkista moottorin vikakoodit."
    else:
        response = "Analysoidaan tilanne..."

    return {
        "input": user_message,
        "response": response
    }
