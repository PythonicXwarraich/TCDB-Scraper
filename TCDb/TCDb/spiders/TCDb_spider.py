
import scrapy

class ExampleSpider(scrapy.Spider):
    name = "spidername"
    allowed_domains = ["www.tcdb.com"]
    start_urls = ["https://www.tcdb.com/ViewAll.cfm/sp/Baseball/year/2022"]
    custom_settings = {
            'FEEDS': {
                'TCDb_output2.csv': {
                    'format': 'csv',
                    'encoding': 'utf-8'
                }
            },
           
        }

    def parse(self, response):
        
        
        for i in range(1, 80):  # Assuming you want to iterate from 1 to 79
            all_links = response.xpath(f'//*[@id="content"]/div[1]/div[2]/ul[1]/li[{i}]/a[1]/@href').getall()
            for link in all_links:
                url = response.urljoin(link)
                yield scrapy.Request(url=url, callback=self.detail_parse)

    def detail_parse(self, response):
        first_set_html = response.xpath('//*[@class="col-md-8 nopadding"]').get()
        first_set_response = scrapy.Selector(text=first_set_html)
        title = first_set_response.xpath('//h4[@class="site"]/text()').get()
        total_cards = first_set_response.xpath('//p/strong[text()="Total Cards:"]/following-sibling::text()').get()
        self.release_dates = []
        released_date = first_set_response.xpath('//ul/li/text()').get()
        if not released_date:
            release_dates = first_set_response.xpath('//ul//li//li/text()').getall()
            release_dates = [date.strip().replace('\r\n', '') for date in release_dates]
            self.release_dates = release_dates
        else:
            released_date = released_date.strip().replace('\r\n', '')
            self.release_dates = [released_date]
        release_dates = self.release_dates
        next_link = first_set_response.xpath('//*[@class="more"]/a/@href').get()
        next_link = response.urljoin(next_link)
        for i in range(1, 11): 
            page_link = f"{next_link}?PageIndex={i}"
        request = scrapy.Request(url=next_link, callback=self.nextPage)
        request.meta['first_set'] = title
        request.meta['total_cards'] = total_cards
        request.meta['released_date'] = release_dates
        
        yield request

    def nextPage(self, response):
        first_set = response.meta.get('first_set', 'NAN')
        total_cards = response.meta.get('total_cards', 'NAN')
        released_date = response.meta.get('released_date', 'NAN')

        all_cards = response.css(".col-md-6 .block1 tr")

        if all_cards:
            for card in all_cards[1:]:  # Skip the header row if necessary
                image_1 = card.css('td[valign="top"] img::attr(data-original)').get()
                images = card.css('td[valign="top"] img::attr(data-original)').getall()
                image_2 = images[1] if len(images) > 1 else None


        all_cards = response.css(".col-md-6 .block1 tr")
        if all_cards:
            for card in all_cards[1:]: 
                all_values = []
                for td in card.css('td[valign="top"]'):
                    texts = td.css('::text').getall()
                    cleaned_texts = [text.strip() for text in texts if text.strip()]
                    combined_text = ' '.join(cleaned_texts)
                    all_values.append(combined_text)
                all_values = [value for value in all_values if value]
                print(all_values)  # Print the extracted values for debugging

                if all_values and len(all_values) >= 3:
                    card_num = all_values[-3]
                    player_name = all_values[-2]
                    team_name = all_values[-1]
                   
                yield {
                    'Image 1': response.urljoin(image_1) if image_1 else 'NAN',
                    'Image 2': response.urljoin(image_2) if image_2 else 'NAN',
                    'Player Name': player_name or 'NAN',
                    'Team Name': team_name or 'NAN',
                    'First Set': first_set or 'NAN',
                    'Total Cards': total_cards or 'NAN',
                    'Released Date': released_date or 'NAN'
                }

