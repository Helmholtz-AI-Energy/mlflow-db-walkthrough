import mlflow

# Launch a run. The experiment is inferred from the MLFLOW_EXPERIMENT_NAME environment
# variable, or from the --experiment-name parameter passed to the MLflow CLI (the latter
# taking precedence)
with mlflow.start_run():
    mlflow.log_param("a", 1)
    mlflow.log_metric("b", 2)
    mlflow.set_tag("usage", "simple")
    # mlflow.log_artifact("hello_world.txt")
