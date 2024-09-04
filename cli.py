# aris_tools/cli.py

from pdf_tools.pdf_export_pattern import pdf_export_pattern
from pdf_tools.pdf_erase_line import pdf_erase_line

def main_menu():
    while True:
        print("\nAris Tools")
        print("1. Replace lines in PDF")
        print("2. Extract text based on a pattern in PDF")
        print("0. Exit")

        choice = input("Select action: ")

        if choice == '0':
            print("Exiting program")
            break

        elif choice == '1':
            pdf_file = input("Enter PDF file path: ")
            output_file = input("Enter output file name: ")
            pdf_erase_line(pdf_file, output_file, "Untracked")

        elif choice == '2':
            pdf_file = input("Enter PDF file path: ")
            output_file = input("Enter output file name: ")
            pdf_export_pattern(pdf_file, output_file)

        else:
            print("Invalid Choice")