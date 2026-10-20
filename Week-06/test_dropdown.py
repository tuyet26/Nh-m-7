
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def test_dropdown():
    driver = webdriver.Chrome()
    try:
        driver.get("https://the-internet.herokuapp.com/dropdown")
        dropdown = Select(driver.find_element(By.ID, "dropdown"))

        dropdown.select_by_visible_text("Option 1")
        assert dropdown.first_selected_option.text == "Option 1"

        dropdown.select_by_value("2")
        assert dropdown.first_selected_option.get_attribute("value") == "2"

        dropdown.select_by_index(1)
        assert dropdown.first_selected_option.text == "Option 1"
    finally:
        driver.quit()
