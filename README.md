# Direct-Link
Xuất liên kết tải trực tiếp từ OneDrive Dropbox và Google Drive

Direct Link Google Drive, OneDrive, DropBox by ChatGPT 

Từ một người không hiểu 1 lệnh nào của Python nhờ sự trợ giúp của ChatGPT nên tôi đã tự thiết kế được cho mình 1 phần mềm (tôi thích gọi nó là Script hơn) nhỏ chạy bằng Python để tạo liên kết tải xuống trực tiếp cho OneDrive, Dropbox và Google Drive 

Giới thiệu (hỗ trợ bởi ChatGPT)
Script này được xây dựng với mục đích giúp người dùng chuyển đổi các liên kết từ OneDrive, Dropbox và Google Drive thành liên kết tải xuống. Nó có thể đọc liên kết từ tập tin hoặc nhập từ bàn phím và ghi kết quả vào tập tin.

Các chức năng chính:
Đọc các liên kết từ tập tin hoặc nhập từ bàn phím
Chuyển đổi các liên kết từ OneDrive, Dropbox và Google Drive thành liên kết tải xuống
Hiển thị liên kết trực tiếp sau khi chuyển đổi
Ghi kết quả vào tập tin

Ưu điểm:
Dễ sử dụng
Chuyển đổi nhanh chóng
Có thể nháy đúp bôi đen copy liên kết tải xuống trực tiếp ngay

Nhược điểm:
Chưa đóng gói lại được thành exe
Phải thêm nguồn thủ công vào input.txt hoặc nhập từ bàn phím không như những phần mềm/tiện ích khác có thể trực tiếp thêm ngay khi copy vào clipboard

Chuẩn bị trước khi chạy:
Cài đặt Python
Chuẩn bị input.txt nằm chung với Script
Mỗi liên kết là 1 dòng trong input.txt
Đối với OneDrive phải vào thao tác trên từng tệp muốn chia sẻ
Chuột phải vào tệp cần chia sẻ và chọn tuỳ chọn Embed
Generate để lấy liên kết nhúng
Dán liên kết nhúng vào input.txt (hoặc dán luôn vào Script sau khi đã nhấn phím "t" *)

Cách sử dụng:
Chạy Script
Nhập "f" để đọc từ tập tin input.txt hoặc "t" để nhập từ bàn phím
Đối với nhập liên kết từ bàn phím có thể dán từng liên kết hoặc dán nhiều liên kết nhưng phải đảm bảo mỗi liên kết là 1 dòng*
Sao chép các liên kết hoặc mở tập tin output.txt để đọc liên kết
Các liên kết hợp lệ sẽ được ghi vào tập tin "output.txt".
