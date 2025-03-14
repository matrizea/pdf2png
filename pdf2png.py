import sys
import os
from pdf2image import convert_from_path

def pdf_to_images(pdf_file, dpi=300):
    """
    PDFファイルを読み込み、各ページを画像(PNG形式)に変換して保存する関数。
    
    :param pdf_file: 変換対象のPDFファイルのパス
    :param dpi: 画像解像度（デフォルトは300dpi）
    """
    try:
        # PDFの各ページを画像として読み込み
        pages = convert_from_path(pdf_file, dpi=dpi)
    except Exception as e:
        print(f"PDFの変換中にエラーが発生しました: {e}")
        return

    # PDFファイル名から拡張子を除いた部分を取得
    base, _ = os.path.splitext(pdf_file)
    # 各ページごとに画像として保存
    for i, page in enumerate(pages):
        filename = f"{base}_page_{i+1}.png"
        page.save(filename, 'PNG')
        print(f"保存しました: {filename}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("使い方: python pdf2png.py <PDFファイル>")
        sys.exit(1)
    pdf_file = sys.argv[1]
    pdf_to_images(pdf_file)

