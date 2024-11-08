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

#Prepare the entity for data transformation
@dataclass(frozen = True)
class DataTransformationConfiguration:
    root_directory: Path
    data_path: Path

#Prepare the entity for model training
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_directory: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    alpha: float
    l1_ratio: float
    target_column: str