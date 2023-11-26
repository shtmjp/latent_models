import os
from pathlib import Path


# pipenvに読ませるための.envを作成する
# srcフォルダの絶対パスをPYTHONPATHに書き込む
# notebooksでimportするときに、srcをルートとしてimportできるようになる
def main() -> None:
    root_dir = Path(__file__).resolve().parents[1]
    src_dir = root_dir / "src"
    # .envがなければ作成する
    # TODO: .envがあるときの挙動を追加
    if not os.path.isfile(root_dir / ".env"):
        with open(root_dir / ".env", "w") as f:
            f.write("PYTHONPATH=" + str(src_dir))


if __name__ == "__main__":
    main()
