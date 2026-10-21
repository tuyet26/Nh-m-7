import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

URL_DROPDOWN = "https://the-internet.herokuapp.com/dropdown"

def get_driver(headless=True):
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1280,900")
    return webdriver.Chrome(options=options)

def save_evidence(driver, filename):
    folder = os.path.join(os.path.dirname(__file__), "evidence")
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, filename)
    driver.save_screenshot(path)
    return path
def run_tests(driver=None, keep_open=False):
    close_after = False
    if driver is None:
        driver = get_driver(headless=False)
        close_after = not keep_open

    results = []
    print("\n" + "="*60)
    print("▶ BẮT ĐẦU CHẠY KIỂM THỬ - THÀNH VIÊN 2 (TC04 - TC06)")
    print("="*60)

    try:
        driver.get(URL_DROPDOWN)
        time.sleep(1)

        dropdown_element = driver.find_element(By.ID, "dropdown")
        select = Select(dropdown_element)

        # -------------------------------------------------------------
        # TC05: Kiểm tra lựa chọn ban đầu / đầu tiên bằng first_selected_option
        # (Chạy trước khi đổi giá trị để kiểm tra trạng thái mặc định)
        # -------------------------------------------------------------
        print("\n--- TC05: Kiểm tra lựa chọn đầu tiên bằng first_selected_option ---")
        initial_selected = select.first_selected_option
        print(f"Lựa chọn mặc định ban đầu: '{initial_selected.text}'")
        assert "Please select an option" in initial_selected.text, "Lựa chọn ban đầu không phải là placeholder mặc định"

        img_tc05 = save_evidence(driver, "tc05_kiem_tra_lua_chon_dau_tien.png")
        print(f"✅ TC05 PASS - Kiểm tra đúng lựa chọn ban đầu. Ảnh minh chứng: {img_tc05}")
        results.append({"id": "TC05", "name": "Kiểm tra lựa chọn ban đầu (first_selected_option)", "status": "PASS", "image": img_tc05})

        # -------------------------------------------------------------
        # TC04: Chọn phần tử theo chỉ số bằng select_by_index (chỉ số 1 là Option 1)
        # -------------------------------------------------------------
        print("\n--- TC04: Chọn phần tử theo chỉ số bằng select_by_index ---")
        # index 0: 'Please select an option', index 1: 'Option 1', index 2: 'Option 2'
        select.select_by_index(1)
        time.sleep(1)

        current_option = select.first_selected_option
        print(f"Chọn index 1 -> Mục được chọn: '{current_option.text}'")
        assert current_option.text == "Option 1", f"Kỳ vọng 'Option 1' nhưng nhận được '{current_option.text}'"

        img_tc04 = save_evidence(driver, "tc04_chon_theo_chi_so.png")
        print(f"✅ TC04 PASS - Chọn thành công index 1. Ảnh minh chứng: {img_tc04}")
        results.append({"id": "TC04", "name": "Chọn phần tử theo chỉ số (select_by_index=1)", "status": "PASS", "image": img_tc04})

        # -------------------------------------------------------------
        # TC06: Kiểm tra giá trị đang được chọn sau khi thay đổi (get_attribute)
        # -------------------------------------------------------------
        print("\n--- TC06: Kiểm tra giá trị đang được chọn sau khi thay đổi ---")
        # Đổi sang index 2 (Option 2)
        select.select_by_index(2)
        time.sleep(1)

        updated_option = select.first_selected_option
        val = updated_option.get_attribute("value")
        txt = updated_option.text
        print(f"Sau khi đổi sang index 2 -> Text: '{txt}', Value attribute: '{val}'")

        assert txt == "Option 2", f"Kỳ vọng text 'Option 2' nhưng nhận được '{txt}'"
        assert val == "2", f"Kỳ vọng value '2' nhưng nhận được '{val}'"

        img_tc06 = save_evidence(driver, "tc06_kiem_tra_gia_tri_sau_doi.png")
        print(f"✅ TC06 PASS - Giá trị và thuộc tính value khớp sau khi thay đổi. Ảnh: {img_tc06}")
        results.append({"id": "TC06", "name": "Kiểm tra giá trị và thuộc tính value sau thay đổi", "status": "PASS", "image": img_tc06})

    except Exception as e:
        print(f"❌ Xảy ra lỗi trong quá trình chạy: {e}")
        results.append({"id": "Lỗi", "name": "Lỗi thực thi", "status": "FAIL", "error": str(e)})
    finally:
        if close_after:
            driver.quit()

    return results

if __name__ == "__main__":
    run_tests()
