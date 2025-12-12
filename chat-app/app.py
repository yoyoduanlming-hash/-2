from flask import Flask, render_template, request, jsonify
import time

# 关键：必须定义一个名为app的变量作为Flask应用入口
app = Flask(__name__)

# 存储消息的列表
messages = []

# 根路由，返回聊天页面
@app.route('/')
def index():
    return render_template('index.html')

# 处理发送消息的请求
@app.route('/send', methods=['POST'])
def send_message():
    data = request.get_json()
    message = {
        'username': data['username'],
        'text': data['text'],
        'time': time.strftime('%H:%M:%S')
    }
    messages.append(message)
    return jsonify(success=True)

# 提供消息列表的接口
@app.route('/messages')
def get_messages():
    return jsonify(messages)

# 本地运行时使用
if __name__ == '__main__':
    app.run(debug=True)
