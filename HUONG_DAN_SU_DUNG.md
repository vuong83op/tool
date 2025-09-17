# 🎯 HƯỚNG DẪN SỬ DỤNG TOOL XỔ SỐ MIỀN BẮC

## 🚀 Cách Chạy Tool

### **Phương Pháp 1: Simple App (Khuyến nghị)**
```bash
python simple_app.py
```
- ✅ **Đơn giản, ổn định**
- ✅ **Không cần dependencies phức tạp**
- ✅ **Có đầy đủ tính năng demo**

### **Phương Pháp 2: Full App**
```bash
python web_app.py
```
- ⚠️ **Cần cài đặt đầy đủ dependencies**
- ⚠️ **Có thể gặp lỗi import**

### **Phương Pháp 3: File Batch (Windows)**
```bash
run.bat
```
- Chọn option 3: "Web Interface"

## 🌐 Truy Cập Web Interface

1. **Mở trình duyệt** (Chrome, Firefox, Edge...)
2. **Truy cập**: `http://localhost:5000`
3. **Hoặc**: `http://127.0.0.1:5000`

## 📱 Cách Sử Dụng

### **1. Làm Mới Dự Đoán**
- Nhấn nút **"🔄 Làm Mới Dự Đoán"**
- Tool sẽ phân tích dữ liệu mới nhất
- Hiển thị kết quả lô đề và cặp xuyên

### **2. Soi Cầu Theo Ngày**
- **Chọn ngày** trong ô date picker
- Nhấn nút **"📅 Soi Cầu Theo Ngày"**
- Tool sẽ phân tích dữ liệu cho ngày đó
- Hiển thị dự đoán cụ thể

## 🔧 Khắc Phục Lỗi

### **Lỗi "Failed to fetch"**
```bash
# Kiểm tra server có chạy không
netstat -an | findstr :5000

# Nếu không có, chạy lại
python simple_app.py
```

### **Lỗi Import**
```bash
# Cài đặt dependencies
pip install flask requests beautifulsoup4 numpy

# Hoặc sử dụng simple_app.py
python simple_app.py
```

### **Lỗi Port 5000 đã được sử dụng**
```bash
# Tìm và kill process
netstat -ano | findstr :5000
taskkill /PID <PID_NUMBER> /F

# Hoặc đổi port trong code
```

## 📊 Tính Năng Hiện Có

### ✅ **Đã Hoạt Động**
- Web interface đẹp mắt
- API endpoints đầy đủ
- Form nhập ngày
- Hiển thị kết quả dự đoán
- Responsive design

### 🔄 **Đang Phát Triển**
- Web scraping thực tế từ xoso.com.vn
- Phân tích dữ liệu nâng cao
- Thuật toán dự đoán chính xác

## 🎯 Demo Data

Tool hiện đang sử dụng **dữ liệu demo** để test:

### **Lô Đề Demo**
- 12 (tần suất: 5)
- 34 (số lạnh: 2)
- 56 (xu hướng gần đây: 3)
- 78 (chu kỳ ngày)
- 90 (tương quan cao)

### **Cặp Xuyên Demo**
- 12-34 (tần suất: 3)
- 56-78 (cặp lạnh: 1)
- 90-12 (xu hướng gần đây)
- 34-56 (pattern chẵn/lẻ)
- 78-90 (chu kỳ tuần)

## 📞 Hỗ Trợ

### **Nếu gặp vấn đề:**
1. **Kiểm tra Python**: `python --version`
2. **Kiểm tra Flask**: `python -c "import flask; print('OK')"`
3. **Kiểm tra port**: `netstat -an | findstr :5000`
4. **Chạy simple_app.py**: `python simple_app.py`

### **Logs và Debug:**
- Server sẽ hiển thị logs trong terminal
- Kiểm tra console của trình duyệt (F12)
- Xem network tab để debug API calls

## 🎉 Kết Luận

Tool đã sẵn sàng sử dụng với:
- ✅ **Giao diện web đẹp mắt**
- ✅ **Tính năng soi cầu theo ngày**
- ✅ **API endpoints đầy đủ**
- ✅ **Responsive design**
- ✅ **Dữ liệu demo để test**

**Chạy `python simple_app.py` và truy cập `http://localhost:5000` để bắt đầu!** 🚀
