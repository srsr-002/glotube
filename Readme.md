## 環境構築手順
1. コンテナの構築  
`docker compose up -d`
2. appコンテナに入る  
`docker compose exec -it app bash`
3. スクリプトの実行  
`python main.py`