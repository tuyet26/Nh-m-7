# 📝 Ghi chú Tuần 04 — Smoke Test

## Nguyễn Minh Tuấn

### Điều đã học
<!-- Viết vài dòng bằng lời của mình về điều đã học trong tuần này -->
- (Viết ở đây)

### Trả lời câu hỏi phần đọc
<!-- Trả lời 1–2 câu hỏi từ tài liệu đọc trong tuần -->
- (Viết ở đây)

### Sử dụng AI (nếu có)
<!-- Nếu có dùng AI, ghi lại: đã hỏi AI điều gì, câu trả lời có đúng không, mình hiểu thêm được gì -->
- (Viết ở đây, hoặc ghi "Không sử dụng AI")

---

## Đỗ Trung Hiếu

### Điều đã học
<!-- Viết vài dòng bằng lời của mình về điều đã học trong tuần này -->
- (Viết ở đây)

### Trả lời câu hỏi phần đọc
<!-- Trả lời 1–2 câu hỏi từ tài liệu đọc trong tuần -->
- (Viết ở đây)

### Sử dụng AI (nếu có)
<!-- Nếu có dùng AI, ghi lại: đã hỏi AI điều gì, câu trả lời có đúng không, mình hiểu thêm được gì -->
- (Viết ở đây, hoặc ghi "Không sử dụng AI")

---

## Đặng Thành Nam

### Điều đã học
<!-- Viết vài dòng bằng lời của mình về điều đã học trong tuần này -->
- (Viết ở đây)

### Trả lời câu hỏi phần đọc
<!-- Trả lời 1–2 câu hỏi từ tài liệu đọc trong tuần -->
- (Viết ở đây)

### Sử dụng AI (nếu có)
<!-- Nếu có dùng AI, ghi lại: đã hỏi AI điều gì, câu trả lời có đúng không, mình hiểu thêm được gì -->
- (Viết ở đây, hoặc ghi "Không sử dụng AI")

---

## Lưu Thị Tuyết

### Điều đã học
<!-- Viết vài dòng bằng lời của mình về điều đã học trong tuần này -->
- (Viết ở đây)

### Trả lời câu hỏi phần đọc
<!-- Trả lời 1–2 câu hỏi từ tài liệu đọc trong tuần -->
- (Viết ở đây)

### Sử dụng AI (nếu có)
<!-- Nếu có dùng AI, ghi lại: đã hỏi AI điều gì, câu trả lời có đúng không, mình hiểu thêm được gì -->
- (Viết ở đây, hoặc ghi "Không sử dụng AI")

---

## Đỗ Đình Việt

### Điều đã học

- Tuần này mình học về **Smoke Test** — đây là loại kiểm thử cơ bản nhất, được chạy đầu tiên sau khi có bản build mới. Mục đích là kiểm tra nhanh xem các chức năng chính có hoạt động hay không, trước khi làm các kiểm thử chi tiết hơn. Nếu smoke test không qua thì không cần test tiếp, tiết kiệm thời gian.
- Mình đã thực hành viết smoke test bằng Python với thư viện **pytest** và **requests** để kiểm thử một REST API (JSONPlaceholder). Mình test các thao tác CRUD cơ bản: GET (lấy dữ liệu), POST (tạo mới), PUT (cập nhật), DELETE (xóa), và cả trường hợp lỗi 404.
- Mình cũng hiểu thêm về cách đọc mã trạng thái HTTP: 200 là thành công, 201 là tạo mới thành công, 404 là không tìm thấy. Đây là kiến thức quan trọng khi kiểm thử API.

### Trả lời câu hỏi phần đọc

- **Smoke test khác gì với các loại kiểm thử khác?**
  Smoke test chỉ kiểm tra ở mức "hệ thống có chạy được không", không đi sâu vào từng chức năng cụ thể. Nó giống như khi kiểm tra một chiếc xe, smoke test là xem xe có nổ máy được không, chứ chưa phải lái thử trên đường. Nếu smoke test fail thì bản build bị reject luôn, không cần test chi tiết nữa.

- **Tại sao smoke test quan trọng trong quy trình phát triển phần mềm?**
  Vì nó giúp phát hiện sớm các lỗi nghiêm trọng ngay sau khi deploy hoặc build xong, tiết kiệm thời gian và công sức cho đội kiểm thử. Trong CI/CD pipeline, smoke test thường được chạy tự động đầu tiên.

### Sử dụng AI (nếu có)

- Mình có sử dụng AI (Antigravity/Gemini) để hỗ trợ viết code smoke test cho API JSONPlaceholder.
- **Đã hỏi AI điều gì**: Nhờ AI tạo bộ smoke test bằng pytest cho REST API, bao gồm các test cho GET, POST, PUT, DELETE.
- **Câu trả lời có đúng không**: Đúng. AI tạo ra 8 test case chạy đều pass, code có chú thích tiếng Việt rõ ràng, dễ hiểu. Cấu trúc code sạch, dùng class để nhóm các test lại với nhau.
- **Mình hiểu thêm được gì**: Mình hiểu cách dùng thư viện `requests` để gửi HTTP request, cách dùng `assert` trong pytest để kiểm tra kết quả, và cách tổ chức test case theo class. Mình cũng học được rằng smoke test nên cover các thao tác CRUD chính và cả trường hợp lỗi.
