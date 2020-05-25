from WIET_sourcing.tasks.config import huey
from WIET_sourcing.tasks import create_app_huey
from huey import crontab
from WIET_sourcing.models import db
from WIET_sourcing.question_loader.question_loader_manager import QuestionLoaderManager
import logging

huey_app = create_app_huey()


@huey.periodic_task(crontab(minute="*/15"))
def recalculate_dataset_answer_summary():
    """
    TODO: look through all datasets and close those that have convergence above threshold and satisfactory
        amount of answers
    """
    pass
