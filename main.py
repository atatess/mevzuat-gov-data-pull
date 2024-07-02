import requests
import os
import time
from PyPDF2 import PdfReader
from io import BytesIO

base_url = "https://www.mevzuat.gov.tr/MevzuatMetin/1.5."
output_dir = "mevzuat_pdfs"
text_output_dir = "mevzuat_texts"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

if not os.path.exists(text_output_dir):
    os.makedirs(text_output_dir)


def pdf_exists(url):
    response = requests.head(url)
    return response.status_code == 200


def download_pdf(url, output_path):
    response = requests.get(url)
    with open(output_path, 'wb') as f:
        f.write(response.content)


def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with open(pdf_path, 'rb') as f:
            reader = PdfReader(f)
            for page in reader.pages:
                text += page.extract_text()
    except Exception as e:
        print(f"Failed to extract text from {pdf_path}: {e}")
    return text


for number in range(1, 7316):
    pdf_url = f"{base_url}{number}.pdf"
    output_path = f"{output_dir}/{number}.pdf"
    text_output_path = f"{text_output_dir}/{number}.txt"

    if pdf_exists(pdf_url):
        print(f"Downloading {pdf_url}")
        try:
            download_pdf(pdf_url, output_path)
            print(f"Extracting text from {output_path}")
            text = extract_text_from_pdf(output_path)
            with open(text_output_path, 'w', encoding='utf-8') as f:
                f.write(text)
        except Exception as e:
            print(f"Error processing {pdf_url}: {e}")
        time.sleep(1)  # Be polite to the server
    else:
        print(f"PDF {pdf_url} does not exist.")