import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


animals_data = load_data('animals_data.json')
output = ""

for fox in animals_data:
    fox_name = fox.get("name")
    fox_diet = fox.get("characteristics").get("diet")
    fox_locations = ", ".join(list(fox.get("locations")))
    fox_type = fox.get("characteristics").get("type")

    output += "<li class=\"cards__item\">"
    if fox_name:
        output += f"Name: {fox_name}<br/>\n"
    if fox_diet:
        output += f"Diet: {fox_diet}<br/>\n"
    if fox_locations:
        output += f"Location: {fox_locations}<br/>\n"
    if fox_type:
        output += f"Type: {fox_type}<br/>\n"
    output += '</li>'
    output += "\n"

print(output)

with open("animals_template.html", "r") as f:
    animals_html_text = f.read()

updated_html = animals_html_text.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w") as f:
    f.write(updated_html)

