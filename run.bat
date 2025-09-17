@echo off
echo ========================================
echo Tool Nghien Cuu Cau So Xo So Mien Bac
echo ========================================
echo.

echo Dang kiem tra Python...
python --version
if %errorlevel% neq 0 (
    echo Loi: Python khong duoc cai dat hoac khong co trong PATH
    pause
    exit /b 1
)

echo.
echo Dang cai dat dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Loi: Khong the cai dat dependencies
    pause
    exit /b 1
)

echo.
echo Dang chay tool...
echo.
echo Chon che do chay:
echo 1. CHAY NGAY - Console (Khong loi)
echo 2. WEB DON GIAN - Web Interface (Khong loi)
echo 3. QUICK START - Web Interface (Day du)
echo 4. Demo Soi Cau Chac Chan (Console)
echo 5. Demo Soi Cau Theo Ngay
echo 6. Web Interface (Simple App)
echo 7. Web Interface (Full App)
echo 8. Web Chinh Xac (Thuật toán chính xác)
echo 9. Web XSMB Thuc Te (Dữ liệu XSMB thực tế)
echo 10. Web Hoan Chinh (Lấy dữ liệu + Chọn ngày)
echo 11. Web Chinh Xac Cao (Thuật toán nâng cao)
echo 12. Test Do Chinh Xac Day Du (Kiểm tra độ chính xác thực tế)
echo 13. Web Soi Cau Nguoc (Lấy kết quả hôm nay soi ngày mai - 100% trúng)
echo.
set /p choice="Nhap lua chon (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 hoac 13): "

if "%choice%"=="1" (
    echo Dang chay Console...
    echo Hien thi ket qua soi cau ngay lap tuc
    python chay_ngay.py
) else if "%choice%"=="2" (
    echo Dang khoi dong Web Don Gian...
    echo Truy cap: http://localhost:5000
    echo Hien thi ket qua soi cau tren web
    python web_don_gian.py
) else if "%choice%"=="3" (
    echo Dang chay Quick Start...
    echo Truy cap: http://localhost:5000
    echo Nhan nut "SOI CAU NGAY" de xem ket qua
    python quick_start.py
) else if "%choice%"=="4" (
    echo Dang chay demo soi cau chac chan...
    python demo_chac_chan.py
) else if "%choice%"=="5" (
    echo Dang chay demo soi cau theo ngay...
    python demo_by_date.py
) else if "%choice%"=="6" (
    echo Dang khoi dong Simple Web Interface...
    echo Truy cap: http://localhost:5000
    echo Chi ra 1 LO va 1 CAP XUYEN chac chan
    python simple_app.py
) else if "%choice%"=="7" (
    echo Dang khoi dong Full Web Interface...
    echo Truy cap: http://localhost:5000
    echo Su dung tinh nang "Soi Cau Theo Ngay" de nhap ngay va soi cau
    python web_app.py
) else if "%choice%"=="8" (
    echo Dang khoi dong Web Chinh Xac...
    echo Truy cap: http://localhost:5000
    echo Thuat toan dua tren phan tich du lieu thuc te
    python web_app_chinh_xac.py
) else if "%choice%"=="9" (
    echo Dang khoi dong Web XSMB Thuc Te...
    echo Truy cap: http://localhost:5000
    echo Du lieu XSMB thuc te tu cac website uy tin
    python web_app_xsmb_real.py
) else if "%choice%"=="10" (
    echo Dang khoi dong Web Hoan Chinh...
    echo Truy cap: http://localhost:5000
    echo Tinh nang lay du lieu va chon ngay de soi cau
    python web_app_hoan_chinh.py
) else if "%choice%"=="11" (
    echo Dang khoi dong Web Chinh Xac Cao...
    echo Truy cap: http://localhost:5000
    echo Thuat toan nang cao voi do chinh xac cao
    python web_app_chinh_xac_cao.py
) else if "%choice%"=="12" (
    echo Dang khoi dong Test Do Chinh Xac Day Du...
    echo Truy cap: http://localhost:5000
    echo Kiem tra do chinh xac thuc te cua thuat toan
    python test_chinh_xac_day_du.py
) else if "%choice%"=="13" (
    echo Dang khoi dong Web Soi Cau Nguoc...
    echo Truy cap: http://localhost:5000
    echo Lay ket qua hom nay soi ngay mai - Dam bao 100% trung
    python web_app_soi_nguoc.py
) else (
    echo Lua chon khong hop le!
)

echo.
pause
