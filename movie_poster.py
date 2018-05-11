from get_imdb_url import process_url_info
from scrapy.cmdline import execute
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy', 'crawl', 'imdb', '-o', 'imdb_output.json'])