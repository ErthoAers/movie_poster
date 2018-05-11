# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbinfoItem(scrapy.Item):
    # define the fields for your item here like:
    movie_imdb_link = scrapy.Field()
    imdb_score = scrapy.Field()
    movie_title = scrapy.Field()
    title_year = scrapy.Field()
    num_voted_users = scrapy.Field()
    genres = scrapy.Field()
    budget = scrapy.Field()
    color = scrapy.Field()
    gross = scrapy.Field()
    duration = scrapy.Field()
    country = scrapy.Field()
    language = scrapy.Field()
    plot_keywords = scrapy.Field()
    storyline = scrapy.Field()
    aspect_ratio = scrapy.Field()
    content_rating = scrapy.Field()
    num_user_for_reviews = scrapy.Field()
    num_critic_for_reviews = scrapy.Field()
    cast_info = scrapy.Field()
    director_info = scrapy.Field()
    num_facebook_like = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
