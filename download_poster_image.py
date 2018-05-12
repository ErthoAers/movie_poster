import json, requests, re, sys

def get_movie_id_from_url(url):
        if url is None:
            return None
        return re.search("(tt[0-9]{7})", url).group()

def downloader():
    print("********** Download posters **********")

    with open('imdb_output.json') as f:
        movies = json.load(f)
    movies_processed, i = [], 0

    for m in movies:
        if m['image_urls'] != []:
            movie_num = get_movie_id_from_url(m['movie_imdb_link'])
            with open('poster/%s.jpg' % movie_num, 'wb') as p:
                r = requests.get(m['image_urls'][0])
                p.write(r.content)
            movies_processed.append({movie_num:m})
            i += 1
            if i % 1000 == 0:
                sys.stdout.write("\r%d" % i + ' complete')
                sys.stdout.flush() 
    sys.stdout.write("\rDownload complete, saved %d posters.\n\n" % (i))

    print("Saving processed imdb data...")
    with open('imdb_process.json', 'w') as f:
        json.dump(movies_processed, f)
    print("Process complete, saved as imdb_process.json.")

if __name__ == '__main__':
    downloader()