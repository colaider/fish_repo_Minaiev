import datetime
from datetime import date
from typing import List, Union



# method
# attributes


class Fish:
    def __init__(self, name, weight, price_in_uah_per_kilo, catch_date) -> None:
        self.name = name
        self.price_in_uah_per_kilo = price_in_uah_per_kilo
        self.catch_date = catch_date
        self.origin = "Norway"
        self.body_only = True
        self.weight = weight


class FishShop:
    arr_of_fihes = []
    total_price_of_sold_fish = 0.0
    total_weight_of_sold_fish = 0.0

    def add_fish(self, fish_name: str, total_weight: float, fish_price: float, date: date) -> None:
        fish = Fish(name = fish_name, weight = total_weight, price_in_uah_per_kilo = fish_price, catch_date=date)
        self.arr_of_fihes.append(fish)


    def get_fish_names_sorted_by_price(self) -> List[Union[str, float]]:
        sorted_arr_of_fishes = sorted(self.arr_of_fihes, key=lambda x:x.price_in_uah_per_kilo, reverse=False)
        length = len(self.arr_of_fihes)
        for i in range(length):
            print(sorted_arr_of_fishes[i].price_in_uah_per_kilo)
        return(sorted_arr_of_fishes)

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



class Seller:
    def set_price_per_kilo_to_fish(self, name:str):
        pass
    def calculate_kilo_of_sold_fish(self):
        pass

class Buyer:
    count_of_money = 0
    def buy_fish_by_name(self, name:str):
        pass

fish_de_market_la_pizza = FishShop()
fish_de_market_la_pizza.add_fish("Pachini", 12.4, 34.4, date(2022, 1, 15))
fish_de_market_la_pizza.add_fish("Pablo", 1.4, 3.4,date(2022, 1, 25))
fish_de_market_la_pizza.add_fish("Franchesko", 132.4, 344.4,date(2022, 1, 10))
fish_de_market_la_pizza.get_fish_names_sorted_by_price()
fish_de_market_la_pizzasell_fish("Pablo", 1.4)
fish_de_market_la_pizza.cast_out_old_fish()
