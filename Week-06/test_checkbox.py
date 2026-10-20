
import os
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# =========================
# CAU HINH
# =========================
URL = "https://the-internet.herokuapp.com/checkboxes"
SCREENSHOT_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "screenshots"
)

os.makedirs(SCREENSHOT_DIR, exist_ok=True)


def save_screenshot(driver, test_name):
    """Luu anh khi test PASS."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{test_name}_{timestamp}.png"
    filepath = os.path.join(SCREENSHOT_DIR, filename)

    driver.save_screenshot(filepath)
    print(f"Da luu anh: {filepath}")


def pause(message):
    input(f"\n{message}\nNhan Enter de tiep tuc...")


def get_checkboxes(driver):
    """Cho checkbox hien thi va tra ve danh sach checkbox."""
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "input[type='checkbox']")
        )
    )
    return driver.find_elements(
        By.CSS_SELECTOR, "input[type='checkbox']"
    )


def run_test(driver, test_name, test_function):
    """Chi chup anh neu test khong phat sinh loi."""
    print("\n" + "=" * 45)
    print(test_name)

    try:
        test_function(driver)
        print(f"{test_name} PASS")
        save_screenshot(driver, test_name.replace(" ", "_"))
        return True

    except Exception as error:
        print(f"{test_name} FAIL: {error}")

        # Neu trang van mo, luu anh loi de de kiem tra
        try:
            save_screenshot(
                driver,
                test_name.replace(" ", "_") + "_FAIL"
            )
        except Exception:
            print("Khong the chup anh loi: trinh duyet co the da dong.")

        return False


# =========================
# TEST CASES
# =========================

def tc10_checkbox_enabled(driver):
    """TC10: Kiem tra checkbox co duoc kich hoat khong."""
    checkboxes = get_checkboxes(driver)
    checkbox = checkboxes[0]

    assert checkbox.is_enabled(), (
        "Checkbox dau tien dang bi vo hieu hoa."
    )

    print("TC10 PASS: Checkbox dau tien duoc kich hoat.")



def tc11_checkbox_selected(driver):
    """TC11: Kiem tra checkbox dau tien mac dinh chua duoc chon."""
    checkboxes = get_checkboxes(driver)
    checkbox = checkboxes[0]

    assert not checkbox.is_selected(), (
        "Checkbox dau tien dang duoc chon, trong khi mong doi la chua chon."
    )

    print("TC11 PASS: Checkbox dau tien mac dinh chua duoc chon.")

def tc12_checkbox_value(driver):
    """TC12: Kiem tra thuoc tinh value cua checkbox dau tien."""
    checkboxes = get_checkboxes(driver)
    checkbox = checkboxes[0]

    actual_value = checkbox.get_attribute("value")
    print(f"TC12 - Actual value: {actual_value!r}")

    assert actual_value == "on", (
        f"Mong doi value='on', nhung nhan duoc {actual_value!r}."
    )

    print("TC12 PASS: Thuoc tinh value bang 'on'.")


# =========================
# CHUONG TRINH CHINH
# =========================

def main():
    driver = None
    results = []

    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        # Selenium Manager tu tim ChromeDriver
        driver = webdriver.Chrome(options=options)
        driver.get(URL)

        print("Da mo trang:", URL)
        print("Thu muc luu anh:", SCREENSHOT_DIR)

        tests = [
            ("TC10 Checkbox Enabled", tc10_checkbox_enabled),
            ("TC11 Checkbox Selected", tc11_checkbox_selected),
            ("TC12 Checkbox Value", tc12_checkbox_value),
        ]

        for index, (name, test_function) in enumerate(tests):
            result = run_test(driver, name, test_function)
            results.append((name, result))

            if index < len(tests) - 1:
                pause("Hoan thanh test hien tai.")

        print("\n" + "=" * 45)
        print("KET QUA TONG HOP")

        for name, passed in results:
            status = "PASS" if passed else "FAIL"
            print(f"{name}: {status}")

        total_pass = sum(1 for _, passed in results if passed)
        total_fail = len(results) - total_pass

        print(f"\nTong so test: {len(results)}")
        print(f"PASS: {total_pass}")
        print(f"FAIL: {total_fail}")
        print("Anh screenshot duoc luu trong thu muc screenshots.")

        pause("Da chay xong tat ca test.")

    except KeyboardInterrupt:
        print("\nBan da dung chuong trinh.")

    except Exception as error:
        print(f"\nLoi chuong trinh: {error}")

    finally:
        if driver is not None:
            try:
                driver.quit()
                print("Da dong trinh duyet Chrome.")
            except Exception:
                pass


if __name__ == "__main__":
    main()
