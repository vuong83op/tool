#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test cầu tổng quát - Kiểm tra thuật toán áp dụng cho tất cả các ngày
"""

def test_cau_tong_quat():
    """Test cầu tổng quát với nhiều ngày khác nhau"""
    print("=" * 70)
    print("🎯 TEST CẦU TỔNG QUÁT - ÁP DỤNG CHO TẤT CẢ CÁC NGÀY")
    print("=" * 70)
    
    # Dữ liệu mẫu cho nhiều ngày khác nhau
    test_days = {
        '2025-09-14': {
            'dac_biet': '95594',
            'giai_1': '46898',
            'giai_2': ['97704', '22800'],
            'giai_3': ['01900', '80091', '60886', '43343', '56656', '78878'],
            'giai_4': ['9999', '0000', '1111', '2222'],
            'giai_5': ['3333', '4444', '5555', '6666', '7777', '8888'],
            'giai_6': ['999', '000', '111'],
            'giai_7': ['43', '28', '16', '00']
        },
        '2025-09-15': {
            'dac_biet': '17705',
            'giai_1': '13036',
            'giai_2': ['76900', '78768'],
            'giai_3': ['73396', '16527', '26221', '86471', '47830', '63620'],
            'giai_4': ['7391', '8287', '4952', '3145'],
            'giai_5': ['1770', '7526', '8472', '3722', '1192', '0925'],
            'giai_6': ['479', '389', '851'],
            'giai_7': ['12', '29', '11', '33']
        },
        '2025-09-16': {
            'dac_biet': '17705',
            'giai_1': '13036',
            'giai_2': ['76900', '78768'],
            'giai_3': ['73396', '16527', '26221', '86471', '47830', '63620'],
            'giai_4': ['7391', '8287', '4952', '3145'],
            'giai_5': ['1770', '7526', '8472', '3722', '1192', '0925'],
            'giai_6': ['479', '389', '851'],
            'giai_7': ['12', '29', '11', '33']
        }
    }
    
    def extract_two_digit_numbers(data):
        """Trích xuất tất cả số 2 chữ số từ dữ liệu XSMB"""
        two_digit_numbers = []
        
        # Từ giải đặc biệt
        db = data['dac_biet']
        two_digit_numbers.extend([db[:2], db[1:3], db[2:4], db[3:5]])
        
        # Từ các giải khác
        for giai in ['giai_1', 'giai_2', 'giai_3', 'giai_4', 'giai_5', 'giai_6']:
            if isinstance(data[giai], list):
                for num in data[giai]:
                    if len(num) >= 2:
                        two_digit_numbers.extend([num[:2], num[1:3]] if len(num) > 2 else [num])
            else:
                num = data[giai]
                if len(num) >= 2:
                    two_digit_numbers.extend([num[:2], num[1:3]] if len(num) > 2 else [num])
        
        # Từ giải 7 (đã là 2 chữ số)
        two_digit_numbers.extend(data['giai_7'])
        
        return two_digit_numbers
    
    def apply_universal_pattern(source_data, source_date, target_date):
        """Áp dụng cầu tổng quát"""
        from collections import Counter
        
        # 1. Trích xuất số 2 chữ số
        numbers = extract_two_digit_numbers(source_data)
        
        # 2. Đếm tần suất
        freq = Counter(numbers)
        
        # 3. Tìm số nóng nhất từ giải 7 (ưu tiên cao nhất)
        giai_7_numbers = source_data.get('giai_7', [])
        best_lo = None
        best_lo_freq = 0
        
        if giai_7_numbers:
            giai_7_freq = Counter(giai_7_numbers)
            best_giai_7 = giai_7_freq.most_common(1)[0]
            best_lo = best_giai_7[0]
            best_lo_freq = best_giai_7[1]
        
        # 4. Nếu không có giải 7, lấy số nóng nhất tổng thể
        if not best_lo:
            hot_numbers = freq.most_common(10)
            if hot_numbers:
                best_lo = hot_numbers[0][0]
                best_lo_freq = hot_numbers[0][1]
        
        # 5. Tìm cặp nóng nhất
        pair_freq = Counter()
        for i in range(len(numbers) - 1):
            pair = f"{numbers[i]}-{numbers[i+1]}"
            pair_freq[pair] += 1
        
        best_pair = None
        best_pair_freq = 0
        if pair_freq:
            best_pair_data = pair_freq.most_common(1)[0]
            best_pair = best_pair_data[0]
            best_pair_freq = best_pair_data[1]
        
        # 6. Nếu không có cặp, tạo cặp từ số nóng nhất
        if not best_pair and best_lo:
            best_pair = f"{best_lo}-{str(int(best_lo) + 1).zfill(2)}"
            best_pair_freq = 1
        
        # 7. Đảm bảo có kết quả mặc định
        if not best_lo:
            best_lo = "23"
            best_lo_freq = 4
        
        if not best_pair:
            best_pair = "23-30"
            best_pair_freq = 2
        
        return {
            'source_date': source_date,
            'target_date': target_date,
            'lo': best_lo,
            'lo_freq': best_lo_freq,
            'pair': best_pair,
            'pair_freq': best_pair_freq,
            'method': 'universal_pattern'
        }
    
    # Test với từng ngày
    results = []
    for source_date, source_data in test_days.items():
        target_date = source_date  # Giả sử soi cho cùng ngày để test
        
        result = apply_universal_pattern(source_data, source_date, target_date)
        results.append(result)
        
        print(f"📅 NGÀY {source_date}:")
        print(f"   Giải 7: {source_data['giai_7']}")
        print(f"   Dự đoán Lô: {result['lo']} ({result['lo_freq']} lần)")
        print(f"   Dự đoán Cặp: {result['pair']} ({result['pair_freq']} lần)")
        print()
    
    # Thống kê tổng thể
    print("📊 THỐNG KÊ TỔNG THỂ:")
    print(f"   Tổng số ngày test: {len(results)}")
    
    # Đếm số lần xuất hiện của từng số
    lo_counts = {}
    pair_counts = {}
    
    for result in results:
        lo = result['lo']
        pair = result['pair']
        
        lo_counts[lo] = lo_counts.get(lo, 0) + 1
        pair_counts[pair] = pair_counts.get(pair, 0) + 1
    
    print("\n🔥 SỐ LÔ XUẤT HIỆN NHIỀU NHẤT:")
    for lo, count in sorted(lo_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"   {lo}: {count} lần")
    
    print("\n🔗 CẶP XUYÊN XUẤT HIỆN NHIỀU NHẤT:")
    for pair, count in sorted(pair_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"   {pair}: {count} lần")
    
    # Đánh giá tính nhất quán
    most_common_lo = max(lo_counts.items(), key=lambda x: x[1])
    most_common_pair = max(pair_counts.items(), key=lambda x: x[1])
    
    print(f"\n✅ CẦU TỔNG QUÁT NHẤT QUÁN:")
    print(f"   Lô phổ biến nhất: {most_common_lo[0]} ({most_common_lo[1]}/{len(results)} ngày)")
    print(f"   Cặp phổ biến nhất: {most_common_pair[0]} ({most_common_pair[1]}/{len(results)} ngày)")
    
    consistency_score = (most_common_lo[1] + most_common_pair[1]) / (2 * len(results)) * 100
    print(f"   Điểm nhất quán: {consistency_score:.1f}%")
    
    if consistency_score >= 80:
        print("🎉 XUẤT SẮC! Cầu tổng quát rất nhất quán!")
    elif consistency_score >= 60:
        print("👍 TỐT! Cầu tổng quát khá nhất quán!")
    else:
        print("⚠️ CẦN CẢI THIỆN! Cầu tổng quát cần tối ưu hóa!")
    
    print("=" * 70)

if __name__ == "__main__":
    test_cau_tong_quat()
