import re
from pprint import pprint
import codecs
import urllib.request
from bs4 import BeautifulSoup
from googletrans import Translator

class ScrapeLiepin(object):

    def __init__(self):
        pass




if __name__ == '__main__':
    print("Webscrape: Liepin")
    translator = Translator()

    # Loop through all job paginations, up to 100 pages
    # jobs_root_page = 'https://www.liepin.com/job/pn{}'
    # lst_jobs_pages = []
    # for i in range(1, 100):
    #     lst_jobs_pages.append(jobs_root_page.format(str(i)))

    # First time download, can save html to local. Decode the page in utf8 Chinese chars
    #html_page = urllib.request.urlopen("https://www.liepin.com/job/pn0").read().decode('utf-8')
    # Next time can load local html download, no need to keep requesting site
    html_page = codecs.open("/Users/addseq/PycharmProjects/anaconda3_projects/webscraping/liepin/liepin_job.html", "r", "utf-8").read()
    #print(html_page)

    # Create BS4 object
    #soup = BeautifulSoup(html_page, 'html.parser')
    soup = BeautifulSoup(html_page, 'lxml')

    # Main Job Posting page typically has up to 40 job posts a page, and up to 100 paginations
    JOB_POSTS_CRAWL_LIMIT = 1
    job_postings = soup.findAll('div', attrs={'class':'sojob-item-main clearfix'}, limit=JOB_POSTS_CRAWL_LIMIT)
    for job in job_postings:
        # print(job)

        # Extract Job Posting fields
        job_name_tag = job.find('a', attrs={'class': 'job-name'})
        job_url = job_name_tag['href']
        job_title = job_name_tag['title']
        job_type = job_name_tag.text.strip()
        print(job_url)
        print(job_title)
        print(job_type)

        job_condition_tag = job.find('p', attrs={'class': 'condition clearfix'})
        job_salary = job_condition_tag.find('span', class_='text-warning').text.strip()
        job_loc = job_condition_tag.find('span', class_='area').text.strip()
        job_edu = job_condition_tag.find('span', class_='edu').text.strip()
        job_exp = job_condition_tag.find('span', class_=None).text.strip()
        print(job_salary)
        print(job_loc)
        print(job_edu)
        print(job_exp)

        job_posting_time_tag = job.find('p', attrs={'class': 'time-info clearfix'})
        job_posting_date = job_posting_time_tag.find('time')['title']
        job_posting_hours_ago = job_posting_time_tag.text.strip()
        print(job_posting_date)
        print(job_posting_hours_ago)

        # Extract Company fields
        company_tag = job.find('p', attrs={'class': 'company-name'})
        company_url = company_tag.find('a').get('href')
        company_name = company_tag.text.strip()
        print(company_url)
        print(company_name)

        industry_tag = job.find('p', attrs={'class': 'field-financing'})
        industry = industry_tag.text.strip()
        print(industry)

        # Go into Job Detail Page, Extract more Job detail fields
        #html_job_detail = urllib.request.urlopen(job_url).read().decode('utf-8')
        html_job_detail = codecs.open("/Users/addseq/PycharmProjects/anaconda3_projects/webscraping/liepin/liepin_job_detail.html",
                                "r", "utf-8").read()
        job_detail = BeautifulSoup(html_job_detail, 'lxml')
        job_desc = job_detail.find('div', class_="content content-word").text.strip()
        job_welfare = job_detail.find('div', class_="job-welfare clearfix").text.strip().replace('\n', '|')
        print(job_desc)
        print(job_welfare)
        #print(translator.translate(job_desc).text)
        #print(translator.translate(job_welfare).text)

        print('----------------------------------------------------------')

    # Get all links
    # lst_urls = soup.findAll('a', limit=None)
    # for url in lst_urls:
    #     print(url.get('href'))

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
