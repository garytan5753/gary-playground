# Vi Editor

### Open/Create a file using vi

`vi gary_file.txt`

### Edit/Save/Quit

- Insert `i` to enter into editing mode to edit the file.  
- Press `ESC`/`Escape` button to escape from the edit mode.
- Type `:w` to save the changes you made on the file
- Type `:q` to exit/quit without saving
- Type `:wq` to write/save and exit/quit
- Type `:q!` to exit/quit and discard the changes had made.

| **Operation**            | **Command**                     | **Description**                                      |
|--------------------------|----------------------------------|------------------------------------------------------|
| Navigation               | Arrow keys or `h`, `j`, `k`, `l` | Move left, down, up, and right respectively.          |
| Delete a character       | `x`                              | Delete the character under the cursor.                |
| Delete a line            | `dd`                             | Remove the entire line.                               |
| Copy a line       | `yy`                             | Copy the current line into the buffer.                |
| Paste copied content     | `p`                              | Paste the copied or deleted content.                  |
| Scroll up                | `Ctrl+u`                         | Scroll up within the document.                        |
| Scroll down              | `Ctrl+d`                         | Scroll down within the document.                      |
| Command prompt           | `:`                              | Enter further commands (e.g., save, quit).            |

### Search for specific text in the file in vi
Find a word or phrase, switch to command mode and type the following:  
`/texttosearch`  
*All occurrences of search word/phase will be highlighted. Press `N` to jump to the next match and continue pressing `N` to cycle through additional matches.*

