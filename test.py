import re
from pprint import pprint
import urllib.request
from bs4 import BeautifulSoup

class ScrapeLiepin(object):

    def __init__(self):
        pass




if __name__ == '__main__':
    print("Webscrape: Liepin")

    jobs_root_page = 'https://www.liepin.com/job/pn{}'

    lst_jobs_pages = []
    for i in range(1, 100):
        lst_jobs_pages.append(jobs_root_page.format(str(i)))

    # Decode the page in utf8 Chinese chars
    html_page = urllib.request.urlopen("https://www.liepin.com/job/pn0").read().decode('utf-8')
    #print(html_page)

    #soup = BeautifulSoup(html_page, 'html.parser')
    soup = BeautifulSoup(html_page, 'lxml')

    job_postings = soup.findAll('div', attrs={'class':'sojob-item-main clearfix'}, limit=None)
    for job in job_postings[0]:
        print(job)

    #company_name_txt = company_name.text.strip()
    #print(company_name_txt)

    # # extract title
    # res = re.findall(r"<title>(.+?)</title>", html)
    # print("\nPage title is: ", res[0])
    #
    # # extract all inks
    # res = re.findall(r'href="(.*?)"', html)
    # lst_valid_urls = [i for i in res if i.startswith('https://')]
    # print("\nAll links: ")
    # pprint(lst_valid_urls)