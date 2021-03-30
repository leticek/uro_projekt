class TrainingPlan:
    def __init__(self, exercises=None, name=None, length=None, focus=None, client=None) -> None:
        super().__init__()

        self.client = client
        self.name = name
        self.length = length
        self.focus = focus
        self.exercises = exercises
