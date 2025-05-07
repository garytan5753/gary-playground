# Linux Commands
## Working with Directory and Files
| **Command** | **Description** | **Example Usage** |
|-------------|-----------------|-------------------|
| `echo`      | Prints a line of text or the value of an environment variable | `echo Hi` |
| `ls`        | Lists the contents of a directory | `ls` |
| `cd`        | Changes the current directory | `cd my_dir1` |
| `pwd`       | Displays the current working directory | `pwd` |
| `mkdir`     | Creates a new directory | `mkdir new_directory` |
| `rm`        | Removes files or directories | `rm sample_file.txt` |
| `cp`        | Copies files or directories (use `-R` for directories recursively) | `cp new_file.txt copy_file.txt` |
| `mv`        | Moves or renames files and directories | `mv new_file.txt sample_file.txt` |
| `touch`     | Creates a new, empty file | `touch new_file.txt` |

### Create an entire directory tree in single command, 
`mkdir -p /home/gary/folder1/subfoler1`

`-p` option ensures the entire directory tree is created if it not exist.

### Remove a direcrtory and its contents recursively
`rm -r /home/gary/folder1/subfolder1`

`-r` refer to recursive

### Create  an empty file
`touch gary.txt`

### Add content into a file using redirection
`cat > gary.txt`  
[Enter your content]  
`Press CTRL+D to save`

### Display the file contents
`cat gary.txt`

### Copy file
`cp file_name.txt to_be_copy_file_name.txt`  

### Copy file to another directory
`cp file_name.txt /home/user/Documents`

### Rename the while when copying
`cp file_name.txt /home/user/Documents/new_file_name.txt`

### Copy entire directory and contents to into another directory
`cp -R gary_dir/ /home/user/Documents`

### Move or rename file
`mv new_file_name.txt to_be_rename_file_name.txt`

### Move directory and contents inside to another directory
`my gary_dir /home/user/Documents/`  
*Note: unlike `cp`, `mv` does not require the `-R` option because it automatically moves directories recursively*

### Remove/Delete File
`rm gary.txt`

### Remove/Delete directory and all its contents recursively and forcefully
`rm -rf gary_dir`  
*Note: `r`(--recursive) Removes directories and contents recursively, `-f` (--force) Force removal without confirmation even files are write-protected*

## User Account Commands
### Check cuurent username is being use
`whoami`

### To retrieve detailed information about your user account—including user ID, group ID, and group memberships
`id`

### Switch to another user account
`su userB`

### SSH with username
`ssh username@hostname/ip`

### Sudo Privileges
`sudo ls /root`

### curl

| **Operation**                    | **Command Example**                                              | **Description**                                              |
|----------------------------------|------------------------------------------------------------------|--------------------------------------------------------------|
| Download a file                  | `curl -O https://example.com/file.zip`                           | Saves the file with its original name.                        |
| Save output to a specific file   | `curl -o newfile.zip https://example.com/file.zip`               | Saves the file as `newfile.zip`.                              |
| Follow redirects                 | `curl -L https://example.com`                                    | Follows HTTP redirects.                                       |
| Get HTTP headers only            | `curl -I https://example.com`                                    | Fetches only the HTTP headers.                                |
| Send a GET request               | `curl https://api.example.com/data`                              | Sends a simple GET request.                                   |
| Send a POST request              | `curl -X POST -d "param1=value1&param2=value2" https://example.com/post` | Sends form data with a POST request.                          |
| Send JSON with POST              | `curl -X POST -H "Content-Type: application/json" -d '{"key":"value"}' https://example.com/api` | Sends JSON data in a POST request.                            |
| Add custom headers               | `curl -H "Authorization: Bearer YOUR_TOKEN" https://api.example.com` | Adds an Authorization header to your request.                |
| Download silently (no progress)  | `curl -s -O https://example.com/file.zip`                        | Downloads a file without showing progress.                    |
| Check HTTP status code           | `curl -o /dev/null -s -w "%{http_code}\n" https://example.com`   | Prints only the HTTP status code.                             |

### Check Operating System

`cat /etc/*release*`

Example:

```bash
CentOS Linux release 7.7.1908 (Core)
Derived from Red Hat Enterprise Linux 7.7 (Source)
NAME="CentOS Linux"
VERSION="7 (Core)"
ID="centos"
ID_LIKE="rhel fedora"
VERSION_ID="7"
PRETTY_NAME="CentOS Linux 7 (Core)"
ANSI_COLOR="0;31"
CPE_NAME="cpe:/o:centos:7"
HOME_URL="https://www.centos.org/"
BUG_REPORT_URL="https://bugs.centos.org/"
```

## Package Management

### RPM-Based Package Management
Centos, Red Hat & Fedora

`i` - Install a package  
`-e` - Uninstall a package  
`-q` - Query package details  
*Note - RPM does not automatically resolve dependencies. For example, if you install Ansible—which requires Python and additional libraries—using RPM alone will not install missing dependencies.*

### Yum
- Overcome RPM limitations regarding dependencies.
- Yum retrieves packages from software repositories—collections of RPM packages stored locally or on remote servers.
- Repository configuration files are located in the `/etc/yum.repos.d/` directory.  

Example;  
`yum install ansible`

### List available repositories;  
`yum repolist`

### List configuration files that define these repositories;  
`ls /etc/yum.repos.d/`

### Upgrade to Newer Version

Example update repo using commands;  
`yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm`  
`yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm`

### List installed/available packages
`yum list ansible`

### Removing an installed package
`yum remove ansible`

### List all available package versions
`yum --showduplicates list ansible`

### Install specific version
`yum install ansible-X.X.X.X`
