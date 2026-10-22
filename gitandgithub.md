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