import logging
import sys
import mlflow
import tempfile
import os


class NotebookMlflowLogger:
    def __init__(self):
        self.logger = None
        self.filename = ""

    def get_logger(self, level=logging.INFO):
        if os.getenv("DKUBE_JOB_CLASS") != "notebook":
            return logging.getLogger()
        logger = logging.getLogger()
        logger.handlers.clear()
        logger.setLevel(level)
        log_formatter = logging.Formatter(
            "%(asctime)s  %(name)s  |%(levelname)-5.5s|  %(message)s")
        temp = tempfile.NamedTemporaryFile(suffix='.log', delete=False)
        self.filename = temp.name
        file_handler = logging.FileHandler(temp.name)
        file_handler.setFormatter(log_formatter)
        logger.addHandler(file_handler)

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(log_formatter)
        logger.addHandler(console_handler)
        self.logger = logger
        return logger

    def flush(self):
        if os.getenv("DKUBE_JOB_CLASS") != "notebook":
            return

        if mlflow.active_run():
            try:
                mlflow.log_artifact(self.filename, "logs")
                os.remove(self.filename)
            except Exception as e:
                print("Failed to capture logs", e)
        else:
            print("No active run found")
