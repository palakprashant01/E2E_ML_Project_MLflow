import dagshub
dagshub.init(repo_owner='palakprashant01', repo_name='E2E_ML_Project_MLflow', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)

