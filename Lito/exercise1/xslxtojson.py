import os
import sys
import json
import pandas as panda

class xslxtojson:

    def __init__(self):
        pass

    def read_exceltolist(self, excelpath: str) -> dict:
        # Read excel file and return it as a list
        try:
            excel_data = panda.read_excel(excelpath)
            data_list = excel_data.to_dict(orient='records')
            return data_list
        except Exception as e:
            return None

    def write_listtojson(self, jsonpath: str, data_list: list) -> bool:
        # Save list as a json file
        try:
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
            with open(jsonpath, 'w') as json_file:
                json.dump(data_list, json_file, default=serialize, indent=4)
            return True
        except Exception as e:
            return False

    # def read_exceltolist(self, excelpath: str) -> list:
    #     self.excelpath = excelpath
    #     # Read excel file and return it as a list
    #     try:
    #         excel_data = panda.read_excel(self.excelpath)
    #         data_list = excel_data.values.tolist()
    #         data_list = [[None if panda.isna(cell) else cell for cell in row] for row in data_list]
    #         return data_list
    #     except Exception as e:
    #         return None

    # def write_listtojson(self, jsonpath: str, data_list: list) -> bool:
    #     self.jsonpath = jsonpath
    #     self.data_list = data_list
    #     # Save list as a json file
    #     try:
    #         # convert object to string
    #         for row in range(len(data_list)):
    #             for col in range(len(data_list[row])):
    #                 if isinstance(data_list[row][col], panda.Timestamp):
    #                     data_list[row][col] = data_list[row][col].strftime('%d-%m-%Y')
    #         json_data = json.dumps(self.data_list, indent=4)
    #         with open(self.jsonpath, 'w') as json_file:
    #             json_file.write(json_data)
    #         return True
    #     except Exception as e:
    #         return False