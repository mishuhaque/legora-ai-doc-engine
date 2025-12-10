from openai import OpenAI
import json
import re

client = OpenAI()

def suggest_workflow(category, fields):
    prompt = f"""
Given the document type (“{category}”) and extracted fields:

{fields}

Suggest automated workflow actions.
Return valid JSON only. No code fences.
"""

    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    raw = resp.choices[0].message.content.strip()
    cleaned = re.sub(r"```json|```", "", raw).strip()

    try:
        return json.loads(cleaned)
    except:
        return {"error": "Failed to parse JSON", "raw": cleaned}
