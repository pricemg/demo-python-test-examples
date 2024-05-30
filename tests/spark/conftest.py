import logging

from pyspark.sql import SparkSession
import pytest


def suppress_py4j_logging():
    """Suppress spark logging."""
    logger = logging.getLogger('py4j')
    logger.setLevel(logging.WARN)


@pytest.fixture(scope='session')
def spark_session():
    """Set up spark session fixture."""
    suppress_py4j_logging()

    yield (
        SparkSession
        .builder
        .master('local[2]')
        .appName('cprices_test_context')
        .config('spark.sql.shuffle.partitions', 1)
        # This stops progress bars appearing in the console whilst running
        .config('spark.ui.showConsoleProgress', 'false')
        # .config('spark.sql.execution.arrow.enabled', 'true')
        .config('spark.executorEnv.ARROW_PRE_0_15_IPC_FORMAT', 1)
        .config('spark.workerEnv.ARROW_PRE_0_15_IPC_FORMAT', 1)
        .getOrCreate()
    )
