import json
from pathlib import Path
from dataclasses import dataclass, field

PROJECT_PATH = Path(__file__).resolve().parent.parent


@dataclass
class DatabaseOperations:
    DATA: dict = field(repr=True, default=None)
    DATABASE_PATH: str = field(
        repr=True, default=f"{PROJECT_PATH}\database\servers.json"
    )

    def __post_init__(self):
        self.read_data()
        if self.DATA == {}:
            initial_struct = {"sshServers": []}
            with open(self.DATABASE_PATH, "w") as database_file:
                json.dump(initial_struct, database_file, indent=2)

    def read_data(self):
        with open(self.DATABASE_PATH, "r") as database_file:
            try:
                self.DATA = json.load(database_file)
            except json.JSONDecodeError:
                self.DATA = {}

    def write_data(self, data: dict):
        self.read_data()
        self.DATA["sshServers"].append(data)

        with open(self.DATABASE_PATH, "w") as database_file:
            json.dump(self.DATA, database_file, indent=2)

    def __clear_database(self):
        initial_struct = {"sshServers": []}
        with open(self.DATABASE_PATH, "w") as database_file:
            json.dump(initial_struct, database_file, indent=2)
