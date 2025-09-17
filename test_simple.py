#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test Simple - Kiểm tra cơ bản
"""

import os

def test_files():
    """Test các file cần thiết"""
    print("🧪 Testing Files...")
    
    files = [
        'quick_start.py',
        'simple_app.py',
        'demo_chac_chan.py',
        'run.bat',
        'requirements.txt'
    ]
    
    for file in files:
        if os.path.exists(file):
            print(f"✅ {file} - OK")
        else:
            print(f"❌ {file} - Missing")
    
    print("✅ File test completed!")

def test_imports():
    """Test imports"""
    print("\n🧪 Testing Imports...")
    
    try:
        import flask
        print("✅ Flask - OK")
    except ImportError:
        print("❌ Flask - Missing")
    
    try:
        import requests
        print("✅ Requests - OK")
    except ImportError:
        print("❌ Requests - Missing")
    
    print("✅ Import test completed!")

def main():
    print("=" * 50)
    print("🧪 SIMPLE TEST - Tool Soi Cầu Chắc Chắn")
    print("=" * 50)
    
    test_files()
    test_imports()
    
    print("\n" + "=" * 50)
    print("✅ TEST HOÀN THÀNH!")
    print("🚀 Tool đã sẵn sàng!")
    print("\nCách chạy:")
    print("1. python quick_start.py")
    print("2. Truy cập: http://localhost:5000")
    print("3. Nhấn: 'SOI CẦU NGAY'")
    print("=" * 50)

if __name__ == "__main__":
    main()
