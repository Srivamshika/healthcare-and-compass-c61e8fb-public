from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title='Healthcare And Compass', version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"https://[a-z0-9-]+\.vercel\.app",
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)
PRODUCT = {"project_id": "c61e8fb0-d58b-496f-9da5-8a32de76a124", "product_name": "Healthcare And Compass", "idea": "The healthcare and fitness sector remains ripe for disruption, particularly through digital and personalized solutions. Strong opportunities include Hospital-at-Home operations software, AI-driven nutritional and fitness coaching based on wearable or CGM (Continuous Glucose Monitor) data, and specialized telehealth platforms for elder care and family coordination.", "problem": "Clinical and care-operations teams need a safer, faster way to turn fragmented patient and workflow signals into a reviewable next action. The opportunity should be tested through one repeatable decision workflow.", "elevator_pitch": "Healthcare And Compass helps clinical and care-operations teams turn scattered evidence into a human-approved next action and prove whether the workflow improves a measurable outcome.", "target_users": ["clinical and care-operations teams", "domain specialists", "a clinical operations or service-line leader"], "features": ["Structured case or workflow intake", "Evidence-backed recommendation with confidence and rationale", "Human approval and override with an audit trail", "Pilot dashboard for time, quality, and adoption outcomes"], "market_gap": "A narrow healthcare workflow that links evidence, a human approval, and a measurable outcome remains more defensible than another general AI chat surface."}

@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "generated-mvp-api"}

@app.get("/api/overview")
def overview() -> dict:
    return {
        "product_name": PRODUCT["product_name"],
        "pitch": PRODUCT["elevator_pitch"],
        "problem": PRODUCT["problem"],
        "target_users": PRODUCT["target_users"],
        "features": PRODUCT["features"],
        "demo_data": True,
    }
