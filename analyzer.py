#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module phân tích và tính toán cầu số xổ số miền Bắc
"""

import numpy as np
from collections import defaultdict, Counter
from datetime import datetime, timedelta
import statistics
import math

class SoiCauAnalyzer:
    """Class phân tích dữ liệu xổ số để tìm cầu số"""
    
    def __init__(self):
        self.analysis_cache = {}
        
    def analyze_data(self, data):
        """Phân tích dữ liệu xổ số"""
        if not data:
            return {}
        
        analysis = {
            'basic_stats': self._calculate_basic_stats(data),
            'number_frequency': self._analyze_number_frequency(data),
            'pair_analysis': self._analyze_pairs(data),
            'pattern_analysis': self._analyze_patterns(data),
            'trend_analysis': self._analyze_trends(data),
            'cycle_analysis': self._analyze_cycles(data),
            'correlation_analysis': self._analyze_correlations(data)
        }
        
        return analysis
    
    def _calculate_basic_stats(self, data):
        """Tính toán thống kê cơ bản"""
        stats = {
            'total_days': len(data),
            'date_range': {
                'start': data[0]['date'],
                'end': data[-1]['date']
            },
            'avg_gdb': 0,
            'std_gdb': 0,
            'min_gdb': 99999,
            'max_gdb': 0
        }
        
        gdb_values = []
        for result in data:
            gdb = int(result['giai_dac_biet'])
            gdb_values.append(gdb)
            stats['min_gdb'] = min(stats['min_gdb'], gdb)
            stats['max_gdb'] = max(stats['max_gdb'], gdb)
        
        if gdb_values:
            stats['avg_gdb'] = statistics.mean(gdb_values)
            stats['std_gdb'] = statistics.stdev(gdb_values) if len(gdb_values) > 1 else 0
        
        return stats
    
    def _analyze_number_frequency(self, data):
        """Phân tích tần suất xuất hiện của các số"""
        frequency = defaultdict(int)
        last_digits = defaultdict(int)
        first_digits = defaultdict(int)
        
        for result in data:
            gdb = result['giai_dac_biet']
            
            # Đếm từng chữ số
            for digit in gdb:
                frequency[digit] += 1
            
            # Đếm 2 số cuối
            if len(gdb) >= 2:
                last_two = gdb[-2:]
                last_digits[last_two] += 1
            
            # Đếm 2 số đầu
            if len(gdb) >= 2:
                first_two = gdb[:2]
                first_digits[first_two] += 1
        
        return {
            'digit_frequency': dict(frequency),
            'last_two_frequency': dict(last_digits),
            'first_two_frequency': dict(first_digits),
            'hot_numbers': self._get_hot_numbers(frequency),
            'cold_numbers': self._get_cold_numbers(frequency)
        }
    
    def _analyze_pairs(self, data):
        """Phân tích các cặp số"""
        pair_frequency = defaultdict(int)
        consecutive_pairs = defaultdict(int)
        
        for result in data:
            gdb = result['giai_dac_biet']
            
            # Phân tích cặp số liền kề
            for i in range(len(gdb) - 1):
                pair = gdb[i:i+2]
                pair_frequency[pair] += 1
            
            # Phân tích cặp số cách nhau 1 vị trí
            for i in range(len(gdb) - 2):
                pair = gdb[i] + gdb[i+2]
                consecutive_pairs[pair] += 1
        
        return {
            'adjacent_pairs': dict(pair_frequency),
            'consecutive_pairs': dict(consecutive_pairs),
            'hot_pairs': self._get_hot_pairs(pair_frequency),
            'cold_pairs': self._get_cold_pairs(pair_frequency)
        }
    
    def _analyze_patterns(self, data):
        """Phân tích các pattern trong dữ liệu"""
        patterns = {
            'sum_patterns': self._analyze_sum_patterns(data),
            'parity_patterns': self._analyze_parity_patterns(data),
            'sequence_patterns': self._analyze_sequence_patterns(data),
            'repetition_patterns': self._analyze_repetition_patterns(data)
        }
        
        return patterns
    
    def _analyze_sum_patterns(self, data):
        """Phân tích pattern về tổng các chữ số"""
        sum_frequency = defaultdict(int)
        sum_last_digit = defaultdict(int)
        
        for result in data:
            gdb = result['giai_dac_biet']
            digit_sum = sum(int(d) for d in gdb)
            sum_frequency[digit_sum] += 1
            sum_last_digit[digit_sum % 10] += 1
        
        return {
            'sum_frequency': dict(sum_frequency),
            'sum_last_digit_frequency': dict(sum_last_digit)
        }
    
    def _analyze_parity_patterns(self, data):
        """Phân tích pattern về chẵn/lẻ"""
        even_count = defaultdict(int)
        odd_count = defaultdict(int)
        
        for result in data:
            gdb = result['giai_dac_biet']
            even_digits = sum(1 for d in gdb if int(d) % 2 == 0)
            odd_digits = len(gdb) - even_digits
            
            even_count[even_digits] += 1
            odd_count[odd_digits] += 1
        
        return {
            'even_digits_frequency': dict(even_count),
            'odd_digits_frequency': dict(odd_count)
        }
    
    def _analyze_sequence_patterns(self, data):
        """Phân tích pattern về dãy số"""
        ascending_count = 0
        descending_count = 0
        mixed_count = 0
        
        for result in data:
            gdb = result['giai_dac_biet']
            digits = [int(d) for d in gdb]
            
            if digits == sorted(digits):
                ascending_count += 1
            elif digits == sorted(digits, reverse=True):
                descending_count += 1
            else:
                mixed_count += 1
        
        return {
            'ascending': ascending_count,
            'descending': descending_count,
            'mixed': mixed_count
        }
    
    def _analyze_repetition_patterns(self, data):
        """Phân tích pattern về số lặp lại"""
        repetition_count = defaultdict(int)
        
        for result in data:
            gdb = result['giai_dac_biet']
            digit_count = Counter(gdb)
            max_repetition = max(digit_count.values())
            repetition_count[max_repetition] += 1
        
        return dict(repetition_count)
    
    def _analyze_trends(self, data):
        """Phân tích xu hướng"""
        trends = {
            'recent_trend': self._analyze_recent_trend(data),
            'weekly_trend': self._analyze_weekly_trend(data),
            'monthly_trend': self._analyze_monthly_trend(data)
        }
        
        return trends
    
    def _analyze_recent_trend(self, data, days=7):
        """Phân tích xu hướng gần đây"""
        recent_data = data[-days:] if len(data) >= days else data
        
        if not recent_data:
            return {}
        
        recent_frequency = defaultdict(int)
        for result in recent_data:
            gdb = result['giai_dac_biet']
            for digit in gdb:
                recent_frequency[digit] += 1
        
        return dict(recent_frequency)
    
    def _analyze_weekly_trend(self, data):
        """Phân tích xu hướng theo tuần"""
        weekly_frequency = defaultdict(lambda: defaultdict(int))
        
        for result in data:
            date = datetime.strptime(result['date'], '%Y-%m-%d')
            week_day = date.weekday()  # 0 = Monday, 6 = Sunday
            
            gdb = result['giai_dac_biet']
            for digit in gdb:
                weekly_frequency[week_day][digit] += 1
        
        return {str(day): dict(freq) for day, freq in weekly_frequency.items()}
    
    def _analyze_monthly_trend(self, data):
        """Phân tích xu hướng theo tháng"""
        monthly_frequency = defaultdict(lambda: defaultdict(int))
        
        for result in data:
            date = datetime.strptime(result['date'], '%Y-%m-%d')
            month = date.month
            
            gdb = result['giai_dac_biet']
            for digit in gdb:
                monthly_frequency[month][digit] += 1
        
        return {str(month): dict(freq) for month, freq in monthly_frequency.items()}
    
    def _analyze_cycles(self, data):
        """Phân tích chu kỳ"""
        cycles = {
            'daily_cycle': self._analyze_daily_cycle(data),
            'weekly_cycle': self._analyze_weekly_cycle(data),
            'monthly_cycle': self._analyze_monthly_cycle(data)
        }
        
        return cycles
    
    def _analyze_daily_cycle(self, data):
        """Phân tích chu kỳ ngày"""
        daily_frequency = defaultdict(int)
        
        for result in data:
            date = datetime.strptime(result['date'], '%Y-%m-%d')
            day = date.day
            daily_frequency[day] += 1
        
        return dict(daily_frequency)
    
    def _analyze_weekly_cycle(self, data):
        """Phân tích chu kỳ tuần"""
        weekly_frequency = defaultdict(int)
        
        for result in data:
            date = datetime.strptime(result['date'], '%Y-%m-%d')
            week_day = date.weekday()
            weekly_frequency[week_day] += 1
        
        return dict(weekly_frequency)
    
    def _analyze_monthly_cycle(self, data):
        """Phân tích chu kỳ tháng"""
        monthly_frequency = defaultdict(int)
        
        for result in data:
            date = datetime.strptime(result['date'], '%Y-%m-%d')
            month = date.month
            monthly_frequency[month] += 1
        
        return dict(monthly_frequency)
    
    def _analyze_correlations(self, data):
        """Phân tích tương quan"""
        correlations = {
            'digit_correlations': self._analyze_digit_correlations(data),
            'position_correlations': self._analyze_position_correlations(data),
            'time_correlations': self._analyze_time_correlations(data)
        }
        
        return correlations
    
    def _analyze_digit_correlations(self, data):
        """Phân tích tương quan giữa các chữ số"""
        correlations = {}
        
        for i in range(10):
            for j in range(10):
                if i != j:
                    correlation = self._calculate_correlation(data, str(i), str(j))
                    correlations[f"{i}-{j}"] = correlation
        
        return correlations
    
    def _analyze_position_correlations(self, data):
        """Phân tích tương quan giữa các vị trí"""
        correlations = {}
        
        for i in range(5):  # 5 vị trí trong số
            for j in range(5):
                if i != j:
                    correlation = self._calculate_position_correlation(data, i, j)
                    correlations[f"pos{i}-pos{j}"] = correlation
        
        return correlations
    
    def _analyze_time_correlations(self, data):
        """Phân tích tương quan theo thời gian"""
        correlations = {}
        
        # Tương quan giữa ngày hiện tại và ngày trước
        for i in range(1, min(8, len(data))):
            correlation = self._calculate_time_correlation(data, i)
            correlations[f"day-{i}"] = correlation
        
        return correlations
    
    def _calculate_correlation(self, data, digit1, digit2):
        """Tính tương quan giữa 2 chữ số"""
        if len(data) < 2:
            return 0
        
        count1 = 0
        count2 = 0
        count_both = 0
        
        for result in data:
            gdb = result['giai_dac_biet']
            has_digit1 = digit1 in gdb
            has_digit2 = digit2 in gdb
            
            if has_digit1:
                count1 += 1
            if has_digit2:
                count2 += 1
            if has_digit1 and has_digit2:
                count_both += 1
        
        if count1 == 0 or count2 == 0:
            return 0
        
        # Tính correlation coefficient
        n = len(data)
        correlation = (n * count_both - count1 * count2) / math.sqrt((n * count1 - count1**2) * (n * count2 - count2**2))
        
        return correlation if not math.isnan(correlation) else 0
    
    def _calculate_position_correlation(self, data, pos1, pos2):
        """Tính tương quan giữa 2 vị trí"""
        if len(data) < 2:
            return 0
        
        values1 = []
        values2 = []
        
        for result in data:
            gdb = result['giai_dac_biet']
            if len(gdb) > max(pos1, pos2):
                values1.append(int(gdb[pos1]))
                values2.append(int(gdb[pos2]))
        
        if len(values1) < 2:
            return 0
        
        return np.corrcoef(values1, values2)[0, 1] if not math.isnan(np.corrcoef(values1, values2)[0, 1]) else 0
    
    def _calculate_time_correlation(self, data, lag):
        """Tính tương quan theo thời gian"""
        if len(data) < lag + 1:
            return 0
        
        current_values = []
        lagged_values = []
        
        for i in range(lag, len(data)):
            current_gdb = data[i]['giai_dac_biet']
            lagged_gdb = data[i - lag]['giai_dac_biet']
            
            current_values.append(int(current_gdb))
            lagged_values.append(int(lagged_gdb))
        
        if len(current_values) < 2:
            return 0
        
        return np.corrcoef(current_values, lagged_values)[0, 1] if not math.isnan(np.corrcoef(current_values, lagged_values)[0, 1]) else 0
    
    def _get_hot_numbers(self, frequency, top=10):
        """Lấy các số nóng"""
        return dict(Counter(frequency).most_common(top))
    
    def _get_cold_numbers(self, frequency, top=10):
        """Lấy các số lạnh"""
        return dict(Counter(frequency).most_common()[-top:])
    
    def _get_hot_pairs(self, pair_frequency, top=10):
        """Lấy các cặp số nóng"""
        return dict(Counter(pair_frequency).most_common(top))
    
    def _get_cold_pairs(self, pair_frequency, top=10):
        """Lấy các cặp số lạnh"""
        return dict(Counter(pair_frequency).most_common()[-top:])
