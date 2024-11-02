import json


def load_data(file_path: str) -> dict:
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def load_html_template(file_path: str) -> str:
    """ Loads an HTML file """
    with open(file_path, "r") as handle:
        return handle.read()


def get_animals_data_string() -> str:
    """ Returns a string of animals data """
    animals_data = load_data("animals_data.json")

    animals_data_string = ""
    for animal in animals_data:
        animals_data_string += f"Name: {animal['name']}\n"
        if "characteristics" in animal:
            if "diet" in animal["characteristics"]:
                animals_data_string += f"Diet: {animal['characteristics']['diet']}\n"
            if "type" in animal["characteristics"]:
                animals_data_string += f"Type: {animal['characteristics']['type']}\n"
        if "locations" in animal:
            animals_data_string += f"Locations: {', '.join(animal['locations'])}\n"
        animals_data_string += "\n"
    print(animals_data_string)
    return animals_data_string


if __name__ == "__main__":
    new_html = load_html_template("animals_template.html")
    animals_data = get_animals_data_string()
    new_html = new_html.replace("__REPLACE_ANIMALS_INFO__", animals_data)
    with open("animals.html", "w") as handle:
        handle.write(new_html)