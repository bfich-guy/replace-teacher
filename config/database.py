from enum import Enum

class DatabaseFilePath(Enum):
    USERS = "database/users.json"

class DatabaseMethodsNames(Enum):
    READ_PRIMARY_KEY = "read_primary_key"
    CREATE_DATA = "create_data_in_database_file"
    READ_DATA = "read_data_from_database_file"
    UPDATE_DATA = "update_data_in_database_file"
    DELETE_DATA = "delete_data_from_database_file"

class User:
    def __init__(self, *,
                 name: str | None,
                 password: str | None,
                 status: str | None,
                 unique_id: str | None,
                 ) -> None:
        
        self.name: str | None = name
        self.password: str | None = password
        self.status: str | None = status
        self.unique_id: str | None = unique_id