# Tree-into-Shadow
A unique privilege escalation vector exploiting the `tree` binary via the `--fromfile` parameter. Demonstrates how to exfiltrate and map root password hashes directly from `/etc/shadow`. This can be used when the SUID permissions are set on this binary for example. 

## The Technique: Tree Arbitrary File Disclosure

In misconfigured Linux environments or Capture The Flag (CTF) scenarios, the `tree` binary might be granted elevated capabilities or custom SUID execution permissions. While `tree` does not explicitly contain functions to view file contents (like `cat` or `less`), it features an architectural parameter: `--fromfile`.

### How the Infiltration Works
The `--fromfile` argument forces `tree` to treat every single line of an inputted text file as a relative path to a directory structure rather than scanning the actual local disk. 

When an attacker points a privileged `tree` command directly at a protected system configuration ledger:
```bash
tree --fromfile /etc/shadow
```

The binary reads each structural authentication profile configuration entry, including raw cryptographic hash fields (e.g., `root:$6$vK9!...:19842:0:99999:7:::`), and renders the complete line content out onto the screen disguised as terminal tree branches (`├──` and `└──`).

This utility sanitizes those visual structural branch indicators, parses broken multi-line string buffers, and restores the configuration blocks back into a pure layout format suitable for immediate auditing or offline brute-force cracking tools like Hashcat or John the Ripper.

---

## Features
- **Automated Sanitation:** Strips out complex terminal tree branches (`├──`, `└──`, `│`).
- **Multi-line Concatenation:** Intelligently strings back together fragmented hash sequences broken by `tree` layout rules.
- **Flexible Terminal Outputs:** Save directly to a local target output map or output the plain format stream cleanly into standard pipelines.

---

## Usage

### Basic Parsing (Standard Output)
Print the sanitized configurations directly onto the terminal layer:
```bash
python3 Tree-into-Shadow.py -i broken_tree_output.txt
```

### Save Output with Terminal Visibility
Isolate the restored profile records straight into a dedicated ledger while maintaining screen trace validation via the `--show` (`-s`) flag:
```bash
python3 Tree-into-Shadow.py -i broken_tree_output.txt -o restored_shadow.txt --show
```

### Command Line Arguments
```text
options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Path to the broken tree output file
  -o OUTPUT, --output OUTPUT
                        Path to save the reconstructed shadow file (optional)
  -s, --show            Print full reconstructed shadow content to terminal 
                        even if output file is specified
```

<img width="1126" height="606" alt="afbeelding" src="https://github.com/user-attachments/assets/fb8660a1-1310-4979-8e1b-f308d3025dd2" />
