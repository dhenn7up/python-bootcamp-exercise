import os
import sys
import json
import pandas as pd

#[START] - Class Body
class file_writer_class:
    #--------------------------------------------------------------------------------------
    # Initialize all variables used in the class
    #--------------------------------------------------------------------------------------
    def __init__(self, content):
        self.success = False;
        self.content = content;
    

    def write_to_file(self, file_path: str):
        try:
            json_data = []
            for index, row in self.content.iterrows():
                row_dict = row.to_dict()
                json_data.append(row_dict)

            # Convert Timestamps to ISO format (string)
            for col in self.content.columns:
                if pd.api.types.is_datetime64_any_dtype(self.content[col]):
                    self.content[col] = self.content[col].apply(lambda x: x.isoformat() if x is not None else None)

            # Convert to list of dictionaries
            json_data = self.content.to_dict(orient='records')

            # Write the JSON list to a .json file
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(json_data, f, ensure_ascii=False, indent=4)
                self.success = True
                return self.success
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")
            self.success = False

    #Properties Get
    def get_wheel_count(self):
        return self.wheel_count;
    

#[END] - Class Body