import csv
import random
import json


class Handlecsv:
    def __init__(self) -> None:
        self.cities = []
        self.cities_dict = {}
        self.movie_dict = {}
        self.movies_updated = []
        self.read_csv_cities()
        self.read_csv_movies()
        self.convert_cities_to_array()
        self.update_movies()

    def read_csv_movies(self) -> None:
        csv_file = open("./csvFiles/netflix1.csv", newline="")
        self.movie_dict = csv.DictReader(csv_file)

    def read_csv_cities(self) -> None:
        csv_file = open("./csvFiles/cities.csv", newline="")
        self.cities_dict = csv.DictReader(csv_file)

    def remove_special_characters(self, value: str) -> str:
        special_characters = ["@", "#", "$", "*", "&"]
        normal_string = value

        for i in special_characters:
            normal_string = normal_string.replace(i, "and")

        return normal_string

    def convert_cities_to_array(self) -> None:
        for valor in list(self.cities_dict):
            self.cities.append(valor["cities"])

    def update_raking_value(self) -> float:
        return round(random.uniform(3, 10), 1)

    def update_movies(self) -> None:

        for value in self.movie_dict:
            value["city"] = self.cities[random.randint(0, 199)]
            value["listed_in"] = self.remove_special_characters(value["listed_in"])
            value["title"] = self.remove_special_characters(value["title"])
            value["rating"] = self.update_raking_value()

            self.movies_updated.append(value)

    def write_new_csv(self) -> None:
        new_file = open("netflix_updated.csv", "w", newline="")
        fields = [
            "show_id",
            "type",
            "title",
            "director",
            "country",
            "date_added",
            "release_year",
            "rating",
            "duration",
            "listed_in",
            "city",
        ]
        writer = csv.DictWriter(new_file, fieldnames=fields)

        writer.writeheader()

        for value in self.movies_updated:
            writer.writerow(value)

    def get_movies(self):
        return self.movies_updated


handle = Handlecsv()

print(handle.get_movies())
