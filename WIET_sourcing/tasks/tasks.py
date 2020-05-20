from WIET_sourcing.tasks.config import huey
from WIET_sourcing.tasks import create_app_huey
from huey import crontab
from WIET_sourcing.models import db
import logging

huey_app = create_app_huey()


@huey.periodic_task(crontab(minute="*/15"))
def recalculate_dataset_answer_summary():
    # TODO: implement transaction on database
    logging.info("periodic task is run")
    
    pass
