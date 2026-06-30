# Git cheatsheet

## Frequently used commands

### Creating a repository

/// define
```bash
git init
```

- Create a local Git repository
///

/// define
```bash
git clone <remote_url>
```

- To obtain a remote repository. Get the `remote_url` from GitHub
///

### Local changes & commits
/// define
```bash
git status
```

- View the status of your repository
///

/// define
```bash
git add <file_path>
```

- Add a file to the staging area
///

/// define
```bash
git rm <file_path>
```

- Remove a file from the staging area
///

/// define
```bash
git commit -m "<message>"
```

- Commit everything in the staging area. Choose a concise and descriptive message.
///

/// define
```bash
git log
```

- Show the commit history. Press `q` when reaching the end of the log to exit.
///

/// define
```bash
git log --oneline
```

- Show the commit history. Uses a single line per commit. Less detail, easier to keep the overview.
///

### Branching
/// define
```bash
git branch
```

- Check what branch you are currently on
///

/// define
```bash
git checkout <branch_name>
```

- Switch to a different branch
///

/// define
```bash
git branch <new_branch_name>
```

- Create a new branch from the current branch
///

/// define
```bash
git merge <other_branch>
```

- Merge all the changes on `other_branch` into the current branch
///

/// define
```bash
git branch -d <branch_name>
```

- Delete a (local) branch
///

### Syncing with remote
/// define
```bash
git remote -v
```

- Show information on the rconfigured remote(s)
///

/// define
```bash
git fetch
```

- Obtain changes from remote. This does **not** change your code locally.
///

/// define
```bash
git pull
```

- Obtain the changes to the current branch from remote. Merge them with your local branch.
///

/// define
```bash
git push
```

- Upload your local changes to the current branch to remote. Merge them with the remote branch.
///

### Undoing changes
/// define
```bash
git reset --soft <commit_hash>
```

- Remove the commit with `commit_hash`. Keep the changes made in that commit in the staging area. Discards history for the commit.
///

/// define
```bash
git revert <commit_hash>
```

- Create a new commit that undos all changes in `commit_hash`. Preserves history for the commit.
///

## Workflow example
In this example, we will add a new function that calculates square roots to our imaginary script `mathematics.py`. A

1. Start on your local `main` branch
2. `git pull` to ensure you are up-to-date with remote
3. git branch `feature/sqrt`
4. Write the code in `mathematics.py`
5. `git add mathematics.py` to stage the changes
6. `git commit -m "add square root function"`
7. (optional) Obtain feedback from a peer
    1. `git push` to upload your local branch to remote. You may need to set the *upstream* (remote) branch. Git will provide you with the command.
    2. Create a Pull Request on GitHub and ask your peer for feedback.
    3. If the PR is approved, continue with step 8.
8. `git checkout main` to return to the main branch
9. `git merge feature/sqrt` to merge the changes into main
10. `git push` to make sure the changes are also on remote
11. (optional) `git branch -d feature/sqrt` to clean-up the feature branch

## Further reading
- [The official Git cheatsheet](https://git-scm.com/cheat-sheet)
- [The official Git tutorial](https://git-scm.com/docs/gittutorial)