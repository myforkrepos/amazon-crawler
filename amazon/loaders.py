from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join
from w3lib.html import remove_tags


class DefaultItemLoader(ItemLoader):
    default_in_processor = MapCompose(remove_tags, unicode.strip)
    default_output_processor = TakeFirst()


class ListingItemLoader(DefaultItemLoader):
	is_prime_in = MapCompose(bool)


class ReviewItemLoader(DefaultItemLoader):
    date_in = MapCompose(lambda x: x[3:] if len(x) >= 3 else x)
