import os
import glob

def count_pdfs_in_folder(folder_path):
    pdf_files = glob.glob(os.path.join(folder_path, '*.pdf'))
    return len(pdf_files)

if __name__ == "__main__":
    folder_path = '/path/to/your/folder'  # Replace this with the actual folder path
    pdf_count = count_pdfs_in_folder(folder_path)
    print(f"Number of PDF files in the folder: {pdf_count}")
