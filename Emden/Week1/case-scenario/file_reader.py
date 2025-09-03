import openpyxl

#[START] - Class Body
class file_reader:
    #--------------------------------------------------------------------------------------
    # Initialize all variables used in the class
    #--------------------------------------------------------------------------------------
    def __init__(self):
        self.success = False
        self.content = None
        self.file_path = None

    #--------------------------------------------------------------------------------------
    # Method to read data from an Excel file
    #--------------------------------------------------------------------------------------
    def read_excel(self, file_path="C:\\Users\\JV833VJ\\OneDrive - EY\\Documents\\Python Lessons\\PythonTraining.xlsx", sheet_name="Employee"):
        self.success = True
        self.file_path = file_path  # Store the file path
        try:
            wb = openpyxl.load_workbook(file_path, data_only=True)
            ws = wb[sheet_name] if sheet_name else wb.active
            self.content = [
                [cell for cell in row]
                for row in ws.iter_rows(values_only=True)
            ]
            print(f"Excel file '{file_path}' read successfully.")
        except Exception as e:
            self.success = False
            print(f"An error occurred while reading the Excel file: {e}")
            self.content = None
        return self.success

    #--------------------------------------------------------------------------------------
    # Property to get the content
    #--------------------------------------------------------------------------------------
    def get_content(self):
        return self.content

#[END] - Class Body