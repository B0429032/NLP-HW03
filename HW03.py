import requests
from bs4 import BeautifulSoup

import csv

with open('HW03.csv', 'w', encoding='utf-8-sig', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['名稱', '分類', '劇情介紹','上映⽇期'])
    for id_number in range(1, 11400):
        url = 'https://movies.yahoo.com.tw/movieinfo_main/id='
        r = requests.get(url+ str(id_number))
        soup = BeautifulSoup(r.text)
        soup
        for d in soup.find_all('div', class_="movie_intro_info_r"):
            name = d.find('h1', class_="").text.strip()
        level_name_box = d.find('div', class_="level_name_box").text.strip()

        for d in soup.find_all('div', class_="gray_infobox storeinfo"):
            story = d.find('div', class_="gray_infobox_inner").text.split('詳全文')[0].strip()


        for d in soup.find_all('div', class_="movie_intro_info_r"):
            release_time = d.find('span', class_="").text.split('：')[-1].strip()
    
        csv_writer.writerow([name, level_name_box, story, release_time])
        if id_number%100 == 0 :
            print(id_number)
