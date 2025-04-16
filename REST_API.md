# じゃんけんゲーム REST API 設計

## 概要
このドキュメントでは、既存のじゃんけんゲーム（Rock, Paper, Scissors, Lizard, Spock）をREST APIとして実装するための設計を記述します。

## 技術スタック
- **言語**: Python
- **フレームワーク**: Flask（軽量で使いやすいWebフレームワーク）
- **データ形式**: JSON

## 必要パッケージ
- Flask
- Flask-CORS（クロスオリジンリクエスト対応）

## APIエンドポイント

### 1. ゲームプレイ
- **エンドポイント**: `/api/play`
- **メソッド**: POST
- **説明**: プレイヤーの選択を送信し、コンピュータの選択と勝敗結果を返します
- **リクエストボディ**:
  ```json
  {
    "choice": "rock" // "rock", "paper", "scissors", "lizard", "spock"のいずれか
  }
  ```
- **レスポンス**:
  ```json
  {
    "player_choice": "rock",
    "computer_choice": "scissors",
    "result": "あなたの勝ち",
    "timestamp": "2025-04-14T12:34:56"
  }
  ```

### 2. 選択肢一覧取得
- **エンドポイント**: `/api/choices`
- **メソッド**: GET
- **説明**: 有効な選択肢の一覧を返します
- **レスポンス**:
  ```json
  {
    "choices": [
      {"id": "rock", "name": "グー (Rock)"},
      {"id": "paper", "name": "パー (Paper)"},
      {"id": "scissors", "name": "チョキ (Scissors)"},
      {"id": "lizard", "name": "リザード (Lizard)"},
      {"id": "spock", "name": "スポック (Spock)"}
    ]
  }
  ```

### 3. ゲームルール取得
- **エンドポイント**: `/api/rules`
- **メソッド**: GET
- **説明**: ゲームのルールを返します
- **レスポンス**:
  ```json
  {
    "rules": {
      "rock": ["scissors", "lizard"],
      "paper": ["rock", "spock"],
      "scissors": ["paper", "lizard"],
      "lizard": ["paper", "spock"],
      "spock": ["rock", "scissors"]
    },
    "description": "各選択肢は、配列内の選択肢に対して勝利します"
  }
  ```

### 4. ヘルスチェック
- **エンドポイント**: `/api/health`
- **メソッド**: GET
- **説明**: APIの稼働状態を確認します
- **レスポンス**:
  ```json
  {
    "status": "ok",
    "version": "1.0.0"
  }
  ```

## データモデル

### 選択肢
```python
{
  "id": str,  # "rock", "paper", "scissors", "lizard", "spock"
  "name": str  # 表示名（日本語と英語）
}
```

### ゲーム結果
```python
{
  "player_choice": str,
  "computer_choice": str,
  "result": str,  # "あなたの勝ち", "コンピューターの勝ち", "引き分け"
  "timestamp": str  # ISO形式の日時
}
```

## 実装計画

1. **app.py**: FlaskアプリケーションとAPIエンドポイントの実装
2. **api_game.py**: ゲームロジックをAPIから呼び出せるように修正
3. **config.py**: 設定ファイル

## エラーハンドリング
- 400 Bad Request: 無効な選択肢が送信された場合
- 500 Internal Server Error: サーバー側のエラーが発生した場合

## セキュリティ考慮事項
- 入力値のバリデーション
- レートリミットの実装（大量リクエスト対策）

## テスト計画
- 単体テスト: 各APIエンドポイントの機能テスト
- 統合テスト: クライアントからのリクエストシミュレーション

## デプロイ方法
- ローカル環境: `flask run`
- 本番環境: Gunicornなどの本番用WSGIサーバーを使用

## 今後の拡張可能性
- ユーザー認証機能
- ゲーム履歴の保存と取得
- スコアボードやランキング機能