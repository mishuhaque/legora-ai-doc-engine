from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from utils.extract_text import extract_text
from utils.classify_doc import classify_document
from utils.extract_fields import extract_fields
from utils.suggest_workflow import suggest_workflow
from utils.extract_rules import extract_rules

app = FastAPI()

# 🚨 IMPORTANT: Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
@app.post("/analyze")
async def analyze_document(file: UploadFile = File(...)):
    content = await file.read()
    text = extract_text(content)
    category = classify_document(text)
    fields = extract_fields(text, category)
    workflow = suggest_workflow(category, fields)
    rules = extract_rules(text, category)

    return {
        "category": category,
        "fields": fields,
        "workflow": workflow,
        "rules": rules
    }
