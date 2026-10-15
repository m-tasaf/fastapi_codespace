from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hey this is a sample fastapi server run inside github codespacea"}