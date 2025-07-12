import sys
import re
import os


def display_help():
    print("使い方: python3 generate_prh.py <入力ファイル名> <出力ファイル名>")
    print(".txt ファイルから textlint の prh で使用する .yml ファイルを生成します。入力ファイル名と出力ファイル名はフルパスで指定してください。")
    sys.exit(1)


def parse_input_text_file(file_path):
    """
    input_text_file.txtファイルを解析して、漢字とルビのペアを抽出する

    Args:
        file_path (str): input_text_file.txtファイルのパス

    Returns:
        list: [(漢字, ルビ), ...] のリスト
    """
    kanji_ruby_pairs = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            # 漢字(ルビ)の形式を解析
            match = re.match(r'^(.+?)\((.+?)\)$', line)
            if match:
                kanji = match.group(1)
                ruby = match.group(2)
                kanji_ruby_pairs.append((kanji, ruby))
            else:
                print(f"警告: 解析できない行をスキップします: {line}")

    return kanji_ruby_pairs


def generate_prh_rules(kanji_ruby_pairs):
    """
    漢字とルビのペアからprh.ymlのルール部分を生成する

    Args:
        kanji_ruby_pairs (list): [(漢字, ルビ), ...] のリスト

    Returns:
        list: prh.ymlのrulesセクション用の辞書のリスト
    """
    rules = []

    for kanji, ruby in kanji_ruby_pairs:
        # 期待される形式 (漢字(ルビ))
        expected = f"{kanji}({ruby})"

        # パターン: 「漢字(ルビ)」の形式ではない場合にマッチ
        pattern = f"/{kanji}(?!\\({ruby}\\))/"

        # エラーメッセージ
        prh_message = f"「{kanji}」のルビ「{ruby}」が抜けています。"

        rule = f"  - expected: {expected}\n    pattern: {pattern}\n    prh: {prh_message}"

        rules.append(rule)

    return rules


def generate_prh_yml(input_file, output_file):
    """
    入力ファイルから .yml ファイルを生成する

    Args:
        input_file (str): 入力ファイルのフルパス
        output_file (str): 出力ファイルのフルパス
    """
    # input_text_file.txtファイルを解析
    kanji_ruby_pairs = parse_input_text_file(input_file)

    if not kanji_ruby_pairs:
        print("エラー: 有効な漢字とルビのペアが見つかりませんでした。")
        return

    print(f"解析結果: {len(kanji_ruby_pairs)}個の漢字とルビのペアを発見しました。")

    # prh.ymlのルールを生成
    rules = generate_prh_rules(kanji_ruby_pairs)

    # prh.ymlの構造を作成
    prh_data = f"version: 1\nrules:"

    # YAMLファイルとして出力
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(prh_data + '\n')

        for rule in rules:
            file.write(rule + '\n')

    print(f".yml ファイルを生成しました: {output_file}")
    print(f"生成されたルール数: {len(rules)}")
    return


if len(sys.argv) < 3:
    display_help()

else:
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    input_extension = os.path.splitext(input_file)[1]
    output_extension = os.path.splitext(output_file)[1]

    if input_extension != ".txt":
        print("入力ファイルには .txt ファイルを指定してください。")
        sys.exit(1)

    if output_extension != ".yml":
        output_file = output_file + ".yml"

    generate_prh_yml(input_file, output_file)

sys.exit(0)
