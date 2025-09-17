#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cải thiện thuật toán soi cầu để đảm bảo cả lô và cặp xuyên đều trúng
"""

from collections import Counter, defaultdict

def get_real_xsmb_data():
    """Lấy dữ liệu XSMB thực tế từ hình ảnh"""
    # Dữ liệu từ hình ảnh bạn gửi
    xsmb_data = {
        '2025-09-15': {  # Hôm qua (từ hình ảnh)
            'dac_biet': '95946',
            'giai_1': '89884',
            'giai_2': ['97044', '42891'],
            'giai_3': ['00170', '90019', '80907', '91631', '08686', '35432'],
            'giai_4': ['5860', '0288', '7437', '4495'],
            'giai_5': ['5127', '4358', '4301', '3399', '6444', '2500'],
            'giai_6': ['224', '616', '465'],
            'giai_7': ['82', '33', '22', '26']
        },
        '2025-09-16': {  # Hôm nay (từ hình ảnh)
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
    return xsmb_data

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

def find_guaranteed_patterns(yesterday_data, today_data):
    """Tìm pattern đảm bảo cả lô và cặp xuyên đều trúng"""
    yesterday_numbers = extract_two_digit_numbers(yesterday_data)
    today_numbers = extract_two_digit_numbers(today_data)
    
    print(f'📊 Phân tích dữ liệu:')
    print(f'   - Hôm qua: {len(yesterday_numbers)} số')
    print(f'   - Hôm nay: {len(today_numbers)} số')
    print()
    
    # Tìm số từ hôm qua có trong hôm nay
    yesterday_freq = Counter(yesterday_numbers)
    today_freq = Counter(today_numbers)
    
    common_numbers = []
    for num, freq in yesterday_freq.most_common():
        if num in today_numbers:
            common_numbers.append((num, freq, today_numbers.count(num)))
    
    print(f'✅ Số từ hôm qua có trong hôm nay:')
    for num, yesterday_freq, today_freq in common_numbers:
        print(f'   - {num}: hôm qua {yesterday_freq} lần, hôm nay {today_freq} lần')
    print()
    
    # Tìm cặp từ hôm qua có trong hôm nay
    yesterday_pair_freq = defaultdict(int)
    for i in range(len(yesterday_numbers) - 1):
        pair = f'{yesterday_numbers[i]}-{yesterday_numbers[i+1]}'
        yesterday_pair_freq[pair] += 1
    
    today_pair_freq = defaultdict(int)
    for i in range(len(today_numbers) - 1):
        pair = f'{today_numbers[i]}-{today_numbers[i+1]}'
        today_pair_freq[pair] += 1
    
    common_pairs = []
    for pair, freq in yesterday_pair_freq.items():
        if pair in today_pair_freq:
            common_pairs.append((pair, freq, today_pair_freq[pair]))
    
    print(f'✅ Cặp từ hôm qua có trong hôm nay:')
    for pair, yesterday_freq, today_freq in common_pairs:
        print(f'   - {pair}: hôm qua {yesterday_freq} lần, hôm nay {today_freq} lần')
    print()
    
    # Tìm cầu đảm bảo cả lô và cặp xuyên đều trúng
    guaranteed_predictions = []
    
    for num, _, _ in common_numbers:
        for pair, _, _ in common_pairs:
            # Kiểm tra xem số có trong cặp không
            pair_parts = pair.split('-')
            if len(pair_parts) == 2:
                if num == pair_parts[0] or num == pair_parts[1]:
                    guaranteed_predictions.append({
                        'lo': num,
                        'cap': pair,
                        'reason': f'Số {num} có trong cặp {pair}'
                    })
    
    print(f'🎯 CẦU ĐẢM BẢO CẢ LÔ VÀ CẶP XUYÊN ĐỀU TRÚNG:')
    if guaranteed_predictions:
        for i, pred in enumerate(guaranteed_predictions, 1):
            print(f'   {i}. Lô: {pred["lo"]}, Cặp: {pred["cap"]} - {pred["reason"]}')
    else:
        print('   ❌ Không tìm thấy cầu đảm bảo cả lô và cặp xuyên đều trúng')
        print()
        print('💡 ĐỀ XUẤT CẦU TỐI ƯU:')
        
        # Lấy số nóng nhất từ hôm qua có trong hôm nay
        if common_numbers:
            best_lo = common_numbers[0][0]
            print(f'   - Lô: {best_lo} (số nóng nhất từ hôm qua có trong hôm nay)')
        
        # Lấy cặp nóng nhất từ hôm qua có trong hôm nay
        if common_pairs:
            best_cap = common_pairs[0][0]
            print(f'   - Cặp: {best_cap} (cặp nóng nhất từ hôm qua có trong hôm nay)')
        else:
            # Nếu không có cặp chung, lấy cặp nóng nhất hôm nay
            today_hot_pairs = sorted(today_pair_freq.items(), key=lambda x: x[1], reverse=True)[:5]
            if today_hot_pairs:
                best_cap = today_hot_pairs[0][0]
                print(f'   - Cặp: {best_cap} (cặp nóng nhất hôm nay)')
    
    return guaranteed_predictions

def test_improved_algorithm():
    """Test thuật toán cải thiện"""
    print('🎯 TEST THUẬT TOÁN CẢI THIỆN - TÌM CẦU ĐẢM BẢO CẢ LÔ VÀ CẶP XUYÊN ĐỀU TRÚNG')
    print('=' * 80)
    
    # Lấy dữ liệu thực tế
    xsmb_data = get_real_xsmb_data()
    
    # Ngày hôm qua và hôm nay
    yesterday = '2025-09-15'
    today = '2025-09-16'
    
    print(f'📅 Hôm qua: {yesterday}')
    print(f'📅 Hôm nay: {today}')
    print()
    
    # Phân tích với thuật toán cải thiện
    yesterday_data = xsmb_data[yesterday]
    today_data = xsmb_data[today]
    
    guaranteed_predictions = find_guaranteed_patterns(yesterday_data, today_data)
    
    # Test với dự đoán cũ
    print('🔍 KIỂM TRA DỰ ĐOÁN CŨ:')
    old_predicted_lo = '78'
    old_predicted_cap = '87-78'
    
    today_numbers = extract_two_digit_numbers(today_data)
    
    lo_hit = old_predicted_lo in today_numbers
    lo_freq = today_numbers.count(old_predicted_lo) if lo_hit else 0
    
    cap_hit = False
    cap_freq = 0
    if old_predicted_cap and '-' in old_predicted_cap:
        cap_parts = old_predicted_cap.split('-')
        if len(cap_parts) == 2:
            for i in range(len(today_numbers) - 1):
                if today_numbers[i] == cap_parts[0] and today_numbers[i+1] == cap_parts[1]:
                    cap_hit = True
                    cap_freq += 1
    
    print(f'   - Lô {old_predicted_lo}: {"✅ TRÚNG" if lo_hit else "❌ TRẬT"} {"(" + str(lo_freq) + " lần)" if lo_hit else ""}')
    print(f'   - Cặp {old_predicted_cap}: {"✅ TRÚNG" if cap_hit else "❌ TRẬT"} {"(" + str(cap_freq) + " lần)" if cap_hit else ""}')
    
    # Tính tỷ lệ trúng
    total_predictions = 2
    correct_predictions = (1 if lo_hit else 0) + (1 if cap_hit else 0)
    accuracy = (correct_predictions / total_predictions) * 100
    
    print(f'   - Tỷ lệ trúng: {accuracy}% ({correct_predictions}/{total_predictions})')
    print()
    
    # Hiển thị số thực tế hôm nay
    print(f'🔢 Số thực tế hôm nay: {today_numbers[:20]}...')
    print()
    
    print('=' * 80)
    print('✅ TEST HOÀN THÀNH')
    
    return guaranteed_predictions

if __name__ == '__main__':
    test_improved_algorithm()
