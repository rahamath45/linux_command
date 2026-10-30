rag.py-la code change panra — Working tree.

git add rag.py run panra — Staging area.

git commit -m "Add RAG retrieval" run panra — Local repository-la commit save aagum.

git push run pannina — commit remote repository-ku send aagum.

Object	        Enna seyyum?	                          Example
Blob	        File content-ai store pannum	       rag.py-oda content
Tree	        Files and directories-oda 
                structure-ai represent pannum	       Project folder structure
Commit       	Oru project snapshot-oda tree, 
                parent commit, author and message 
                pondra details-ai store pannum	         Add RAG retrieval
Annotated     	Oru specific commit-ku label 
   tag          and metadata kudukkum	                  v1.0.0

   1. HEAD
Nee ippo endha branch-la work pannura nu Git-ku therivikkum.

Example:
git switch feature/login


Ippo nee feature/login branch-la work pannura. HEAD andha branch-ai point pannum.
2. Detached HEAD
Branch-la illaama, oru specific old commit-la direct-ah irukkuradhu.

Example:
git checkout a1b2c3d


Ippo nee andha commit-ai paakkalaam. Aana idhula pudhu commit create pannina, adhu branch moolama track aagaama pogalaam.
3. ORIG_HEAD
Sila major Git operations-ku munnaadi irundha position-ai save panni vaikkum.

Example: Nee git reset maadhiri operation pannumbodhu, munnaadi irundha commit-ku thirumba pogaradhu useful-ah irukkalaam.
4. FETCH_HEAD
Remote repository-lendhu last-ah fetch pannina information-ai Git store pannum.

Example:
git fetch origin


GitHub-la irundhu latest changes patriya information-ai edukkum. FETCH_HEAD adhu sambandhamaana details-ai store pannum.
5. Tags
Oru important commit-ku name vaikkuradhu.

Example:
git tag v1.0


Un FastAPI project-oda first stable version-ai v1.0 nu identify pannalaam.


1.4 .git/, packfiles, git gc, git fsck
- .git/ — local Git metadata and repository information irukkura directory.
- Packfiles — Git objects-ai efficient-ah store panna use pannappadum.
- git gc — repository maintenance; objects-ai optimize pannalaam.
- git fsck — Git object database integrity-ai check panna use pannalaam.
- Reflog — local-la HEAD and references move aana history-ai track pannum; sila thappana operations-lendhu recover panna help aagum.
Practice-ku useful commands:
git rev-parse --show-toplevel
git log --oneline -5
git cat-file -t HEAD
git reflog -5


git cat-file -t HEAD usually commit nu output kudukkum.

git gc-a ippo run panna thevai illa. .git/-kulla irukkura files-ai direct-ah edit/delete pannavum vendaam.

Topic 2: Daily Git workflow
Ippo daily development-la nee use panna vendiya commands.
2.1 Repository status check
git status
git branch --show-current
git log --oneline -5


- status — modified, staged, untracked files.
- branch --show-current — current branch.
- log --oneline -5 — last 5 commits.
Rule: Edhuvum change pannuradhukku munnaadi git status check pannu.
2.2 git diff — enna change pannirukka?
git diff


Working tree-la irukkura unstaged changes-ai kaattum.
git diff --staged


Commit panna staging area-la ready-ah irukkura changes-ai kaattum.
git diff branchA...branchB


Rendu branches-oda common ancestor-lendhu branchB varaikkum irukkura changes-ai compare panna use aagum.
2.3 git add — changes select pannuradhu
git add filename.py


Oru file mattum stage pannum.
git add -p


Oru file-la irukkura changes-ai chunks-a review panni, thevaiyana parts mattum stage pannalaam.
git status
git diff --staged


Commit panna munnaadi staged changes correct-ah irukka nu check pannu.
2.4 git commit — local snapshot save pannuradhu
git commit -m "feat: add RAG retrieval"


Nalla commit message enna solludhu na, enna change pannirukka nu short-ah explain pannanum.

Examples:
- feat: add recipe search API
- fix: handle missing embedding
- docs: update setup instructions
- test: add retrieval unit tests
Atomic commit: Oru commit-la oru logically related change mattum irundha review and debugging easy-aagum.
git commit --amend
git commit --amend


Last commit-ai amend panna use aagum. Idhu previous commit-ai replace pannum; already shared/pushed commits-ku use pannumbodhu careful-ah irukkanum. Team workflow puriyaama use panna vendaam.
2.5 git restore — changes discard/unstage pannuradhu
git restore --staged filename.py


File-ai staging area-lendhu remove pannum; working tree-la irukkura edits-ai retain pannum.
git restore filename.py


Staged aagaadha working-tree edits-ai discard pannum. Idhu changes-ai lose panna vaikkalaam. File-la important work irundha run panna vendaam.
2.6 git switch — branch change pannuradhu
git switch branch-name


Existing branch-ku switch pannum.
git switch -c feature/rag-search


Pudhu branch create panni adhukku switch pannum.

Un office rule padi main-la direct-ah work panna vendaam. Existing repo-la practice panna munnaadi current branch, uncommitted changes, and team rules check pannanum. Existing uncommitted work irundha pudhu branch-ku switch pannuradhukku munnaadi stop panni verify pannu.
2.7 git stash — work-ai temporary-ah save pannuradhu
git stash push -m "WIP: retrieval changes"
git stash list
git stash apply


- stash push — temporary-ah changes save pannum.
- stash list — saved stashes list.
- stash apply — saved changes-ai thirumba apply pannum; stash-ai delete pannaadhu.
git stash pop apply pannitu stash-ai remove panna try pannum. Conflict irundha careful-ah handle pannanum.
2.8 .gitignore
AI projects-la .env, Python virtual environment, cache files, generated data pondravai accidentally commit aagama irukka .gitignore use pannuvom.

Example:
.env
.venv/
__pycache__/
*.pyc


Already Git track pannura file-ai .gitignore mattum add pannina tracking stop aagaadhu. Adhukku separate action thevaippadum.

---

# Topic 3: Branching and History

Branch-nu sonna enna? Un project-oda main code-lendhu oru separate line of development create pannuradhu. Idhu moolama nee main code-ai paathukaappaa vachukittu, pudhu features try pannalaam, bugs fix pannalaam.

---

## 3.1 Merge Types — Branches-ai merge pannura vazhigal

Rendu branches-oda work-ai combine panra process-ku "merge" nu soldrom. Naalu vazhigal irukku:

### a) Fast-Forward Merge
Main branch-la extra commits illaama, feature branch mattum munnaadi poirundhaa, Git simple-ah pointer-ai move pannum. Pudhu merge commit create aagaadhu.

```bash
# Setup: main branch-la irundhukittu feature branch create pannu
git switch main
git switch -c feature/fast-forward-demo

# Feature branch-la oru commit pannu
echo "fast forward feature" > ff_demo.txt
git add ff_demo.txt
git commit -m "feat: add fast-forward demo file"

# Main-ku thirumba poi merge pannu
git switch main
git merge feature/fast-forward-demo

# Log paaru — merge commit illa, direct-ah pointer move aagirukkum
git log --oneline -5
```
**Output-la:** Separate merge commit irukkaadhu. feature branch-oda commit directly main-la varum.

---

### b) Three-Way Merge
Main branch-layum feature branch-layum separate commits irundha, Git rendu branches-um adhoda common ancestor-um (moonu points) vachchi oru **new merge commit** create pannum.

```bash
git switch main
git switch -c feature/three-way-demo

# Feature branch-la commit
echo "three way feature" > tw_demo.txt
git add tw_demo.txt
git commit -m "feat: add three-way demo"

# Main-ku poi verum commit pannu (so both branches diverge)
git switch main
echo "main change" > main_change.txt
git add main_change.txt
git commit -m "chore: add main change"

# Ippo merge — three-way merge aagum
git merge feature/three-way-demo

# Log paaru — merge commit irukkum
git log --oneline --graph -5
```
**Output-la:** `Merge branch 'feature/three-way-demo'` nu oru extra merge commit varum.

---

### c) --no-ff (No Fast-Forward)
Fast-forward possible-aana situation-layum force-ah merge commit create panna --no-ff use pannalaam. Idhu history-la "indha feature branch merge aachu" nu clear-ah theriyum.

```bash
git switch main
git switch -c feature/noff-demo

echo "no-ff demo" > noff.txt
git add noff.txt
git commit -m "feat: add no-ff demo"

git switch main
git merge --no-ff feature/noff-demo -m "merge: no-ff demo branch"

git log --oneline --graph -5
```
**Output-la:** Fast-forward possible-aanalum, merge commit create aagirukkum.

---

### d) Squash Merge
Feature branch-la 5 commits irundha, main-la merge pannum bodhu ellaa changes-aiyum **oru single commit-ah** konduvara squash use aagum. Clean history kidaikkum.

```bash
git switch main
git switch -c feature/squash-demo

echo "file1" > sq1.txt && git add sq1.txt && git commit -m "feat: sq1"
echo "file2" > sq2.txt && git add sq2.txt && git commit -m "feat: sq2"
echo "file3" > sq3.txt && git add sq3.txt && git commit -m "feat: sq3"

git switch main
git merge --squash feature/squash-demo
git commit -m "feat: squash merge all squash-demo changes"

git log --oneline -5
```
**Output-la:** 3 commits ellaam oru single commit-ah main-la varum.

---

## 3.2 Rebase vs Merge — Eppo edha use pannuradhu?

### Merge
- Rendu branches-oda history-ai preserve pannum
- Merge commit create aagum
- Team-oda shared branches-ku safe

### Rebase
- Un branch-oda commits-ai main branch-oda latest commit-ku mela "replay" pannum
- Clean, linear history kidaikkum
- **⚠️ RULE: Shared/pushed branch-la NEVER rebase pannaadhe!** Teammates-oda work mess aagum.

```bash
# Rebase example
git switch main
git switch -c feature/rebase-demo

echo "rebase work" > rb.txt
git add rb.txt
git commit -m "feat: rebase demo"

# Main-la vera commit add aagudhu nu assume pannu
git switch main
echo "main update" > main_update.txt
git add main_update.txt
git commit -m "chore: main update"

# Feature branch-ku poi rebase pannu
git switch feature/rebase-demo
git rebase main

# Ippo feature branch main-oda latest-ku mela move aagirukkum
git log --oneline --graph -5
```

**Eppo Merge use pannuradhu:**
- Shared/team branches (main, develop)
- History preserve panna vendumna

**Eppo Rebase use pannuradhu:**
- Un own feature branch-ai main-oda latest-ku update panna
- Clean linear history venum na
- Push pannaadhA private branch-la mattum

---

## 3.3 Interactive Rebase — Commits-ai edit/reorder/squash pannuradhu

Un feature branch-la 5 messy commits irukku. Push pannuradhukku munnaadi clean up panna interactive rebase use pannu.

```bash
# Last 3 commits-ai interactive-ah edit panna
git rebase -i HEAD~3
```

Editor open aagum, idhu maadiri kaattum:
```
pick abc1234 feat: add login
pick def5678 fix: typo in login
pick ghi9012 feat: add logout
```

**Available actions:**
| Command | Enna seyyum? |
|---------|-------------|
| `pick` | Commit-ai adhe maadiri vachukko |
| `reword` | Commit message-ai maattu |
| `squash` | Munnaadi irukkura commit-oda combine pannu (messages merge aagum) |
| `fixup` | squash maadiri, aana indha commit-oda message-ai throw away pannum |
| `drop` | Commit-ai delete pannu |
| `edit` | Commit-la stop panni changes pannu |

```bash
# Example: Last 2 commits-ai squash pannu
git rebase -i HEAD~2
# Editor-la second commit-oda "pick" -> "squash" maathu, save pannu

# --autosquash — fixup! prefix commit-ai automatically squash pannum
git commit --fixup=HEAD~1
git rebase -i --autosquash HEAD~3
```

---

## 3.4 Cherry-Pick — Specific commit(s) mattum edukkaradhu

Vera branch-la irukkura oru particular commit-ai un branch-la apply panna cherry-pick use pannu.

```bash
# Oru specific commit cherry-pick
git cherry-pick <commit-hash>

# -x flag — original commit hash-ai message-la reference-ah add pannum
git cherry-pick -x <commit-hash>

# Range of commits cherry-pick (A exclusive, B inclusive)
git cherry-pick A..B

# Cherry-pick-la conflict vandha
git cherry-pick <commit-hash>
# Conflict resolve pannu (files edit pannu)
git add .
git cherry-pick --continue

# Cherry-pick cancel panna
git cherry-pick --abort
```

**Practice:**
```bash
# Vera branch-la commit hash paaru
git log feature/some-branch --oneline -5

# Adha un current branch-la apply pannu
git cherry-pick -x abc1234
```

---

## 3.5 Conflict Resolution — Merge/Rebase conflicts handle pannuradhu

Rendu branches same file-la same line-ai maathina, Git-ku confusion — idhukkudhan "conflict" nu solrom.

### Conflict markers epdi theriyum:
```
<<<<<<< HEAD
Un current branch-oda code
=======
Incoming branch-oda code
>>>>>>> feature/branch
```

### Resolve panna steps:
```bash
# 1. Conflict irukkura files paaru
git status

# 2. File open panni conflict markers remove pannu
#    <<<<<<< ======= >>>>>>> ellam edukka vendiyathu
#    Correct code mattum vachukko

# 3. Resolved files add pannu
git add <resolved-file>

# 4. Merge continue pannu
git merge --continue
# (or rebase-la irundhaa)
git rebase --continue

# 5. Abort panna (everything revert aagum)
git merge --abort
git rebase --abort
```

### ours vs theirs — enna difference?
**Merge-la:**
- `ours` = un current branch (HEAD)
- `theirs` = incoming branch

**Rebase-la (FLIP aagum! ⚠️):**
- `ours` = rebase target (main) — because Git replays on top of it
- `theirs` = un commits

```bash
# Merge-la — un branch version keep panna
git checkout --ours <file>
git add <file>

# Merge-la — incoming branch version keep panna
git checkout --theirs <file>
git add <file>
```

### rerere — Repeated conflicts auto-resolve
```bash
# Enable rerere (reuse recorded resolution)
git config --global rerere.enabled true

# Ippo nee oru conflict resolve pannina, Git remember pannum
# Adhey conflict next time vandha auto-resolve pannidum
```

### mergetool — GUI tool use pannuradhu
```bash
# Default mergetool use pannu
git mergetool

# Specific tool set pannu (example: VS Code)
git config --global merge.tool vscode
git config --global mergetool.vscode.cmd 'code --wait $MERGED'
```

---

## 3.6 range-diff — Rebased branch compare pannuradhu

Nee oru branch rebase pannina appo, old version-um new version-um compare panna range-diff use pannu.

```bash
# Syntax: git range-diff base old-tip new-tip
git range-diff main feature/old-version feature/new-version

# Example: Rebase pannuradhukku munnaadi reflog-la old tip note pannu
git reflog
# Suppose old tip = abc1234, new tip = def5678
git range-diff main abc1234 def5678
```

**Idhu useful-ah irukku because:**
- Rebase-la commit hash maaridum
- Normal diff enna maarichu nu kaattaadhu
- range-diff commit-by-commit compare pannum

---

## 🧪 Section 3 — Terminal-la Practice Pannu!

```bash
# 1. Merge types try pannu
git switch main
git switch -c test/merge-practice
echo "test merge" > merge_test.txt
git add . && git commit -m "feat: merge test"
git switch main
git merge --no-ff test/merge-practice -m "merge: practice branch"
git log --oneline --graph -5

# 2. Interactive rebase try pannu
git switch -c test/rebase-practice
echo "a" > a.txt && git add . && git commit -m "add a"
echo "b" > b.txt && git add . && git commit -m "add b"
echo "c" > c.txt && git add . && git commit -m "add c"
git rebase -i HEAD~3
# Editor-la "squash" try pannu

# 3. Cherry-pick try pannu
git switch main
git log test/rebase-practice --oneline -3
# Copy a commit hash
git cherry-pick -x <paste-commit-hash>

# 4. Stash + branch switch practice
git switch -c test/stash-practice
echo "work in progress" > wip.txt
git add wip.txt
git stash push -m "WIP: testing stash"
git stash list
git switch main
git switch test/stash-practice
git stash pop

# 5. Conflict resolution practice
git switch main
echo "main version" > conflict_test.txt
git add . && git commit -m "main: add conflict test"
git switch -c test/conflict-practice
echo "feature version" > conflict_test.txt
git add . && git commit -m "feat: conflict test"
git switch main
git merge test/conflict-practice
# Conflict varum! File edit panni resolve pannu
# git add conflict_test.txt
# git merge --continue
```