import sys, os
import urllib.request
import json, csv

def process_url_info():
    print("********** Download IMDb basic data ***********")
    url = 'https://datasets.imdbws.com/title.basics.tsv.gz'
    name = 'title.basics.tsv.gz'

    def report(count, blockSize, totalSize):
        percent = int(count * blockSize * 100 / totalSize)
        sys.stdout.write("\r%d%%" % percent + ' complete')
        sys.stdout.flush()
    sys.stdout.write('\rFetching ' + name + '...\n')
    try:
        urllib.request.urlretrieve(url, name, reporthook=report)
    except:
        print('Download failed.')
    sys.stdout.write("\rDownload complete, saved as %s\n\n" % (name))
    sys.stdout.flush()

    print("********** Extract IMDb basic data ***********")
    os.system('gunzip %s' % name)
    print("Extract complete, saved as title.basics.tsv\n")

    print("********** Get the url of all movies **********")
    f = open('title.basics.tsv')
    reader = csv.reader(f, delimiter='\t')
    data, i = [], 0
    for row in reader:
        if row[1] == 'movie':
            info = {"movie_imdb_link": "http://www.imdb.com/title/%s/?ref_=fn_tt_tt_1" % row[0], "movie_name": row[2]}
            data.append(info)
            i += 1
            if i % 1000 == 0:
                sys.stdout.write("\r%d" % i + ' complete')
                sys.stdout.flush() 
    f.close()
    fetch_name ='fetch_imdb_url.json'
    sys.stdout.write('\rProcess ' + fetch_name + '...\n') 
    with open(fetch_name, 'w') as f:
        json.dump(data, f)
    sys.stdout.write("\rProcess complete, saved as %s\n\n" % (fetch_name))

if __name__ == '__main__':
    process_url_info()