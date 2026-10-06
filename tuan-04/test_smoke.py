from selenium import webdriver


def test_smoke():
    # Mở trình duyệt Chrome
    driver = webdriver.Chrome()

    # Truy cập trang The Internet
    driver.get("https://the-internet.herokuapp.com/")

    # Kiểm tra tiêu đề trang
    assert driver.title == "The Internet"

    # Đóng trình duyệt
    driver.quit()
