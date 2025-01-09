from fastapi import FastAPI
from app.routes import router
from app.database import Base, engine

# Initialize FastAPI app
app = FastAPI()

# Create all database tables
Base.metadata.create_all(bind=engine)

# Include API routes
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to LiveCAD Backend"}