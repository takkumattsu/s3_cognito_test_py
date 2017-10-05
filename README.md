# What?

[PythonでCognito経由でS3リソースにアクセスする](https://qiita.com/kempe/items/c53a9833a57ea1b3ce23)を試してみた


# How to Use

- Use python3
- バケット名とかリージョンは適宜変更

```bash
# venv使うなりしてpython3を利用
#
#  python3 -m venv test
#  source test/bin/activate
#
# 必要なモジュールインストール
pip install --require requirements.txt
# 実行
python s3_test.py 
```

# Thanks

- [imgcat doesn't work in a tmux session](https://gitlab.com/gnachman/iterm2/issues/3898#note_14097715)
- [PythonでCognito経由でS3リソースにアクセスする](https://qiita.com/kempe/items/c53a9833a57ea1b3ce23)
