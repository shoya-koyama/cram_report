# 塾講師指導報告書app

## 実装されている機能

- 報告書の投稿・一覧表示（新しい順）・詳細表示・編集・削除
- 報告書へのコメント投稿
- 対応ブラウザーの Web Speech API を使った音声入力と、入力した文章の音声読み上げ
- YouTube Data API による動画検索（API キーが必要）
- Google Calendar の当日予定タイトル取得（Google OAuth の認証情報が必要）
- Django 標準のログイン画面

チャット画面のテンプレートはありますが、WebSocket のサーバー側処理は未実装です。いいね機能とファイルアップロードも現在は無効です。

## ローカルで Django アプリを起動する

以下は macOS / Linux のターミナルでの手順です。プロジェクトのルートディレクトリ（`manage.py` がある場所）で実行してください。

### 1. Python 環境を用意する

このプロジェクトは Django 4.1.7 を使うため、Python 3.10 または 3.11 を使ってください。macOS に Python 3.14 など複数のバージョンがある場合、`python3` がどのバージョンを指すか確認し、Python 3.11 の実行ファイルを指定して仮想環境を作成します。

```bash
python3.11 --version
python3.11 -m venv venv
source venv/bin/activate
python --version
```

`python3.11` が見つからない場合は、Python 3.11 をインストールしてから実行してください。既存の仮想環境が別バージョンの Python で作られている場合は、その環境を使わず、新しい環境を作成します。

仮想環境を有効にした後、必要な Python パッケージをインストールします。このリポジトリには `requirements.txt` が含まれていないため、初回はアプリが利用するパッケージを次のようにインストールしてください。

```bash
python -m pip install --upgrade pip
python -m pip install "Django==4.1.7" python-decouple django-environ dj-database-url whitenoise django-reversion django-import-export google-auth google-auth-oauthlib google-api-python-client
```

### 2. ローカル用の環境変数を設定する

プロジェクトのルートに `.env` ファイルを作成し、次の値を設定します。以下は開発専用の例です。`.env` は Git 管理対象外です。

```dotenv
YOUTUBE_API_KEY=local-development-placeholder
SECRET_KEY=local-development-secret-key
SUPERUSER_NAME=localadmin
SUPERUSER_EMAIL=localadmin@example.com
SUPERUSER_PASSWORD=local-password-change-me
```

トップページの表示・報告書投稿を試すだけなら、YouTube や Google Calendar の実 API キーは不要です。YouTube 検索や Google Calendar 連携を使う場合は、それぞれ有効な認証情報を設定してください。

### 3. データベースを準備する

仮想環境を有効にした状態で、データベースのマイグレーションを実行します。

```bash
python manage.py migrate --run-syncdb
```

このアプリは SQLite を標準で使い、プロジェクト直下に `db.sqlite3` を作成します。

### 4. Django 開発サーバーを起動する

```bash
python manage.py runserver 127.0.0.1:8000
```

ブラウザーで [http://127.0.0.1:8000/](http://127.0.0.1:8000/) を開きます。サーバーを終了するには、起動したターミナルで `Ctrl+C` を押します。別のターミナルを使う場合は、そちらでも `venv` を有効にしてください。

## 機能の実装・変更手順

このアプリは Django で構成されています。画面や機能を変更するときは、基本的に次のファイルを編集します。

| 内容 | 主なファイル |
| --- | --- |
| データモデル | `cram/models.py` |
| リクエスト処理 | `cram/views.py` |
| URL と画面の対応 | `cram/urls.py`、`config/urls.py` |
| HTML 画面 | `cram/templates/project/` |
| JavaScript / CSS / 画像 | `cram/static/cram/` |

機能追加は、モデルが必要なら `models.py`、処理を `views.py`、URL を `cram/urls.py`、画面を対応するテンプレートに追加します。モデルを変更した場合は仮想環境内でマイグレーションを作成・適用します。

```bash
python manage.py makemigrations cram
python manage.py migrate
```

生成された `cram/migrations/` のファイルは、モデル変更と一緒に Git へ登録します。変更後はローカルサーバーで画面を確認し、必要な E2E テストを `tests/` に追加して `npm test` で確認します。

## Playwright によるローカル E2E テスト

Playwright はローカルの Django アプリをブラウザー操作でテストします。設定は `playwright.config.ts`、テストは `tests/` にあります。Chromium、Firefox、WebKit を対象にします。

### 初回セットアップ

Node.js がインストールされていることを確認し、プロジェクトのルートで Node.js の依存関係と Playwright ブラウザーをインストールします。

```bash
node --version
npm --version
npm install
npx playwright install
```

Linux でブラウザーに必要な OS 依存パッケージもまとめて入れる場合は、次を使います。

```bash
npx playwright install --with-deps
```

### テストを実行する

仮想環境を有効にして、プロジェクトのルートで実行します。Playwright が Django 開発サーバーを自動起動し、テスト終了後に停止するため、別途サーバーを起動する必要はありません。

```bash
npm test
```

ブラウザーを指定して実行:

```bash
npm run test:chromium
npx playwright test --project=firefox
npx playwright test --project=webkit
```

特定のテストファイルだけを実行:

```bash
npx playwright test tests/report.spec.ts
```

### テストの内容とデータベース

`tests/report.spec.ts` はトップページで報告書を投稿し、詳細ページにタイトルと本文が表示されることを確認します。Playwright は `127.0.0.1:8000` で Django を起動し、起動前に `migrate --run-syncdb` を実行します。

E2E テストでは、通常の開発用 `db.sqlite3` と分離した `playwright.sqlite3` を使います。設定ファイルがテストプロセス用の環境変数を渡すため、E2E テストを実行するだけなら `.env` は不要です。テスト DB は自動作成・更新され、`.gitignore` により Git 管理対象外です。

同じポート `127.0.0.1:8000` で既にサーバーが動いている場合、ローカルでは Playwright がそのサーバーを再利用します。専用のテスト DB を使いたい場合は、手動起動した Django サーバーを停止してから `npm test` を実行してください。

### 画面を見ながら実行・デバッグする

ブラウザー画面を表示:

```bash
npx playwright test --project=chromium --headed
```

UI モードでテストを選択・再実行:

```bash
npm run test:ui
```

Inspector で一時停止しながらデバッグ:

```bash
npx playwright test --project=chromium --debug
```

### HTML レポートとテスト成果物

テスト実行後に HTML レポートを開く:

```bash
npx playwright show-report
```

レポートは `playwright-report/` に、失敗時のスクリーンショット・動画・トレースなどは `test-results/` に保存されます。いずれもテスト実行時に生成される成果物で、Git 管理対象外です。

### GitHub Actions から手動実行する

`.github/workflows/playwright-issue.yml` の `Playwright E2E (manual)` を GitHub Actions 画面から選び、`Run workflow` で対象 Issue 番号を入力して実行します。Chromium のテスト結果とスクリーンショットが Issue にコメントされ、実行ログへのリンクも記載されます。このワークフローを手動実行するには、ワークフローファイルを既定ブランチにマージし、リポジトリの **Settings → Secrets and variables → Actions** に `GH_ATTACHMENT_TOKEN` という名前で Classic Personal Access Token を登録しておきます。トークンの所有者は対象リポジトリへの書き込み権限が必要です。画像添付に必要なため、このトークンを使います。

### テストを追加する

新しい E2E テストは `tests/` に `*.spec.ts` ファイルとして追加します。`page.goto('/')` でトップページを開き、`getByRole()` や `getByLabel()` などで操作し、`expect()` で結果を検証します。

```ts
import { test, expect } from '@playwright/test';

test('トップページに報告書フォームが表示される', async ({ page }) => {
  await page.goto('/');
  await expect(page.getByRole('heading', { name: '塾講師指導報告書' })).toBeVisible();
  await expect(page.getByLabel('生徒氏名：タイトル')).toBeVisible();
});
```
