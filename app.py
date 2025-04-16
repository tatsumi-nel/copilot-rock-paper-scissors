from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import api_game
import json
import os

# Flaskアプリケーションの初期化
app = Flask(__name__)
CORS(app)  # クロスオリジンリクエストを許可

# JSONエンコーディング設定を変更して日本語をエスケープしないようにする
app.config['JSON_AS_ASCII'] = False

# バージョン情報
API_VERSION = "1.0.0"

@app.route('/api/play', methods=['POST'])
def play():
    """
    ゲームをプレイするエンドポイント
    """
    try:
        data = request.get_json()
        if not data or 'choice' not in data:
            return make_response(jsonify({'error': '選択が指定されていません'}), 400)
            
        user_choice = data['choice'].lower()
        result = api_game.play_game(user_choice)
        return jsonify(result)
        
    except ValueError as e:
        return make_response(jsonify({'error': str(e)}), 400)
    except Exception as e:
        return make_response(jsonify({'error': '内部サーバーエラー', 'details': str(e)}), 500)

@app.route('/api/choices', methods=['GET'])
def get_choices():
    """
    選択肢一覧を返すエンドポイント
    """
    try:
        choices = api_game.get_choices()
        return jsonify({'choices': choices})
    except Exception as e:
        return make_response(jsonify({'error': '内部サーバーエラー', 'details': str(e)}), 500)

@app.route('/api/rules', methods=['GET'])
def get_rules():
    """
    ゲームルールを返すエンドポイント
    """
    try:
        rules = api_game.get_rules()
        return jsonify(rules)
    except Exception as e:
        return make_response(jsonify({'error': '内部サーバーエラー', 'details': str(e)}), 500)

@app.route('/api/health', methods=['GET'])
def health_check():
    """
    ヘルスチェックエンドポイント
    """
    return jsonify({
        'status': 'ok',
        'version': API_VERSION
    })

# エラーハンドラー
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'リソースが見つかりません'}), 404)

@app.errorhandler(405)
def method_not_allowed(error):
    return make_response(jsonify({'error': '許可されていないメソッドです'}), 405)

@app.errorhandler(500)
def internal_error(error):
    return make_response(jsonify({'error': '内部サーバーエラー'}), 500)

# メイン実行部分
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port, debug=True)
