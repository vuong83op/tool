#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tool nghiên cứu cầu số xổ số miền Bắc
Tác giả: AI Assistant
Mô tả: Tool phân tích và dự đoán số xổ số miền Bắc
"""

import sys
import os
from datetime import datetime
from web_scraper import XoSoScraper
from analyzer import SoiCauAnalyzer
from predictor import SoiCauPredictor
from web_app import create_app

def main():
    """Hàm chính của ứng dụng"""
    print("=" * 60)
    print("🎯 TOOL NGHIÊN CỨU CẦU SỐ XỔ SỐ MIỀN BẮC")
    print("=" * 60)
    print(f"Thời gian: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print()
    
    try:
        # Khởi tạo các module
        scraper = XoSoScraper()
        analyzer = SoiCauAnalyzer()
        predictor = SoiCauPredictor()
        
        print("📊 Đang lấy dữ liệu từ web...")
        # Lấy dữ liệu từ web
        data = scraper.get_latest_results()
        
        if not data:
            print("❌ Không thể lấy dữ liệu từ web!")
            return
        
        print(f"✅ Đã lấy được {len(data)} kết quả")
        
        print("\n🔍 Đang phân tích dữ liệu...")
        # Phân tích dữ liệu
        analysis = analyzer.analyze_data(data)
        
        print("\n🎲 Đang dự đoán số...")
        # Dự đoán số
        predictions = predictor.predict(analysis)
        
        # Hiển thị kết quả
        print("\n" + "=" * 60)
        print("📈 KẾT QUẢ DỰ ĐOÁN")
        print("=" * 60)
        
        print("\n🎯 LÔ ĐỀ ĐỀ XUẤT:")
        for i, lo in enumerate(predictions['lo_de'], 1):
            print(f"  {i}. {lo}")
        
        print("\n🔗 CẶP XUYÊN ĐỀ XUẤT:")
        for i, cap in enumerate(predictions['cap_xuyen'], 1):
            print(f"  {i}. {cap}")
        
        print("\n📊 THỐNG KÊ:")
        print(f"  - Độ tin cậy: {predictions['confidence']:.1f}%")
        print(f"  - Số lượng phân tích: {len(data)} kết quả")
        
        print("\n" + "=" * 60)
        print("🌐 Khởi động web interface...")
        print("Truy cập: http://localhost:5000")
        print("=" * 60)
        
        # Khởi động web app
        app = create_app()
        app.run(host='0.0.0.0', port=5000, debug=True)
        
    except Exception as e:
        print(f"❌ Lỗi: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
