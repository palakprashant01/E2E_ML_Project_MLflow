# E2E_ML_Project_MLflow

## Workflows:

This project will follow the following workflow:
1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the app.py (UI related functionality)

# How to run this project?:
1. Clone the repository
```bash
https://github.com/palakprashant01/E2E_ML_Project_MLflow
```

2. Create a conda environment after opening the repository
```bash
conda create -n mlproj python=3.8 -y
```

```bash
conda activate mlproj
```

3. Install the requirements
```bash
pip install -r requirements.txt
```

```bash
#Run the following command
python app.py
```

Now, open your local host and port

# MLflow:
[Documentation](https://mlflow.org/docs/latest/index.html)

# On DagsHub:
[dagshub](https://dagshub.com/)
MLFLOW_TRACKING_URI = https://dagshub.com/palakprashant01/E2E_ML_Project_MLflow \
MLFLOW_TRACKING_USERNAME = palakprashant01
MLFLOW_TRACKING_PASSWORD = 3cf233390d08aba5d82ef1c44cba9481b0cfecb5

Run this to export as environment variables:
```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/palakprashant01/E2E_ML_Project_MLflow
export MLFLOW_TRACKING_USERNAME=palakprashant01
export MLFLOW_TRACKING_PASSWORD=3cf233390d08aba5d82ef1c44cba9481b0cfecb5

```
