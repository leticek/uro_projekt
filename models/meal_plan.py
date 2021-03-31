class MealPlan:

    def __init__(self, plan_category=None, meals=None, name=None) -> None:
        super().__init__()

        self.name = name
        self.plan_category = plan_category
        self.meals = meals
