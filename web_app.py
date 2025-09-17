#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Web application để hiển thị kết quả dự đoán xổ số
"""

from flask import Flask, render_template, jsonify, request
from datetime import datetime
import json
import sys
import os

# Thêm thư mục hiện tại vào Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from web_scraper import XoSoScraper
    from analyzer import SoiCauAnalyzer
    from predictor import SoiCauPredictor
except ImportError as e:
    print(f"Lỗi import: {e}")
    print("Đang sử dụng chế độ demo...")
    XoSoScraper = None
    SoiCauAnalyzer = None
    SoiCauPredictor = None

def create_app():
    """Tạo Flask app"""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'xoso_mien_bac_2024'
    
    # Khởi tạo các module
    if XoSoScraper:
        scraper = XoSoScraper()
        analyzer = SoiCauAnalyzer()
        predictor = SoiCauPredictor()
    else:
        scraper = None
        analyzer = None
        predictor = None
    
    @app.route('/')
    def index():
        """Trang chủ"""
        return render_template('index.html')
    
    @app.route('/api/predict')
    def api_predict():
        """API dự đoán số"""
        try:
            if not scraper or not analyzer or not predictor:
                return jsonify({
                    'error': 'Modules chưa được khởi tạo đúng cách',
                    'predictions': {
                        'lo_de': ['00 (demo)', '11 (demo)', '22 (demo)', '33 (demo)', '44 (demo)'],
                        'cap_xuyen': ['00-11 (demo)', '22-33 (demo)', '44-55 (demo)', '66-77 (demo)', '88-99 (demo)'],
                        'confidence': 50,
                        'analysis_summary': {'total_days_analyzed': 0},
                        'recommendations': ['Đang ở chế độ demo']
                    }
                })
            
            # Lấy dữ liệu từ web
            data = scraper.get_latest_results()
            
            if not data:
                return jsonify({
                    'error': 'Không thể lấy dữ liệu từ web',
                    'predictions': predictor._get_default_prediction()
                })
            
            # Phân tích dữ liệu
            analysis = analyzer.analyze_data(data)
            
            # Dự đoán số
            predictions = predictor.predict(analysis)
            
            return jsonify({
                'success': True,
                'predictions': predictions,
                'data_count': len(data),
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
            
        except Exception as e:
            return jsonify({
                'error': str(e),
                'predictions': {
                    'lo_de': ['00 (lỗi)', '11 (lỗi)', '22 (lỗi)', '33 (lỗi)', '44 (lỗi)'],
                    'cap_xuyen': ['00-11 (lỗi)', '22-33 (lỗi)', '44-55 (lỗi)', '66-77 (lỗi)', '88-99 (lỗi)'],
                    'confidence': 30,
                    'analysis_summary': {'total_days_analyzed': 0},
                    'recommendations': ['Có lỗi xảy ra']
                }
            })
    
    @app.route('/api/predict_by_date', methods=['POST'])
    def api_predict_by_date():
        """API dự đoán số theo ngày cụ thể"""
        try:
            data_request = request.get_json()
            target_date = data_request.get('date')
            
            if not target_date:
                return jsonify({
                    'error': 'Thiếu thông tin ngày',
                    'predictions': predictor._get_default_prediction()
                })
            
            # Lấy dữ liệu theo ngày
            data = scraper.get_results_by_date(target_date)
            
            if not data:
                return jsonify({
                    'error': f'Không tìm thấy dữ liệu cho ngày {target_date}',
                    'predictions': predictor._get_default_prediction()
                })
            
            # Phân tích dữ liệu
            analysis = analyzer.analyze_data(data)
            
            # Dự đoán số
            predictions = predictor.predict(analysis)
            
            return jsonify({
                'success': True,
                'predictions': predictions,
                'target_date': target_date,
                'data_count': len(data),
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
            
        except Exception as e:
            return jsonify({
                'error': str(e),
                'predictions': predictor._get_default_prediction()
            })
    
    @app.route('/api/data')
    def api_data():
        """API lấy dữ liệu thô"""
        try:
            data = scraper.get_latest_results()
            
            if not data:
                return jsonify({
                    'error': 'Không thể lấy dữ liệu từ web',
                    'data': []
                })
            
            return jsonify({
                'success': True,
                'data': data,
                'count': len(data),
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
            
        except Exception as e:
            return jsonify({
                'error': str(e),
                'data': []
            })
    
    @app.route('/api/analysis')
    def api_analysis():
        """API phân tích dữ liệu"""
        try:
            data = scraper.get_latest_results()
            
            if not data:
                return jsonify({
                    'error': 'Không thể lấy dữ liệu từ web',
                    'analysis': {}
                })
            
            analysis = analyzer.analyze_data(data)
            
            return jsonify({
                'success': True,
                'analysis': analysis,
                'data_count': len(data),
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
            
        except Exception as e:
            return jsonify({
                'error': str(e),
                'analysis': {}
            })
    
    @app.route('/api/statistics')
    def api_statistics():
        """API thống kê"""
        try:
            data = scraper.get_latest_results()
            
            if not data:
                return jsonify({
                    'error': 'Không thể lấy dữ liệu từ web',
                    'statistics': {}
                })
            
            statistics = scraper.get_statistics(data)
            
            return jsonify({
                'success': True,
                'statistics': statistics,
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
            
        except Exception as e:
            return jsonify({
                'error': str(e),
                'statistics': {}
            })
    
    @app.route('/refresh')
    def refresh():
        """Làm mới dữ liệu"""
        try:
            # Xóa cache
            scraper.cache.clear()
            
            # Lấy dữ liệu mới
            data = scraper.get_latest_results()
            
            if not data:
                return jsonify({
                    'error': 'Không thể lấy dữ liệu từ web',
                    'data_count': 0
                })
            
            return jsonify({
                'success': True,
                'data_count': len(data),
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
            
        except Exception as e:
            return jsonify({
                'error': str(e),
                'data_count': 0
            })
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
