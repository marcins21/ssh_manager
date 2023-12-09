import json
from pathlib import Path
from dataclasses import dataclass, field

PROJECT_PATH = Path(__file__).resolve().parent.parent


@dataclass
class DatabaseOperations:
    DATA: dict = field(repr=True, default=None)
    DATABASE_PATH: str = field(
        repr=False, default=f"{PROJECT_PATH.parent.parent}\database\servers.json"
    )

    def read_data(self):
        with open(self.DATABASE_PATH, "r") as database_file:
            self.DATA = json.load(database_file)
