import argparse
import sys
import fitz  # PyMuPDF

def crop_pdf(input_path, output_path):
    try:
        # PDFを開く
        doc = fitz.open(input_path)
    except Exception as e:
        print(f"エラー: PDFファイルを開けませんでした ({input_path}): {e}", file=sys.stderr)
        sys.exit(1)
    
    for page in doc:
        # ページ内の単語（テキスト）の座標を取得してタイトな矩形を計算
        words = page.get_text("words")
        
        if words:
            x0 = min(w[0] for w in words)
            y0 = min(w[1] for w in words)
            x1 = max(w[2] for w in words)
            y1 = max(w[3] for w in words)
            
            # 周囲に少しだけ余裕（マージン: 5pt程度）を持たせる
            margin = 5
            tight_rect = fitz.Rect(x0 - margin, y0 - margin, x1 + margin, y1 + margin)
            
            # ページのCropBoxを書き換え
            page.set_cropbox(tight_rect)
        else:
            # テキストがない場合は図形描画の領域を走査（必要に応じて拡張可能）
            pass

    # 保存
    doc.save(output_path)
    doc.close()
    print(f"完了しました: {output_path}")

if __name__ == "__main__":
    # コマンドライン引数のパーサーを設定
    parser = argparse.ArgumentParser(description="Keynote等で出力されたPDFの余白や不要な枠を自動トリミングします。")
    parser.add_argument("src", help="入力するPDFファイルのパス (例: input.pdf)")
    parser.add_argument("dist", help="出力するPDFファイルのパス (例: output.pdf)")
    
    args = parser.parse_args()
    
    crop_pdf(args.src, args.dist)