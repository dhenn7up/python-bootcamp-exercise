# Import standard and third-party libraries
import os
import pandas as pd  # For reading Excel and CSV files
import json  # For writing JSON output
import ast  # For safely evaluating string representations of Python literals
import math  # For checking NaN values
from datetime import datetime  # For formatting datetime objects
from pathlib import Path  # For handling file paths
from dotenv import load_dotenv  # For loading environment variables from a .env file

# Load environment variables from .env file
load_dotenv()

# Class responsible for reading input files
class FileReader:
    def __init__(self, file_path: Path):
        self.file_path = file_path

        # Load supported formats from environment variable and convert to list
        formats_str = os.getenv("SUPPORTED_FORMATS")
        self.SUPPORTED_FORMATS = ast.literal_eval(formats_str)

        # Load sheet name for Excel files from environment variable
        self.sheet_name = os.getenv("SHEET_NAME")

    # Method to read data from the file and return a list of dictionaries
    def read(self) -> list[dict]:
        # Check if the file exists
        if not self.file_path.exists():
            raise FileNotFoundError(f"File not found: {self.file_path}")

        # Check if the file format is supported
        if self.file_path.suffix not in self.SUPPORTED_FORMATS:
            raise ValueError(
                f"Unsupported file format '{self.file_path.suffix}'. "
                f"Supported formats are: {', '.join(self.SUPPORTED_FORMATS)}"
            )

        try:
            # Read Excel or CSV file based on file extension
            if self.file_path.suffix in [".xlsx", ".xls"]:
                df = pd.read_excel(self.file_path, sheet_name=self.sheet_name)
            elif self.file_path.suffix == ".csv":
                df = pd.read_csv(self.file_path)

            # Raise error if the file is empty
            if df.empty:
                raise ValueError("Input file is empty.")

            # Convert DataFrame to list of dictionaries
            return df.to_dict(orient="records")

        except Exception as e:
            # Raise a runtime error with the original exception
            raise RuntimeError(f"Failed to read file: {e}") from e

# Class responsible for cleaning and writing data to a JSON file
class JsonWriter:
    def __init__(self, output_path: Path):
        self.output_path = output_path

    # Method to clean data before writing to JSON
    def data_cleaner(self, data: list[dict]) -> list[dict]:
        for record in data:
            for key, value in record.items():
                # Replace None or NaN values with None
                if value is None or (isinstance(value, float) and math.isnan(value)):
                    record[key] = None
                # Strip whitespace from string values
                elif isinstance(value, str):
                    record[key] = value.strip()
                # Format datetime objects to YYYY-MM-DD
                elif isinstance(value, (pd.Timestamp, datetime)):
                    record[key] = value.strftime("%Y-%m-%d")
                # Ensure all values are JSON serializable
                else:
                    try:
                        json.dumps(value)
                    except TypeError:
                        # Convert non-serializable objects to strings
                        record[key] = str(value)
        return data
    # Method to write cleaned data to a JSON file
    def write_json(self, data: list[dict]):
        clean_data = self.data_cleaner(data)

        try:
            # Create output directory if it doesn't exist
            self.output_path.parent.mkdir(parents=True, exist_ok=True)

            # Write data to JSON file with indentation
            with open(self.output_path, "w", encoding="utf-8") as f:
                json.dump(clean_data, f, indent=4)
        except Exception as e:
            # Raise a runtime error if writing fails
            raise RuntimeError(f"Failed to write JSON file: {e}") from e
