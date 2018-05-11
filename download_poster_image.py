import json, requests, re

def get_movie_id_from_url(url):
        if url is None:
            return None
        return re.search("(tt[0-9]{7})", url).group()

def downloader():
    with open('imdb_output.json') as f:
        movies = json.load(f)

    movies_processed = []
    for m in movies:
        if m['image_urls'] != []:
            movie_num = get_movie_id_from_url(m['movie_imdb_link'])
            with open('poster/%s.jpg' % movie_num, 'wb') as p:
                r = requests.get(m['image_urls'][0])
                p.write(r.content)
            movies_processed.append({movie_num:m})

    with open('imdb_process.json', 'w') as f:
        json.dump(movies_processed, f)

if __name__ == '__main__':
    downloader()