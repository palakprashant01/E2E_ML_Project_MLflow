from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen = True)
class DataIngestionConfiguration:
    root_directory: Path
    source_URL: str
    local_data: Path
    unzip_directory: Path