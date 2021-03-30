class Exercise:
    def __init__(self, weight=None, exercise=None, reps=None, series=None) -> None:
        super().__init__()

        self.exercise = exercise
        self.reps = reps
        self.series = series
        self.weight = weight
