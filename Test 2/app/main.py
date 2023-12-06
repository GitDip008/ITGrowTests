from fastapi import FastAPI

from app.api import author,book,client
app = FastAPI()



@app.get("/")
async def root():
    return {"status": "running"}

app.include_router(author.router, tags=["authors"])
app.include_router(book.router, tags=["books"])
app.include_router(client.router, tags=["clients"])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
