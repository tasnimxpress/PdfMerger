from PyPDF2 import PdfMerger
import os

def merge_pdfs_with_blank(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through each folder in the input folder
    for folder in os.listdir(input_folder):
        folder_path = os.path.join(input_folder, folder)

        # Check if the item in the folder is a directory
        if os.path.isdir(folder_path):
            pdf_files = [f for f in os.listdir(folder_path) if f.endswith(".pdf")]
            pdf_files.sort()

            output_file = os.path.join(output_folder, f"{folder}.pdf")

            # Using Unicode escape sequences for file name
            merger = PdfMerger()

            for pdf_file in pdf_files:
                pdf_path = os.path.join(folder_path, pdf_file)

                # Using Unicode escape sequences for file name
                merger.append(pdf_path)

            # Save the merged PDF to the output folder
            merger.write(output_file)
            merger.close()

if __name__ == "__main__":
    input_folder = "Input folder"
    output_folder = "Folder Name"

    merge_pdfs_with_blank(input_folder, output_folder)
