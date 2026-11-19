from fastapi import FastAPI

app = FastAPI(title="GlitchLens AI API", version="0.1.0", docs_url="/docs")

@app.get("/health")
def health():
    return {"status": "ok", "service": "glitchlens-api"}
