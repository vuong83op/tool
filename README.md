# 🎯 Tool Nghiên Cứu Cầu Số Xổ Số Miền Bắc

## 📋 Mô Tả

Tool nghiên cứu cầu số xổ số miền Bắc là một ứng dụng web được phát triển bằng Python Flask, giúp phân tích và dự đoán số xổ số miền Bắc dựa trên dữ liệu thực tế từ các trang web xổ số.

## ✨ Tính Năng

### 🔍 Phân Tích Dữ Liệu
- **Web Scraping**: Tự động lấy dữ liệu từ các trang web xổ số miền Bắc
- **Phân Tích Tần Suất**: Thống kê tần suất xuất hiện của các số
- **Phân Tích Pattern**: Tìm các pattern trong dữ liệu (tổng số, chẵn/lẻ, dãy số)
- **Phân Tích Xu Hướng**: Phân tích xu hướng gần đây, theo tuần, theo tháng
- **Phân Tích Chu Kỳ**: Tìm chu kỳ trong dữ liệu
- **Phân Tích Tương Quan**: Tìm mối tương quan giữa các số

### 🎲 Dự Đoán
- **Lô Đề**: Dự đoán các số lô đề có khả năng về cao
- **Cặp Xuyên**: Dự đoán các cặp số xuyên
- **Độ Tin Cậy**: Tính toán độ tin cậy của dự đoán
- **Khuyến Nghị**: Đưa ra các khuyến nghị dựa trên phân tích
- **Soi Cầu Theo Ngày**: Cho phép nhập ngày cụ thể để soi cầu

### 🌐 Giao Diện Web
- **Responsive Design**: Giao diện thân thiện, tương thích mọi thiết bị
- **Real-time Updates**: Cập nhật dữ liệu theo thời gian thực
- **Interactive Charts**: Biểu đồ tương tác hiển thị thống kê
- **Auto Refresh**: Tự động làm mới dữ liệu mỗi 5 phút

## 🚀 Cài Đặt

### Yêu Cầu Hệ Thống
- Python 3.8+
- pip (Python package manager)
- Kết nối Internet để lấy dữ liệu từ web

### Cài Đặt Dependencies

```bash
# Clone repository
git clone <repository-url>
cd nghiencuu

# Tạo virtual environment (khuyến nghị)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# hoặc
venv\Scripts\activate     # Windows

# Cài đặt dependencies
pip install -r requirements.txt
```

### Chạy Ứng Dụng

```bash
# Chạy ứng dụng chính
python main.py

# Chạy web app trực tiếp
python web_app.py

# Demo console
python demo.py

# Demo soi cầu theo ngày
python demo_by_date.py

# Sử dụng file batch (Windows)
run.bat
```

Ứng dụng sẽ chạy tại: `http://localhost:5000`

### 🌟 Tính Năng Mới: Soi Cầu Theo Ngày

Tool hiện đã hỗ trợ tính năng **Soi Cầu Theo Ngày**:

1. **Web Interface**: Truy cập `http://localhost:5000`, chọn ngày và nhấn "Soi Cầu Theo Ngày"
2. **Console Demo**: Chạy `python demo_by_date.py` để test tính năng
3. **API**: Sử dụng endpoint `/api/predict_by_date` với POST request

**Cách sử dụng:**
- Chọn ngày bất kỳ (tối đa là hôm nay)
- Tool sẽ lấy dữ liệu từ [xoso.com.vn](https://xoso.com.vn/xo-so-mien-bac/xsmb-p1.html) cho ngày đó
- Phân tích và đưa ra dự đoán lô đề, cặp xuyên

## 📁 Cấu Trúc Dự Án

```
nghiencuu/
├── main.py                 # File chính của ứng dụng
├── web_scraper.py          # Module web scraping
├── analyzer.py             # Module phân tích dữ liệu
├── predictor.py            # Module dự đoán
├── web_app.py              # Flask web application
├── requirements.txt        # Dependencies
├── README.md              # Documentation
└── templates/
    └── index.html         # Giao diện web
```

## 🔧 Cấu Hình

### Cấu Hình Web Scraping

Trong file `web_scraper.py`, bạn có thể:

- Thêm/bớt các URL trang web xổ số
- Điều chỉnh thời gian cache
- Thay đổi User-Agent
- Cấu hình timeout

### Cấu Hình Phân Tích

Trong file `analyzer.py`, bạn có thể:

- Điều chỉnh số ngày phân tích
- Thay đổi thuật toán phân tích
- Cấu hình các pattern cần tìm
- Điều chỉnh độ nhạy của thuật toán

### Cấu Hình Dự Đoán

Trong file `predictor.py`, bạn có thể:

- Thay đổi số lượng dự đoán
- Điều chỉnh thuật toán dự đoán
- Cấu hình độ tin cậy
- Thay đổi các yếu tố ảnh hưởng

## 📊 API Endpoints

### `/api/predict`
- **Method**: GET
- **Description**: Lấy dự đoán số mới nhất
- **Response**: JSON chứa dự đoán lô đề, cặp xuyên, độ tin cậy

### `/api/data`
- **Method**: GET
- **Description**: Lấy dữ liệu thô từ web
- **Response**: JSON chứa dữ liệu xổ số

### `/api/analysis`
- **Method**: GET
- **Description**: Lấy kết quả phân tích dữ liệu
- **Response**: JSON chứa các thống kê và phân tích

### `/api/statistics`
- **Method**: GET
- **Description**: Lấy thống kê cơ bản
- **Response**: JSON chứa thống kê

### `/api/predict_by_date`
- **Method**: POST
- **Description**: Dự đoán số theo ngày cụ thể
- **Request Body**: `{"date": "YYYY-MM-DD"}`
- **Response**: JSON chứa dự đoán cho ngày đó

### `/refresh`
- **Method**: GET
- **Description**: Làm mới cache và dữ liệu
- **Response**: JSON chứa trạng thái làm mới

## 🎨 Giao Diện

Giao diện web được thiết kế với:

- **Bootstrap 5**: Framework CSS hiện đại
- **Font Awesome**: Icons đẹp mắt
- **Gradient Background**: Nền gradient đẹp mắt
- **Card Layout**: Layout dạng card dễ đọc
- **Responsive**: Tương thích mọi thiết bị
- **Interactive**: Tương tác mượt mà

## 🔒 Bảo Mật

- Sử dụng Flask secret key
- Validate input data
- Error handling toàn diện
- Rate limiting (có thể thêm)
- CORS protection (có thể thêm)

## 🚨 Lưu Ý Quan Trọng

⚠️ **DISCLAIMER**: Tool này chỉ mang tính chất nghiên cứu và giải trí. Không đảm bảo độ chính xác của dự đoán. Việc sử dụng tool này để đặt cược là trách nhiệm của người dùng.

## 🐛 Troubleshooting

### Lỗi Kết Nối
- Kiểm tra kết nối Internet
- Kiểm tra firewall/antivirus
- Thử thay đổi User-Agent

### Lỗi Dependencies
- Cập nhật pip: `pip install --upgrade pip`
- Cài đặt lại dependencies: `pip install -r requirements.txt --force-reinstall`

### Lỗi Web Scraping
- Kiểm tra các trang web xổ số có thay đổi cấu trúc không
- Thử thay đổi timeout
- Kiểm tra robots.txt của các trang web

## 📈 Roadmap

- [ ] Thêm database để lưu trữ dữ liệu
- [ ] Cải thiện thuật toán dự đoán
- [ ] Thêm biểu đồ tương tác
- [ ] Hỗ trợ nhiều loại xổ số
- [ ] Thêm tính năng export dữ liệu
- [ ] Tối ưu hóa performance
- [ ] Thêm unit tests

## 🤝 Đóng Góp

Mọi đóng góp đều được chào đón! Vui lòng:

1. Fork repository
2. Tạo feature branch
3. Commit changes
4. Push to branch
5. Tạo Pull Request

## 📄 License

MIT License - Xem file LICENSE để biết thêm chi tiết.

## 👨‍💻 Tác Giả

AI Assistant - Tool được phát triển với sự hỗ trợ của AI

## 📞 Hỗ Trợ

Nếu gặp vấn đề, vui lòng:

1. Kiểm tra phần Troubleshooting
2. Tạo issue trên GitHub
3. Liên hệ qua email

---

**Chúc bạn may mắn với tool nghiên cứu cầu số! 🍀**
