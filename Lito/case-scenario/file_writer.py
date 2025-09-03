import os
import sys

import json
import pandas as panda

#[START] - Class Body
class file_writer:
    #--------------------------------------------------------------------------------------
    # Initialize all variables used in the class
    #--------------------------------------------------------------------------------------
    def __init__(self, content):
        self.success = False;
        self.content = content;
    

    def write_to_file(self, file_path: str):
        success = True
        try:
            data_list: list = self.content
            # Convert object to string
            def serialize(obj):
                if isinstance(obj, panda.Timestamp):
                    return obj.strftime('%d-%m-%Y')
                raise TypeError(f"Type {type(obj)} not serializable")
            # Replace NaN with None
            for row in data_list:
                for key, value in row.items():
                    if panda.isna(value):
                        row[key] = None
            # Serialize List to json
            with open(file_path, 'w') as json_file:
                json.dump(data_list, json_file, default=serialize, indent=4)

        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")
            success = False

        return success

    #Properties Get
    def get_wheel_count(self):
        return self.wheel_count;
    

#[END] - Class Body