import json
import os.path

import scrapy
import requests
from scrapy.cmdline import execute


class Chownow1Spider(scrapy.Spider):
    name = "chownow1"
    # allowed_domains = ["order.chownow.com"]
    # start_urls = ["https://order.chownow.com"]
    def start_requests(self):


        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'origin': 'https://order.chownow.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://order.chownow.com/',
            'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        }


        yield scrapy.Request(method="GET",url='https://api.chownow.com/api/restaurant/8126',headers=headers,callback=self.parse)

    def parse(self, response):
        data=json.loads(response.text)

        restaurant_address=data['address']
        restaurant_company_id=data['company_id']
        restaurant_name=data['name']
        storeopeninghours=data['fulfillment']['delivery']['display_hours']
        phone=data['phone']
        tax_rate=data['tax_rate']
        cuisines=data['cuisines']



        cookies = {
            'cn_experiment_cookie_v2': 'diner-db2ae278-1b01-44d2-a52d-9e48fd5531c5',
            '_fbp': 'fb.1.1718110978089.564941836796523946',
            '__ssid': 'beffbccedc65e3c1eaf14c5db76a320',
            '__cfruid': '20b24da25536eb75a668edbed63f660027b49ac2-1718252393',
            '_cfuvid': 'WZ3d4sTC75fEikQScf.RU0a5vBAYSZsoq8i.YODsz4s-1718252393304-0.0.1.1-604800000',
            'OptanonAlertBoxClosed': '2024-06-13T05:30:39.962Z',
            'OptanonConsent': 'isGpcEnabled=0&datestamp=Thu+Jun+13+2024+11%3A00%3A41+GMT%2B0530+(India+Standard+Time)&version=202306.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CSSPD_BG%3A1%2CC0004%3A1%2CC0005%3A1%2CC0002%3A1&AwaitingReconsent=false&geolocation=IN%3BGJ',
            'session': '942c0adf-8760-9380-cc09-67f3c46b4a35',
            '__cf_bm': '2klH0cXmRpxSgKPEmuvUK0bXtu_u53mVbBMp_5bK5zQ-1718256628-1.0.1.1-5nr9bBjMbTKtGPPn29PwyTi9b92vIBsvVGUghjfunlX08Xb_5v6U4f06mWt5wdntWm5r0rmRnnLiXS0FxAx1v0CLz9sgKb4dkeMZUawdK48',
        }

        headers = {
            'accept': 'application/json version=5.0;',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/json; charset=UTF-8',
            # 'cookie': 'cn_experiment_cookie_v2=diner-db2ae278-1b01-44d2-a52d-9e48fd5531c5; _fbp=fb.1.1718110978089.564941836796523946; __ssid=beffbccedc65e3c1eaf14c5db76a320; __cfruid=20b24da25536eb75a668edbed63f660027b49ac2-1718252393; _cfuvid=WZ3d4sTC75fEikQScf.RU0a5vBAYSZsoq8i.YODsz4s-1718252393304-0.0.1.1-604800000; OptanonAlertBoxClosed=2024-06-13T05:30:39.962Z; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Jun+13+2024+11%3A00%3A41+GMT%2B0530+(India+Standard+Time)&version=202306.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CSSPD_BG%3A1%2CC0004%3A1%2CC0005%3A1%2CC0002%3A1&AwaitingReconsent=false&geolocation=IN%3BGJ; session=942c0adf-8760-9380-cc09-67f3c46b4a35; __cf_bm=2klH0cXmRpxSgKPEmuvUK0bXtu_u53mVbBMp_5bK5zQ-1718256628-1.0.1.1-5nr9bBjMbTKtGPPn29PwyTi9b92vIBsvVGUghjfunlX08Xb_5v6U4f06mWt5wdntWm5r0rmRnnLiXS0FxAx1v0CLz9sgKb4dkeMZUawdK48',
            'origin': 'https://order.chownow.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://order.chownow.com/',
            'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
            'x-cn-app-info': 'Direct-Web/5.110.0',
        }


        yield scrapy.Request(method="GET",url='https://api.chownow.com/api/restaurant/8126/menu/202406131115',headers=headers,callback=self.parse1,
                             meta={"restaurant_name":restaurant_name,"restaurant_company_id":restaurant_company_id,"restaurant_address":restaurant_address,
                                   "storeopeninghours":storeopeninghours,"cuisines":cuisines,"tax_rate":tax_rate,"phone":phone})

    def parse1(self,response):
        data = json.loads(response.text)
        main_dump_dict = {}
        main_dump_dict['restaurant_name'] =response.meta.get('restaurant_name')
        main_dump_dict['restaurant_company_id'] = response.meta.get('restaurant_company_id')
        main_dump_dict['restaurant_address'] = response.meta.get('restaurant_address')
        main_dump_dict['storeopeninghours'] = response.meta.get('storeopeninghours')
        main_dump_dict['cuisines'] = response.meta.get('cuisines')
        main_dump_dict['tax_rate'] = response.meta.get('tax_rate')
        main_dump_dict['phone'] = response.meta.get('phone')

        menu_list = []

        menu_categories = data['menu_categories']

        for each_menu_categories in menu_categories:

            each_menu_dict = {}

            each_menu_dict['menu_id'] = each_menu_categories['id']
            each_menu_dict['menu_name'] = each_menu_categories['name']

            categories_items=each_menu_categories ['items']
            all_item_list = []
            for each_categories_items in categories_items:

                each_item_dict = {}

                each_item_dict['item_id']=each_categories_items['id']
                each_item_dict['item_name']=each_categories_items['name']
                each_item_dict['item_description']=each_categories_items['description']

                add_ons_list = []
                item_price = []


                if 'meta_item_details' in each_categories_items.keys():

                    if 'serving_size_group' in each_categories_items['meta_item_details'].keys():
                        if 'child_items' in each_categories_items['meta_item_details']['serving_size_group'].keys():


                            child_items = each_categories_items['meta_item_details']['serving_size_group']['child_items']

                            for each_child_items in child_items:
                                sizes = {}
                                sizes['size'] = each_child_items['size']
                                sizes['price'] =each_child_items['price']
                                child_modifier_categories = each_child_items['modifier_categories']
                                for each_child_modifier_categories in child_modifier_categories:

                                    for each_modifier_category in data['modifier_categories']:

                                        if each_child_modifier_categories == each_modifier_category['id']:
                                            child_modifiers = each_modifier_category['modifiers']
                                            for each_child_modifier in child_modifiers:
                                                for each_modifiers in data['modifiers']:
                                                    if each_child_modifier== each_modifiers['id']:
                                                        each_modifiers['addonsCategory'] =each_modifier_category['name']
                                                        add_ons_list.append(each_modifiers)

                                item_price.append(sizes)




                else:
                    modifier_categories = each_categories_items['modifier_categories']
                    sizes = {}
                    sizes['size'] = each_categories_items['size']
                    sizes['price'] = each_categories_items['price']
                    for each_modifier_categories in modifier_categories:
                        for each_modifier_category in data['modifier_categories']:
                            if each_modifier_categories == each_modifier_category['id']:
                                item_modifiers = each_modifier_category['modifiers']
                                for each_item_modifiers in item_modifiers:
                                    modifiers = data['modifiers']
                                    for each_modifiers in modifiers:
                                        if each_item_modifiers == each_modifiers['id']:
                                            each_modifiers['addonsCategory'] = each_modifier_category['name']
                                            add_ons_list.append(each_modifiers)
                    item_price.append(sizes)
                each_item_dict['item_price'] = item_price
                each_item_dict['add_ons'] = add_ons_list
                all_item_list.append(each_item_dict)

            each_menu_dict['items'] = all_item_list

            menu_list.append(each_menu_dict)

        main_dump_dict['menus'] = menu_list

        with open('chownow.json', 'w') as f:
            json.dump(main_dump_dict, f)

        print(response.text)

if __name__ == '__main__':
    execute('scrapy crawl chownow1'.split())
