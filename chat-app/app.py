from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)
application = app  # Vercel必须的入口变量

# 全局错误捕获
@app.errorhandler(500)
def internal_error(error):
    # 显示错误详情，方便调试
    return f"服务器错误: {str(error)}", 500

messages = []

@app.route('/')
def index():
    try:
        # 尝试加载模板，捕获可能的模板错误
        return render_template('index.html')
    except Exception as e:
        return f"加载页面失败: {str(e)}", 500

# 其他路由保持不变，但都加上try-except
@app.route('/send', methods=['POST'])
def send_message():
    try:
        data = request.get_json()
        if not data or 'username' not in data or 'text' not in data:
            return jsonify(success=False, error="缺少用户名或消息内容"), 400
        
        message = {
            'username': data['username'],
            'text': data['text'],
            'time': time.strftime('%H:%M:%S')
        }
        messages.append(message)
        return jsonify(success=True)
    except Exception as e:
        return jsonify(success=False, error=f"发送消息失败: {str(e)}"), 500

@app.route('/messages')
def get_messages():
    try:
        return jsonify(messages)
    except Exception as e:
        return jsonify(error=f"获取消息失败: {str(e)}"), 500

if __name__ == '__main__':
    app.run(debug=True)
