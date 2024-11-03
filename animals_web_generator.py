import json


def load_data(file_path: str) -> dict:
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def load_html_template(file_path: str) -> str:
    """ Loads an HTML file """
    with open(file_path, "r") as handle:
        return handle.read()


def get_animals_data() -> dict[str, dict[str, str]]:
    """ Returns a dictionary with the relevant data for each animal """
    full_animals_data = load_data("animals_data.json")

    animals_data = {}
    for animal in full_animals_data:
        animal_data = {}
        animal_data["taxonomy"] = " >> ".join(animal["taxonomy"].values())
        if "characteristics" in animal:
            if "diet" in animal["characteristics"]:
                animal_data["Diet"] = animal["characteristics"]["diet"]
            if "type" in animal["characteristics"]:
                animal_data["Type"] = animal["characteristics"]["type"]
            if "lifespan" in animal["characteristics"]:
                animal_data["Lifespan"] = animal["characteristics"]["lifespan"]
        if "locations" in animal:
            animal_data["Location"] = " and ".join(animal["locations"])
        animals_data[animal["name"]] = animal_data
    return animals_data


def build_animal_info_html(animal_name: str, animal_data: dict[str, str]) -> str:
    """ Returns the HTML code for the information of an animal """
    html_code = '<li class="cards__item">\n'
    html_code += f'<div class="card__title">{animal_name}</div>\n'
    html_code += f'<p class="card__taxonomy">{animal_data["taxonomy"]}</p>\n'
    html_code += '<p class="card__text">\n'
    for key, value in animal_data.items():
        if key != "taxonomy":
            html_code += f'<strong>{key}:</strong> {value}<br/>\n'
    html_code = html_code[:-6]
    html_code += '\n</p>\n</li>\n'
    return html_code


if __name__ == "__main__":
    new_html = load_html_template("animals_template.html")
    animals_data = get_animals_data()

    html_animals_data = ""
    for animal_name, animal_data in animals_data.items():
        html_animals_data += build_animal_info_html(animal_name, animal_data)

    new_html = new_html.replace("__REPLACE_ANIMALS_INFO__", html_animals_data)
    with open("animals.html", "w") as handle:
        handle.write(new_html)