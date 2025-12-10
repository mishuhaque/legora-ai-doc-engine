from openai import OpenAI
client = OpenAI()

PROMPT = """
Classify this document into one of the following categories ONLY:
- HR Document
- Invoice
- Contract
- SOP
- Policy Document
- Legal Document
- Benefits Summary
- Technical Specification

Return ONLY the category string.
"""


def classify_document(text):
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": text}
        ]
    )
    return resp.choices[0].message.content.strip()
