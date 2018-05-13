import json, requests, re, sys
from multiprocessing.dummy import Pool as ThreadPool

def get_movie_id_from_url(url):
        if url is None:
            return None
        return re.search("(tt[0-9]{7})", url).group()

i = 0
def download_poster(m):
    global i
    if m['image_urls'] != None:
        try:
            movie_num = get_movie_id_from_url(m['movie_imdb_link'])
            r = requests.get(m['image_urls'][0])
        except:
            return None
        with open('poster/%s.jpg' % movie_num, 'wb') as p:
            p.write(r.content)
        i += 1
        if i % 100 == 0:
            sys.stdout.write("\r%d" % i + ' complete')
            sys.stdout.flush()
        return {movie_num:m}
    return None

def downloader():
    print("********** Download posters **********")
    print("Loading the JSON file...")
    with open('imdb_output.json') as f:
        movies = json.load(f)
    print("Loading finish.")

    print("Download start.")
    pool = ThreadPool(16)
    movies_first_processed = pool.map(download_poster, movies)
    movies_processed = [m for m in movies_first_processed if m != None]
    print("Download complete, saved %d posters." % (len(movies_processed)))

    print("Saving processed imdb data...")
    with open('imdb_process.json', 'w') as f:
        json.dump(movies_processed, f)
    print("Process complete, saved as imdb_process.json.")

if __name__ == '__main__':
    downloader()