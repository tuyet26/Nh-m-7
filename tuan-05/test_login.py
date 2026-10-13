# test_login.py - Bài kiểm thử chức năng Đăng nhập
# Mục đích: Kiểm tra chức năng đăng nhập của trang Sauce Demo
# bao gồm đăng nhập thành công, sai mật khẩu, và bỏ trống thông tin.
#
# Trang kiểm thử: https://www.saucedemo.com
# Đây là trang demo phổ biến dùng để học Selenium WebDriver.
#
# Nhóm thực hiện:
#   - Nguyễn Minh Tuấn
#   - Đỗ Trung Hiếu
#   - Đặng Thành Nam
#   - Lưu Thị Tuyết
#   - Đỗ Đình Việt

import pytest                          # Framework kiểm thử
from selenium import webdriver         # Thư viện điều khiển trình duyệt
from selenium.webdriver.common.by import By        # Cách xác định phần tử
from selenium.webdriver.common.keys import Keys    # Các phím đặc biệt (Enter, Tab,...)
from selenium.webdriver.support.ui import WebDriverWait          # Chờ phần tử xuất hiện
from selenium.webdriver.support import expected_conditions as EC  # Điều kiện chờ


# URL trang đăng nhập
URL_DANG_NHAP = "https://www.saucedemo.com"

# URL trang sản phẩm (sau khi đăng nhập thành công)
URL_SAN_PHAM = "https://www.saucedemo.com/inventory.html"


class TestDangNhap:
    """
    Lớp chứa các bài kiểm thử cho chức năng Đăng nhập.
    Mỗi bài kiểm thử sẽ mở trình duyệt mới, thực hiện thao tác,
    kiểm tra kết quả, rồi đóng trình duyệt.
    """

    def setup_method(self):
        """
        Hàm chạy TRƯỚC mỗi bài kiểm thử.
        Mục đích: Mở trình duyệt Chrome và truy cập trang đăng nhập.
        """
        # Tạo tùy chọn cho trình duyệt Chrome
        tuy_chon = webdriver.ChromeOptions()

        # Tùy chọn: chạy ẩn trình duyệt (không hiện cửa sổ)
        # Bỏ dấu # ở dòng dưới nếu muốn chạy ẩn:
        # tuy_chon.add_argument("--headless")

        # Mở trình duyệt Chrome
        self.driver = webdriver.Chrome(options=tuy_chon)

        # Đặt thời gian chờ tối đa khi tìm phần tử (10 giây)
        self.driver.implicitly_wait(10)

        # Truy cập trang đăng nhập
        self.driver.get(URL_DANG_NHAP)

    def teardown_method(self):
        """
        Hàm chạy SAU mỗi bài kiểm thử.
        Mục đích: Đóng trình duyệt để giải phóng tài nguyên.
        """
        self.driver.quit()

    # ========================
    # CÁC HÀM HỖ TRỢ
    # ========================

    def nhap_ten_dang_nhap(self, ten):
        """Tìm ô tên đăng nhập theo ID và nhập giá trị vào."""
        # Xác định ô nhập bằng ID "user-name"
        # Dùng ID vì nó là duy nhất trên trang, ổn định nhất
        o_ten = self.driver.find_element(By.ID, "user-name")
        o_ten.clear()       # Xóa nội dung cũ (nếu có)
        o_ten.send_keys(ten)  # Nhập tên đăng nhập

    def nhap_mat_khau(self, mat_khau):
        """Tìm ô mật khẩu theo ID và nhập giá trị vào."""
        # Xác định ô mật khẩu bằng ID "password"
        o_mat_khau = self.driver.find_element(By.ID, "password")
        o_mat_khau.clear()             # Xóa nội dung cũ
        o_mat_khau.send_keys(mat_khau)  # Nhập mật khẩu

    def nhan_nut_dang_nhap(self):
        """Tìm và nhấn nút Đăng nhập."""
        # Xác định nút đăng nhập bằng ID "login-button"
        nut = self.driver.find_element(By.ID, "login-button")
        nut.click()  # Nhấn nút

    def lay_thong_bao_loi(self):
        """Lấy nội dung thông báo lỗi trên trang."""
        # Thông báo lỗi nằm trong thẻ có data-test="error"
        phan_tu_loi = self.driver.find_element(
            By.CSS_SELECTOR, "[data-test='error']"
        )
        return phan_tu_loi.text  # Trả về nội dung văn bản

    # ========================
    # CÁC BÀI KIỂM THỬ
    # ========================

    def test_dang_nhap_thanh_cong(self):
        """
        TC-01: Đăng nhập thành công với tài khoản hợp lệ.

        Bước thực hiện:
        1. Nhập tên đăng nhập: standard_user
        2. Nhập mật khẩu: secret_sauce
        3. Nhấn nút Login

        Kết quả mong đợi:
        - Chuyển hướng đến trang sản phẩm (/inventory.html)
        """
        # Bước 1: Nhập tên đăng nhập đúng
        self.nhap_ten_dang_nhap("standard_user")

        # Bước 2: Nhập mật khẩu đúng
        self.nhap_mat_khau("secret_sauce")

        # Bước 3: Nhấn nút Đăng nhập
        self.nhan_nut_dang_nhap()

        # Chờ trang chuyển hướng đến trang sản phẩm (tối đa 10 giây)
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be(URL_SAN_PHAM)
        )

        # Kiểm tra: URL hiện tại phải là trang sản phẩm
        assert self.driver.current_url == URL_SAN_PHAM, \
            f"Sau khi đăng nhập thành công phải chuyển đến {URL_SAN_PHAM}"

    def test_dang_nhap_sai_mat_khau(self):
        """
        TC-02: Đăng nhập thất bại với mật khẩu sai.

        Bước thực hiện:
        1. Nhập tên đăng nhập: standard_user
        2. Nhập mật khẩu sai: sai_mat_khau
        3. Nhấn nút Login

        Kết quả mong đợi:
        - Vẫn ở trang đăng nhập
        - Hiển thị thông báo lỗi phù hợp
        """
        # Bước 1: Nhập tên đăng nhập đúng
        self.nhap_ten_dang_nhap("standard_user")

        # Bước 2: Nhập mật khẩu SAI
        self.nhap_mat_khau("sai_mat_khau")

        # Bước 3: Nhấn nút Đăng nhập
        self.nhan_nut_dang_nhap()

        # Kiểm tra: Vẫn ở trang đăng nhập (URL không thay đổi)
        assert self.driver.current_url == URL_DANG_NHAP + "/", \
            "Khi nhập sai mật khẩu, phải ở lại trang đăng nhập"

        # Kiểm tra: Có thông báo lỗi hiển thị
        thong_bao = self.lay_thong_bao_loi()
        assert "Username and password do not match" in thong_bao, \
            f"Thông báo lỗi phải chứa nội dung phù hợp, nhận được: {thong_bao}"

    def test_dang_nhap_bo_trong(self):
        """
        TC-03: Đăng nhập thất bại khi bỏ trống cả hai ô.

        Bước thực hiện:
        1. Không nhập gì vào ô Username
        2. Không nhập gì vào ô Password
        3. Nhấn nút Login

        Kết quả mong đợi:
        - Vẫn ở trang đăng nhập
        - Hiển thị thông báo lỗi yêu cầu nhập tên đăng nhập
        """
        # Không nhập gì, nhấn nút Đăng nhập luôn
        self.nhan_nut_dang_nhap()

        # Kiểm tra: Vẫn ở trang đăng nhập
        assert self.driver.current_url == URL_DANG_NHAP + "/", \
            "Khi bỏ trống, phải ở lại trang đăng nhập"

        # Kiểm tra: Có thông báo lỗi yêu cầu nhập username
        thong_bao = self.lay_thong_bao_loi()
        assert "Username is required" in thong_bao, \
            f"Thông báo lỗi phải yêu cầu nhập tên đăng nhập, nhận được: {thong_bao}"


# Cho phép chạy file trực tiếp bằng lệnh: python test_login.py
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
