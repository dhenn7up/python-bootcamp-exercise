import sys
import os

os.chdir(sys.path[0])

from file_reader import file_reader
from file_writer import file_writer

try:
    # Initialize file_reader and extract Excel data
    reader = file_reader()
    excel_path = "C:\\Users\\JV833VJ\\OneDrive - EY\\Documents\\Python Lessons\\PythonTraining.xlsx"
    sheet_name = "Employee"  # Change if needed

    success = reader.read_excel(file_path=excel_path, sheet_name=sheet_name)

    if success:
        content = reader.get_content()
        
        # Initialize file_writer and write to JSON
        writer = file_writer(content)
        json_path = "C:\\Users\\JV833VJ\\OneDrive - EY\\Documents\\Python Lessons\\output.json"
        write_success = writer.write_to_json(json_path)
        
        if write_success:
            print("JSON file written successfully.")
        else:
            print("Failed to write the JSON file.")
    else:
        print("Failed to read the Excel file.")

except Exception as e:
    print(f"An error occurred: {e}")