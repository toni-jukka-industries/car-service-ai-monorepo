from fastapi import FastAPI

app = FastAPI(title="Diagnostic Bridge")

@app.get("/")
def root():
    return {"status": "Diagnostic Bridge running"}

@app.post("/diagnose")
def diagnose(data: dict):
    issue = data.get("issue", "")

    # yksinkertainen demo logiikka
    if "ei käynnisty" in issue.lower():
        return {"diagnosis": "Mahdollinen akku tai starttimoottori"}
    
    if "kolisee" in issue.lower():
        return {"diagnosis": "Mahdollinen alustan osa tai iskunvaimennin"}
    
    return {"diagnosis": "Ei tunnistettu vielä"}
