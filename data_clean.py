import json

print('Loading...')
with open('imdb_process.json') as f:
    movies = json.load(f)
print('Data loaded.')

print('Process...')
for m in movies:
    tt = list(m.keys())[0]
    try:
        m[tt]['color'] = [i.strip() for i in m[tt]['color']]
        m[tt]['duration'] = [i.strip() for i in m[tt]['duration']]
        m[tt]['gross'] = [i.strip() for i in m[tt]['gross']]
        m[tt]['genres'] = [i.strip() for i in m[tt]['genres']]
        m[tt]['gross'] = [i.strip() for i in m[tt]['gross']]
        m[tt]['movie_title'] = m[tt]['movie_title'].strip()
        m[tt]['plot_keywords'] = [i.strip() for i in m[tt]['plot_keywords']]
        m[tt]['language'] = [i.strip() for i in m[tt]['language']]
        m[tt]['content_rating'] = [i.strip() for i in m[tt]['content_rating']]
        m[tt]['budget'] = [i.strip() for i in m[tt]['budget']]
        m[tt]['imdb_score'] = [i.strip() for i in m[tt]['imdb_score']]
        m[tt]['aspect_ratio'] = m[tt]['aspect_ration'].strip()
    except:
        continue
print('Done.')

print('Saving...')
with open('imdb_cleaned.json', 'w') as f:
    json.dump(movies, f)
print('Done.')
