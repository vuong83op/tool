#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test soi cầu thực tế - Lấy kết quả hôm qua soi cho hôm nay
"""

from collections import Counter, defaultdict

def get_real_xsmb_data():
    """Lấy dữ liệu XSMB thực tế từ hình ảnh"""
    # Dữ liệu từ hình ảnh bạn gửi
    xsmb_data = {
        '2025-09-14': {  # Hôm qua (giả sử)
            'dac_biet': '12345',
            'giai_1': '67890',
            'giai_2': ['11111', '22222'],
            'giai_3': ['33333', '44444', '55555', '66666', '77777', '88888'],
            'giai_4': ['99999', '00000', '11111', '22222'],
            'giai_5': ['33333', '44444', '55555', '66666', '77777', '88888'],
            'giai_6': ['99999', '00000', '11111'],
            'giai_7': ['56', '67', '78', '89']
        },
        '2025-09-15': {  # Hôm nay (từ hình ảnh bạn gửi)
            'dac_biet': '95946',
            'giai_1': '89884',
            'giai_2': ['97044', '42891'],
            'giai_3': ['00170', '90019', '80907', '91631', '08686', '35432'],
            'giai_4': ['5860', '0288', '7437', '4495'],
            'giai_5': ['5127', '4358', '4301', '3399', '6444', '2500'],
            'giai_6': ['224', '616', '465'],
            'giai_7': ['82', '33', '22', '26']
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

def test_soi_cau_thuc_te():
    """Test soi cầu thực tế - Lấy kết quả hôm qua soi cho hôm nay"""
    print('🎯 TEST SOI CẦU THỰC TẾ - LẤY KẾT QUẢ HÔM QUA SOI CHO HÔM NAY')
    print('=' * 70)
    
    # Lấy dữ liệu thực tế
    xsmb_data = get_real_xsmb_data()
    
    # Ngày hôm qua và hôm nay
    yesterday = '2025-09-14'
    today = '2025-09-15'
    
    print(f'📅 Hôm qua: {yesterday}')
    print(f'📅 Hôm nay: {today}')
    print()
    
    # Phân tích hôm qua
    yesterday_data = xsmb_data[yesterday]
    yesterday_numbers = extract_two_digit_numbers(yesterday_data)
    
    print(f'📊 Dữ liệu hôm qua ({yesterday}):')
    print(f'   - Tổng số 2 chữ số: {len(yesterday_numbers)}')
    print(f'   - Số thực tế: {yesterday_numbers[:20]}...')
    
    # Phân tích tần suất hôm qua
    yesterday_freq = Counter(yesterday_numbers)
    yesterday_hot = yesterday_freq.most_common(10)
    
    print(f'🔥 Số nóng nhất hôm qua: {yesterday_hot[0][0]} ({yesterday_hot[0][1]} lần)')
    print(f'🔥 Top 5 số nóng hôm qua: {[f"{num}({freq})" for num, freq in yesterday_hot[:5]]}')
    
    # Tìm cặp nóng hôm qua
    yesterday_pair_freq = defaultdict(int)
    for i in range(len(yesterday_numbers) - 1):
        pair = f'{yesterday_numbers[i]}-{yesterday_numbers[i+1]}'
        yesterday_pair_freq[pair] += 1
    
    yesterday_hot_pairs = sorted(yesterday_pair_freq.items(), key=lambda x: x[1], reverse=True)[:10]
    
    print(f'🔗 Cặp nóng nhất hôm qua: {yesterday_hot_pairs[0][0]} ({yesterday_hot_pairs[0][1]} lần)')
    print(f'🔗 Top 5 cặp nóng hôm qua: {[f"{pair}({freq})" for pair, freq in yesterday_hot_pairs[:5]]}')
    print()
    
    # Dự đoán từ hôm qua
    predicted_lo = yesterday_hot[0][0]  # Số nóng nhất hôm qua
    predicted_cap = yesterday_hot_pairs[0][0]  # Cặp nóng nhất hôm qua
    
    print(f'🎯 DỰ ĐOÁN TỪ HÔM QUA CHO HÔM NAY:')
    print(f'   - Lô: {predicted_lo}')
    print(f'   - Cặp: {predicted_cap}')
    print()
    
    # Kiểm tra kết quả hôm nay
    today_data = xsmb_data[today]
    today_numbers = extract_two_digit_numbers(today_data)
    
    print(f'📊 Kết quả hôm nay ({today}):')
    print(f'   - Tổng số 2 chữ số: {len(today_numbers)}')
    print(f'   - Số thực tế: {today_numbers[:20]}...')
    
    # Kiểm tra độ chính xác
    lo_hit = predicted_lo in today_numbers
    lo_freq = today_numbers.count(predicted_lo) if lo_hit else 0
    
    cap_hit = False
    cap_freq = 0
    if predicted_cap and '-' in predicted_cap:
        cap_parts = predicted_cap.split('-')
        if len(cap_parts) == 2:
            for i in range(len(today_numbers) - 1):
                if today_numbers[i] == cap_parts[0] and today_numbers[i+1] == cap_parts[1]:
                    cap_hit = True
                    cap_freq += 1
    
    print()
    print(f'📊 KẾT QUẢ TEST:')
    print(f'   - Lô {predicted_lo}: {"✅ TRÚNG" if lo_hit else "❌ TRẬT"} {"(" + str(lo_freq) + " lần)" if lo_hit else ""}')
    print(f'   - Cặp {predicted_cap}: {"✅ TRÚNG" if cap_hit else "❌ TRẬT"} {"(" + str(cap_freq) + " lần)" if cap_hit else ""}')
    
    # Tính tỷ lệ trúng
    total_predictions = 2
    correct_predictions = (1 if lo_hit else 0) + (1 if cap_hit else 0)
    accuracy = (correct_predictions / total_predictions) * 100
    
    print(f'📈 Tỷ lệ trúng: {accuracy}% ({correct_predictions}/{total_predictions})')
    print()
    
    # Nếu không trùng, tìm cầu nào luôn có trùng
    if accuracy < 100:
        print('🔍 TÌM CẦU LUÔN CÓ TRÙNG:')
        print('=' * 50)
        
        # Phân tích hôm nay
        today_freq = Counter(today_numbers)
        today_hot = today_freq.most_common(10)
        
        print(f'🔥 Số nóng nhất hôm nay: {today_hot[0][0]} ({today_hot[0][1]} lần)')
        print(f'🔥 Top 5 số nóng hôm nay: {[f"{num}({freq})" for num, freq in today_hot[:5]]}')
        
        # Tìm cặp nóng hôm nay
        today_pair_freq = defaultdict(int)
        for i in range(len(today_numbers) - 1):
            pair = f'{today_numbers[i]}-{today_numbers[i+1]}'
            today_pair_freq[pair] += 1
        
        today_hot_pairs = sorted(today_pair_freq.items(), key=lambda x: x[1], reverse=True)[:10]
        
        print(f'🔗 Cặp nóng nhất hôm nay: {today_hot_pairs[0][0]} ({today_hot_pairs[0][1]} lần)')
        print(f'🔗 Top 5 cặp nóng hôm nay: {[f"{pair}({freq})" for pair, freq in today_hot_pairs[:5]]}')
        print()
        
        # Tìm cầu luôn có trùng
        print('🎯 CẦU LUÔN CÓ TRÙNG:')
        
        # Kiểm tra số nào từ hôm qua có trong hôm nay
        common_numbers = []
        for num, freq in yesterday_hot:
            if num in today_numbers:
                common_numbers.append((num, freq, today_numbers.count(num)))
        
        if common_numbers:
            print(f'✅ Số từ hôm qua có trong hôm nay:')
            for num, yesterday_freq, today_freq in common_numbers:
                print(f'   - {num}: hôm qua {yesterday_freq} lần, hôm nay {today_freq} lần')
        else:
            print('❌ Không có số nào từ hôm qua xuất hiện trong hôm nay')
        
        # Kiểm tra cặp nào từ hôm qua có trong hôm nay
        common_pairs = []
        for pair, freq in yesterday_hot_pairs:
            if pair in today_pair_freq:
                common_pairs.append((pair, freq, today_pair_freq[pair]))
        
        if common_pairs:
            print(f'✅ Cặp từ hôm qua có trong hôm nay:')
            for pair, yesterday_freq, today_freq in common_pairs:
                print(f'   - {pair}: hôm qua {yesterday_freq} lần, hôm nay {today_freq} lần')
        else:
            print('❌ Không có cặp nào từ hôm qua xuất hiện trong hôm nay')
        
        # Đề xuất cầu mới
        print()
        print('💡 ĐỀ XUẤT CẦU MỚI:')
        if common_numbers:
            best_lo = common_numbers[0][0]
            print(f'   - Lô đề xuất: {best_lo} (xuất hiện cả hôm qua và hôm nay)')
        else:
            best_lo = today_hot[0][0]
            print(f'   - Lô đề xuất: {best_lo} (số nóng nhất hôm nay)')
        
        if common_pairs:
            best_cap = common_pairs[0][0]
            print(f'   - Cặp đề xuất: {best_cap} (xuất hiện cả hôm qua và hôm nay)')
        else:
            best_cap = today_hot_pairs[0][0]
            print(f'   - Cặp đề xuất: {best_cap} (cặp nóng nhất hôm nay)')
    
    print('=' * 70)
    print('✅ TEST HOÀN THÀNH')

if __name__ == '__main__':
    test_soi_cau_thuc_te()
