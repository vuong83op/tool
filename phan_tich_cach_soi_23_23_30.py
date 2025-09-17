#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phân tích cách thức tool soi ra lô 23 và cặp 23-30
Từ ngày 16/09/2025 cho ngày 17/09/2025
"""

from collections import Counter, defaultdict

def get_xsmb_data_16_09():
    """Dữ liệu XSMB ngày 16/09/2025 (từ hình ảnh bạn gửi)"""
    return {
        'dac_biet': '17705',
        'giai_1': '13036',
        'giai_2': ['76900', '78768'],
        'giai_3': ['73396', '16527', '26221', '86471', '47830', '63620'],
        'giai_4': ['7391', '8287', '4952', '3145'],
        'giai_5': ['1770', '7526', '8472', '3722', '1192', '0925'],
        'giai_6': ['479', '389', '851'],
        'giai_7': ['12', '29', '11', '33']
    }

def extract_two_digit_numbers(data):
    """Trích xuất tất cả số 2 chữ số từ dữ liệu XSMB"""
    two_digit_numbers = []
    
    # Từ giải đặc biệt
    if 'dac_biet' in data:
        db = data['dac_biet']
        two_digit_numbers.extend([db[:2], db[1:3], db[2:4], db[3:5]])
    
    # Từ các giải khác
    for giai in ['giai_1', 'giai_2', 'giai_3', 'giai_4', 'giai_5', 'giai_6']:
        if giai in data:
            if isinstance(data[giai], list):
                for num in data[giai]:
                    if len(num) >= 2:
                        two_digit_numbers.extend([num[:2], num[1:3]] if len(num) > 2 else [num])
            else:
                num = data[giai]
                if len(num) >= 2:
                    two_digit_numbers.extend([num[:2], num[1:3]] if len(num) > 2 else [num])
    
    # Từ giải 7 (đã là 2 chữ số)
    if 'giai_7' in data:
        two_digit_numbers.extend(data['giai_7'])
    
    return two_digit_numbers

def analyze_prediction_method():
    """Phân tích cách thức dự đoán lô 23 và cặp 23-30"""
    print('🎯 PHÂN TÍCH CÁCH THỨC SOI RA LÔ 23 VÀ CẶP 23-30')
    print('=' * 60)
    print('📅 Từ ngày 16/09/2025 → Ngày 17/09/2025')
    print('🎯 Kết quả: Lô 23, Cặp 23-30')
    print()
    
    # Lấy dữ liệu ngày 16/09
    data_16_09 = get_xsmb_data_16_09()
    numbers_16_09 = extract_two_digit_numbers(data_16_09)
    
    print(f'📊 Dữ liệu ngày 16/09/2025:')
    print(f'   - Tổng số 2 chữ số: {len(numbers_16_09)}')
    print(f'   - Các số: {numbers_16_09[:20]}...')
    print()
    
    # Phân tích tần suất số
    number_freq = Counter(numbers_16_09)
    print('📈 TẦN SUẤT CÁC SỐ:')
    for num, freq in number_freq.most_common(10):
        print(f'   - {num}: {freq} lần')
    print()
    
    # Kiểm tra số 23
    print('🔍 KIỂM TRA SỐ 23:')
    if '23' in number_freq:
        print(f'   ✅ Số 23 xuất hiện {number_freq["23"]} lần trong dữ liệu ngày 16/09')
    else:
        print('   ❌ Số 23 KHÔNG xuất hiện trong dữ liệu ngày 16/09')
    print()
    
    # Phân tích cặp
    print('🔍 PHÂN TÍCH CẶP 23-30:')
    pair_freq = defaultdict(int)
    for i in range(len(numbers_16_09) - 1):
        pair = f'{numbers_16_09[i]}-{numbers_16_09[i+1]}'
        pair_freq[pair] += 1
    
    if '23-30' in pair_freq:
        print(f'   ✅ Cặp 23-30 xuất hiện {pair_freq["23-30"]} lần trong dữ liệu ngày 16/09')
    else:
        print('   ❌ Cặp 23-30 KHÔNG xuất hiện trong dữ liệu ngày 16/09')
    
    print('   📊 Các cặp nóng nhất:')
    for pair, freq in sorted(pair_freq.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f'      - {pair}: {freq} lần')
    print()
    
    # Phân tích từ giải 7
    print('🔍 PHÂN TÍCH TỪ GIẢI 7:')
    giai_7_numbers = data_16_09['giai_7']
    print(f'   - Giải 7: {giai_7_numbers}')
    
    giai_7_freq = Counter(giai_7_numbers)
    hot_giai_7 = giai_7_freq.most_common(1)[0]
    print(f'   - Số nóng nhất giải 7: {hot_giai_7[0]} ({hot_giai_7[1]} lần)')
    
    if hot_giai_7[0] == '23':
        print('   ✅ Số 23 là số nóng nhất từ giải 7!')
    else:
        print(f'   ❌ Số 23 KHÔNG phải số nóng nhất từ giải 7 (số nóng nhất: {hot_giai_7[0]})')
    print()
    
    # Phân tích từ giải đặc biệt
    print('🔍 PHÂN TÍCH TỪ GIẢI ĐẶC BIỆT:')
    db = data_16_09['dac_biet']
    db_numbers = [db[:2], db[1:3], db[2:4], db[3:5]]
    print(f'   - Giải đặc biệt: {db}')
    print(f'   - Các số 2 chữ số: {db_numbers}')
    
    if '23' in db_numbers:
        print('   ✅ Số 23 có trong giải đặc biệt!')
    else:
        print('   ❌ Số 23 KHÔNG có trong giải đặc biệt')
    print()
    
    # Tìm pattern khác
    print('🔍 TÌM PATTERN KHÁC:')
    
    # Pattern 1: Số từ giải 1
    giai_1 = data_16_09['giai_1']
    giai_1_numbers = [giai_1[:2], giai_1[1:3], giai_1[2:4], giai_1[3:5]]
    print(f'   - Giải 1: {giai_1} → {giai_1_numbers}')
    
    if '23' in giai_1_numbers:
        print('   ✅ Số 23 có trong giải 1!')
    else:
        print('   ❌ Số 23 KHÔNG có trong giải 1')
    
    # Pattern 2: Số từ giải 2
    giai_2_numbers = []
    for num in data_16_09['giai_2']:
        giai_2_numbers.extend([num[:2], num[1:3], num[2:4], num[3:5]])
    print(f'   - Giải 2: {data_16_09["giai_2"]} → {giai_2_numbers}')
    
    if '23' in giai_2_numbers:
        print('   ✅ Số 23 có trong giải 2!')
    else:
        print('   ❌ Số 23 KHÔNG có trong giải 2')
    
    # Pattern 3: Số từ giải 3
    giai_3_numbers = []
    for num in data_16_09['giai_3']:
        giai_3_numbers.extend([num[:2], num[1:3], num[2:4], num[3:5]])
    print(f'   - Giải 3: {data_16_09["giai_3"]} → {giai_3_numbers[:10]}...')
    
    if '23' in giai_3_numbers:
        print('   ✅ Số 23 có trong giải 3!')
    else:
        print('   ❌ Số 23 KHÔNG có trong giải 3')
    print()
    
    # Kết luận
    print('🎯 KẾT LUẬN VỀ CÁCH THỨC SOI:')
    print('=' * 60)
    
    # Kiểm tra tất cả các nguồn
    all_sources = []
    
    if '23' in giai_7_numbers:
        all_sources.append('Giải 7')
    if '23' in db_numbers:
        all_sources.append('Giải đặc biệt')
    if '23' in giai_1_numbers:
        all_sources.append('Giải 1')
    if '23' in giai_2_numbers:
        all_sources.append('Giải 2')
    if '23' in giai_3_numbers:
        all_sources.append('Giải 3')
    
    if all_sources:
        print(f'✅ Số 23 xuất hiện từ: {", ".join(all_sources)}')
    else:
        print('❌ Số 23 KHÔNG xuất hiện từ bất kỳ nguồn nào trong dữ liệu ngày 16/09')
    
    # Phân tích cặp 23-30
    if '23-30' in pair_freq:
        print(f'✅ Cặp 23-30 xuất hiện {pair_freq["23-30"]} lần trong dữ liệu ngày 16/09')
    else:
        print('❌ Cặp 23-30 KHÔNG xuất hiện trong dữ liệu ngày 16/09')
    
    print()
    print('💡 CÁCH THỨC SOI CÓ THỂ LÀ:')
    print('   1. Tool sử dụng thuật toán khác không dựa trên dữ liệu ngày 16/09')
    print('   2. Tool sử dụng dữ liệu từ nhiều ngày trước đó')
    print('   3. Tool sử dụng pattern đặc biệt hoặc thuật toán machine learning')
    print('   4. Tool sử dụng dữ liệu từ nguồn khác (không phải từ hình ảnh)')
    
    return {
        'lo_23_sources': all_sources,
        'cap_23_30_freq': pair_freq.get('23-30', 0),
        'number_23_freq': number_freq.get('23', 0)
    }

def main():
    """Chạy phân tích cách thức soi"""
    print('🎯 PHÂN TÍCH CÁCH THỨC TOOL SOI RA LÔ 23 VÀ CẶP 23-30')
    print('=' * 80)
    print('📅 Từ ngày 16/09/2025 → Ngày 17/09/2025')
    print('🎯 Kết quả: Lô 23, Cặp 23-30')
    print('=' * 80)
    
    result = analyze_prediction_method()
    
    print('\n' + '=' * 80)
    print('✅ PHÂN TÍCH HOÀN THÀNH')
    print(f'📊 Kết quả: Số 23 từ {len(result["lo_23_sources"])} nguồn, Cặp 23-30 xuất hiện {result["cap_23_30_freq"]} lần')

if __name__ == '__main__':
    main()
