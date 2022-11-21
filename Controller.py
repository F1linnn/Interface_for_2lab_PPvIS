from Profile import Profile
from Income import Income
from Sort import Sort
from money import Money
from balance import Balance
from Consumption import Consumption
from model_Budget_Manager import Model
class Controller:
    def authorization(self,name: str, password: str):
        pass

    def add_profile(self, name: name, password: str):
        pass

    def change_profile(self, profile: Profile):
        pass

    def delete_profile(self, name: str, password: str):
        pass

    def load_profile():
        pass

    def check_profile(self,name: str, password: str) -> bool:
        pass

    def add_income(self, income: Income):
        pass

    def add_consumption(self, consunmp: Consumption):
        pass

    def change_income(self, income: Income):
        pass

    def change_consumption(self, consump: Consumption):
        pass

    def delete_income(self, income: Income):
        pass

    def delete_consumption(self,consump: Consumption):
        pass
