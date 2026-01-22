from pypdf import PdfReader

def load_cv_text(path="data/cv.pdf"):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text
