class MealPlan:

    def __init__(self, weight_before=None, weigh_goal=None, plan_category=None, meals=None, client=None) -> None:
        super().__init__()

        self.client = client
        self.weight_before = weight_before
        self.weight_goal = weigh_goal
        self.plan_category = plan_category
        self.meals = meals
