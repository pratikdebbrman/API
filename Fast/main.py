from fastapi import FastAPI,Depends,HTTPException
import requests
from fastapi.responses import HTMLResponse
import uvicorn
from routers import album_router



app = FastAPI()

app.include_router(album_router.router)

@app.get("/hello")
async def root():
    return {"message": "Hello World"}


if __name__=='__main__':
    uvicorn.run("main:app",reload=True)