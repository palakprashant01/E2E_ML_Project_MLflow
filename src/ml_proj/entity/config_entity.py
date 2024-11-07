from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen = True)
class DataIngestionConfiguration:
    root_directory: Path
    source_URL: str
    local_data: Path
    unzip_directory: Path

#Prepare the entity for data validation
@dataclass(frozen = True)
class DataValidationConfiguration:
    root_directory: Path
    status_file: str
    unzip_data_directory: Path
    entire_schema: dict