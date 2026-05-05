from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from app.api.agent import router as agent_router

app = FastAPI(
    title="AgentOS API",
    description="The core brain and orchestrator for AgentOS",
    version="0.1.0"
)

# Configure CORS for the React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, replace with the actual frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(agent_router)

@app.get("/")
async def root():
    return {
        "status": "online",
        "message": "AgentOS Brain is active",
        "version": "0.1.0"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
