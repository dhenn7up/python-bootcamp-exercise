import os
import sys
import pandas as pd
import json
#[START] - Class Body
class file_reader:
    #--------------------------------------------------------------------------------------
    # Initialize all variables used in the class
    #--------------------------------------------------------------------------------------
    def __init__(self):
        self.success = False
        self.content = None
        
    #Methods
    def read_file(self, excel_file):
        self.success = True
        try:
            # Simulate file reading logic here
            # Load the Excel file
            
            self.content = pd.read_excel(excel_file,sheet_name='Employee')
            
            pass
        except Exception as e:
            self.success = False
            print(f"An error occurred while reading the file: {e}")
            
        return self.success        

    #Properties Get
    def get_content(self):
        return self.content
        

    

#[END] - Class Body