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