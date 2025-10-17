import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, 'r', encoding='utf-8') as handle:
        return json.load(handle)


animals_data = load_data('animals_data.json')
output = ''

for fox in animals_data:
    fox_name = fox.get('name')
    fox_diet = fox.get('characteristics').get('diet')
    fox_locations = ', '.join(list(fox.get('locations')))
    fox_type = fox.get('characteristics').get('type')

    output += '<li class=\"cards__item\">'
    if fox_name:
        output += f'<div class="card__title">{fox_name}</div>\n'
        output += '<p class="card__text">'
    if fox_diet:
        output += f'<strong>Diet:</strong> {fox_diet}<br/>\n'
    if fox_locations:
        output += f'<strong>Location:</strong> {fox_locations}<br/>\n'
    if fox_type:
        output += f'<strong>Type:</strong> {fox_type}<br/>\n'
    output += '</p>\n'
    output += '</li>\n'

print(output)

with open('animals_template.html', 'r', encoding='utf-8') as f:
    animals_html_text = f.read()

updated_html = animals_html_text.replace('__REPLACE_ANIMALS_INFO__', output)

# Ensures the HTML file declares UTF-8 encoding to prevent character display issues
updated_html = updated_html.replace('<head>', '<head>\n        <meta charset="UTF-8">')

with open('animals.html', 'w', encoding='utf-8') as f:
    f.write(updated_html)

