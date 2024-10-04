# 必要なライブラリのインポート
from pypdf import PdfReader, PdfWriter
import os
import glob
from natsort import natsorted

# 対象のディレクトリパス
directory = "../../../../niyu/Downloads/unitext/オペレーティングシステム 第2版 3刷 (情報工学レクチャーシリーズ) (32632)/pdf/*.pdf"

# ディレクトリ内のPDFファイルを取得
files = natsorted(glob.glob(directory))

# PdfWriterインスタンスを作成
merger = PdfWriter()

# 各ファイルを順番に追加
for file in files:
    pdf_reader = PdfReader(file)
    #ファイルのデータの読み込み
    merger.append(pdf_reader)

# マージ後のPDFを書き出し
output_path = "../../../shcool/オペレーティングシステム.pdf"
with open(output_path, "wb") as output_pdf:
    merger.write(output_pdf)

print("完了")

