import os
import sys
import re


def display_help():
    print("Usage: python3 extract_kanji_with_kana.py <input file> <output file>")
    print("Extract Chinese character words having Japanese kana from the input .md or .txt file and output them to a text file.")
    sys.exit(1)


if len(sys.argv) < 3:
    display_help()

else:
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    input_extension = os.path.splitext(input_file)[1]
    output_extension = os.path.splitext(output_file)[1]

    # 漢字の単語＋半角丸カッコのパターンを検索
    # 漢字は[\u4e00-\u9fff]の範囲で、その後に(英数字や平仮名)が続くパターン
    pattern = r'[\u4e00-\u9fff]+\([^)]+\)'

    if input_extension != ".md" and input_extension != ".txt":
        print("Input file must be a markdown or text file")
        sys.exit(1)

    if output_extension != ".txt":
        output_file = output_file + ".txt"

    with open(input_file, "r") as file:
        input_contents = file.read()

    # マッチするパターンを全て抽出
    matches = re.findall(pattern, input_contents)

    # 重複を削除してソート
    unique_matches = sorted(set(matches))

    # 結果をファイルに保存
    with open(output_file, 'w', encoding='utf-8') as file:
        for match in unique_matches:
            file.write(match + '\n')

    print(f"Input file name: {input_file}")
    print(f"Output file name: {output_file}")
    print(
        f"Extracted Chinese character words having Japanese kana: {len(unique_matches)}")

    sys.exit(0)
