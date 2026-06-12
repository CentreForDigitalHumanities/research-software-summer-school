# Rewriting History
## Objectives
In this module, you will learn:

 - How to undo commits using `git reset`
 - How to safely reverse commits using `git revert`
 - How to move commits between branches using `git cherry-pick`
 - How to update a branch using `git rebase`


## Git Reset

`git reset` allows you to move the pointer of the current branch to a different commit, essentially walking back in time. Git has three main modes for resetting:

 - Mixed reset: `git reset --mixed` - keep changes in the working directory (no work is lost)
 - Soft reset: `git reset --soft` - keeps the changes and adds them to the staging area (no work is lost)
 - Hard reset: `git reset --hard` - discards all changes and overwrites files to the state from the intended commit (work is lost)

With `git reset` you can undo a commit that was made too early or with an incorrect commit message.

/// details | Rewriting history
    type: warning

Avoid using `git reset` on commits that have already been shared with collaborators unless you understand the consequences. Resetting rewrites project history.
///

## Exercise: undo a commit with git reset

//// tab | Using the VSCode Git plugin

 - Step 1: Open your `playground` repository.
 - Step 2: Add a new term to `glossary.md`.
 - Step 3: Commit the changes, but with a bad commit message.
 - Step 4: Open the Source Control Graph and locate the latest commit.
 - Step 5: Right-click the commit immediately before it and select **Reset Current Branch to Commit...**.
 - Step 6: Choose **Soft Reset**.
 - Step 7: Observe that the changes are still staged and ready to commit.
 - Step 8: Create a new commit with a better message.

////

//// tab | Using the command line

 - Step 1: Open your `playground` repository.
 - Step 2: Add a new term to `glossary.md`.
 - Step 3: Commit the changes, but with a bad commit message.
 - Step 4: View the commit history using `git log --oneline`.
 - Step 5: Undo the most recent commit while keeping the changes staged:

   `git reset --soft HEAD~1` or `git reset --soft <intended_commit_id>`

 - Step 6: Verify that the changes are still staged using `git status`.
 - Step 7: Commit the changes again using a better commit message.

////

## Git Revert

Unlike `git reset`, `git revert` does not remove commits from history. Instead, it creates a new commit that reverses the changes introduced by an earlier commit.

Because it preserves project history, `git revert` is often the preferred way to undo changes that have already been shared with others.

## Exercise: revert a commit

//// tab | Using the VSCode Git plugin

 - Step 1: Open your `playground` repository.
 - Step 2: Add a glossary entry called "Bad Definition".
 - Step 3: Commit the change.
 - Step 4: Open the Source Control Graph.
 - Step 5: Right-click the commit containing the glossary entry.
 - Step 6: Select **Revert Commit**.
 - Step 7: Observe that Git creates a new commit.
 - Step 8: Verify that the glossary entry has disappeared.

////

//// tab | Using the command line

 - Step 1: Open your `playground_NAME` repository.
 - Step 2: Add a glossary entry called "Bad Definition".
 - Step 3: Commit the change.
 - Step 4: Locate the commit using `git log --oneline`.
 - Step 5: Revert the commit:

   `git revert <COMMIT_HASH>`

 - Step 6: Verify that Git creates a new commit.
 - Step 7: Confirm that the glossary entry has been removed.

////

## Git Cherry-pick

Sometimes you only want a single commit from another branch rather than all of the work on that branch. For example, when your colleague has fixed a bug on their branch, but that branch is not ready to merge yet, you can cherry-pick it into your own branch. This will create the commit on your own branch, and if you and your colleague both merge, two identical commits will show up in the history, the later one seemingly not changing anything. Usually this is fine, but it can be a cause of **merge conflicts**....

## Exercise: copy a commit between branches

//// tab | Using the VSCode Git plugin

 - Step 1: Create a branch called `feature/glossary-improvements`.
 - Step 2: Add a new glossary term and commit it.
 - Step 3: Copy the commit hash from the Source Control Graph.
 - Step 4: Switch back to `main`.
 - Step 5: Create a second branch called `feature/documentation-update`.
 - Step 6: Right-click the commit from the first branch.
 - Step 7: Select **Cherry Pick Commit**.
 - Step 8: Verify that the glossary term now appears on the second branch.

////

//// tab | Using the command line

 - Step 1: Create a branch called `feature/glossary-improvements`.
 - Step 2: Add a new glossary term and commit it.
 - Step 3: Copy the commit hash using `git log --oneline`.
 - Step 4: Switch back to `main`.
 - Step 5: Create a second branch called `feature/documentation-update`.
 - Step 6: Run `git cherry-pick <COMMIT_HASH>`.
 - Step 7: Verify that the glossary term now exists on the second branch.

////

## Git Rebase

Rebasing allows you to replay your branch on top of the latest version of another branch, creating a cleaner and more linear project history. It essentially *moves* the starting point of your branch to the last commit of the branch on which you are rebasing, and then applies all the changes from your branch *after* it.

/// details | Rewriting history
    type: warning

Avoid using `git rebase` on commits that have already been shared with collaborators unless you understand the consequences. Rebasing rewrites project history. Are you ready for that?
///

## Exercise: rebase a feature branch

TODO: MAKE BETTER

//// tab | Using the VSCode Git plugin

 - Step 1: Create a branch called `feature/add-more-definitions`.
 - Step 2: Make two separate commits that add glossary terms.
 - Step 3: Switch back to `main`.
 - Step 4: Add another glossary term and commit it.
 - Step 5: Switch back to `feature/add-more-definitions`.
 - Step 6: Select **Rebase Branch...** from the Source Control menu.
 - Step 7: Choose `main` as the branch to rebase onto.
 - Step 8: Inspect the Source Control Graph and observe that your feature branch now sits on top of the latest commit from `main`.

////

//// tab | Using the command line

 - Step 1: Create a branch called `feature/add-more-definitions`.
 - Step 2: Make two separate commits that add glossary terms.
 - Step 3: Switch back to `main`.
 - Step 4: Add another glossary term and commit it.
 - Step 5: Switch back to `feature/add-more-definitions`.
 - Step 6: Run `git rebase main`.
 - Step 7: Inspect the history using `git log --oneline --graph`.
 - Step 8: Observe that the feature branch commits now appear after the latest commit on `main`.

////

## Works cited:
https://git-scm.com/book/en/v2
https://www.atlassian.com/git/tutorials
https://carpentries-incubator.github.io/python-intermediate-development/14-collaboration-using-git.html
