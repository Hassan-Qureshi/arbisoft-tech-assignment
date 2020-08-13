import requests
from bs4 import BeautifulSoup
from src.constant import constants
import csv
import time
import os
from src.utility import manage_directories as dir_manager

CWD = os.path.normpath(os.path.normpath(os.path.abspath(__file__) + os.sep + os.pardir) + os.sep + os.pardir)
os.chdir(CWD)


class Scrapper:
    # Constants
    CWUR_URL = constants.CWUR_URL
    BASE_URL = constants.BASE_URL
    PARSER = constants.PARSER

    # CSV File Paths
    OUTPUT_FILE_DIR = os.path.join(constants.OUTPUT_DIR_BASE, constants.SCRAPED_DATA_FILES)
    SCRAPPED_FILE_NAME = os.path.join(OUTPUT_FILE_DIR, constants.UNIVERSITIES_LIST_FILE_NAME)

    def __init__(self):
        dir_manager.create_dir_if_not(self.OUTPUT_FILE_DIR)

    @staticmethod
    def get_content(url: str):
        """
        Get web content from given URL in HTML format.
        :param url: web url e.g: https://cwur.org
        :return: HTML in byte format
        """
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
            }
            response = requests.get(url=url, headers=headers)
            if response.status_code != constants.RESPONSE_OK:
                raise Exception("Incorrect Response from server", response.status_code)
            else:
                print('Getting Content from URL = {}'.format(url))
                return response.content
        except Exception as e:
            raise Exception(e)

    def parse_extract_domain(self, url: str) -> str:
        """
        This method takes URL of university specific page. It parse the content and extract 'DOMAIN'
        :param url: Complete URL for specific University e.g: https://cwur.org/2018-19/Harvard-University.php
        :return: Domain or website domain e.g: harvard.edu
        """
        soup = self.get_soup(url)
        uni_spec_table = soup.find('table', {'class': ['table', 'table-bordered', 'table-hover']})
        uni_domain = uni_spec_table.findAll('tr')[-1].findAll('td')[-1].text
        return uni_domain.strip()

    def get_soup(self, url: str):
        """
        This method returns the beautiful soup object after applying parsing by default it uses lxml parser
        :param url: url to parse
        :return: Beautiful Soup Object
        """
        try:
            html_page = self.get_content(url=url)
            soup = BeautifulSoup(html_page, self.PARSER)
            return soup
        except Exception as e:
            print(e)

    def parse_main_page(self, url: str):
        soup = self.get_soup(url=url)
        university_table = soup.find('table', class_='table')
        table_contents = university_table.find('tbody').findAll('tr')
        return table_contents

    def merge_save(self, url: str):
        table_contents = self.parse_main_page(url=url)
        with open(self.SCRAPPED_FILE_NAME, "w", newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(constants.CSV_HEADERS)

        with open(self.SCRAPPED_FILE_NAME, "a", encoding="utf-8", newline='') as csv_file:
            writer = csv.writer(csv_file)
            for content in table_contents[:100]:
                data = content.findAll('td')
                world_ranking = data[0].text.strip()
                institute_name = data[1].text.strip()
                location = data[2].text.strip()
                score = data[-1].text.strip()
                # Getting URL for respective university
                next_page_url = data[1].find('a')['href'].strip().encode("utf-8").decode()
                # Creating URL
                uni_domain_url = '{BASE_URL}/{NEXT_PAGE_URL}'.format(BASE_URL=self.BASE_URL,
                                                                     NEXT_PAGE_URL=next_page_url)

                uni_domain = self.parse_extract_domain(uni_domain_url)
                print(world_ranking, institute_name, location, score, uni_domain)

                writer.writerow([world_ranking, institute_name, location, score, uni_domain])
                time.sleep(2)


if __name__ == '__main__':
    scrapper = Scrapper()
    scrapper.merge_save(scrapper.CWUR_URL)

