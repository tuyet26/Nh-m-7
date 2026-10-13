# test_smoke.py - Bài kiểm thử smoke test đầu tiên
# Mục đích: Kiểm tra nhanh các chức năng cơ bản của API JSONPlaceholder
# để đảm bảo hệ thống hoạt động ổn định trước khi kiểm thử chi tiết.
#
# API được sử dụng: https://jsonplaceholder.typicode.com
# Đây là một API giả lập miễn phí dùng để học tập và thử nghiệm.
#
# Nhóm thực hiện:
#   - Nguyễn Minh Tuấn
#   - Đỗ Trung Hiếu
#   - Đặng Thành Nam
#   - Lưu Thị Tuyết
#   - Đỗ Đình Việt

import requests  # Thư viện gửi HTTP request đến API
import pytest     # Framework kiểm thử phổ biến nhất của Python

# URL gốc của API mà chúng ta sẽ kiểm thử
BASE_URL = "https://jsonplaceholder.typicode.com"


class TestSmokeAPI:
    """
    Lớp chứa các bài kiểm thử smoke test cho API JSONPlaceholder.
    Smoke test là kiểm thử ở mức cơ bản nhất, chỉ kiểm tra xem
    hệ thống có "chạy được" hay không, chưa đi sâu vào chi tiết.
    """

    # --- Kiểm thử GET: Lấy dữ liệu ---

    def test_lay_danh_sach_bai_viet(self):
        """
        Kiểm tra API trả về danh sách bài viết thành công.
        Endpoint: GET /posts
        Kỳ vọng: Mã trạng thái 200 và danh sách không rỗng.
        """
        # Gửi yêu cầu GET đến endpoint /posts để lấy tất cả bài viết
        response = requests.get(f"{BASE_URL}/posts")

        # Kiểm tra mã trạng thái HTTP là 200 (thành công)
        assert response.status_code == 200, "API phải trả về mã 200"

        # Chuyển dữ liệu trả về thành danh sách Python
        data = response.json()

        # Kiểm tra danh sách không rỗng (API có dữ liệu)
        assert len(data) > 0, "Danh sách bài viết không được rỗng"

        # JSONPlaceholder luôn trả về đúng 100 bài viết
        assert len(data) == 100, "Phải có đúng 100 bài viết"

    def test_lay_mot_bai_viet_theo_id(self):
        """
        Kiểm tra API trả về đúng một bài viết khi truy vấn theo ID.
        Endpoint: GET /posts/1
        Kỳ vọng: Mã 200, bài viết có đầy đủ các trường dữ liệu.
        """
        # Gửi yêu cầu lấy bài viết có ID = 1
        response = requests.get(f"{BASE_URL}/posts/1")

        assert response.status_code == 200, "API phải trả về mã 200"

        post = response.json()

        # Kiểm tra bài viết có đầy đủ các trường cần thiết
        # (userId, id, title, body) - đây là cấu trúc chuẩn của một bài viết
        assert "userId" in post, "Bài viết phải có trường userId"
        assert "id" in post, "Bài viết phải có trường id"
        assert "title" in post, "Bài viết phải có trường title"
        assert "body" in post, "Bài viết phải có trường body"

        # Đảm bảo ID trả về khớp với ID yêu cầu
        assert post["id"] == 1, "ID bài viết phải bằng 1"

    def test_lay_danh_sach_binh_luan(self):
        """
        Kiểm tra endpoint lấy danh sách bình luận hoạt động bình thường.
        Endpoint: GET /comments
        Kỳ vọng: Mã 200 và có dữ liệu trả về.
        """
        response = requests.get(f"{BASE_URL}/comments")

        assert response.status_code == 200, "API phải trả về mã 200"

        comments = response.json()
        assert len(comments) > 0, "Danh sách bình luận không được rỗng"

        # Kiểm tra cấu trúc của một bình luận
        first_comment = comments[0]
        assert "email" in first_comment, "Bình luận phải có trường email"
        assert "body" in first_comment, "Bình luận phải có trường body"

    # --- Kiểm thử POST: Tạo dữ liệu mới ---

    def test_tao_bai_viet_moi(self):
        """
        Kiểm tra API cho phép tạo bài viết mới thành công.
        Endpoint: POST /posts
        Kỳ vọng: Mã 201 (Created) và dữ liệu trả về khớp với dữ liệu gửi.
        """
        # Chuẩn bị dữ liệu bài viết mới
        bai_viet_moi = {
            "title": "Bài viết kiểm thử",
            "body": "Đây là nội dung bài viết dùng để smoke test.",
            "userId": 1
        }

        # Gửi yêu cầu POST để tạo bài viết
        response = requests.post(f"{BASE_URL}/posts", json=bai_viet_moi)

        # Mã 201 nghĩa là tài nguyên đã được tạo thành công
        assert response.status_code == 201, "API phải trả về mã 201 khi tạo mới"

        data = response.json()

        # Kiểm tra dữ liệu trả về có khớp với dữ liệu đã gửi
        assert data["title"] == bai_viet_moi["title"], "Tiêu đề phải khớp"
        assert data["body"] == bai_viet_moi["body"], "Nội dung phải khớp"
        assert "id" in data, "Bài viết mới phải được gán một ID"

    # --- Kiểm thử PUT: Cập nhật dữ liệu ---

    def test_cap_nhat_bai_viet(self):
        """
        Kiểm tra API cho phép cập nhật toàn bộ bài viết.
        Endpoint: PUT /posts/1
        Kỳ vọng: Mã 200 và dữ liệu được cập nhật đúng.
        """
        # Dữ liệu cập nhật cho bài viết ID = 1
        du_lieu_cap_nhat = {
            "id": 1,
            "title": "Tiêu đề đã cập nhật",
            "body": "Nội dung đã được thay đổi để kiểm thử.",
            "userId": 1
        }

        response = requests.put(f"{BASE_URL}/posts/1", json=du_lieu_cap_nhat)

        assert response.status_code == 200, "API phải trả về mã 200 khi cập nhật"

        data = response.json()
        assert data["title"] == du_lieu_cap_nhat["title"], "Tiêu đề phải được cập nhật"

    # --- Kiểm thử DELETE: Xóa dữ liệu ---

    def test_xoa_bai_viet(self):
        """
        Kiểm tra API cho phép xóa bài viết.
        Endpoint: DELETE /posts/1
        Kỳ vọng: Mã 200 (xóa thành công).
        """
        # Gửi yêu cầu xóa bài viết có ID = 1
        response = requests.delete(f"{BASE_URL}/posts/1")

        # API trả về mã 200 nghĩa là xóa thành công
        assert response.status_code == 200, "API phải trả về mã 200 khi xóa"

    # --- Kiểm thử trường hợp lỗi ---

    def test_bai_viet_khong_ton_tai(self):
        """
        Kiểm tra API xử lý đúng khi truy vấn bài viết không tồn tại.
        Endpoint: GET /posts/99999
        Kỳ vọng: Mã 404 (Not Found).
        """
        # Truy vấn bài viết với ID rất lớn (không tồn tại)
        response = requests.get(f"{BASE_URL}/posts/99999")

        # API phải trả về mã 404 khi không tìm thấy tài nguyên
        assert response.status_code == 404, "API phải trả về mã 404 cho tài nguyên không tồn tại"

    def test_lay_danh_sach_nguoi_dung(self):
        """
        Kiểm tra endpoint lấy danh sách người dùng hoạt động bình thường.
        Endpoint: GET /users
        Kỳ vọng: Mã 200, có 10 người dùng, mỗi người có tên và email.
        """
        response = requests.get(f"{BASE_URL}/users")

        assert response.status_code == 200, "API phải trả về mã 200"

        users = response.json()

        # JSONPlaceholder có đúng 10 người dùng mẫu
        assert len(users) == 10, "Phải có đúng 10 người dùng"

        # Kiểm tra mỗi người dùng có tên và email
        for user in users:
            assert "name" in user, "Người dùng phải có trường name"
            assert "email" in user, "Người dùng phải có trường email"


# Cho phép chạy file trực tiếp bằng lệnh: python test_smoke.py
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
