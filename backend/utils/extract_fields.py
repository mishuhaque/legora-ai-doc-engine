from openai import OpenAI
import json
import re

client = OpenAI()

def extract_fields(text, category):
    prompt = f"""
Extract key-value pairs from the document.
Document Type: {category}

Return clean JSON only. No code fences.

Text:
{text}
"""

    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    raw = resp.choices[0].message.content.strip()

    # Remove code fences if present
    cleaned = re.sub(r"```json|```", "", raw).strip()

    try:
        return json.loads(cleaned)
    except:
        return {"error": "Failed to parse JSON", "raw": cleaned}
