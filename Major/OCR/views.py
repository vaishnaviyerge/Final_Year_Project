import pytesseract

def extract_text_from_image(preprocessed_image):

    text = pytesseract.image_to_string(preprocessed_image)
    return text

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'