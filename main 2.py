import datetime
from datetime import date
from typing import List, Union


class Fish:
    def __init__(self, age_in_month:float ,weight:float):
       self.age_in_month = age_in_month
       self.weight = weight

class FishInfo(Fish):
    def __init__(self, name:str, weight:float, price_in_uah_per_kilo:float, catch_date:datetime) -> None:
        self.name = name
        self.price_in_uah_per_kilo = price_in_uah_per_kilo
        self.catch_date = catch_date
        self.due_date = catch_date
        self.origin = "Norway"
        self.body_only = True

class FishBox:
    def __init__(self, fishInfo: FishInfo, weight:float, package_date:datetime, height:float, width:float, is_alive:bool):
        self.fishInfo = fishInfo
        self.weight = weight
        self.package_date = package_date
        self.height = height
        self.width = width
        self.is_alive = is_alive

class FishShop:
    arr_of_fihes = []
    arr_of_fishBoxes = []
    total_price_of_sold_fish = 0.0
    total_weight_of_sold_fish = 0.0

    def add_fish(self, fish_name: str, total_weight: float, fish_price: float, date: date) -> None:
        fish = FishInfo(name = fish_name, weight = total_weight, price_in_uah_per_kilo = fish_price, catch_date=date)
        self.arr_of_fihes.append(fish)

    def add_fish(self, fishInfo: FishInfo, weight:float, package_date:datetime, height: float, width: float, is_alive: bool) -> None:
        fish = FishBox(fishInfo = fishInfo, weight = weight, package_date = package_date, height = height, width = width, is_alive = is_alive)
        self.arr_of_fihes.append(fish)


    def get_fish_names_sorted_by_price(self) -> List[Union[str, float]]:
        sorted_arr_of_fishes = sorted(self.arr_of_fihes, key=lambda x:x.price_in_uah_per_kilo, reverse=False)
        length = len(self.arr_of_fihes)
        for i in range(length):
            print(sorted_arr_of_fishes[i].price_in_uah_per_kilo)
        return(sorted_arr_of_fishes)

    def get_frozen_fish_names_sorted_by_price(self) -> List[Union[str, float]]:
        sorted_arr_of_fishes = sorted(self.arr_of_fishBoxes, key=lambda x:x.price_in_uah_per_kilo, reverse=False)
        sorted_arr_of_fishes_names = []

        length = len(sorted_arr_of_fishes)
        for i in range(length):
            if(i.is_alive == False):
                sorted_arr_of_fishes_names.append(i.fishInfo.fish_name)
        return(sorted_arr_of_fishes_names)

    def get_fresh_fish_names_sorted_by_price(self) -> List[Union[str, float]]:
        sorted_arr_of_fishes = sorted(self.arr_of_fishBoxes, key=lambda x: x.price_in_uah_per_kilo, reverse=False)
        sorted_arr_of_fishes_names = []

        length = len(sorted_arr_of_fishes)
        for i in range(length):
            if (i.is_alive == True):
                sorted_arr_of_fishes_names.append(i.fishInfo.fish_name)
        return (sorted_arr_of_fishes_names)

    def sell_fish(self, fish_name: str, weight: float) -> None:
        for i in self.arr_of_fihes:
            index_of_elemnt_in_arrey = 0
            if(i.name == fish_name):
                self.total_price_of_sold_fish += i.price_in_uah_per_kilo*weight
                self.total_weight_of_sold_fish += i.weight
                del self.arr_of_fihes[index_of_elemnt_in_arrey]
            self.index_of_elemnt_in_arrey = index_of_elemnt_in_arrey+1
        print(self.total_price_of_sold_fish)

    def cast_out_old_fish(self) -> List[Union[str, float]]:
        today_date = date.today()
        diference_between_two_dates = today_date - self.arr_of_fihes[1].catch_date
        for i in self.arr_of_fihes:
            index_of_elemnt_in_arrey = 0
            diference_between_two_dates = i.catch_date - today_date
            if(diference_between_two_dates.days > 5):
                del self.arr_of_fihes[index_of_elemnt_in_arrey]

            self.index_of_elemnt_in_arrey = index_of_elemnt_in_arrey + 1
            print(i.name)

