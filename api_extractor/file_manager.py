import os
import json
import csv
from datetime import datetime
from typing import Optional


class FileManager:

    BASE_DIR = "storage"
    FOLDERS = {
        "json": "json",
        "csv": "csv",
    }

    @staticmethod
    def _get_timestamp() -> str:
        return datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    @classmethod
    def _setup_folders(cls) -> None:
        for folder in cls.FOLDERS.values():
            if not os.path.exists(f"{cls.BASE_DIR}/{folder}"):
                os.makedirs(f"{cls.BASE_DIR}/{folder}")

    @classmethod
    def _prepare_file_path(
        cls,
        file_type: str,
        file_name: Optional[str] = None,
    ) -> str:
        if file_type not in cls.FOLDERS:
            raise ValueError(f"Unsupported file type: {file_type}")
        cls._setup_folders()
        file_name = file_name or cls.get_timestamp()
        file_name = f"{file_name}.{file_type}"
        return os.path.join(cls.BASE_DIR, cls.FOLDERS[file_type], file_name)

    @classmethod
    def save_json(
        cls,
        data: dict[str, any],
        file_name: Optional[str] = None,
    ) -> str:
        file_path = cls._prepare_file_path("json", file_name)
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
        return file_path

    @classmethod
    def save_csv(
        cls,
        data: dict[str, any],
        file_name: Optional[str] = None,
    ) -> str:
        file_path = cls._prepare_file_path("csv", file_name)
        with open(file_path, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        return file_path
