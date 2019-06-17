

import allure
import time
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SearchPage(BaseAction):

    search_edit_text = By.ID, "android:id/search_src_text"

    back_button = By.XPATH, "//*[@content-desc='收起']"

    @allure.step(title="搜索页面--输入关键字")
    def input_search(self, value):
        allure.attach('输入',value,allure.attach_type.TEXT)
        self.input(self.search_edit_text, value)
        time.sleep(2)
        self.driver.get_screenshot_as_file('haha.png')
        with open('./haha.png','r')as f:
            allure.attach('截图',f,allure.attach_type.PNG)

    @allure.step(title="点击返回")
    def click_back(self):
        self.click(self.back_button)