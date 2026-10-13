from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ============================================================
# TC01 - Đăng nhập thành công
# ============================================================
def test_login_success():
    # Mở trình duyệt Chrome
    driver = webdriver.Chrome()

    try:
        # Truy cập trang Login
        driver.get("https://the-internet.herokuapp.com/login")

        # Nhập username
        driver.find_element(
            By.ID, "username"
        ).send_keys("tomsmith")

        # Nhập password
        driver.find_element(
            By.ID, "password"
        ).send_keys("SuperSecretPassword!")

        # Bấm nút Login
        driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        ).click()

        # Chờ thông báo xuất hiện
        message_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.ID, "flash")
            )
        )

        # Lấy nội dung thông báo
        message = message_element.text

        # Kiểm tra đăng nhập thành công
        assert "You logged into a secure area!" in message

    finally:
        # Đóng trình duyệt
        driver.quit()


# ============================================================
# TC02 - Đăng nhập với password sai
# ============================================================
def test_login_wrong_password():
    # Mở trình duyệt Chrome
    driver = webdriver.Chrome()

    try:
        # Truy cập trang Login
        driver.get("https://the-internet.herokuapp.com/login")

        # Nhập username đúng
        driver.find_element(
            By.ID, "username"
        ).send_keys("tomsmith")

        # Nhập password sai
        driver.find_element(
            By.ID, "password"
        ).send_keys("WrongPassword123")

        # Bấm nút Login
        driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        ).click()

        # Chờ thông báo lỗi xuất hiện
        message_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.ID, "flash")
            )
        )

        # Lấy nội dung thông báo
        message = message_element.text

        # Kiểm tra thông báo password sai
        assert "Your password is invalid!" in message

    finally:
        # Đóng trình duyệt
        driver.quit()


# ============================================================
# TC03 - Đăng nhập với username sai
# ============================================================
def test_login_wrong_username():
    # Mở trình duyệt Chrome
    driver = webdriver.Chrome()

    try:
        # Truy cập trang Login
        driver.get("https://the-internet.herokuapp.com/login")

        # Nhập username sai
        driver.find_element(
            By.ID, "username"
        ).send_keys("wronguser")

        # Nhập password đúng
        driver.find_element(
            By.ID, "password"
        ).send_keys("SuperSecretPassword!")

        # Bấm nút Login
        driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        ).click()

        # Chờ thông báo lỗi xuất hiện
        message_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.ID, "flash")
            )
        )

        # Lấy nội dung thông báo
        message = message_element.text

        # Kiểm tra thông báo username sai
        assert "Your username is invalid!" in message

    finally:
        # Đóng trình duyệt
        driver.quit()
