import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, 'r', encoding='utf-8') as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """Converts an animal dictionary into an HTML list item string."""
    animal_name = animal_obj.get('name')
    animal_diet = animal_obj.get('characteristics').get('diet')
    animal_locations = ', '.join(list(animal_obj.get('locations')))
    animal_type = animal_obj.get('characteristics').get('type')

    output = ''
    output += '<li class=\"cards__item\">'
    if animal_name:
        output += f'<div class="card__title">{animal_name}</div>\n'
        output += '<p class="card__text">'
    if animal_diet:
        output += f'<strong>Diet:</strong> {animal_diet}<br/>\n'
    if animal_locations:
        output += f'<strong>Location:</strong> {animal_locations}<br/>\n'
    if animal_type:
        output += f'<strong>Type:</strong> {animal_type}<br/>\n'
    output += '</p>\n'
    output += '</li>\n'

    return output


def main():
    """Generates an HTML file with animal information from a JSON data source."""
    animals_data = load_data('animals_data.json')

    output = ''
    for animal in animals_data:
        output += serialize_animal(animal)

    with open('animals_template.html', 'r', encoding='utf-8') as f:
        animals_html_text = f.read()

    updated_html = animals_html_text.replace('__REPLACE_ANIMALS_INFO__', output)

    # Ensures the HTML file declares UTF-8 encoding to prevent character display issues
    updated_html = updated_html.replace('<head>', '<head>\n        <meta charset="UTF-8">')

    with open('animals.html', 'w', encoding='utf-8') as f:
        f.write(updated_html)


if __name__ == "__main__":
    main()
