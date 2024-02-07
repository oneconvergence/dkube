import logging
import sys
import mlflow
import tempfile
import os


class NotebookMlflowLogger:
    def get_logger(self, level=logging.INFO):
        if os.getenv("DKUBE_JOB_CLASS") != "notebook":
            return logging.getLogger()
        logger = logging.getLogger()
        if logger.handlers:
            return logger
        else:
            logger.setLevel(level)
            log_formatter = logging.Formatter(
                "%(asctime)s  %(name)s  |%(levelname)-5.5s|  %(message)s")
            temp = tempfile.NamedTemporaryFile(suffix='.log', delete=False)
            file_handler = logging.FileHandler(temp.name)
            file_handler.setFormatter(log_formatter)
            logger.addHandler(file_handler)

            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setFormatter(log_formatter)
            logger.addHandler(console_handler)
            return logger

    def flush(self):
        if os.getenv("DKUBE_JOB_CLASS") != "notebook":
            return
        logger = logging.getLogger()
        log_paths = [handler.baseFilename for handler in logger.handlers if isinstance(
            handler, logging.FileHandler)]
        log_file = next(iter(log_paths))
        if mlflow.active_run():
            mlflow.log_artifact(log_file, "logs")
            os.remove(log_file)
        else:
            print("No active run found")
