#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demo script để test tính năng soi cầu theo ngày
"""

from web_scraper import XoSoScraper
from analyzer import SoiCauAnalyzer
from predictor import SoiCauPredictor
from datetime import datetime, timedelta

def demo_by_date():
    """Demo function cho tính năng soi cầu theo ngày"""
    print("=" * 60)
    print("🎯 DEMO SOI CẦU THEO NGÀY - XỔ SỐ MIỀN BẮC")
    print("=" * 60)
    print(f"Thời gian: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print()
    
    try:
        # Khởi tạo các module
        print("📊 Khởi tạo modules...")
        scraper = XoSoScraper()
        analyzer = SoiCauAnalyzer()
        predictor = SoiCauPredictor()
        
        # Lấy ngày hôm qua để test
        yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
        
        print(f"🌐 Đang lấy dữ liệu cho ngày {yesterday}...")
        data = scraper.get_results_by_date(yesterday)
        
        if not data:
            print("❌ Không thể lấy dữ liệu từ web!")
            return
        
        print(f"✅ Đã lấy được {len(data)} kết quả cho ngày {yesterday}")
        
        # Phân tích dữ liệu
        print("\n🔍 Đang phân tích dữ liệu...")
        analysis = analyzer.analyze_data(data)
        
        # Dự đoán
        print("\n🎲 Đang dự đoán số...")
        predictions = predictor.predict(analysis)
        
        # Hiển thị kết quả
        print("\n" + "=" * 60)
        print(f"📈 KẾT QUẢ SOI CẦU CHO NGÀY {yesterday}")
        print("=" * 60)
        
        print("\n🎯 LÔ ĐỀ ĐỀ XUẤT:")
        for i, lo in enumerate(predictions['lo_de'], 1):
            print(f"  {i}. {lo}")
        
        print("\n🔗 CẶP XUYÊN ĐỀ XUẤT:")
        for i, cap in enumerate(predictions['cap_xuyen'], 1):
            print(f"  {i}. {cap}")
        
        print("\n📊 THỐNG KÊ:")
        print(f"  - Độ tin cậy: {predictions['confidence']:.1f}%")
        print(f"  - Số lượng phân tích: {predictions['analysis_summary']['total_days_analyzed']} ngày")
        
        print("\n🔥 SỐ NÓNG:")
        hot_numbers = predictions['analysis_summary']['hot_numbers']
        if hot_numbers:
            print(f"  {', '.join(hot_numbers)}")
        else:
            print("  Không có dữ liệu")
        
        print("\n❄️ SỐ LẠNH:")
        cold_numbers = predictions['analysis_summary']['cold_numbers']
        if cold_numbers:
            print(f"  {', '.join(cold_numbers)}")
        else:
            print("  Không có dữ liệu")
        
        print("\n💡 KHUYẾN NGHỊ:")
        for rec in predictions['recommendations']:
            print(f"  - {rec}")
        
        print("\n" + "=" * 60)
        print("✅ Demo hoàn thành!")
        print("🌐 Để sử dụng web interface, chạy: python web_app.py")
        print("📅 Sau đó truy cập: http://localhost:5000")
        print("📝 Chọn ngày và nhấn 'Soi Cầu Theo Ngày'")
        print("=" * 60)
        
    except Exception as e:
        print(f"❌ Lỗi: {str(e)}")
        import traceback
        traceback.print_exc()

def interactive_demo():
    """Demo tương tác cho phép người dùng nhập ngày"""
    print("=" * 60)
    print("🎯 DEMO TƯƠNG TÁC - SOI CẦU THEO NGÀY")
    print("=" * 60)
    
    try:
        # Khởi tạo các module
        scraper = XoSoScraper()
        analyzer = SoiCauAnalyzer()
        predictor = SoiCauPredictor()
        
        while True:
            print("\n📅 Nhập ngày để soi cầu (format: YYYY-MM-DD)")
            print("📝 Ví dụ: 2024-09-16")
            print("🚪 Nhập 'quit' để thoát")
            
            user_input = input("\nNgày: ").strip()
            
            if user_input.lower() == 'quit':
                print("👋 Tạm biệt!")
                break
            
            if not user_input:
                print("❌ Vui lòng nhập ngày!")
                continue
            
            try:
                # Validate ngày
                datetime.strptime(user_input, '%Y-%m-%d')
            except ValueError:
                print("❌ Format ngày không đúng! Vui lòng nhập theo format YYYY-MM-DD")
                continue
            
            print(f"\n🌐 Đang lấy dữ liệu cho ngày {user_input}...")
            data = scraper.get_results_by_date(user_input)
            
            if not data:
                print("❌ Không tìm thấy dữ liệu cho ngày này!")
                continue
            
            print(f"✅ Đã lấy được {len(data)} kết quả")
            
            # Phân tích và dự đoán
            print("🔍 Đang phân tích...")
            analysis = analyzer.analyze_data(data)
            
            print("🎲 Đang dự đoán...")
            predictions = predictor.predict(analysis)
            
            # Hiển thị kết quả
            print(f"\n📈 KẾT QUẢ SOI CẦU CHO NGÀY {user_input}")
            print("-" * 50)
            
            print("\n🎯 LÔ ĐỀ ĐỀ XUẤT:")
            for i, lo in enumerate(predictions['lo_de'][:5], 1):
                print(f"  {i}. {lo}")
            
            print("\n🔗 CẶP XUYÊN ĐỀ XUẤT:")
            for i, cap in enumerate(predictions['cap_xuyen'][:5], 1):
                print(f"  {i}. {cap}")
            
            print(f"\n📊 Độ tin cậy: {predictions['confidence']:.1f}%")
            
    except KeyboardInterrupt:
        print("\n👋 Tạm biệt!")
    except Exception as e:
        print(f"❌ Lỗi: {str(e)}")

if __name__ == "__main__":
    print("Chọn chế độ demo:")
    print("1. Demo tự động (ngày hôm qua)")
    print("2. Demo tương tác (nhập ngày)")
    
    choice = input("Nhập lựa chọn (1 hoặc 2): ").strip()
    
    if choice == "1":
        demo_by_date()
    elif choice == "2":
        interactive_demo()
    else:
        print("Lựa chọn không hợp lệ!")
