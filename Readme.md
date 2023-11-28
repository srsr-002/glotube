## 環境構築手順
1. コンテナの構築  
`docker compose up -d`
2. appコンテナに入る  
`docker compose exec -it app bash`
3. スクリプトの実行  
`python main.py`

## Gitの使い方
1. git clone 
→ リモートリポジトリをローカルにコピーする。最初1回だけ実行。

2. git checkout -b ブランチ名
→ 現在のブランチから新しいブランチを作成する。
ブランチ名は「タイプ_分岐目的」の形で英語で指定すること。
 例) collect_image_init

3. commit
→コードの修正履歴を保存する。
commitメッセージはhttps://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716
を参考にして「タグ:作業内容」の形で作成する。(英語/日本語どっちもおｋ)
例) git commit -m "feat: collect_imageのプロトタイプ作成"

4. Publish branch
→ ローカルで作成したブランチをリモートリポジトリに公開する。

5. Push
→ ローカルブランチの変更をリモートブランチにプッシュする。

6. Pull Requestの作成
→メインブランチに変更事項を統合するためにプルリクエストを作成。

7. レビュー
→6.で作成されたプルリクを見て動作に問題はないか、ネーミングルールは守られたかなどをレビューする。レビューした結果、問題がある場合は修正を依頼し、その後再度レビューする。問題がなかった場合、メインブランチにマージする。
