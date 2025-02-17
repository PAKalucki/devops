import os
from io import BytesIO
from PyPDF2 import PdfReader, PdfWriter

def split_pdf_to_max_size(input_pdf_path, output_dir, max_size_mb=20):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    reader = PdfReader(input_pdf_path)
    total_pages = len(reader.pages)
    writer = PdfWriter()
    file_index = 1

    for i, page in enumerate(reader.pages):
        writer.add_page(page)

        # Measure the size of the current PDF content
        temp_buffer = BytesIO()
        writer.write(temp_buffer)
        current_output_size = temp_buffer.tell() / (1024 * 1024)  # Convert bytes to MB

        # Check if the current output size exceeds the max size or if it's the last page
        if current_output_size >= max_size_mb or i == total_pages - 1:
            output_pdf_path = os.path.join(output_dir, f'output_part_{file_index}.pdf')
            with open(output_pdf_path, 'wb') as output_pdf:
                writer.write(output_pdf)
            
            # Reset for the next file
            writer = PdfWriter()
            file_index += 1

if __name__ == "__main__":
    input_pdf_path = "Players-Handbook-5e-Transcription-v2.pdf"  # Replace with the path to your input PDF
    output_dir = "output_pdfs"  # Replace with your desired output directory
    max_size_mb = 19  # Maximum size of each split file in MB

    split_pdf_to_max_size(input_pdf_path, output_dir, max_size_mb)
