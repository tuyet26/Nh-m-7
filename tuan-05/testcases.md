# 📋 Danh sách Test Cases — Chức năng Đăng nhập (Login)

> **Môn học:** Kiểm thử phần mềm  
> **Nhóm thực hiện:** Nhóm 7 (Nguyễn Minh Tuấn, Đỗ Trung Hiếu, Đặng Thành Nam, Lưu Thị Tuyết, Đỗ Đình Việt)  
> **Tuần 05:** Kiểm thử chức năng Đăng nhập (Web)

---

# PHẦN 1: BỘ KIỂM THỬ TRÊN SAUCE DEMO (Chính)
> **Trang kiểm thử:** https://www.saucedemo.com  
> **File code thực thi:** `test_login.py`

## TC01 - Đăng nhập thành công với tài khoản hợp lệ

| Mục | Nội dung |
| --- | --- |
| **Mã test** | TC01 |
| **Tiêu đề** | Đăng nhập thành công với tên đăng nhập và mật khẩu đúng |
| **Điều kiện trước** | Trình duyệt đã mở, chưa đăng nhập |
| **Mức ưu tiên** | Cao |

### Các bước thực hiện

| Bước | Hành động | Dữ liệu |
| --- | --- | --- |
| 1 | Mở trình duyệt Chrome, truy cập trang đăng nhập | https://www.saucedemo.com |
| 2 | Nhập tên đăng nhập vào ô "Username" | `standard_user` |
| 3 | Nhập mật khẩu vào ô "Password" | `secret_sauce` |
| 4 | Nhấn nút "Login" | |

### Kết quả mong đợi

- Đăng nhập thành công, trang chuyển hướng đến trang sản phẩm (`/inventory.html`).
- URL sau khi đăng nhập: `https://www.saucedemo.com/inventory.html`
- Không hiển thị thông báo lỗi nào.

---

## TC02 - Đăng nhập thất bại với mật khẩu sai

| Mục | Nội dung |
| --- | --- |
| **Mã test** | TC02 |
| **Tiêu đề** | Đăng nhập thất bại khi nhập mật khẩu không đúng |
| **Điều kiện trước** | Trình duyệt đã mở, chưa đăng nhập |
| **Mức ưu tiên** | Cao |

### Các bước thực hiện

| Bước | Hành động | Dữ liệu |
| --- | --- | --- |
| 1 | Mở trình duyệt Chrome, truy cập trang đăng nhập | https://www.saucedemo.com |
| 2 | Nhập tên đăng nhập vào ô "Username" | `standard_user` |
| 3 | Nhập mật khẩu sai vào ô "Password" | `sai_mat_khau` |
| 4 | Nhấn nút "Login" | |

### Kết quả mong đợi

- Đăng nhập thất bại, vẫn ở trang đăng nhập.
- Hiển thị thông báo lỗi: **"Epic sadface: Username and password do not match any user in this service"**
- Các ô nhập hiển thị biểu tượng báo lỗi màu đỏ.

---

## TC03 - Đăng nhập thất bại khi bỏ trống cả hai ô

| Mục | Nội dung |
| --- | --- |
| **Mã test** | TC03 |
| **Tiêu đề** | Đăng nhập thất bại khi không nhập tên đăng nhập và mật khẩu |
| **Điều kiện trước** | Trình duyệt đã mở, chưa đăng nhập |
| **Mức ưu tiên** | Cao |

### Các bước thực hiện

| Bước | Hành động | Dữ liệu |
| --- | --- | --- |
| 1 | Mở trình duyệt Chrome, truy cập trang đăng nhập | https://www.saucedemo.com |
| 2 | Không nhập gì vào ô "Username" | _(để trống)_ |
| 3 | Không nhập gì vào ô "Password" | _(để trống)_ |
| 4 | Nhấn nút "Login" | |

### Kết quả mong đợi

- Đăng nhập thất bại, vẫn ở trang đăng nhập.
- Hiển thị thông báo lỗi: **"Epic sadface: Username is required"**
- Các ô nhập hiển thị biểu tượng báo lỗi màu đỏ.

---

# PHẦN 2: BỘ KIỂM THỬ TRÊN THE INTERNET (Bổ sung)
> **Trang kiểm thử:** https://the-internet.herokuapp.com/login  
> **File code thực thi:** `test_login_the_internet.py`

## TC01_INT - Đăng nhập thành công

### Mục tiêu
Kiểm tra người dùng có thể đăng nhập thành công với username và password hợp lệ.

### Test data
- **Username:** `tomsmith`
- **Password:** `SuperSecretPassword!`

### Các bước thực hiện
1. Mở trình duyệt Chrome.
2. Truy cập trang `https://the-internet.herokuapp.com/login`.
3. Nhập username `tomsmith`.
4. Nhập password `SuperSecretPassword!`.
5. Nhấn nút Login.

### Kết quả mong đợi
Đăng nhập thành công và hệ thống hiển thị thông báo:
`You logged into a secure area!`

---

## TC02_INT - Đăng nhập với password sai

### Mục tiêu
Kiểm tra hệ thống xử lý khi người dùng nhập password không đúng.

### Test data
- **Username:** `tomsmith`
- **Password:** `WrongPassword123`

### Các bước thực hiện
1. Mở trình duyệt Chrome.
2. Truy cập trang `https://the-internet.herokuapp.com/login`.
3. Nhập username `tomsmith`.
4. Nhập password `WrongPassword123`.
5. Nhấn nút Login.

### Kết quả mong đợi
Hệ thống không cho đăng nhập và hiển thị thông báo lỗi:
`Your password is invalid!`

---

## TC03_INT - Đăng nhập với username sai

### Mục tiêu
Kiểm tra hệ thống xử lý khi người dùng nhập username không đúng.

### Test data
- **Username:** `wronguser`
- **Password:** `SuperSecretPassword!`

### Các bước thực hiện
1. Mở trình duyệt Chrome.
2. Truy cập trang `https://the-internet.herokuapp.com/login`.
3. Nhập username `wronguser`.
4. Nhập password `SuperSecretPassword!`.
5. Nhấn nút Login.

### Kết quả mong đợi
Hệ thống không cho đăng nhập và hiển thị thông báo lỗi:
`Your username is invalid!`
