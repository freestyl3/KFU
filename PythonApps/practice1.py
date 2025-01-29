from pprint import pprint
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import bs4
from selenium.webdriver.ie.webdriver import WebDriver

PAGES_COUNT = 3

def main():
    driver = webdriver.Edge()
    url = "https://lenta.ru/parts/news"
    driver.get(url)

    for _ in range(PAGES_COUNT):
        get_more_button = driver.find_element(By.LINK_TEXT, 'Показать еще')
        get_more_button.send_keys(Keys.END)
        get_more_button.click()
        time.sleep(3)

    soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')
    links = soup.find_all(class_="parts-page__item")
    links.pop(-1)
    # print(soup.prettify())
    # print(links)

    news = {}

    for link in links:
        title = link.findNext(class_="card-full-news__title").text
        date = link.findNext(class_="card-full-news__info-item card-full-news__date").text
        rubric = link.findNext(class_="card-full-news__info-item card-full-news__rubric").text
        direct_link = 'https://lenta.ru' + link.find('a').get('href')
        # item = link.findNext(class_=f"card-full-news _parts_news")
        # print(key.text, item, sep='\n')
        news[direct_link] = {
            'date' : date,
            'rubric' : rubric,
            'title' : title
        }



    # soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')
    # links = soup.find_all(class_="parts-page__item")
    # links.pop(-1)
    #
    # print(links)
    #
    # for link in links:
    #     key = link.findNext(class_="card-full-news__title").text
    #     date = link.findNext(class_="card-full-news__info-item card-full-news__date").text
    #     rubric = link.findNext(class_="card-full-news__info-item card-full-news__rubric").text
    #     direct_link = 'https://lenta.ru' + link.find('a').get('href')
    #     # item = link.findNext(class_=f"card-full-news _parts_news")
    #     # print(key.text, item, sep='\n')
    #     news[key] = {
    #         'date' : date,
    #         'rubric' : rubric,
    #         'direct_link' : direct_link
    #     }

    for link in news.keys():
        print(news[link]['title'])

    # button = driver.find_element(by=By.CLASS_NAME, value="loadmore_button")
    # button.click()





if __name__ == "__main__":
    main()