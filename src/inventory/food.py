from src.inventory.base_class import BaseProduct
import datetime as dt
from typing import List, Dict


class Food(BaseProduct):
    def __init__(self, kcal: int, best_before: dt.datetime, nutritional_value: Dict, *args, **kwargs):
        self.kcal = kcal
        self.best_before = best_before
        self.nutritional_value = nutritional_value
        super().__init__(1, 1, "1")


