import mlflow
from mlflow.tracking import MlflowClient
import os

client = MlflowClient()
exp_id = client.create_experiment(
    name="scraggle-town",
    artifact_location=f"{os.environ['HOME']}/mlflow/mlartifacts/",
)
experiment = client.get_experiment(exp_id)

# Show experiment info
print("Name: {}".format(experiment.name))
print("Experiment ID: {}".format(experiment.experiment_id))
print("Artifact Location: {}".format(experiment.artifact_location))
print("Lifecycle_stage: {}".format(experiment.lifecycle_stage))

# Log a run to it
with mlflow.start_run(experiment_id=experiment.experiment_id):
    mlflow.log_param("a", 1)
    mlflow.log_metric("b", 2)
