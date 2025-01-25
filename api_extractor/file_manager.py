import os
import json
import csv
from datetime import datetime


class FileManager:

    BASE_DIR = "storage"
    FOLDERS = {"json": "json", "csv": "csv"}

    @classmethod
    def setup_folders(cls):
        for folder in cls.FOLDERS.values():
            if not os.path.exists(f"{cls.BASE_DIR}/{folder}"):
                os.makedirs(f"{cls.BASE_DIR}/{folder}")

    @classmethod
    def get_timestamp():
        return datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    @classmethod
    def save_json(
        cls,
        data: dict[str, any],
        file_name: str = None,
    ):
        cls.setup_folders()
        file_name = f"{file_name}.json" or f"{cls.get_timestamp()}.json"
        file_path = os.path.join(cls.BASE_DIR, cls.FOLDERS["json"], file_name)
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
        return file_path

    @classmethod
    def save_csv(
        cls,
        data: dict[str, any],
        file_name: str = None,
    ):
        cls.setup_folders()
        file_name = f"{file_name}.csv" or f"{cls.get_timestamp()}.csv"
        file_path = os.path.join(cls.BASE_DIR, cls.FOLDERS["csv"], file_name)
        with open(file_path, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        return file_path
