import tool

INDEX_MEMORY_GOODS = """//*[@id="components-layout-demo-custom-trigger"]/section/main/main/div[2]/div/div[2]/main/div[2]/div[1]/div/div[1]/img"""
INDEX_BUY_FIRST_GOODS_BUTTON = """//*[@id="components-layout-demo-custom-trigger"]/section/main/main/div[2]/div/div[1]/main/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div[2]/button"""
INDEX_CLOSE_ORDER_MODAL_BUTTON = """/html/body/div/div/div[2]/div/div[2]/button/span"""
GOODS_LIST_FIRST_GOODS = """//*[@id="components-layout-demo-custom-trigger"]/section/main/main/div/div[1]/div/div[1]/img"""
GOODS_LIST_SECOND_GOODS = """//*[@id="components-layout-demo-custom-trigger"]/section/main/main/div/div[2]/div/div[1]/img"""
DETAILS_ADD_TO_SHOPPING_CART_BUTTON = """//*[@id="components-layout-demo-custom-trigger"]/section/main/main/div[1]/div/div/div[3]/div/div[3]/div[3]/button"""
USER_PAGE_SUBMIT_ORDER_BUTTON = """//*[@id="components-layout-demo-custom-trigger"]/section/main/main/div[3]/div[2]/button"""
ALL_SEARCH_INPUT = """//*[@id="components-layout-demo-custom-trigger"]/section/header/div/section/main/ul/span[2]/input"""
ALL_SEARCH_BUTTON = """//*[@id="components-layout-demo-custom-trigger"]/section/header/div/section/main/ul/span[2]/span/i"""


def index_buy_goods(browser):
    button = tool.get_element_by_xpath(browser, INDEX_BUY_FIRST_GOODS_BUTTON)
    button.click()


def index_close_order(browser):
    button = tool.get_element_by_xpath(browser, INDEX_CLOSE_ORDER_MODAL_BUTTON)
    button.click()


def index_open_goods(browser):
    button = tool.get_element_by_xpath(browser, INDEX_MEMORY_GOODS)
    button.click()


# list_open_goods in goods_list page
def goods_list_open_goods_for_category(browser):
    button = tool.get_element_by_xpath(browser, GOODS_LIST_FIRST_GOODS)
    button.click()


# add_to_shopping_cart in details page
def details_add_to_shopping_cart(browser):
    button = tool.get_element_by_xpath(browser, DETAILS_ADD_TO_SHOPPING_CART_BUTTON)
    button.click()


def search(browser):
    __input_search_text(browser, "i7")
    __click_search_button(browser)


def goods_list_open_goods_for_search(browser):
    button = tool.get_element_by_xpath(browser, GOODS_LIST_SECOND_GOODS)
    button.click()


def user_page_buy_all(browser):
    button = tool.get_element_by_xpath(browser, USER_PAGE_SUBMIT_ORDER_BUTTON)
    button.click()


def __input_search_text(browser, text):
    search_input = tool.get_element_by_xpath(browser, ALL_SEARCH_INPUT)
    search_input.send_keys(text)


def __click_search_button(browser):
    button = tool.get_element_by_xpath(browser, ALL_SEARCH_BUTTON)
    button.click()
