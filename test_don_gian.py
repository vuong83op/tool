#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test đơn giản cầu tổng quát
"""

def test_simple():
    print("🎯 TEST CẦU TỔNG QUÁT")
    print("=" * 50)
    
    # Dữ liệu mẫu
    data_16 = {
        'giai_7': ['12', '29', '11', '33']
    }
    
    data_15 = {
        'giai_7': ['12', '29', '11', '33']
    }
    
    data_14 = {
        'giai_7': ['43', '28', '16', '00']
    }
    
    from collections import Counter
    
    # Test với ngày 16/09
    freq_16 = Counter(data_16['giai_7'])
    best_16 = freq_16.most_common(1)[0]
    print(f"📅 Ngày 16/09: Lô {best_16[0]} ({best_16[1]} lần)")
    
    # Test với ngày 15/09
    freq_15 = Counter(data_15['giai_7'])
    best_15 = freq_15.most_common(1)[0]
    print(f"📅 Ngày 15/09: Lô {best_15[0]} ({best_15[1]} lần)")
    
    # Test với ngày 14/09
    freq_14 = Counter(data_14['giai_7'])
    best_14 = freq_14.most_common(1)[0]
    print(f"📅 Ngày 14/09: Lô {best_14[0]} ({best_14[1]} lần)")
    
    print("\n✅ CẦU TỔNG QUÁT:")
    print("   - Ưu tiên số nóng nhất từ giải 7")
    print("   - Áp dụng cho tất cả các ngày")
    print("   - Đảm bảo có kết quả mặc định")
    
    print("=" * 50)

if __name__ == "__main__":
    test_simple()
