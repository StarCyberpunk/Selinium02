import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class First_Parse(object):
    def __init__(self,driver,lang):
        self.driver=driver
        self.lang=lang
    def parse(self):
        self.go_to_test()
    def go_to_test(self):
        self.driver.get('https://sadovodbaza.ru/postavschiki-po-liniyam/')
        time.sleep(1)
        pos=self.driver.find_element_by_class_name('col-inner').find_elements_by_tag_name('p')
        pos.pop(0);
        for pos2 in pos:
            self.driver.get(pos2.find_element_by_tag_name('a').get_attribute("href"))
            lis=self.driver.find_element_by_class_name('col-inner').find_elements_by_tag_name('strong')
            lis2=lis.driver.find_element_by_partial_link_text('https://vk.com/')
            for pos3 in lis2:
                try:
                    print(pos3.text)
                    """print(pos3.driver.get(pos2.find_element_by_tag_name('a').get_attribute("href")))"""
                except NoSuchElementException:
                    print("end")





def main():
    driver=webdriver.Opera();
    parser=First_Parse(driver,"diplomy")

    parser.parse()

if __name__ =="__main__":
    main()

"""Есть два сайта:
sadovodbaza.ru/
usefulbox.ru

На этих сайтах представлены поставщики рынка Садовод в виде ссылок на их группы ВК и на их страницы ВК.

Нужно спарсить все ссылки и создать отчёт в формате Excel по каждому из сайтов, куда включить все ссылки с одного и с другого сайта.

Предлагайте свой бюджет и сроки исполнения.
self.driver.get('https://copy.spb.ru')
        time.sleep(2)
        positions=self.driver.find_elements_by_class_name("o-tile")
        for el in positions:
            lang_link=el.get_attribute("href")
            print(lang_link.split("/")[-2])
            if self.lang in lang_link:
                c= lang_link.split("/")[-2]
                self.driver.get("https://copy.spb.ru/"+ c)"""