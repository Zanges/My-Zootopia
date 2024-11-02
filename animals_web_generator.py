import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def list_animals():
    """ Lists the animals in the data """
    animals_data = load_data("animals_data.json")
    for animal in animals_data:
        print(f"Name: {animal['name']}")
        if "characteristics" in animal:
            if "diet" in animal["characteristics"]:
                print(f"Diet: {animal['characteristics']['diet']}")
            if "type" in animal["characteristics"]:
                print(f"Type: {animal['characteristics']['type']}")
        if "locations" in animal:
            print(f"Location: {', '.join(animal['locations'])}")
        print()


if __name__ == "__main__":
    list_animals()