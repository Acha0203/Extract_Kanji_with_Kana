# Extract Kanji with Kana

## 使い方

1. 文書内のルビを振りたい漢字の後に、ルビを半角丸カッコで囲んで記載しておきます。

    例:

    ```txt
    文書(ぶんしょ)内のルビを振りたい漢字の後に、ルビを半角丸カッコで囲んで記載(きさい)しておきます。
    ```

2. 次のコマンドを実行すると、抽出元のファイルからルビの付いた漢字をルビごと抽出して「output_file_path」で指定したテキストファイルに保存します。

    - 「input_file_path」に抽出元のファイルを、「output_file_path」に結果を保存するファイルをフルパスで指定します。
    - 抽出元のファイルは .md または .txt のみです。
    - 結果を保存するファイルは .txt のみです。

    ```shell
    python3 extract_kanji_with_kana.py input_file_path output_file_path
    ```

    結果:

    ```txt
    文書(ぶんしょ)
    記載(きさい)
    ```
