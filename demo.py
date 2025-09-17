#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demo script để test tool nghiên cứu cầu số
"""

from web_scraper import XoSoScraper
from analyzer import SoiCauAnalyzer
from predictor import SoiCauPredictor
from datetime import datetime

def demo():
    """Demo function"""
    print("=" * 60)
    print("🎯 DEMO TOOL NGHIÊN CỨU CẦU SỐ XỔ SỐ MIỀN BẮC")
    print("=" * 60)
    print(f"Thời gian: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print()
    
    try:
        # Khởi tạo các module
        print("📊 Khởi tạo modules...")
        scraper = XoSoScraper()
        analyzer = SoiCauAnalyzer()
        predictor = SoiCauPredictor()
        
        # Lấy dữ liệu
        print("🌐 Đang lấy dữ liệu từ web...")
        data = scraper.get_latest_results(days=30)
        
        if not data:
            print("❌ Không thể lấy dữ liệu từ web!")
            return
        
        print(f"✅ Đã lấy được {len(data)} kết quả")
        
        # Phân tích dữ liệu
        print("\n🔍 Đang phân tích dữ liệu...")
        analysis = analyzer.analyze_data(data)
        
        # Dự đoán
        print("\n🎲 Đang dự đoán số...")
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
        print("🌐 Để chạy web interface, sử dụng: python web_app.py")
        print("=" * 60)
        
    except Exception as e:
        print(f"❌ Lỗi: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    demo()

