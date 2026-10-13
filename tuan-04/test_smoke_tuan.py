from selenium import webdriver


def test_smoke():
    # 1. Mở trình duyệt Chrome
    driver = webdriver.Chrome()

    # 2. Phóng to cửa sổ và thiết lập thời gian chờ tải trang (tối đa 10 giây)
    driver.maximize_window()
    driver.implicitly_wait(10)

    try:
        # 3. Truy cập trang web The Internet
        driver.get("https://the-internet.herokuapp.com/")

        # 4. Kiểm tra tiêu đề trang
        assert driver.title == "The Internet"
        print("\nTest passed: Tiêu đề trang khớp thành công!")

    finally:
        # 5. Đóng trình duyệt an toàn sau khi đã thực hiện xong kiểm thử
        driver.quit()