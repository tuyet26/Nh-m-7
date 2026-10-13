from selenium import webdriver

def test_smoke():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.google.com")
        assert "Google" in driver.title
    finally:
        driver.quit()