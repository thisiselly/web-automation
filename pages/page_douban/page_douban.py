from datetime import datetime
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from utils.sql_server_utils import SqlServerDB


class PageDouBan(BasePage):
    article = (By.CSS_SELECTOR, '.article>.mod>.col5>.clearfix')
    rank = (By.CSS_SELECTOR, '.green-num-box')
    song_name = (By.CSS_SELECTOR, '[href="javascript:;"]')
    artist_and_play_count = (By.CSS_SELECTOR, '.p')
    days_on_chart = (By.CSS_SELECTOR, '.days')

    def get_music_datas(self):
        songs = self.find_elements(self.article)
        data_to_insert = []
        for song in songs:
            if len(data_to_insert) >= 10:  # 检查长度
                break
                
            song_info = song.text.split("\n")
            rank = int(song_info[0])
            song_name = song_info[1]
            artist, play_count = song_info[2].split(" / ")
            play_count = int(play_count.split("次")[0])
            days_on_chart = int(song_info[3].split("上榜")[1].split("天")[0])
            current_date = datetime.now().strftime("%Y-%m-%d")
            data_to_insert.append((rank, song_name, artist, play_count, days_on_chart, current_date))
        print(data_to_insert)
        return data_to_insert

    def insert_music_data(self):
        sql_server = SqlServerDB()
        all_datas = self.get_music_datas()
        for data in all_datas:
            sql = "insert into music_charts (rank, song_name, artist, play_count, days_on_chart, last_updated) values (?, ?, ?, ?, ?, ?)"
            sql_server.insert_sql(sql, data)