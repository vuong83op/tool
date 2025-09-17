#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test app đơn giản để kiểm tra Flask
"""

from flask import Flask, render_template_string
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test Tool Xổ Số</title>
    <style>
        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
        }
        .container {
            background: white;
            border-radius: 20px;
            padding: 30px;
            max-width: 800px;
            margin: 0 auto;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
            text-align: center;
        }
        .btn {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border: none;
            padding: 12px 30px;
            border-radius: 25px;
            cursor: pointer;
            font-size: 16px;
            margin: 10px;
        }
        .btn:hover {
            transform: translateY(-2px);
        }
        .result {
            background: #f8f9fa;
            border-radius: 10px;
            padding: 20px;
            margin: 20px 0;
        }
        .error {
            background: #ff6b6b;
            color: white;
            padding: 15px;
            border-radius: 10px;
            margin: 20px 0;
        }
        .success {
            background: #32cd32;
            color: white;
            padding: 15px;
            border-radius: 10px;
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎯 Test Tool Xổ Số Miền Bắc</h1>
        
        <div style="text-align: center;">
            <button class="btn" onclick="testAPI()">Test API</button>
            <button class="btn" onclick="testDateAPI()">Test Soi Cầu Theo Ngày</button>
        </div>
        
        <div id="result"></div>
        
        <div style="text-align: center; margin-top: 30px;">
            <p>Nếu bạn thấy thông báo này, Flask đã hoạt động!</p>
            <p>Bây giờ hãy test các API endpoints.</p>
        </div>
    </div>
    
    <script>
        function testAPI() {
            fetch('/api/test')
                .then(response => response.json())
                .then(data => {
                    document.getElementById('result').innerHTML = 
                        '<div class="success">✅ API hoạt động! Response: ' + JSON.stringify(data) + '</div>';
                })
                .catch(error => {
                    document.getElementById('result').innerHTML = 
                        '<div class="error">❌ Lỗi API: ' + error.message + '</div>';
                });
        }
        
        function testDateAPI() {
            const today = new Date().toISOString().split('T')[0];
            fetch('/api/test_date', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    date: today
                })
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('result').innerHTML = 
                    '<div class="success">✅ Date API hoạt động! Response: ' + JSON.stringify(data) + '</div>';
            })
            .catch(error => {
                document.getElementById('result').innerHTML = 
                    '<div class="error">❌ Lỗi Date API: ' + error.message + '</div>';
            });
        }
    </script>
</body>
</html>
    ''')

@app.route('/api/test')
def api_test():
    return json.dumps({
        'success': True,
        'message': 'API hoạt động bình thường!',
        'timestamp': '2024-09-17 15:30:00'
    })

@app.route('/api/test_date', methods=['POST'])
def api_test_date():
    from flask import request
    data = request.get_json()
    date = data.get('date', 'N/A')
    
    return json.dumps({
        'success': True,
        'message': f'Date API hoạt động cho ngày {date}!',
        'received_date': date,
        'timestamp': '2024-09-17 15:30:00'
    })

if __name__ == '__main__':
    print("=" * 60)
    print("🧪 TEST APP - Tool Xổ Số Miền Bắc")
    print("=" * 60)
    print("🌐 Đang khởi động test server...")
    print("📱 Truy cập: http://localhost:5000")
    print("🔧 Test các API endpoints")
    print("=" * 60)
    
    app.run(host='0.0.0.0', port=5000, debug=True)
