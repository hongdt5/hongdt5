# Xây dựng trang Blogs cực kỳ đơn giản

Xây dựng trang Blogs đơn giản, cho phép người dùng đăng và xem các bài post, chỉnh sửa bài post cũng như một API để tạo mẫu file .docx đơn giản

Mô tả một số page/chức năng:

-   Trang chủ (homepage): Hiển thị tất cả các bài viết (theo thứ tự mới nhất -> cũ nhất), đồng thời có một form cho phép người dùng nhập thông tin để tạo một post mới
-   Trang cập nhật (edit): Hiển thị form kèm dữ liệu hiện tại về một bài post cụ thể, cho phép người dùng chỉnh sửa thông tin, sau đó cập nhật bài post đó
-   Trang giới thiệu (about) giới thiệu thông tin về bản thân/trang web/...
-   Trang tạo file docx (letter) hiển thị form cho phép người dùng nhập một số thông tin, tạo file .docx theo mẫu (tùy chỉnh), sau đó hiển thị link cho phép người dùng tải file về

Gợi ý các framework/library sử dụng:

-   Flask: https://flask.palletsprojects.com/en/2.0.x/
-   pymysql: https://pypi.org/project/PyMySQL/
-   python-docx: https://python-docx.readthedocs.io/en/latest/

Tham khảo ví dụ mẫu tại link sau: http://banx.pythonanywhere.com/
