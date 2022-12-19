from datetime import datetime
from typing import List, Dict, Optional

from fastapi import FastAPI, Cookie
from fastapi.staticfiles import StaticFiles

from views import router
from api import router as apiRouter


app = FastAPI()

app.mount("/assets", StaticFiles(directory="assets"), name="assets")

app.include_router(router, include_in_schema=False)
app.include_router(apiRouter)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=80, reload=True)
