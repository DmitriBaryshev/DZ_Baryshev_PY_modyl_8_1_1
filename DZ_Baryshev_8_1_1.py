# Задание 1
import json


class CountryCapitals:
    def __init__(self):
        self.data = {}

    def add_data(self, country, capital):
        self.data[country] = capital

    def remove_data(self, country):
        if country in self.data:
            del self.data[country]
        else:
            print(f"{country} not found")

    def search_data(self, country):
        if country in self.data:
            return f"The capital of {country} is {self.data[country]}"
        else:
            return f"{country} not found"

    def edit_data(self, country, new_capital):
        if country in self.data:
            self.data[country] = new_capital
        else:
            print(f"{country} not found")

    def save_data(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.data, file)

    def load_data(self, filename):
        with open(filename, 'r') as file:
            self.data = json.load(file)


cc = CountryCapitals()
cc.add_data("Russia", "Moscow")
cc.add_data("USA", "Washington")
print(cc.search_data("Russia"))
cc.edit_data("Russia", "Saint Petersburg")
print(cc.search_data("Russia"))
cc.save_data("countries.json")
cc.remove_data("USA")
print(cc.search_data("USA"))
cc.load_data("countries.json")
print(cc.search_data("USA"))


# Задание 2
import json

class MusicLibrary:
    def __init__(self):
        self.data = {}

    def add_data(self, group, album):
        self.data[group] = album

    def remove_data(self, group):
        if group in self.data:
            del self.data[group]
        else:
            print(f"{group} not found")

    def search_data(self, group):
        if group in self.data:
            return f"The album of {group} is {self.data[group]}"
        else:
            return f"{group} not found"

    def edit_data(self, group, new_album):
        if group in self.data:
            self.data[group] = new_album
        else:
            print(f"{group} not found")

    def save_data(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.data, file)

    def load_data(self, filename):
        with open(filename, 'r') as file:
            self.data = json.load(file)


ml = MusicLibrary()
ml.add_data("The Beatles", "Abbey Road")
ml.add_data("Led Zeppelin", "Led Zeppelin IV")
print(ml.search_data("The Beatles"))
ml.edit_data("The Beatles", "Sgt. Pepper's Lonely Hearts Club Band")
print(ml.search_data("The Beatles"))
ml.save_data("albums.json")
ml.remove_data("Led Zeppelin")
print(ml.search_data("Led Zeppelin"))
ml.load_data("albums.json")
print(ml.search_data("Led Zeppelin"))
