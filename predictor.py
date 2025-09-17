#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module dự đoán lô và cặp xuyên từ dữ liệu phân tích
"""

import random
import math
from collections import defaultdict, Counter
from datetime import datetime
import numpy as np

class SoiCauPredictor:
    """Class dự đoán số xổ số dựa trên phân tích"""
    
    def __init__(self):
        self.prediction_cache = {}
        
    def predict(self, analysis):
        """Dự đoán số dựa trên phân tích"""
        if not analysis:
            return self._get_default_prediction()
        
        predictions = {
            'lo_de': self._predict_lo_de(analysis),
            'cap_xuyen': self._predict_cap_xuyen(analysis),
            'confidence': self._calculate_confidence(analysis),
            'analysis_summary': self._get_analysis_summary(analysis),
            'recommendations': self._get_recommendations(analysis)
        }
        
        return predictions
    
    def _predict_lo_de(self, analysis):
        """Dự đoán lô đề"""
        lo_de = []
        
        # Dự đoán dựa trên tần suất số
        if 'number_frequency' in analysis:
            freq_analysis = analysis['number_frequency']
            
            # Lấy các số nóng
            hot_numbers = freq_analysis.get('hot_numbers', {})
            for number, count in list(hot_numbers.items())[:5]:
                lo_de.append(f"{number} (tần suất: {count})")
            
            # Lấy các số lạnh (có thể về)
            cold_numbers = freq_analysis.get('cold_numbers', {})
            for number, count in list(cold_numbers.items())[:3]:
                lo_de.append(f"{number} (số lạnh: {count})")
        
        # Dự đoán dựa trên pattern
        if 'pattern_analysis' in analysis:
            pattern_analysis = analysis['pattern_analysis']
            
            # Dự đoán dựa trên tổng số
            sum_patterns = pattern_analysis.get('sum_patterns', {})
            if sum_patterns:
                predicted_sum = self._predict_sum(sum_patterns)
                lo_de.append(f"Tổng dự đoán: {predicted_sum}")
        
        # Dự đoán dựa trên xu hướng gần đây
        if 'trend_analysis' in analysis:
            trend_analysis = analysis['trend_analysis']
            recent_trend = trend_analysis.get('recent_trend', {})
            
            if recent_trend:
                recent_hot = Counter(recent_trend).most_common(3)
                for number, count in recent_hot:
                    lo_de.append(f"{number} (xu hướng gần đây: {count})")
        
        # Dự đoán dựa trên chu kỳ
        if 'cycle_analysis' in analysis:
            cycle_analysis = analysis['cycle_analysis']
            
            # Dự đoán dựa trên chu kỳ ngày
            daily_cycle = cycle_analysis.get('daily_cycle', {})
            if daily_cycle:
                today = datetime.now().day
                cycle_prediction = self._predict_from_cycle(daily_cycle, today)
                if cycle_prediction:
                    lo_de.append(f"{cycle_prediction} (chu kỳ ngày)")
        
        # Dự đoán dựa trên tương quan
        if 'correlation_analysis' in analysis:
            correlation_analysis = analysis['correlation_analysis']
            
            # Tìm các số có tương quan cao
            digit_correlations = correlation_analysis.get('digit_correlations', {})
            if digit_correlations:
                high_corr_numbers = self._find_high_correlation_numbers(digit_correlations)
                for number in high_corr_numbers[:2]:
                    lo_de.append(f"{number} (tương quan cao)")
        
        # Nếu không có đủ dữ liệu, tạo dự đoán ngẫu nhiên
        if len(lo_de) < 5:
            random_numbers = self._generate_random_predictions(5 - len(lo_de))
            lo_de.extend(random_numbers)
        
        return lo_de[:10]  # Trả về tối đa 10 dự đoán
    
    def _predict_cap_xuyen(self, analysis):
        """Dự đoán cặp xuyên"""
        cap_xuyen = []
        
        # Dự đoán dựa trên phân tích cặp số
        if 'pair_analysis' in analysis:
            pair_analysis = analysis['pair_analysis']
            
            # Lấy các cặp số nóng
            hot_pairs = pair_analysis.get('hot_pairs', {})
            for pair, count in list(hot_pairs.items())[:5]:
                cap_xuyen.append(f"{pair} (tần suất: {count})")
            
            # Lấy các cặp số lạnh
            cold_pairs = pair_analysis.get('cold_pairs', {})
            for pair, count in list(cold_pairs.items())[:3]:
                cap_xuyen.append(f"{pair} (cặp lạnh: {count})")
        
        # Dự đoán dựa trên xu hướng gần đây
        if 'trend_analysis' in analysis:
            trend_analysis = analysis['trend_analysis']
            recent_trend = trend_analysis.get('recent_trend', {})
            
            if recent_trend:
                # Tạo cặp từ các số xuất hiện gần đây
                recent_numbers = list(recent_trend.keys())
                for i in range(min(3, len(recent_numbers))):
                    for j in range(i+1, min(3, len(recent_numbers))):
                        pair = recent_numbers[i] + recent_numbers[j]
                        cap_xuyen.append(f"{pair} (xu hướng gần đây)")
        
        # Dự đoán dựa trên pattern
        if 'pattern_analysis' in analysis:
            pattern_analysis = analysis['pattern_analysis']
            
            # Dự đoán dựa trên pattern chẵn/lẻ
            parity_patterns = pattern_analysis.get('parity_patterns', {})
            if parity_patterns:
                predicted_parity = self._predict_parity_pattern(parity_patterns)
                if predicted_parity:
                    cap_xuyen.append(f"{predicted_parity} (pattern chẵn/lẻ)")
        
        # Dự đoán dựa trên chu kỳ
        if 'cycle_analysis' in analysis:
            cycle_analysis = analysis['cycle_analysis']
            
            # Dự đoán dựa trên chu kỳ tuần
            weekly_cycle = cycle_analysis.get('weekly_cycle', {})
            if weekly_cycle:
                today_weekday = datetime.now().weekday()
                cycle_prediction = self._predict_from_cycle(weekly_cycle, today_weekday)
                if cycle_prediction:
                    cap_xuyen.append(f"{cycle_prediction} (chu kỳ tuần)")
        
        # Nếu không có đủ dữ liệu, tạo dự đoán ngẫu nhiên
        if len(cap_xuyen) < 5:
            random_pairs = self._generate_random_pairs(5 - len(cap_xuyen))
            cap_xuyen.extend(random_pairs)
        
        return cap_xuyen[:10]  # Trả về tối đa 10 dự đoán
    
    def _predict_sum(self, sum_patterns):
        """Dự đoán tổng số"""
        sum_frequency = sum_patterns.get('sum_frequency', {})
        
        if not sum_frequency:
            return random.randint(20, 45)
        
        # Tìm tổng có tần suất cao nhất
        max_freq = max(sum_frequency.values())
        high_freq_sums = [s for s, f in sum_frequency.items() if f == max_freq]
        
        # Chọn ngẫu nhiên một trong các tổng có tần suất cao
        return random.choice(high_freq_sums)
    
    def _predict_parity_pattern(self, parity_patterns):
        """Dự đoán pattern chẵn/lẻ"""
        even_freq = parity_patterns.get('even_digits_frequency', {})
        odd_freq = parity_patterns.get('odd_digits_frequency', {})
        
        if not even_freq or not odd_freq:
            return None
        
        # Tìm pattern chẵn/lẻ phổ biến nhất
        max_even = max(even_freq.values())
        max_odd = max(odd_freq.values())
        
        if max_even > max_odd:
            return "Chẵn nhiều hơn"
        elif max_odd > max_even:
            return "Lẻ nhiều hơn"
        else:
            return "Cân bằng chẵn/lẻ"
    
    def _predict_from_cycle(self, cycle_data, current_value):
        """Dự đoán dựa trên chu kỳ"""
        if not cycle_data:
            return None
        
        # Tìm giá trị có tần suất cao nhất trong chu kỳ
        max_freq = max(cycle_data.values())
        high_freq_values = [v for v, f in cycle_data.items() if f == max_freq]
        
        # Chọn giá trị gần nhất với giá trị hiện tại
        if high_freq_values:
            return min(high_freq_values, key=lambda x: abs(x - current_value))
        
        return None
    
    def _find_high_correlation_numbers(self, digit_correlations):
        """Tìm các số có tương quan cao"""
        high_corr_numbers = []
        
        for pair, correlation in digit_correlations.items():
            if abs(correlation) > 0.5:  # Tương quan cao
                high_corr_numbers.extend(pair.split('-'))
        
        # Loại bỏ trùng lặp và trả về
        return list(set(high_corr_numbers))
    
    def _generate_random_predictions(self, count):
        """Tạo dự đoán ngẫu nhiên"""
        predictions = []
        for _ in range(count):
            number = random.randint(0, 99)
            predictions.append(f"{number:02d} (ngẫu nhiên)")
        return predictions
    
    def _generate_random_pairs(self, count):
        """Tạo cặp số ngẫu nhiên"""
        pairs = []
        for _ in range(count):
            pair = f"{random.randint(0, 9)}{random.randint(0, 9)}"
            pairs.append(f"{pair} (ngẫu nhiên)")
        return pairs
    
    def _calculate_confidence(self, analysis):
        """Tính độ tin cậy của dự đoán"""
        confidence = 50  # Độ tin cậy cơ bản
        
        # Tăng độ tin cậy dựa trên chất lượng dữ liệu
        if 'basic_stats' in analysis:
            basic_stats = analysis['basic_stats']
            total_days = basic_stats.get('total_days', 0)
            
            if total_days >= 30:
                confidence += 20
            elif total_days >= 15:
                confidence += 10
            elif total_days >= 7:
                confidence += 5
        
        # Tăng độ tin cậy dựa trên pattern rõ ràng
        if 'pattern_analysis' in analysis:
            pattern_analysis = analysis['pattern_analysis']
            
            # Kiểm tra pattern tổng số
            sum_patterns = pattern_analysis.get('sum_patterns', {})
            if sum_patterns:
                sum_frequency = sum_patterns.get('sum_frequency', {})
                if sum_frequency:
                    max_freq = max(sum_frequency.values())
                    total_count = sum(sum_frequency.values())
                    if max_freq / total_count > 0.3:  # Pattern rõ ràng
                        confidence += 15
        
        # Tăng độ tin cậy dựa trên xu hướng
        if 'trend_analysis' in analysis:
            trend_analysis = analysis['trend_analysis']
            recent_trend = trend_analysis.get('recent_trend', {})
            
            if recent_trend:
                # Kiểm tra xu hướng rõ ràng
                max_freq = max(recent_trend.values())
                total_count = sum(recent_trend.values())
                if max_freq / total_count > 0.4:  # Xu hướng rõ ràng
                    confidence += 10
        
        # Tăng độ tin cậy dựa trên tương quan
        if 'correlation_analysis' in analysis:
            correlation_analysis = analysis['correlation_analysis']
            digit_correlations = correlation_analysis.get('digit_correlations', {})
            
            if digit_correlations:
                high_corr_count = sum(1 for corr in digit_correlations.values() if abs(corr) > 0.5)
                if high_corr_count > 5:  # Nhiều tương quan cao
                    confidence += 10
        
        return min(confidence, 95)  # Tối đa 95%
    
    def _get_analysis_summary(self, analysis):
        """Lấy tóm tắt phân tích"""
        summary = {
            'total_days_analyzed': 0,
            'hot_numbers': [],
            'cold_numbers': [],
            'hot_pairs': [],
            'cold_pairs': [],
            'dominant_patterns': []
        }
        
        if 'basic_stats' in analysis:
            summary['total_days_analyzed'] = analysis['basic_stats'].get('total_days', 0)
        
        if 'number_frequency' in analysis:
            number_freq = analysis['number_frequency']
            summary['hot_numbers'] = list(number_freq.get('hot_numbers', {}).keys())[:5]
            summary['cold_numbers'] = list(number_freq.get('cold_numbers', {}).keys())[:5]
        
        if 'pair_analysis' in analysis:
            pair_analysis = analysis['pair_analysis']
            summary['hot_pairs'] = list(pair_analysis.get('hot_pairs', {}).keys())[:5]
            summary['cold_pairs'] = list(pair_analysis.get('cold_pairs', {}).keys())[:5]
        
        if 'pattern_analysis' in analysis:
            pattern_analysis = analysis['pattern_analysis']
            
            # Tìm pattern chiếm ưu thế
            if 'sum_patterns' in pattern_analysis:
                sum_patterns = pattern_analysis['sum_patterns']
                sum_frequency = sum_patterns.get('sum_frequency', {})
                if sum_frequency:
                    dominant_sum = max(sum_frequency, key=sum_frequency.get)
                    summary['dominant_patterns'].append(f"Tổng số: {dominant_sum}")
            
            if 'parity_patterns' in pattern_analysis:
                parity_patterns = pattern_analysis['parity_patterns']
                even_freq = parity_patterns.get('even_digits_frequency', {})
                odd_freq = parity_patterns.get('odd_digits_frequency', {})
                
                if even_freq and odd_freq:
                    max_even = max(even_freq.values())
                    max_odd = max(odd_freq.values())
                    
                    if max_even > max_odd:
                        summary['dominant_patterns'].append("Chẵn nhiều hơn")
                    elif max_odd > max_even:
                        summary['dominant_patterns'].append("Lẻ nhiều hơn")
        
        return summary
    
    def _get_recommendations(self, analysis):
        """Lấy khuyến nghị"""
        recommendations = []
        
        if 'basic_stats' in analysis:
            total_days = analysis['basic_stats'].get('total_days', 0)
            
            if total_days < 15:
                recommendations.append("Cần thêm dữ liệu để dự đoán chính xác hơn")
            elif total_days < 30:
                recommendations.append("Dữ liệu đủ để phân tích cơ bản")
            else:
                recommendations.append("Dữ liệu đủ để phân tích chi tiết")
        
        if 'pattern_analysis' in analysis:
            pattern_analysis = analysis['pattern_analysis']
            
            if 'sum_patterns' in pattern_analysis:
                sum_patterns = pattern_analysis['sum_patterns']
                sum_frequency = sum_patterns.get('sum_frequency', {})
                
                if sum_frequency:
                    max_freq = max(sum_frequency.values())
                    total_count = sum(sum_frequency.values())
                    
                    if max_freq / total_count > 0.3:
                        recommendations.append("Có pattern tổng số rõ ràng")
                    else:
                        recommendations.append("Pattern tổng số không rõ ràng")
        
        if 'trend_analysis' in analysis:
            trend_analysis = analysis['trend_analysis']
            recent_trend = trend_analysis.get('recent_trend', {})
            
            if recent_trend:
                max_freq = max(recent_trend.values())
                total_count = sum(recent_trend.values())
                
                if max_freq / total_count > 0.4:
                    recommendations.append("Có xu hướng rõ ràng gần đây")
                else:
                    recommendations.append("Xu hướng gần đây không rõ ràng")
        
        if 'correlation_analysis' in analysis:
            correlation_analysis = analysis['correlation_analysis']
            digit_correlations = correlation_analysis.get('digit_correlations', {})
            
            if digit_correlations:
                high_corr_count = sum(1 for corr in digit_correlations.values() if abs(corr) > 0.5)
                
                if high_corr_count > 5:
                    recommendations.append("Có nhiều tương quan cao giữa các số")
                else:
                    recommendations.append("Tương quan giữa các số không cao")
        
        if not recommendations:
            recommendations.append("Không có khuyến nghị đặc biệt")
        
        return recommendations
    
    def _get_default_prediction(self):
        """Dự đoán mặc định khi không có dữ liệu"""
        return {
            'lo_de': [
                '00 (mặc định)',
                '11 (mặc định)',
                '22 (mặc định)',
                '33 (mặc định)',
                '44 (mặc định)'
            ],
            'cap_xuyen': [
                '00-11 (mặc định)',
                '22-33 (mặc định)',
                '44-55 (mặc định)',
                '66-77 (mặc định)',
                '88-99 (mặc định)'
            ],
            'confidence': 30,
            'analysis_summary': {
                'total_days_analyzed': 0,
                'hot_numbers': [],
                'cold_numbers': [],
                'hot_pairs': [],
                'cold_pairs': [],
                'dominant_patterns': []
            },
            'recommendations': ['Không có dữ liệu để phân tích']
        }
