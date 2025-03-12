from pages.page_douban.page_douban import PageDouBan


class TestDouBan:
    def test_scrape_music_data(self, open_douban):
        page_douban = PageDouBan(open_douban)
        page_douban.insert_music_data()
