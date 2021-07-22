import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import baseURL
import pay
import phone_number
import identity
import router
import goods


# TestRunner run test.
class TestRunner:
    def __init__(self, base_url, wait_time=5, close_after_exec=True):
        chrome_options = Options()
        chrome_options.add_argument('--headless')

        self.__browser = webdriver.Chrome(options=chrome_options)
        self.__wait_time = wait_time
        self.__close_after_exec = close_after_exec

        self.__browser.get(base_url)
        self.__browser.implicitly_wait(wait_time)

    def __del__(self):
        if self.__close_after_exec:
            self.__browser.close()

    # __init_test with random username & password
    def __init_test(self):
        user = {
            "phone_number": phone_number.random_phone_number(),
            "password": "foobar123456",
            "username": "foobar",
            "address": "foobar",
        }
        identity.registry(self.__browser, user, self.__wait_time / 2)
        identity.login(self.__browser, user, self.__wait_time / 2)

    def run(self, actions):
        """
        run test points
        :param actions: [{
            act: func(browser),
            wait_time: Integer(null for self.__wait_time),
        }]
        """
        self.__init_test()  # Make sure the user is logged in.
        for action in actions:
            print(action["name"])
            action["act"](self.__browser)
            time.sleep(action["wait_time"])


if __name__ == "__main__":
    runner = TestRunner(baseURL.BASE_URL, 6, False)
    runner.run([
        # show buy directly
        {"name": "open index", "act": router.to_index_page, "wait_time": 3},
        {"name": "buy goods", "act": goods.index_buy_goods, "wait_time": 3},
        {"name": "close order dialog", "act": goods.index_close_order, "wait_time": 3},
        # show user page
        {"name": "show user page", "act": router.to_user_page, "wait_time": 15},
        # open goods in index.
        {"name": "open index", "act": router.to_index_page, "wait_time": 5},
        {"name": "open goods in index", "act": goods.index_open_goods, "wait_time": 2},
        {"name": "add it to shopping cart", "act": goods.details_add_to_shopping_cart, "wait_time": 2},
        # open goods by category method and add into shopping cart.
        {"name": "goto category view", "act": router.to_goods_list_page, "wait_time": 5},
        {"name": "open first goods", "act": goods.goods_list_open_goods_for_category, "wait_time": 2},
        {"name": "add it to shopping cart", "act": goods.details_add_to_shopping_cart, "wait_time": 1},
        # open goods by search method and add into shopping cart.
        {"name": "search a goods", "act": goods.search, "wait_time": 5},
        {"name": "open the goods", "act": goods.goods_list_open_goods_for_search, "wait_time": 2},
        {"name": "add it to shopping cart", "act": goods.details_add_to_shopping_cart, "wait_time": 2},
        # open user page
        {"name": "show user page", "act": router.to_user_page, "wait_time": 2},
        {"name": "buy all", "act": goods.user_page_buy_all, "wait_time": 2},
        {"name": "open alipay", "act": pay.goto_alipay, "wait_time": 2},
        {"name": "login_pay", "act": pay.do_alipay, "wait_time": 1},
        # open user page and show.
        {"name": "show user page", "act": router.to_user_page, "wait_time": 15},
    ])
