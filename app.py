from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "CI/CD Working 🚀"}

@app.get("/")
def health():
    return {"message": "Healthy"}