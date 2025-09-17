#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test Final - Kiểm tra tất cả tính năng của tool
"""

import subprocess
import time
import requests
import json

def test_quick_start():
    """Test Quick Start app"""
    print("🧪 Testing Quick Start...")
    
    try:
        # Khởi động server
        process = subprocess.Popen(['python', 'quick_start.py'], 
                                 stdout=subprocess.PIPE, 
                                 stderr=subprocess.PIPE)
        
        # Đợi server khởi động
        time.sleep(3)
        
        # Test API
        try:
            response = requests.get('http://localhost:5000/api/soi-cau', timeout=5)
            if response.status_code == 200:
                data = response.json()
                print("✅ Quick Start API hoạt động!")
                print(f"   Lô chắc chắn: {data['lo_chac_chan']}")
                print(f"   Cặp xuyên chắc chắn: {data['cap_xuyen_chac_chan']}")
                print(f"   Độ tin cậy: {data['confidence']}%")
                return True
            else:
                print("❌ Quick Start API lỗi!")
                return False
        except:
            print("❌ Không thể kết nối đến Quick Start API!")
            return False
        finally:
            # Tắt server
            process.terminate()
            
    except Exception as e:
        print(f"❌ Lỗi test Quick Start: {e}")
        return False

def test_demo_console():
    """Test demo console"""
    print("\n🧪 Testing Demo Console...")
    
    try:
        # Test demo_chac_chan.py
        result = subprocess.run(['python', 'demo_chac_chan.py'], 
                              input='1\n', 
                              text=True, 
                              capture_output=True, 
                              timeout=10)
        
        if result.returncode == 0:
            print("✅ Demo Console hoạt động!")
            return True
        else:
            print("❌ Demo Console lỗi!")
            return False
            
    except Exception as e:
        print(f"❌ Lỗi test Demo Console: {e}")
        return False

def test_file_structure():
    """Test cấu trúc file"""
    print("\n🧪 Testing File Structure...")
    
    required_files = [
        'quick_start.py',
        'simple_app.py', 
        'web_app.py',
        'demo_chac_chan.py',
        'demo_by_date.py',
        'run.bat',
        'requirements.txt',
        'README.md',
        'CHAY_NGAY.md',
        'TONG_KET.md'
    ]
    
    missing_files = []
    for file in required_files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                pass
        except FileNotFoundError:
            missing_files.append(file)
    
    if not missing_files:
        print("✅ Tất cả file cần thiết đã có!")
        return True
    else:
        print(f"❌ Thiếu file: {missing_files}")
        return False

def main():
    """Main test function"""
    print("=" * 60)
    print("🧪 TEST FINAL - Tool Soi Cầu Chắc Chắn")
    print("=" * 60)
    
    tests = [
        ("File Structure", test_file_structure),
        ("Demo Console", test_demo_console),
        ("Quick Start", test_quick_start)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n🔍 Running {test_name}...")
        result = test_func()
        results.append((test_name, result))
    
    # Tổng kết
    print("\n" + "=" * 60)
    print("📊 KẾT QUẢ TEST")
    print("=" * 60)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\nTổng kết: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 TẤT CẢ TEST ĐỀU PASS!")
        print("✅ Tool đã sẵn sàng sử dụng!")
        print("\n🚀 Cách chạy:")
        print("   python quick_start.py")
        print("   Truy cập: http://localhost:5000")
        print("   Nhấn: 'SOI CẦU NGAY'")
    else:
        print(f"\n⚠️ Có {total - passed} test failed!")
        print("🔧 Cần kiểm tra lại các tính năng.")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
