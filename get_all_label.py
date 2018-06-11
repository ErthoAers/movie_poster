import json

print('Loading data...')
with open('imdb_cleaned.json') as f:
    movies = json.load(f)
print('Data loaded.')

print('Getting all label...')
color, genres, language, country = set(), set(), set(), set()
for m in movies:
    tt = list(m.keys())[0]
    color |= set(m[tt]['color'])
    genres |= set(m[tt]['genres'])
    language |= set(m[tt]['language'])
    country |= set(m[tt]['country'])

label = {'color': list(color), 'genres': list(genres), 'language': list(language), 'country': list(country)}
with open('imdb_label.json', 'w') as f:
    json.dump(label, f)
print('Done. Labels saved as imdb_label.json.')

color_dict = {i: set() for i in color}
genres_dict = {i: set() for i in genres}
language_dict = {i: set() for i in language}
country_dict = {i: set() for i in country}

print('Getting the list for all label...')
for m in movies:
    tt = list(m.keys())[0]
    for i in m[tt]['color']:
        color_dict[i].add(tt)
    for i in m[tt]['genres']:
        genres_dict[i].add(tt)
    for i in m[tt]['language']:
        language_dict[i].add(tt)
    for i in m[tt]['country']:
        country_dict[i].add(tt)

color_save = {k: list(v) for k, v in color_dict.items()}
genres_save = {k: list(v) for k, v in genres_dict.items()}
language_save = {k: list(v) for k, v in language_dict.items()}
country_save = {k: list(v) for k, v in country_dict.items()}
saved = {'color': color_save, 'genres': genres_save, 'language': language_save, 'country': country_save}
with open('label_list.json', 'w') as f:
    json.dump(saved, f)
print('Done.')

color_save = {k: len(v) for k, v in saved['color'].items()}
genres_save = {k: len(v) for k, v in saved['genres'].items()}
language_save = {k: len(v) for k, v in saved['language'].items()}
country_save = {k: len(v) for k, v in saved['country'].items()}
saved = {'color': color_save, 'genres': genres_save, 'language': language_save, 'country': country_save}
with open('label_number.json', 'w') as f:
    json.dump(saved, f)

