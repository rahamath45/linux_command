## Linux Journey - Grasshopper Module Documentation
### 1. Getting Started
What is Linux?: An open-source, Unix-like operating system kernel originally created by Linus Torvalds.
Linux Distributions: Operating system packages built around the Linux kernel with customized desktop environments, system tools, and software management. Key distributions include:
Ubuntu: Beginner-friendly and widely used for desktops and servers.
Debian: Known for strict stability and open-source principles.
Fedora: Cutting-edge feature testing bed sponsored by Red Hat.
Red Hat Enterprise Linux (RHEL): Commercial distribution tailored for enterprise deployments.
Linux Mint: User-friendly desktop environment based on Ubuntu/Debian.
Arch Linux: Lightweight, highly customizable rolling-release distribution.
Gentoo: Source-based distribution compiled specifically for hardware optimization.
OpenSUSE: Flexible distribution focused on ease of configuration via YaST.
Installation Basics: Choosing a distribution, creating bootable media, configuring disk partitions, and completing system installation.
### 2. Command Line
Command Line Interface (CLI): Text-based interface used to execute commands, automate tasks, and interact directly with the operating system shell.
Directory Navigation:
pwd (Print Working Directory): Displays the absolute path of the current directory.
cd (Change Directory): Navigates between system directories (e.g., cd /var/log, cd .. to go up one level).
ls (List): Displays files and folders in the active directory (ls -la displays hidden files and detailed file attributes).
File Operations:
mkdir: Creates new directories.
touch: Creates an empty file or updates access/modification timestamps.
cp: Copies files or directories (cp -r recursively copies folders).
mv: Moves or renames files and directories.
rm: Deletes files (rm -r recursively removes directories).
### 3. Text-Fu
File Viewing Commands:
cat: Concatenates and prints the full contents of a file directly to the stdout/terminal.
less: Interactive viewer allowing page-by-page forward and backward scrolling through text.
head: Displays the top lines of a file (default: 10 lines).
tail: Displays the bottom lines of a file (tail -f monitors live continuous log output).
Text Processing & Redirection:
grep: Searches for specified text patterns or regular expressions within files.
Output Redirection (>, >>): Directs command output to files (> overwrites existing file content, >> appends to file).
Pipelines (|): Chains commands together by passing the stdout of one command as stdin to the next.
### 4. Advanced Text-Fu
Terminal Text Editors: Command-line utilities for creating and modifying text files directly within the shell environment.
Vim Editor:
Modes: Command Mode (navigation and shortcuts), Insert Mode (editing text), Visual Mode (selecting text blocks).
Essential Shortcuts: i (enter Insert Mode), Esc (return to Command Mode), :w (save file), :q (quit), :wq or ZZ (save and quit).
Emacs Editor:
Keybindings: Utilizes Control (C-) and Meta/Alt (M-) modifier keys for commands.
Essential Shortcuts: C-x C-s (save file), C-x C-c (exit Emacs).
### 5. User Management
User Roles & Privilege Levels:
Root User (UID 0): Superuser account with unrestricted system access and administrative control.
Standard Users: Non-privileged accounts restricted to authorized files, home directories, and user commands.
User Account Administration:
useradd / adduser: Commands to create new user accounts.
usermod: Modifies user settings (group memberships, shell assignment, expiration).
userdel: Removes user accounts from the system.
System Configuration Files:
/etc/passwd: Stores account details including username, UID, primary GID, home directory, and default shell.
/etc/shadow: Stores encrypted password hashes and password aging parameters securely.
/etc/group: Defines system groups and list of assigned user accounts.
### 6. Permissions
Permission Types:
Read (r = 4): Permission to view file contents or list directory contents.
Write (w = 2): Permission to modify file contents or add/delete files in a directory.
Execute (x = 1): Permission to run files as scripts/binaries or navigate into directories.
Ownership Hierarchy: User/Owner (u), Group (g), Others/World (o).
Managing Permissions & Ownership:
chmod: Alters access permissions using symbolic mode (e.g., chmod u+x script.sh) or octal/numeric mode (e.g., chmod 755 file.txt).
chown: Changes user and group ownership of files and directories (e.g., chown user:group file).
chgrp: Updates group ownership specifically.
### 7. Processes
Process Overview: An active, running instance of a program identified by a unique Process ID (PID).
Process Monitoring Tools:
ps: Displays a static snapshot of current processes (ps aux lists all system processes).
top / htop: Interactive real-time system monitor displaying CPU, memory, and running process statistics.
kill: Sends signals to terminate processes by PID (e.g., kill -9 <PID> forces termination).
pkill: Terminates processes based on name matching.
Job Control:
Background Execution (&): Appending & runs commands asynchronously in the background.
jobs: Lists active jobs managed by the current shell session.
fg / bg: Brings background jobs to the foreground or resumes stopped jobs in the background.
### 8. Packages
Package Management Overview: System utilities designed to install, update, dependency-resolve, and uninstall software binaries cleanly.
Debian / Ubuntu Family:
dpkg: Low-level tool for directly managing local .deb package files.
apt-get / apt: High-level package manager that resolves dependencies automatically and fetches packages from remote repositories (apt update, apt install <package>).
Red Hat / Fedora / Enterprise Family:
rpm: Low-level utility for managing local .rpm package files.
yum / dnf: High-level package manager handling repository fetching and automatic dependency management (dnf install <package>).

