Linux Journey - Grasshopper Module Documentation

1. Getting Started

What is Linux?

Linux is an open-source, Unix-like operating system kernel originally
created by Linus Torvalds.

Linux Distributions

Linux distributions are operating system packages built around the Linux
kernel with customized desktop environments, system tools, and software
management.

Key distributions include:

Ubuntu: Beginner-friendly and widely used for desktops and
servers.

Debian: Known for strict stability and open-source principles.

Fedora: Cutting-edge feature testing bed sponsored by Red Hat.

Red Hat Enterprise Linux (RHEL): Commercial distribution
tailored for enterprise deployments.

Linux Mint: User-friendly desktop environment based on
Ubuntu/Debian.

Arch Linux: Lightweight, highly customizable rolling-release
distribution.

Gentoo: Source-based distribution compiled specifically for
hardware optimization.

OpenSUSE: Flexible distribution focused on ease of configuration
via YaST.

Installation Basics

Basic installation involves:

Choosing a Linux distribution.

Creating bootable installation media.

Configuring disk partitions.

Completing the system installation.

2. Command Line

Command Line Interface (CLI)

The Command Line Interface (CLI) is a text-based interface used to
execute commands, automate tasks, and interact directly with the
operating system shell.

Directory Navigation

Command    Description                                            Example

pwd      Displays the absolute path of the current directory.   pwd
cd       Navigates between directories.                         cd /var/log
cd ..    Moves up one directory level.                          cd ..
ls       Lists files and folders.                               ls
ls -la   Lists hidden files with detailed attributes.           ls -la

File Operations

Command                 Description             Example

mkdir                 Creates a new           mkdir project
directory.

touch                 Creates an empty file   touch file.txt
or updates timestamps.

cp                    Copies files or         cp file.txt backup.txt
directories.

cp -r                 Recursively copies      cp -r project backup
directories.

mv                    Moves or renames files  mv old.txt new.txt
and directories.

rm                    Deletes files.          rm file.txt

3. Text-Fu

File Viewing Commands

Command                             Description

cat                               Concatenates and prints the full
contents of a file directly to the
terminal.

less                              Interactive viewer allowing
page-by-page forward and backward
scrolling through text.

head                              Displays the top lines of a file.
Default is 10 lines.

tail                              Displays the bottom lines of a
file.

Text Processing & Redirection

grep

Searches for specified text patterns or regular expressions within
files.

Output Redirection

> overwrites existing file content.

>> appends output to an existing file.

Example:

echo "Hello Linux" > file.txt
echo "Another line" >> file.txt

Pipelines

The | operator chains commands together by passing the standard output
(stdout) of one command as the standard input (stdin) to another.

Example:

cat file.txt | grep "Linux"

4. Advanced Text-Fu

Terminal Text Editors

Terminal text editors are command-line utilities used to create and
modify text files directly within the shell.

Vim Editor

Modes

Command Mode: Used for navigation and shortcuts.

Insert Mode: Used for editing text.

Visual Mode: Used for selecting text blocks.

Essential Shortcuts

Shortcut   Action

i        Enter Insert Mode
Esc      Return to Command Mode
:w       Save the file
:q       Quit Vim
:wq      Save and quit
ZZ       Save and quit

Emacs Editor

Emacs uses Control (C-) and Meta/Alt (M-) modifier keys for
commands.

Essential Shortcuts

Shortcut    Action

C-x C-s   Save the file
C-x C-c   Exit Emacs

5. User Management

User Roles & Privilege Levels

Root User (UID 0): Superuser account with unrestricted system
access and administrative control.

Standard Users: Non-privileged accounts restricted to authorized
files, home directories, and user commands.

User Account Administration

Command                             Description

useradd / adduser               Creates new user accounts.

usermod                           Modifies user settings, group
memberships, shell assignment, and
expiration.

userdel                           Removes user accounts.

System Configuration Files

File                                Description

/etc/passwd                       Stores account details including
username, UID, primary GID, home
directory, and default shell.

/etc/shadow                       Stores password hashes and password
aging parameters securely.

6. Permissions

Permission Types

Permission                    Symbol        Numeric Value Description

Read                             r                    4 View file contents
or list directory
contents.

Write                            w                    2 Modify file
contents or
add/delete files
in a directory.

Ownership Hierarchy

Linux permissions are organized around:

User/Owner (u)

Group (g)

Others/World (o)

Managing Permissions & Ownership

chmod

Changes access permissions using symbolic or numeric/octal modes.

Examples:

chmod u+x script.sh
chmod 755 file.txt

chown

Changes user and group ownership.

Example:

chown user:group file

chgrp

Changes the group ownership of a file or directory.

7. Processes

Process Overview

A process is an active, running instance of a program. Each process is
identified by a unique Process ID (PID).

Process Monitoring Tools

Command    Description

ps       Displays a static snapshot of current processes.
ps aux   Lists all system processes.
top      Interactive real-time system monitor.
htop     Interactive process and resource monitor.
kill     Sends signals to a process by PID.
pkill    Terminates processes based on name matching.

Example:

kill -9 <PID>

kill -9 sends a forceful termination signal to the specified process.

Job Control

Command   Description

&       Runs a command asynchronously in the background.
jobs    Lists active jobs managed by the current shell session.
fg      Brings a background job to the foreground.
bg      Resumes a stopped job in the background.

Example:

python app.py &

8. Packages

Package Management Overview

Package management utilities are used to install, update, resolve
dependencies, and uninstall software cleanly.

Debian / Ubuntu Family

Tool                                Purpose

dpkg                              Low-level tool for directly
managing local .deb package
files.

Common commands:

sudo apt update
sudo apt install <package>

Red Hat / Fedora / Enterprise Family

Tool                                Purpose

rpm                               Low-level utility for managing
local .rpm package files.

Example:

sudo dnf install <package>

Quick Command Reference

pwd       Print current working directory
cd        Change directory
ls        List files and directories
mkdir     Create directory
touch     Create file
cp        Copy files/directories
mv        Move or rename files/directories
rm        Remove files/directories
cat       Display file contents
less      View files interactively
head      Show beginning of a file
tail      Show end of a file
grep      Search text patterns
chmod     Change permissions
chown     Change ownership
chgrp     Change group ownership
ps        View processes
top       Monitor processes
kill      Send a signal to a process
pkill     Kill processes by name
jobs      List shell jobs
fg        Bring job to foreground
bg        Resume job in background
apt       Manage Debian/Ubuntu packages
dpkg      Manage local .deb packages
dnf       Manage Fedora/RHEL-family packages
rpm       Manage local .rpm packages