from get_imdb_url import processor
from download_poster_image import downloader
from scrapy.cmdline import execute
import sys, os

processor()

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy', 'crawl', 'imdb', '-o', 'imdb_output.json'])

downloader()
