import scrapy
import json
import re


class LuluSpider(scrapy.Spider):
    name = 'lulu'
    allowed_domains = ['shop.lululemon.com']
    start_urls = [
        'https://shop.lululemon.com/api/p/women-crops/Align-Crop-23-Diamond-Dye']

    def parse(self, response):
        resps = json.loads(response.body)
        prods = resps.get("data").get("attributes").get(
            "child-skus")
        review = resps.get("data").get("attributes").get(
            "purchase-attributes").get("reviews").get("count")
        url = resps.get("data").get("attributes").get(
            "purchase-attributes").get("all-inseam").get("productUrl")

        for prod in prods:
            yield {
                'Brand': 'Lululemon',
                'Size': prod.get("size"),
                'Price': prod.get("price-details").get("list-price"),
                'Saleprice': prod.get("price-details").get("sale-price"),
                'In-Stock': prod.get("available"),
                'Sku': prod.get("id"),
                'reviews': review,
                'url': url

            }

        #
        # name = resp.get("product-sizes")
        # saleprice = resp.get("product-on-sale")
        # if saleprice == "0":
        #     saleprice = "N/A"
        # instock = resp.get("is-sold-out")

        # description = resp.get("why-we-made-this")
        # link = resp.get("product-site-map-pdp-url")
        # sku = resp.get("default-sku")
        # icon = resp.get("sku-sku-images")[0]

        # color = resp.get("data").get("attributes").get(
        # #     "purchase-attributes").get("selected-swatch-color")

        # yield{
        #     'brand': 'lululemon',
        #     'name': name,
        #     'price': price,
        #     'size': size,
        #     'sale-price': saleprice,
        #     'In-Stock': instock,
        #     'Description': description,
        #     'url': link,
        #     'sku': sku,
        #     'icon': icon,
            # 'review': review,
            # 'color': color,
            # 'breadcrumbs': category

        # }

        # nexturl = f"https://shop.lululemon.com/api/r/item-to-items?item-id= {}"
        # lasturl = resp.get("links").get("last")
        # if nexturl:
        #     yield scrapy.Request(nexturl, callback=self.parse)
        # else:
        #     yield scrapy.Request(lasturl, callback=self.parse)

# need to loop through each size and color.
# need to grab description,and color -- find out how
# need url for each item as well
# need pagination, get that from catergories xhr point

# category = resp.get("data").get("attributes").get(
        #     "refinement-crumbs").get("ancestors").get("navigation-state")[0].get("label")[1]
