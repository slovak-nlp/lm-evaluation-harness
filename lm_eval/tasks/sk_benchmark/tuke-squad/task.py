from lm_eval.tasks.squadv2.task import SQuAD2


class SlovakSquad(SQuAD2):
    VERSION = 1  # Set a new version number for the Slovak task
    DATASET_PATH = "TUKE-DeutscheTelekom/squad-sk"

    def __init__(self, config=None):
        super().__init__(config)
