# My Python project template
- pyenv, pipenvのインストールが必要
- デフォルトはPython 3.11.2
  - バージョンはPipfileから変更可能
- `src/make_dotenv.py` は, Notebookから`src`をルートとしてimportできるようにするためのスクリプト
  - `pipenv shell`した時に`.env`を読んでサブシェル内に環境変数を設定してくれることを利用している
      - https://pipenv-ja.readthedocs.io/ja/translate-ja/advanced.html#automatic-loading-of-env を参照
  - これによりグローバル環境を汚さずにサブシェル内でだけ`PYTHON_PATH`を設定できる

## How to set up

```
pipenv install --dev \
&& pipenv run python3 src/make_dotenv.py \
&& pipenv shell
```

## 想定される使用法例
- リモートで管理する場合
  このリポジトリはテンプレート化されているので, テンプレートからリポジトリ作成して, 以下のスクリプトの1行目だけ変えて実行
  ```
  REPONAME="your repo name" \
  && git clone git@github.com:shtmjp/${REPONAME}.git \
  && cd ${REPONAME} \
  && pipenv install --dev \
  && pipenv run python3 src/make_dotenv.py \
  && pipenv shell
  ```
  
- ローカルだけで管理する場合
  上とほぼ同様だが, gitを削除する
  ```
  REPONAME="your repo name" \
  && git clone git@github.com:shtmjp/python_template.git ${REPONAME} \
  && cd ${REPONAME} \
  && git remote rm origin \
  && rm -rf .git \
  && pipenv install --dev \
  && pipenv run python3 src/make_dotenv.py \
  && pipenv shell
  ```

- 途中までローカルだけで管理していたがリモートで管理したくなった場合
  https://note.com/shift_tech/n/nc00511c05f1d このへんを参照して, リモートを変更する.




