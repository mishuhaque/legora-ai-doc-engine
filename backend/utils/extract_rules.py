from openai import OpenAI
import json, re

client = OpenAI()

def extract_rules(text, category):
    prompt = f"""
You are an automation expert. Extract actionable business rules from this {category} document.

Convert rules into this JSON format:

{{
  "rules": [
    {{
      "if": "...",
      "then": "..."
    }}
  ]
}}

Rules must be:
- automation-ready
- atomic
- in clear if → then format
- derived ONLY from the document
- no code fences

Document:
{text}
"""

    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    raw = resp.choices[0].message.content.strip()
    cleaned = re.sub(r"```json|```","",raw).strip()

    try:
        return json.loads(cleaned)
    except:
        return {"error":"Failed to parse rules","raw":cleaned}
