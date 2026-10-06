# Week 5 - Login Test Cases

## TC01 - Đăng nhập thành công

### Mục tiêu
Kiểm tra người dùng có thể đăng nhập thành công với username và password hợp lệ.

### Test data
- Username: tomsmith
- Password: SuperSecretPassword!

### Các bước thực hiện
1. Mở trình duyệt Chrome.
2. Truy cập trang Login.
3. Nhập username `tomsmith`.
4. Nhập password `SuperSecretPassword!`.
5. Nhấn nút Login.

### Kết quả mong đợi
Đăng nhập thành công và hệ thống hiển thị thông báo:

`You logged into a secure area!`


## TC02 - Đăng nhập với password sai

### Mục tiêu
Kiểm tra hệ thống xử lý khi người dùng nhập password không đúng.

### Test data
- Username: tomsmith
- Password: WrongPassword123

### Các bước thực hiện
1. Mở trình duyệt Chrome.
2. Truy cập trang Login.
3. Nhập username `tomsmith`.
4. Nhập password `WrongPassword123`.
5. Nhấn nút Login.

### Kết quả mong đợi
Hệ thống không cho đăng nhập và hiển thị:

`Your password is invalid!`


## TC03 - Đăng nhập với username sai

### Mục tiêu
Kiểm tra hệ thống xử lý khi người dùng nhập username không đúng.

### Test data
- Username: wronguser
- Password: SuperSecretPassword!

### Các bước thực hiện
1. Mở trình duyệt Chrome.
2. Truy cập trang Login.
3. Nhập username `wronguser`.
4. Nhập password `SuperSecretPassword!`.
5. Nhấn nút Login.

### Kết quả mong đợi
Hệ thống không cho đăng nhập và hiển thị:

`Your username is invalid!`
