from git import Repo
import os
print(os.getcwd())

repo = Repo(os.getcwd())
assert not repo.bare

print(repo)
print(repo.is_dirty())
print(repo.untracked_files)

master_local = repo.commit("master")
master_remote = repo.commit("origin/master")

print(master_local)
print(master_remote)

diff_index = master_remote.diff(master_local)
print(diff_index)

for diff in diff_index:
    print(diff.change_type)
    print(diff.a_path)
    print(diff.b_path)
