from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'SQL 문제풀이 웹사이트에 오신 걸 환영합니다!'

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    user_query = data.get('user_query')

    # 임시 정답 쿼리
    correct_query = "SELECT name FROM employees"
    correct_result = [{"name": "Alice"}, {"name": "Bob"}, {"name": "Charlie"}]

    # 간단한 비교
    if user_query.strip().lower() == correct_query.lower():
        return jsonify({"is_correct": True, "result": correct_result})
    else:
        return jsonify({"is_correct": False, "message": "틀렸어요!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

