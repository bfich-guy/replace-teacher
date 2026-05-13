from json import load, dump, JSONDecodeError
from typing import Any
from pathlib import Path

database_config_registry: dict = {
    "reading_mode": "r",
    "writing_mode": "w",
    "encoding": "utf-8",
    "indent": 4,
    "ensure_ascii": False,
    "metadata_file_path": "database/metadata.json",
}

class DataBase:
    def __init__(self, *, 
                 reading_mode: str,
                 writing_mode: str,
                 encoding: str,
                 indent: int,
                 ensure_ascii: bool,
                 metadata_file_path: str,
                 ) -> None:
        
        self.reading_mode: str = reading_mode
        self.writing_mode: str = writing_mode
        self.encoding: str = encoding
        self.indent: int = indent
        self.ensure_ascii = ensure_ascii

        self.metadata_file_path: str = metadata_file_path
        self.primary_key_created: bool = False
        self.primary_key: int = self.create_primary_key()

    #Layer 1: CRUD basic methods of database

    def create_database_file(self, *, 
                             data: dict = {}, 
                             file_path: str,
                             ) -> None:
        
        """
        **Creates JSON database file** and stores value of argument data into it. Works like **json.dump()**. Returns **None**. 
        """

        try:
            with open(file=file_path, mode=self.writing_mode, encoding=self.encoding) as db_file:
                dump(obj=data, fp=db_file, indent=self.indent, ensure_ascii=self.ensure_ascii)
        except JSONDecodeError:
            return None
        
    def read_database_file(self, *, 
                           file_path: str, 
                           ) -> dict | None:
        
        """
        **Returns content of JSON file** by opening it. Works like a **json.load()**. 

        **FileNotFoundError**, **JSONDecodeError** are **handed** and if error happened, function **returns None**. 
        """
        try:
            with open(file=file_path, mode=self.reading_mode, encoding=self.encoding) as db_file:
                file_content: Any = load(db_file)

            return file_content
        except (FileNotFoundError, JSONDecodeError):
            return None
        
    def update_database_file(self, *, 
                             update_data: Any, 
                             rewrite_data: Any = {}, 
                             file_path: str, 
                             rewrite_confirm: bool = False,
                             ) -> None:
        
        """
        **WARNING: Rewrites content of JSON file**. Works like a **json.dump()**. If argument *rewrite_confirm* is True, function rewrites file content as *rewrite_data*, which is **empty dictionary**, else rewrites as *update_data*. 

        **FileNotFoundError**, **JSONDecodeError** are **handed** and if error happened, function **returns None**.  
        """

        target_data: Any = None

        if rewrite_confirm:
            target_data = rewrite_data
        else:
            target_data = update_data

        try:
            with open(file=file_path, mode=self.writing_mode, encoding=self.encoding) as db_file:
                dump(obj=target_data, fp=db_file, indent=self.indent, ensure_ascii=self.ensure_ascii)
        except (FileNotFoundError, JSONDecodeError):
            return None
        
    def delete_database_file(self, *, 
                             file_path: str, 
                             delete_confirm: bool = False,
                             ) -> None:
        
        """
        **WARNING: Deletes content of JSON database file**, if argument *delete_confirm* is true. Uses **pathlib.unlink()**. **NOT RECOMMENDED** to use! 

        **FileNotFoundError** is already **handed** by .unlink(missing_ok=True). 
        """
        if delete_confirm:
            file_to_remove: Path = Path(file_path)
            file_to_remove.unlink(missing_ok=True)

    #Layer 2: CRUD advanced methods for database

    def create_primary_key(self) -> int:
        """
        **Sets primary key** as 0 by getting the value of dictionary key from JSON file called *metadata.json*. If there is no key, primary key **becomes 0**.  

        The method can be called **at once** and **returns primary key**, if primary key is not created, else it **returns 0**, so **DON'T USE** this, if you are not sure. 

        **KeyError** and **TypeError** are already **handed**.  
        """

        metadata: dict | None = self.read_database_file(file_path=self.metadata_file_path)

        if self.primary_key_created or metadata is None:
            return 0
        
        primary_key: int = metadata.setdefault("primary_key", 0)
        self.primary_key = primary_key

        metadata["primary_key"] = self.primary_key

        self.update_database_file(update_data=metadata, file_path=self.metadata_file_path)

        return primary_key
    
    def read_primary_key(self) -> int:
        """
        **Gets primary key** from JSON database file called *metadata.json*. 

        Method **returns primary key**.  
        """

        metadata: dict | None = self.read_database_file(file_path=self.metadata_file_path)

        if metadata is not None:
        
            primary_key: int = metadata.setdefault("primary_key", 0)

        return primary_key

    def update_primary_key(self, *, 
                           amount: int = 1,
                           ) -> int:
        
        """
        **Increments primary key** by getting the value of dictionary key from JSON file called *metadata.json* and adding to this value argument *amount*. Amount **equals 1** as an default value, but **can be redefined**.  
        
        Method **returns primary key** of database. 

        **KeyError** and **TypeError** are already **handed**. 
        """

        metadata: dict | None = self.read_database_file(file_path=self.metadata_file_path)

        if metadata is None:
            return 0
        
        self.primary_key += amount
        metadata["primary_key"] = self.primary_key

        self.update_database_file(update_data=metadata, file_path=self.metadata_file_path)

        return self.primary_key
    
    def delete_primary_key(self, *, delete_confirm: bool = False) -> int:
        """
        **WARNING**: **sets primary key as 0**.

        **NOT RECOMMENDED** to use! 

        Method **returns primary key**. 

        **TypeError** and **KeyError** already **handed**. 
        """

        metadata: dict | None = self.read_database_file(file_path=self.metadata_file_path)

        if not delete_confirm or metadata is None:
            return 0
        
        self.primary_key = 0

        metadata["primary_key"] = self.primary_key

        self.update_database_file(update_data=metadata, file_path=self.metadata_file_path)

        return self.primary_key
        
    #Layer 3: CRUD for data

    def create_data_in_database_file(self, *,
                                     file_path: str,
                                     data: Any,
                                     ) -> str:
        
        """
        **Stores data** in JSON database file and **returns ID** (primary key) of this data. 
        """

        data_id: str = str(self.read_primary_key())
        file_content: dict | None = self.read_database_file(file_path=file_path)

        if file_content is not None:
            file_content[data_id] = data

        self.update_database_file(file_path=file_path, update_data=file_content)
        self.update_primary_key()

        return data_id
    
    def read_data_from_database_file(self, *,
                                     file_path: str,
                                     data_id: str,
                                     ) -> dict | None:
        
        """
        **Returns data** from JSON database file that stored by ID (primary key). 

        **FileNotFoundError**, **JSONDecodeError** and **KeyError** are already **handed** and if the error happened, function **returns None**. 
        """

        file_content: dict | None = self.read_database_file(file_path=file_path)

        if file_content is None:
            return None
        
        try:
            data: dict = file_content[data_id]
            return data
        except KeyError:
            return None
    
    def update_data_in_database_file(self, *,
                                     file_path: str,
                                     data: dict,
                                     data_id: str,
                                     ) -> dict | None:
        
        """
        **Rewrites data** in JSON database file and **returns None**. 
        
        **FileNotFoundError**, **JSONDecodeError**, and **KeyError** are **handed** and if the error happened, function **returns None**. 
        """
    
        file_content: dict | None = self.read_database_file(file_path=file_path)

        if file_content is None:
            return None
        
        try:
            file_content[data_id] = data
            self.update_database_file(file_path=file_path, update_data=file_content)
            return file_content[data_id]
        except KeyError:
            return None

    def delete_data_from_database_file(self, *,
                                       file_path: str,
                                       data_id: str,
                                       delete_confirm: bool = False,
                                       ) -> dict | None:

        """
        **WARNING: deletes all data** in JSON database file, that stored by ID (primary key) and **returns deleted content**, if argument *delete_confirm* is True. 
        
        **NOT RECOMMENDED** to use! 

        **FileNotFoundError**, **JSONDecodeError**, **KeyError** are **handed** and if the error happened, function **returns None**. 
        """

        file_content: dict | None = self.read_database_file(file_path=file_path)

        if not delete_confirm or file_content is None:
            return None
        
        try:
            deleted_data: dict = file_content[data_id]
            del file_content[data_id]
            self.update_database_file(file_path=file_path, update_data=file_content)

            return deleted_data
        except KeyError:
            return None
    
db: DataBase = DataBase(**database_config_registry)