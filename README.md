# 📋 Dự án Kiểm thử Phần mềm — Nhóm 7

## 📖 Giới thiệu

Kho lưu trữ (repository) này chứa bài tập kiểm thử phần mềm của **Nhóm 7** qua các tuần học:
- **Tuần 04:** Smoke Test (Kiểm thử API JSONPlaceholder & Web)
- **Tuần 05:** Kiểm thử chức năng Đăng nhập (Web Login Testing bằng Selenium WebDriver)

---

## 👥 Thành viên nhóm

| STT | Họ và tên | MSSV / Vai trò |
| :---: | :--- | :--- |
| 1 | Nguyễn Minh Tuấn | Thành viên |
| 2 | Đỗ Trung Hiếu | Thành viên |
| 3 | Đặng Thành Nam | Thành viên |
| 4 | Lưu Thị Tuyết | Thành viên |
| 5 | Đỗ Đình Việt | Thành viên |

---

## 📁 Cấu trúc thư mục

```
Nh-m-7/
├── 01-Tổng quan vòng đời PM, khái niệm cơ bản kiểm thử.pptx.pdf  ← Tài liệu bài giảng
├── README.md                                                    ← Hướng dẫn dự án
├── .gitignore                                                   ← Cấu hình bỏ qua git cache
│
├── tuan-04/                                                     ← Tuần 04: Smoke Test
│   ├── test_smoke.py                                            ← Smoke test API JSONPlaceholder (8 test cases)
│   ├── test_smoke_web.py                                        ← Smoke test giao diện Web The Internet
│   ├── notes.md                                                 ← Ghi chú tuần 04
│   ├── tuan4.zip                                                ← File nén bài nộp tuần 04
│   └── anh/                                                     ← Ảnh kết quả kiểm thử
│
└── tuan-05/                                                     ← Tuần 05: Kiểm thử Đăng nhập
    ├── testcases.md                                             ← Danh sách test case bằng lời (Sauce Demo & The Internet)
    ├── test_login.py                                            ← Code kiểm thử Đăng nhập trên Sauce Demo (Chính)
    ├── test_login_the_internet.py                               ← Code kiểm thử Đăng nhập trên The Internet
    ├── notes.md                                                 ← Ghi chú tuần 05 của các thành viên
    └── anh/                                                     ← Ảnh chụp màn hình kết quả chạy test
        ├── ket_qua_3_test_passed.png
        ├── pytest_3_passed.png
        ├── tc01_login_success.png
        ├── tc02_wrong_password.png
        └── tc03_wrong_username.png
```

---

## 🛠️ Yêu cầu cài đặt môi trường

### 1. Cài đặt Python
- Python 3.8 trở lên (khuyên dùng Python 3.10+).
- Khi cài đặt, hãy tích chọn **"Add Python to PATH"**.

Kiểm tra:
```bash
python --version
```

### 2. Cài đặt các thư viện
Mở terminal và chạy lệnh:
```bash
pip install pytest requests selenium
```

- `pytest`: Framework kiểm thử tự động.
- `requests`: Thư viện gửi HTTP request (dùng cho tuần 04 API).
- `selenium`: Thư viện điều khiển trình duyệt tự động (dùng cho tuần 05 Web).

---

## 🚀 Hướng dẫn chạy kiểm thử

### Tuần 04 — Smoke Test

1. Di chuyển vào thư mục tuần 04:
```bash
cd tuan-04
```

2. Chạy bài kiểm thử API:
```bash
pytest test_smoke.py -v
```

3. (Tùy chọn) Chạy bài kiểm thử Web:
```bash
pytest test_smoke_web.py -v
```

---

### Tuần 05 — Kiểm thử chức năng Đăng nhập

1. Di chuyển vào thư mục tuần 05:
```bash
cd tuan-05
```

2. Chạy bài kiểm thử chính (Sauce Demo):
```bash
pytest test_login.py -v
```

3. (Tùy chọn) Chạy bài kiểm thử The Internet:
```bash
pytest test_login_the_internet.py -v
```

---

## ✅ Kết quả mong đợi tuần 05

```
test_login.py::TestDangNhap::test_dang_nhap_thanh_cong       PASSED [ 33%]
test_login.py::TestDangNhap::test_dang_nhap_sai_mat_khau     PASSED [ 66%]
test_login.py::TestDangNhap::test_dang_nhap_bo_trong          PASSED [100%]

============================= 3 passed in 11.83s ==============================
```
