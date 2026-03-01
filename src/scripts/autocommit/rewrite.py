import os
import git_filter_repo as fr
from somecommon import get_original_git_show


maps = {}
for f in os.listdir(rf"tmp"):
    if f.endswith(".msg.txt"):
        continue
    with open(rf"tmp\\{f}", "r", encoding="utf8") as ff:
        diff = ff.read()
    with open(rf"tmp\\{f}.msg.txt", "rb") as ff:
        msg = ff.read()
    maps[diff] = msg

# 谜之每次id会改变。不知道为什么。


def my_commit_callback(commit: fr.Commit, metadata):

    if commit.author_name.decode() not in [  # "test123456654321",
        "HIllya51",
        "恍兮惚兮",
    ]:
        return
    if ".".join(set(commit.message.decode().strip())) != ".":
        return
    old_id = commit.original_id.decode("utf-8")
    commit.message = maps[get_original_git_show(old_id)]


def run_filter():
    args = fr.FilteringOptions.parse_args(["--force"])

    filter_repo = fr.RepoFilter(args, commit_callback=my_commit_callback)
    filter_repo.run()


run_filter()
