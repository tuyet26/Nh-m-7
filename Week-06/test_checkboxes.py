
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_checkboxes():
    driver = webdriver.Chrome()
    try:
        driver.get("https://the-internet.herokuapp.com/checkboxes")
        boxes = driver.find_elements(
            By.CSS_SELECTOR, "input[type='checkbox']"
        )

        boxes[0].click()
        assert boxes[0].is_selected()

        boxes[1].click()
        assert not boxes[1].is_selected()

        assert boxes[0].is_enabled()
        assert boxes[0].get_attribute("type") == "checkbox"
    finally:
        driver.quit()
