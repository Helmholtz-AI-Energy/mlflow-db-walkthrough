import mlflow
from mlflow.tracking import MlflowClient

# Connect to the client and get an experiment
client = MlflowClient()
experiment = client.get_experiment_by_name("flonk")  # returns a list of mlflow.entities.Experiment
print(experiment)

# Log a run to it
with mlflow.start_run(experiment_id=experiment.experiment_id):
    mlflow.log_param("a", 1)
    mlflow.log_metric("b", 2)
    mlflow.set_tag("usage", "flonk")
