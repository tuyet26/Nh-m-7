"""
THÀNH VIÊN 5: KIỂM THỬ TÍCH HỢP VÀ TỔNG HỢP BÁO CÁO KẾT QUẢ
========================================================================
Vai trò trong nhóm:
- Phụ trách tích hợp, kiểm tra liên hoàn cả 2 thành phần (Dropdown & Checkboxes).
- Thực hiện 3 Test Case trọng tâm:
  + TC13: Chọn một giá trị dropdown và xác nhận kết quả (Select, By.ID, first_selected_option, assert)
  + TC14: Thực hiện chọn checkbox theo CSS Selector và xác nhận trạng thái (find_elements, By.CSS_SELECTOR, click, is_selected)
  + TC15: Kết hợp chọn Dropdown và Checkbox trong một luồng kiểm thử liên hoàn (End-to-End Integration Flow)
- Tổng hợp kết quả toàn diện từ Thành viên 1 đến Thành viên 5 (15 Test Cases).
- Tự động chụp ảnh bằng chứng lưu vào thư mục 'anh/'.
"""
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium_helper import get_driver, save_evidence, URL_DROPDOWN, URL_CHECKBOXES

def run_tests(driver=None, keep_open=False):
    """
    Hàm thực thi 3 Test Case của Thành viên 5 (TC13, TC14, TC15).
    """
    close_after = False
    if driver is None:
        driver = get_driver(headless=True)
        close_after = not keep_open

    results = []
    print("\n" + "="*70)
    print("▶ BẮT ĐẦU CHẠY KIỂM THỬ - THÀNH VIÊN 5 (TC13 - TC15)")
    print("  Chủ đề: Kiểm thử tích hợp & Xác nhận trạng thái")
    print("="*70)

    try:
        # =====================================================================
        # TC13: Chọn một giá trị dropdown và xác nhận kết quả
        # =====================================================================
        print("\n" + "-"*60)
        print("📌 [TC13] Chọn một giá trị dropdown và xác nhận kết quả")
        print("   - Thao tác: Mở Dropdown -> Dùng Select chọn 'Option 2' -> Xác minh")
        print("-"*60)
        
        # Bước 1: Mở trang Dropdown
        driver.get(URL_DROPDOWN)
        time.sleep(1)

        # Bước 2: Tìm phần tử dropdown bằng By.ID và khởi tạo đối tượng Select
        dropdown_element = driver.find_element(By.ID, "dropdown")
        select = Select(dropdown_element)

        # Bước 3: Chọn giá trị "Option 2" bằng select_by_visible_text
        select.select_by_visible_text("Option 2")
        time.sleep(1)

        # Bước 4: Xác nhận kết quả
        selected_opt = select.first_selected_option
        actual_text = selected_opt.text
        actual_value = selected_opt.get_attribute("value")

        print(f"   + Text được chọn: '{actual_text}' (Mong đợi: 'Option 2')")
        print(f"   + Value thuộc tính: '{actual_value}' (Mong đợi: '2')")

        assert actual_text == "Option 2", f"TC13 Thất bại: Mong đợi 'Option 2', thực tế '{actual_text}'"
        assert actual_value == "2", f"TC13 Thất bại: Mong đợi value '2', thực tế '{actual_value}'"

        # Chụp ảnh minh chứng
        img_tc13 = save_evidence(driver, "tc13_dropdown_select_option2.png")
        print(f"✅ TC13 PASS - Đã chọn và xác minh Option 2 chính xác.")
        print(f"   📷 Ảnh minh chứng đã lưu: {img_tc13}")
        results.append({
            "id": "TC13",
            "name": "Chọn một giá trị dropdown và xác nhận kết quả",
            "status": "PASS",
            "details": f"Đã chọn Option 2 (value=2), xác minh first_selected_option thành công",
            "image": img_tc13
        })

        # =====================================================================
        # TC14: Thực hiện chọn checkbox theo CSS Selector và xác nhận trạng thái
        # =====================================================================
        print("\n" + "-"*60)
        print("📌 [TC14] Thực hiện chọn checkbox theo CSS Selector và xác nhận trạng thái")
        print("   - Thao tác: Mở Checkboxes -> Tìm bằng By.CSS_SELECTOR -> Click -> Xác minh")
        print("-"*60)

        # Bước 1: Mở trang Checkboxes
        driver.get(URL_CHECKBOXES)
        time.sleep(1)

        # Bước 2: Dùng find_elements với CSS Selector để tìm tất cả checkbox
        css_query = "#checkboxes input[type='checkbox']"
        checkboxes = driver.find_elements(By.CSS_SELECTOR, css_query)
        print(f"   + Selector sử dụng: '{css_query}'")
        print(f"   + Số lượng checkbox tìm thấy: {len(checkboxes)}")
        assert len(checkboxes) >= 2, f"TC14 Thất bại: Cần ít nhất 2 checkbox nhưng chỉ thấy {len(checkboxes)}"

        cb1 = checkboxes[0]
        # Bước 3: Xác nhận trạng thái ban đầu của checkbox 1 là False (chưa chọn)
        print(f"   + Trạng thái Checkbox 1 ban đầu: is_selected = {cb1.is_selected()} (Mong đợi: False)")
        assert cb1.is_selected() is False, "TC14: Checkbox 1 ban đầu không ở trạng thái unchecked"

        # Bước 4: Click để chọn Checkbox 1
        cb1.click()
        time.sleep(1)

        # Bước 5: Xác nhận trạng thái sau khi click đã chuyển sang True
        cb1_status_after = cb1.is_selected()
        print(f"   + Trạng thái Checkbox 1 sau khi click: is_selected = {cb1_status_after} (Mong đợi: True)")
        assert cb1_status_after is True, "TC14: Checkbox 1 không được chọn sau khi gọi lệnh click()"

        # Chụp ảnh minh chứng
        img_tc14 = save_evidence(driver, "tc14_checkbox_css_selector.png")
        print(f"✅ TC14 PASS - Tìm phần tử qua CSS Selector và tích chọn thành công.")
        print(f"   📷 Ảnh minh chứng đã lưu: {img_tc14}")
        results.append({
            "id": "TC14",
            "name": "Thực hiện chọn checkbox theo CSS Selector và xác nhận trạng thái",
            "status": "PASS",
            "details": "Tìm 2 checkbox qua CSS Selector, click Checkbox 1 và xác minh is_selected=True",
            "image": img_tc14
        })

        # =====================================================================
        # TC15: Kết hợp chọn Dropdown và Checkbox trong một luồng kiểm thử liên hoàn
        # =====================================================================
        print("\n" + "-"*60)
        print("📌 [TC15] Kết hợp chọn dropdown và checkbox trong một luồng kiểm thử")
        print("   - Quy trình tích hợp liên hoàn (6 bước theo sơ đồ đề tài):")
        print("     1. Mở trang Dropdown -> 2. Chọn giá trị -> 3. Kiểm tra giá trị đã chọn")
        print("     4. Mở trang Checkboxes -> 5. Tích/bỏ tích Checkbox -> 6. Xác minh trạng thái")
        print("-"*60)

        # Bước 1: Mở trang Dropdown
        print("   [Bước 1/6] Mở trang Dropdown...")
        driver.get(URL_DROPDOWN)
        time.sleep(1)

        # Bước 2: Chọn một giá trị (Chọn Option 1)
        print("   [Bước 2/6] Khởi tạo Select và chọn 'Option 1' bằng select_by_visible_text...")
        dropdown_elem = driver.find_element(By.ID, "dropdown")
        select_int = Select(dropdown_elem)
        select_int.select_by_visible_text("Option 1")
        time.sleep(1)

        # Bước 3: Kiểm tra giá trị đã chọn
        print("   [Bước 3/6] Kiểm tra giá trị đã chọn...")
        opt_selected = select_int.first_selected_option
        print(f"       -> Dropdown đã chọn: text='{opt_selected.text}', value='{opt_selected.get_attribute('value')}'")
        assert opt_selected.text == "Option 1", f"TC15 Bước 3 lỗi: Mong đợi Option 1, thực tế {opt_selected.text}"
        assert opt_selected.get_attribute("value") == "1", "TC15 Bước 3 lỗi: Value không khớp"

        # Bước 4: Mở trang Checkboxes
        print("   [Bước 4/6] Chuyển hướng sang trang Checkboxes...")
        driver.get(URL_CHECKBOXES)
        time.sleep(1)

        # Bước 5: Thao tác tích/bỏ tích checkbox
        print("   [Bước 5/6] Thao tác: Tích Checkbox 1 và Bỏ tích Checkbox 2...")
        cbs = driver.find_elements(By.CSS_SELECTOR, "#checkboxes input[type='checkbox']")
        assert len(cbs) >= 2, "TC15 Bước 5 lỗi: Không tìm thấy 2 ô checkbox"
        
        # Đảm bảo Checkbox 1 được tích
        if not cbs[0].is_selected():
            cbs[0].click()
        # Đảm bảo Checkbox 2 bị bỏ tích
        if cbs[1].is_selected():
            cbs[1].click()
        time.sleep(1)

        # Bước 6: Xác minh trạng thái cuối cùng
        print("   [Bước 6/6] Xác minh trạng thái của cả 2 checkbox...")
        cb1_final = cbs[0].is_selected()
        cb2_final = cbs[1].is_selected()
        print(f"       -> Checkbox 1: is_selected = {cb1_final} (Kỳ vọng: True)")
        print(f"       -> Checkbox 2: is_selected = {cb2_final} (Kỳ vọng: False)")

        assert cb1_final is True, "TC15 Bước 6 lỗi: Checkbox 1 chưa được bật"
        assert cb2_final is False, "TC15 Bước 6 lỗi: Checkbox 2 chưa được tắt"

        # Chụp ảnh minh chứng
        img_tc15 = save_evidence(driver, "tc15_luong_tich_hop_dropdown_checkbox.png")
        print(f"✅ TC15 PASS - Luồng kiểm thử tích hợp 6 bước hoàn thành xuất sắc!")
        print(f"   📷 Ảnh minh chứng đã lưu: {img_tc15}")
        results.append({
            "id": "TC15",
            "name": "Kết hợp chọn dropdown và checkbox trong một luồng kiểm thử",
            "status": "PASS",
            "details": "Kiểm thử liên hoàn: Dropdown Option 1 -> Checkbox 1 ON & Checkbox 2 OFF",
            "image": img_tc15
        })

    except Exception as e:
        print(f"\n❌ Lỗi trong quá trình chạy kiểm thử Thành viên 5: {e}")
        results.append({
            "id": "TC_ERROR",
            "name": "Lỗi ngoại lệ Thành viên 5",
            "status": "FAIL",
            "details": str(e),
            "image": None
        })
    finally:
        if close_after:
            driver.quit()

    # In tóm tắt kết quả kiểm thử của Thành viên 5
    print("\n" + "="*70)
    print("📊 TỔNG KẾT KẾT QUẢ KIỂM THỬ THÀNH VIÊN 5:")
    print("="*70)
    pass_count = sum(1 for r in results if r["status"] == "PASS")
    fail_count = sum(1 for r in results if r["status"] == "FAIL")
    for r in results:
        status_icon = "✅" if r["status"] == "PASS" else "❌"
        print(f"{status_icon} [{r['id']}] {r['name']}: {r['status']}")
    print(f"\nTổng kết: {pass_count} PASS / {fail_count} FAIL trên tổng số {len(results)} test cases.")
    print("="*70 + "\n")

    return results

if __name__ == "__main__":
    import sys
    # Mặc định mở cửa sổ Chrome trực quan nếu chạy trực tiếp file này
    is_headless = "--headless" in sys.argv
    run_tests(driver=get_driver(headless=is_headless), keep_open=False)
