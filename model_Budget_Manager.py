from Profile import Profile
from Income import Income
from Sort import Sort
from money import Money
from balance import Balance
from Consumption import Consumption
class Model:
    __profiles: list[Profile]
    __income: Income
    __comsumption: Consumption
    __sort: Sort
    __balance: Balance
