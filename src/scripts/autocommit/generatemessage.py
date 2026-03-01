from concurrent.futures import ThreadPoolExecutor
from functools import partial
import os
from tqdm import tqdm
from somecommon import generate_commit_messages


def process_file(filename: str):
    with open(rf".\tmp\{filename}", "r", encoding="utf8") as ff:
        diff_text = ff.read()  # [:700000]
        # 有个946kb，超出长度，截断一下
    try:
        msg = generate_commit_messages(diff_text)
    except:
        return
    print(f"{filename}\n{msg}")

    with open(
        rf"tmp\{filename}.msg.txt",
        "w",
        encoding="utf8",
    ) as ff:
        ff.write(msg)


files = [
    f
    for f in os.listdir(rf"tmp")
    if (not f.endswith(".msg.txt") and not os.path.exists(rf"tmp\\{f}.msg.txt"))
]
with ThreadPoolExecutor(max_workers=16) as executor:
    results = list(
        tqdm(
            executor.map(process_file, files),
            total=len(files),
            unit="file",
        )
    )
