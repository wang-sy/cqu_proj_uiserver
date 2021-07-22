import baseURL

GOODS_LIST = "/goodslist?category=vga"
USER_PAGE = "/user"
INDEX = "/"

to_url = baseURL


def to_goods_list_page(browser):
    browser.get(baseURL.BASE_URL + GOODS_LIST)


def to_user_page(browser):
    browser.get(baseURL.BASE_URL + USER_PAGE)


def to_index_page(browser):
    browser.get(baseURL.BASE_URL + INDEX)
