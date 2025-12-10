from pypdf import PdfReader
import io

def extract_text(content):
    reader = PdfReader(io.BytesIO(content))
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text
