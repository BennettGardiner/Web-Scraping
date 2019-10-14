import requests
import webbrowser
from bs4 import BeautifulSoup
from scrapy import Spider
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

# Note that you have to initialise a scrapy project for this to work
# logs into a webpage or webpages using credentials, you should replace
# file_list.txt with the html for the page, containing all the download
# links in the page, figure out how to download them by creating the
# correct urls to visit (click 'inspect' and figure out where they are)

creds = {'Username':'user',
        'Password':'hunter123'}

class MySpider(Spider):
    name = 'login'
    start_urls = ['https://www.someurl.net']

    def parse(self, response):
        return FormRequest.from_response(response, formdata=creds,
                                         callback=self.find_and_open_links)

    def check_login(self, response):
        # Just check we can actually log in
        open_in_browser(response)

    def find_and_open_links(self, response):
        domain_string = start_urls[0]
        # Open the html file containing all the download links
        with open('file_list.txt', 'r+') as html_doc:
            soup = BeautifulSoup(html_doc, 'html.parser')
            # For all the download links create the correct url and visit it to download the file
            for tag in soup.findAll(id="downloadLink"):
                url_string = tag['href']
                file_name = tag['onclick'][23::].split(',')[1][1:-3]
                full_url_string = url_string.replace('[OriginalFilename]', file_name)
                url = domain_string + full_url_string

                if requests.head(url).status_code == 200:
                    webbrowser.open(url) # open url if status is 200
