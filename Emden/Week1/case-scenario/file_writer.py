import os
import sys
import json
import datetime

#[START] - Class Body
class file_writer:
    #--------------------------------------------------------------------------------------
    # Initialize all variables used in the class
    #--------------------------------------------------------------------------------------
    def __init__(self, content):
        self.success = False
        self.content = content
        self.file_path = None

    #--------------------------------------------------------------------------------------
    # Helper method to convert datetime objects to strings
    #--------------------------------------------------------------------------------------
    def _convert_datetime(self, obj):
        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        return obj

    #--------------------------------------------------------------------------------------
    # Method to write content to a JSON file
    #--------------------------------------------------------------------------------------
    def write_to_json(self, file_path: str):
        self.success = True
        self.file_path = file_path
        try:
            # Use default parameter to handle datetime objects
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(self.content, f, ensure_ascii=False, indent=4, default=self._convert_datetime)
            print(f"Data written to JSON file '{file_path}' successfully.")
        except Exception as e:
            print(f"An error occurred while writing to the JSON file: {e}")
            self.success = False
        return self.success

#[END] - Class Body