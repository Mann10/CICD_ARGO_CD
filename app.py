from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "CI/CD Working 🚀"}

@app.get("/health")
def health():
    return {"message": "Healthy"}