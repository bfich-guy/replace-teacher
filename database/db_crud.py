from json import load, dump
from typing import Any
from pathlib import Path

class DataBase:
    def __init__(self) -> None:
        
        self.reading_mode: str = "r"
        self.writing_mode: str = "w"
        self.encoding: str = "utf-8"
        self.indent: int = 4
        self.ensure_ascii = False
        self.max_id: int = 0

        self.db: dict = {}

    #Layer 1: Basic methods of database

    def create_database_file(self, *, data: Any, file_path: str) -> None:
        """
        Creates JSON file. 
        """
        with open(file=file_path, mode=self.writing_mode, encoding=self.encoding) as db_file:
            dump(obj=data, fp=db_file, indent=self.indent, ensure_ascii=self.ensure_ascii)
        
    def remove_database_file(self, *, file_path: str) -> None:
        """
        Removes JSON file. 
        """
        file_to_remove: Path = Path(file_path)
        file_to_remove.unlink(missing_ok=True)

    def load_data(self, *, file_path: str) -> None:
        """
        Loads data from JSON file. 
        """
        with open(file=file_path, mode=self.reading_mode, encoding=self.encoding) as db_file:
            self.db: dict = load(db_file)
        
    def commit(self, *, file_path: str) -> None:
        """
        Dumps content into JSON file.
        """
        with open(file=file_path, mode=self.writing_mode, encoding=self.encoding) as db_file:
            dump(obj=self.db, fp=db_file, indent=self.indent, ensure_ascii=self.ensure_ascii)

    def drop_database(self, *, data: Any, file_path: str, confirm: bool = False) -> None:
        """
        **WARNING**: totally drops db. **NOT RECOMENDED** to use, if you are not sure!
        """
        if confirm:
            with open(file=file_path, mode=self.writing_mode, encoding=self.encoding) as db_file:
                dump(obj=data, fp=db_file, indent=self.indent, ensure_ascii=self.ensure_ascii)

    #Layer 2: CRUD methods for data

    def create_data(self, *, file_path: str, data: Any) -> None:

        self.load_data(file_path=file_path)

        self.db[self.max_id] = data
        self.max_id += 1

        self.commit(file_path=file_path)

    def read_data(self, *, file_path: str, data_id: int) -> Any:

        try:
            self.load_data(file_path=file_path)

            string_data_id: str = str(data_id)
            readed_data: Any = self.db[string_data_id]
            return readed_data
        except (KeyError, IndexError, TypeError):
            return None
    
    def update_data(self, *, file_path: str, data_id: int, new_data: Any) -> Any:

        try:
            self.load_data(file_path=file_path)

            string_data_id: str = str(data_id)
            updated_data = self.db[string_data_id] = new_data
            return updated_data
        except (KeyError, IndexError, TypeError):
            return None
    
    def delete_data(self, *, file_path: str, data_id: int) -> None:

        try:
            self.load_data(file_path=file_path)

            string_data_id: str = str(data_id)
            del self.db[string_data_id]

            self.commit(file_path=file_path)
        except (KeyError, IndexError, TypeError):
            return None
        
db: DataBase = DataBase()