import requests
import PyPDF3
import pdfplumber


PDF_FILE = "Farmer.pdf"
pdfFileObj = open(PDF_FILE, "rb")
pdfReader = PyPDF3.PdfFileReader(pdfFileObj)
pages = pdfReader.numPages
Text_from_pdf = ""


with pdfplumber.open(PDF_FILE) as pdf:
    for i in range(0, pages):
        page = pdf.pages[i]
        text = page.extract_text()
        Text_from_pdf += text


URL = "http://api.voicerss.org/"
API_KEY = "11822bf4cff24627b85a236f91d26414"
PARAM = {
    "key" : API_KEY,
    "hl" : "en-us",
    "src" : Text_from_pdf,
}

response = requests.get(url=URL, params=PARAM)
response.raise_for_status()

AUDIO_FILE = "Farmer.wav"
with open(AUDIO_FILE, "wb") as out:
    out.write(response.content)
    print(f'Generated speech saved to "{AUDIO_FILE}"')

