from somecommon import get_original_git_show
import os
import git_filter_repo as fr

os.makedirs("tmp")


def my_commit_callback(commit: fr.Commit, metadata):

    if commit.author_name.decode() not in [  # "test123456654321",
        "HIllya51",
        "恍兮惚兮",
    ]:
        return
    if ".".join(set(commit.message.decode().strip())) != ".":
        return
    old_id = commit.original_id.decode("utf-8")
    raw_show_info = get_original_git_show(old_id)
    with open(rf"tmp\\{old_id}.txt", "w", encoding="utf8") as ff:
        ff.write(raw_show_info)


def run_filter():
    args = fr.FilteringOptions.parse_args(["--force"])

    filter_repo = fr.RepoFilter(args, commit_callback=my_commit_callback)
    filter_repo.run()


if __name__ == "__main__":
    run_filter()
