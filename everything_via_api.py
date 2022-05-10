import mlflow
from mlflow.tracking import MlflowClient

# First set the tracking URI
mlflow_server = "http://127.0.0.1:1234"
mlflow.set_tracking_uri(mlflow_server)

# This sets the experiment name
experiment_name = "gday"
exp_info = MlflowClient().get_experiment_by_name(experiment_name)

# and create it if it doesn't exist
exp_id = exp_info.experiment_id if exp_info else MlflowClient().create_experiment(experiment_name)

# Log a run to it
with mlflow.start_run(experiment_id=exp_id):
    mlflow.log_param("a", 1)
    mlflow.log_metric("b", 2)
    mlflow.set_tag("usage", "simply pythonic")
