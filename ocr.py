import streamlit as st
from google.cloud import vision
from PIL import Image
import io

# Create a Streamlit app
st.title("PDF OCR App")

# Add a file uploader widget
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

# Add a button to start the OCR process
if st.button("Process OCR"):
    # Check if a file was uploaded
    if uploaded_file is not None:
        # Read the PDF file into memory
        pdf_bytes = uploaded_file.read()

        # Convert the PDF file to an image
        image = Image.open(io.BytesIO(pdf_bytes))

        # Perform OCR on the image
        client = vision.ImageAnnotatorClient()

        response = client.document_text_detection(image=image)

        text = response.full_text_annotation.text

        # Display the OCR results
        st.write(text)

        # Download the OCR results as a text file
        st.download_button(
            label="Download OCR Results",
            data=text,
            file_name="ocr_results.txt",
            mime="text/plain",
        )
    else:
        st.error("Please upload a PDF file.")
