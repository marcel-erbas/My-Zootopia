import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


animals_data = load_data('animals_data.json')

for fox in animals_data:
    fox_name = fox.get("name")
    fox_diet = fox.get("characteristics").get("diet")
    fox_locations = ", ".join(list(fox.get("locations")))
    fox_type = fox.get("characteristics").get("type")

    if fox_name:
        print(f"Name: {fox_name}")
    if fox_diet:
        print(f"Diet: {fox_diet}")
    if fox_locations:
        print(f"Location: {fox_locations}")
    if fox_type:
        print(f"Type: {fox_type}")
    print()
