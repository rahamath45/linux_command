# Linux Journey - Grasshopper Module 🐧

A structured documentation of the **Linux Journey - Grasshopper Module**, covering Linux basics, command-line operations, text processing, editors, user management, permissions, processes, and package management.

## Table of Contents

- [Getting Started](#1-getting-started)
- [Command Line](#2-command-line)
- [Text-Fu](#3-text-fu)
- [Advanced Text-Fu](#4-advanced-text-fu)
- [User Management](#5-user-management)
- [Permissions](#6-permissions)
- [Processes](#7-processes)
- [Packages](#8-packages)
- [Quick Command Reference](#quick-command-reference)

---

## 1. Getting Started

### What is Linux?

Linux is an open-source, Unix-like operating system kernel originally created by **Linus Torvalds**.

Linux is widely used in:

- Desktop computers
- Servers
- Cloud infrastructure
- Embedded systems
- Containers
- DevOps environments

### Linux Distributions

A Linux distribution (distro) is an operating system built around the Linux kernel with its own system tools, package managers, desktop environments, and software.

| Distribution | Description |
|---|---|
| **Ubuntu** | Beginner-friendly and widely used for desktops and servers. |
| **Debian** | Known for stability and strong open-source principles. |
| **Fedora** | Modern distribution used for testing newer technologies, sponsored by Red Hat. |
| **RHEL** | Enterprise-focused commercial Linux distribution from Red Hat. |
| **Linux Mint** | User-friendly desktop distribution based on Ubuntu/Debian. |
| **Arch Linux** | Lightweight and highly customizable rolling-release distribution. |
| **Gentoo** | Source-based distribution that can be compiled for specific hardware. |
| **openSUSE** | Flexible distribution with configuration tools such as YaST. |

### Installation Basics

1. Choose a Linux distribution
2. Download the installation image
3. Create bootable installation media
4. Configure disk partitions
5. Install the operating system
6. Create a user account
7. Configure the system after installation

---

## 2. Command Line

### Command Line Interface (CLI)

The CLI is a text-based interface used to interact with the operating system by entering commands. It can be used to:

- Navigate directories
- Create and manage files
- Install software
- Manage users
- Monitor processes
- Automate tasks
- Configure the system

### Directory Navigation

**`pwd`** — Displays the Present Working Directory.
```bash
pwd
# /home/user
```

**`cd`** — Changes the current directory.
```bash
cd /var/log      # move to a directory
cd ..             # move to parent directory
cd ~              # go to home directory
```

**`ls`** — Lists files and directories.
```bash
ls
ls -l    # detailed information
ls -la   # include hidden files
```

### File Operations

**`mkdir`** — Creates a new directory.
```bash
mkdir project
mkdir -p project/src/components   # nested directories
```

**`touch`** — Creates an empty file or updates its timestamp.
```bash
touch file.txt
```

**`cp`** — Copies files.
```bash
cp file.txt backup.txt
cp -r project backup   # copy directory recursively
```

**`mv`** — Moves or renames files and directories.
```bash
mv old.txt new.txt                      # rename
mv file.txt /home/user/Documents/       # move
```

**`rm`** — Removes files.
```bash
rm file.txt
rm -r project   # remove directory and contents
```

> ⚠️ **Warning:** `rm` permanently removes files. Use it carefully.

---

## 3. Text-Fu

### File Viewing Commands

**`cat`** — Displays complete file contents.
```bash
cat file.txt
cat file1.txt file2.txt   # combine files
```

**`less`** — Displays a file one page at a time.
```bash
less file.txt
```

| Key | Action |
|---|---|
| `Space` | Move forward one page |
| `b` | Move backward one page |
| `↑ / ↓` | Move line by line |
| `q` | Quit |

**`head`** — Displays the first 10 lines by default.
```bash
head file.txt
head -n 20 file.txt
```

**`tail`** — Displays the last 10 lines by default.
```bash
tail file.txt
tail -n 20 file.txt
tail -f app.log   # monitor a file continuously (commonly used for logs)
```

### Text Searching

**`grep`** — Searches for text or patterns inside files.
```bash
grep "Linux" file.txt
grep -r "Linux" .      # search recursively
grep -i "linux" file.txt   # ignore case
```

### Output Redirection

| Operator | Description |
|---|---|
| `>` | Overwrites existing file content |
| `>>` | Appends content to an existing file |

```bash
echo "Hello Linux" > file.txt
echo "Another line" >> file.txt
```

### Pipelines

The pipe operator `|` sends the output of one command as input to another.

```bash
cat file.txt | grep "Linux"
ls -la | grep ".txt"
```

Pipelines allow multiple commands to be combined for more complex operations.

---

## 4. Advanced Text-Fu

### Terminal Text Editors

Common terminal editors include:

- Vim
- Emacs
- Nano

### Vim Editor

Vim is a powerful command-line text editor.

**Vim Modes**

| Mode | Purpose |
|---|---|
| Command Mode | Navigation and commands |
| Insert Mode | Enter and edit text |
| Visual Mode | Select text |

**Essential Vim Commands**

| Command | Action |
|---|---|
| `i` | Enter Insert Mode |
| `Esc` | Return to Command Mode |
| `:w` | Save |
| `:q` | Quit |
| `:wq` | Save and quit |
| `ZZ` | Save and quit |

```bash
vim file.txt
```

### Emacs Editor

**Essential Emacs Shortcuts**

| Shortcut | Action |
|---|---|
| `Ctrl + X, Ctrl + S` | Save |
| `Ctrl + X, Ctrl + C` | Exit |

```bash
emacs file.txt
```

---

## 5. User Management

Linux is a multi-user operating system. Users can have different permissions and access levels.

### User Roles

**Root User** — UID 0, unrestricted administrative access. Root can:
- Install and remove software
- Create and delete users
- Modify system configuration
- Change file ownership
- Manage system services

**Standard Users** — Limited permissions; access only to authorized resources.

### User Account Commands

```bash
sudo useradd username        # create a new user
sudo adduser username        # interactive user creation (Debian-based)
sudo usermod -aG groupname username   # add user to a supplementary group
sudo userdel username        # delete a user account
```

### Important System Files

| File | Description |
|---|---|
| `/etc/passwd` | Basic user account info: username, UID, primary GID, home directory, default shell |
| `/etc/shadow` | Password hashes and password-aging info (requires admin privileges) |
| `/etc/group` | Group information and members |

```bash
cat /etc/passwd
sudo cat /etc/shadow
cat /etc/group
```

---

## 6. Permissions

Linux uses permissions to control access to files and directories.

### Permission Types

| Permission | Symbol | Value | Description |
|---|---|---|---|
| Read | `r` | 4 | Read file contents or list directory contents |
| Write | `w` | 2 | Modify files or create/delete files in a directory |
| Execute | `x` | 1 | Execute files or enter directories |

### Permission Categories

Permissions are assigned to three categories: **User/Owner (u)**, **Group (g)**, **Others (o)**.

```
-rwxr-xr--
```
```
User    → rwx
Group   → r-x
Others  → r--
```

### `chmod`

**Symbolic Mode**
```bash
chmod u+x script.sh   # add execute for owner
chmod g+w file.txt    # add write for group
```

**Numeric / Octal Mode**
```
r = 4
w = 2
x = 1
```
```bash
chmod 755 script.sh
```
`755` means:
```
Owner  → rwx → 7
Group  → r-x → 5
Others → r-x → 5
```

### `chown` / `chgrp`

```bash
sudo chown user:group file.txt
sudo chown nisha:developers project.txt

sudo chgrp developers file.txt
```

---

## 7. Processes

A **process** is a running instance of a program. Every process has a unique **Process ID (PID)**.

### Process Monitoring

```bash
ps          # snapshot of running processes
ps aux      # detailed information

top         # real-time process/system resource info
htop        # interactive alternative to top (may need separate install)
```

`top` commonly displays: CPU usage, memory usage, process IDs, running processes, system load.

### Killing Processes

```bash
kill <PID>       # send a signal to a process
kill -9 <PID>    # forcefully terminate

pkill process_name   # terminate by process name
```

> ⚠️ Use `kill -9` carefully — it terminates a process immediately without allowing normal cleanup.

### Job Control

```bash
python app.py &   # run in background

jobs   # list background jobs
fg     # bring a background job to foreground
bg     # resume a stopped job in background
```

---

## 8. Packages

Package managers are used to install, update, remove software, resolve dependencies, and download packages from repositories. Different distros use different package managers.

### Debian / Ubuntu Family

**`dpkg`** — Low-level tool for local `.deb` packages.
```bash
sudo dpkg -i package.deb
```

**`apt`** — High-level package manager.
```bash
sudo apt update              # update package info
sudo apt upgrade             # upgrade installed packages
sudo apt install <package>   # install a package
sudo apt remove <package>    # remove a package
apt search <package>         # search for a package
```

**`apt-get`** — Commonly used in scripts.
```bash
sudo apt-get update
sudo apt-get install <package>
```

### Red Hat / Fedora / Enterprise Family

**`rpm`** — Low-level utility for `.rpm` packages.
```bash
sudo rpm -i package.rpm
```

**`dnf`** — High-level package manager for modern Fedora/RHEL-family.
```bash
sudo dnf install <package>
sudo dnf update
sudo dnf remove <package>
```

**`yum`** — Older tool, now a compatibility interface to `dnf` on many modern systems.
```bash
sudo yum install <package>
```

---

## Quick Command Reference

| Command | Purpose |
|---|---|
| `pwd` | Print current working directory |
| `cd` | Change directory |
| `ls` | List files and directories |
| `mkdir` | Create a directory |
| `touch` | Create a file |
| `cp` | Copy files/directories |
| `mv` | Move or rename files/directories |
| `rm` | Remove files/directories |
| `cat` | Display file contents |
| `less` | View files page by page |
| `head` | Display beginning of a file |
| `tail` | Display end of a file |
| `grep` | Search text patterns |
| `chmod` | Change permissions |
| `chown` | Change ownership |
| `chgrp` | Change group ownership |
| `ps` | Display processes |
| `top` | Monitor processes |
| `htop` | Interactive process monitor |
| `kill` | Send a signal to a process |
| `pkill` | Kill processes by name |
| `jobs` | List shell jobs |
| `fg` | Bring a job to foreground |
| `bg` | Resume a job in background |
| `dpkg` | Manage `.deb` packages |
| `apt` | Manage Debian/Ubuntu packages |
| `rpm` | Manage `.rpm` packages |
| `dnf` | Manage Fedora/RHEL-family packages |
| `yum` | Traditional Red Hat-family package manager |

---

## Conclusion

This module provides the fundamental Linux knowledge required to work with the command line, manage files and users, control permissions, monitor processes, edit files, and manage software packages.

These concepts form an important foundation for:

- Linux Administration
- DevOps
- Cloud Computing
- Backend Development
- Software Engineering
- Cybersecurity
- System Administration