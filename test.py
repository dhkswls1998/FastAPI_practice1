from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello":"World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="localhost",port=8080)