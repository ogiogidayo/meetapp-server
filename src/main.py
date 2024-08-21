from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from route import routes
_app = FastAPI()

@_app.get("/health", include_in_schema=True)
async def health():
    print("Called")
    return "ok"

_app.include_router(routes.router)

app = CORSMiddleware(
    app=_app,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

handler = Mangum(app, lifespan="off")