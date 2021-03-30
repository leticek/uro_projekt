class Meal:

    def __init__(self, content=None, calories=None, fat=None, protein=None, fibre=None, carbs=None, food_content=None) -> None:
        super().__init__()
        
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.carbs = carbs
        self.fibre = fibre
        self.food_content = food_content