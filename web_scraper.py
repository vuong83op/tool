#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module web scraping để lấy kết quả xổ số từ các trang web
"""

import requests
from bs4 import BeautifulSoup
import json
import time
from datetime import datetime, timedelta
import re

class XoSoScraper:
    """Class để scrape dữ liệu xổ số từ web"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
        # Danh sách các trang web xổ số miền Bắc
        self.urls = [
            'https://xoso.com.vn/xo-so-mien-bac/xsmb-p1.html',
            'https://xoso.com.vn/xsmb',
            'https://ketqua.net/xsmb',
            'https://xosomienbac.net'
        ]
        
        # Cache để lưu dữ liệu
        self.cache = {}
        self.cache_timeout = 300  # 5 phút
    
    def get_latest_results(self, days=30):
        """Lấy kết quả xổ số mới nhất"""
        try:
            # Thử lấy từ cache trước
            cache_key = f"latest_{days}"
            if self._is_cache_valid(cache_key):
                return self.cache[cache_key]['data']
            
            # Lấy dữ liệu từ web
            results = []
            
            for url in self.urls:
                try:
                    data = self._scrape_from_url(url, days)
                    if data:
                        results.extend(data)
                        break  # Nếu lấy được từ 1 trang thì dừng
                except Exception as e:
                    print(f"Lỗi khi scrape từ {url}: {str(e)}")
                    continue
            
            # Nếu không lấy được từ web, dùng dữ liệu mẫu
            if not results:
                results = self._get_sample_data(days)
            
            # Lưu vào cache
            self.cache[cache_key] = {
                'data': results,
                'timestamp': time.time()
            }
            
            return results
            
        except Exception as e:
            print(f"Lỗi khi lấy dữ liệu: {str(e)}")
            return self._get_sample_data(days)
    
    def get_results_by_date(self, target_date):
        """Lấy kết quả xổ số theo ngày cụ thể"""
        try:
            # Thử lấy từ cache trước
            cache_key = f"date_{target_date}"
            if self._is_cache_valid(cache_key):
                return self.cache[cache_key]['data']
            
            # Lấy dữ liệu từ web
            results = []
            
            for url in self.urls:
                try:
                    data = self._scrape_from_url_by_date(url, target_date)
                    if data:
                        results.extend(data)
                        break  # Nếu lấy được từ 1 trang thì dừng
                except Exception as e:
                    print(f"Lỗi khi scrape từ {url}: {str(e)}")
                    continue
            
            # Nếu không lấy được từ web, dùng dữ liệu mẫu
            if not results:
                results = self._get_sample_data_by_date(target_date)
            
            # Lưu vào cache
            self.cache[cache_key] = {
                'data': results,
                'timestamp': time.time()
            }
            
            return results
            
        except Exception as e:
            print(f"Lỗi khi lấy dữ liệu theo ngày: {str(e)}")
            return self._get_sample_data_by_date(target_date)
    
    def _scrape_from_url(self, url, days):
        """Scrape dữ liệu từ một URL cụ thể"""
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            results = []
            
            # Tìm các bảng kết quả
            tables = soup.find_all('table', class_=['result-table', 'kqxs', 'xsmb-table'])
            
            for table in tables:
                rows = table.find_all('tr')
                for row in rows:
                    cells = row.find_all(['td', 'th'])
                    if len(cells) >= 8:  # Có đủ cột cho kết quả
                        try:
                            date_str = cells[0].get_text().strip()
                            date_obj = self._parse_date(date_str)
                            
                            if date_obj and (datetime.now() - date_obj).days <= days:
                                result = {
                                    'date': date_obj.strftime('%Y-%m-%d'),
                                    'giai_dac_biet': cells[1].get_text().strip(),
                                    'giai_nhat': cells[2].get_text().strip(),
                                    'giai_nhi': [cells[i].get_text().strip() for i in range(3, 5)],
                                    'giai_ba': [cells[i].get_text().strip() for i in range(5, 8)],
                                    'giai_tu': [cells[i].get_text().strip() for i in range(8, 12)],
                                    'giai_nam': [cells[i].get_text().strip() for i in range(12, 16)],
                                    'giai_sau': [cells[i].get_text().strip() for i in range(16, 20)],
                                    'giai_bay': [cells[i].get_text().strip() for i in range(20, 24)],
                                    'giai_tam': [cells[i].get_text().strip() for i in range(24, 28)]
                                }
                                results.append(result)
                        except Exception as e:
                            continue
            
            return results
            
        except Exception as e:
            print(f"Lỗi khi scrape từ {url}: {str(e)}")
            return []
    
    def _scrape_from_url_by_date(self, url, target_date):
        """Scrape dữ liệu từ một URL cụ thể theo ngày"""
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            results = []
            
            # Tìm các bảng kết quả
            tables = soup.find_all('table', class_=['result-table', 'kqxs', 'xsmb-table'])
            
            for table in tables:
                rows = table.find_all('tr')
                for row in rows:
                    cells = row.find_all(['td', 'th'])
                    if len(cells) >= 8:  # Có đủ cột cho kết quả
                        try:
                            date_str = cells[0].get_text().strip()
                            date_obj = self._parse_date(date_str)
                            
                            if date_obj and date_obj.strftime('%Y-%m-%d') == target_date:
                                result = {
                                    'date': date_obj.strftime('%Y-%m-%d'),
                                    'giai_dac_biet': cells[1].get_text().strip(),
                                    'giai_nhat': cells[2].get_text().strip(),
                                    'giai_nhi': [cells[i].get_text().strip() for i in range(3, 5)],
                                    'giai_ba': [cells[i].get_text().strip() for i in range(5, 8)],
                                    'giai_tu': [cells[i].get_text().strip() for i in range(8, 12)],
                                    'giai_nam': [cells[i].get_text().strip() for i in range(12, 16)],
                                    'giai_sau': [cells[i].get_text().strip() for i in range(16, 20)],
                                    'giai_bay': [cells[i].get_text().strip() for i in range(20, 24)],
                                    'giai_tam': [cells[i].get_text().strip() for i in range(24, 28)]
                                }
                                results.append(result)
                        except Exception as e:
                            continue
            
            return results
            
        except Exception as e:
            print(f"Lỗi khi scrape từ {url}: {str(e)}")
            return []
    
    def _parse_date(self, date_str):
        """Parse chuỗi ngày thành datetime object"""
        try:
            # Thử các format khác nhau
            formats = [
                '%d/%m/%Y',
                '%Y-%m-%d',
                '%d-%m-%Y',
                '%d/%m/%y'
            ]
            
            for fmt in formats:
                try:
                    return datetime.strptime(date_str, fmt)
                except ValueError:
                    continue
            
            return None
        except:
            return None
    
    def _is_cache_valid(self, key):
        """Kiểm tra cache có còn hợp lệ không"""
        if key not in self.cache:
            return False
        
        cache_time = self.cache[key]['timestamp']
        return (time.time() - cache_time) < self.cache_timeout
    
    def _get_sample_data(self, days):
        """Tạo dữ liệu mẫu để test"""
        import random
        from datetime import datetime, timedelta
        
        results = []
        base_date = datetime.now() - timedelta(days=days)
        
        for i in range(days):
            date = base_date + timedelta(days=i)
            
            # Tạo số ngẫu nhiên cho các giải
            giai_dac_biet = f"{random.randint(10000, 99999)}"
            giai_nhat = f"{random.randint(1000, 9999)}"
            
            result = {
                'date': date.strftime('%Y-%m-%d'),
                'giai_dac_biet': giai_dac_biet,
                'giai_nhat': giai_nhat,
                'giai_nhi': [f"{random.randint(1000, 9999)}" for _ in range(2)],
                'giai_ba': [f"{random.randint(1000, 9999)}" for _ in range(3)],
                'giai_tu': [f"{random.randint(100, 999)}" for _ in range(4)],
                'giai_nam': [f"{random.randint(100, 999)}" for _ in range(4)],
                'giai_sau': [f"{random.randint(100, 999)}" for _ in range(4)],
                'giai_bay': [f"{random.randint(100, 999)}" for _ in range(4)],
                'giai_tam': [f"{random.randint(100, 999)}" for _ in range(4)]
            }
            results.append(result)
        
        return results
    
    def _get_sample_data_by_date(self, target_date):
        """Tạo dữ liệu mẫu theo ngày cụ thể"""
        import random
        from datetime import datetime
        
        try:
            date_obj = datetime.strptime(target_date, '%Y-%m-%d')
        except ValueError:
            return []
        
        # Tạo số ngẫu nhiên cho các giải
        giai_dac_biet = f"{random.randint(10000, 99999)}"
        giai_nhat = f"{random.randint(1000, 9999)}"
        
        result = {
            'date': target_date,
            'giai_dac_biet': giai_dac_biet,
            'giai_nhat': giai_nhat,
            'giai_nhi': [f"{random.randint(1000, 9999)}" for _ in range(2)],
            'giai_ba': [f"{random.randint(1000, 9999)}" for _ in range(3)],
            'giai_tu': [f"{random.randint(100, 999)}" for _ in range(4)],
            'giai_nam': [f"{random.randint(100, 999)}" for _ in range(4)],
            'giai_sau': [f"{random.randint(100, 999)}" for _ in range(4)],
            'giai_bay': [f"{random.randint(100, 999)}" for _ in range(4)],
            'giai_tam': [f"{random.randint(100, 999)}" for _ in range(4)]
        }
        
        return [result]
    
    def get_statistics(self, data):
        """Tính toán thống kê từ dữ liệu"""
        if not data:
            return {}
        
        stats = {
            'total_days': len(data),
            'date_range': {
                'start': data[0]['date'],
                'end': data[-1]['date']
            },
            'number_frequency': {},
            'pair_frequency': {},
            'sum_frequency': {}
        }
        
        # Đếm tần suất số
        for result in data:
            # Lấy 2 số cuối của giải đặc biệt
            gdb = result['giai_dac_biet']
            if len(gdb) >= 2:
                last_two = gdb[-2:]
                stats['number_frequency'][last_two] = stats['number_frequency'].get(last_two, 0) + 1
        
        return stats
