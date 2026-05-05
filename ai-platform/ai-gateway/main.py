from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

class AIRequest(BaseModel):
    message: str


@app.post("/ask")
def ask_ai(request: AIRequest):
    user_message = request.message
    
    try:
        # Lähetetään viesti paikalliselle diagnoosipalvelulle (portti 8001)
        response = requests.post(
            "http://localhost:8001/diagnose",
            json={"issue": user_message}
        )
        # Haetaan vastaus JSON-muodossa
        diagnosis = response.json().get("diagnosis")
    except Exception:
        # Jos yhteys epäonnistuu, palautetaan virheilmoitus
        diagnosis = "Diagnostic service ei vastaa"
        
    return {
        "input": user_message,
        "diagnosis": diagnosis
    }
