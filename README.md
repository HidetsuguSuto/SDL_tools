# 研究室でよく使うツール群（まだ群化してない）
## pdf_crop.py　：PDFファイルの余計な空白を削除する
### 使い方
（入っていなければ）PyMuPDFを入れる

```console
$ pip install PyMuPDF
```
Keynoteなどで作成し，PDF保存したファイル（org.pdf）を空白なしのファイル（new.pdf）に変換する．
```console
$ python3 pdf_crop.py org.pdf new.pdf
```
