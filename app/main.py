from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from app.routes import auth, oauth
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Add SessionMiddleware
app.add_middleware(SessionMiddleware, secret_key=os.getenv("SECRET_KEY", "supersecretkey"))

# Include routes
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(oauth.router, prefix="/oauth", tags=["OAuth"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
