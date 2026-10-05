import argparse
import re
import sys

def logo():
    logo = '''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠖⠒⠢⣄⣀⡀⣀⣀⠀⡠⠔⠒⠒⢤⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⡇⠀⠀⠀⠁⠠⡋⠀⠀⠙⠦⠀⠀⠀⠀⣧⠤⣀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡠⠖⠊⠑⠲⣄⣀⣠⠖⠘⠛⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⢸⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣸⣇⡀⠀⠀⠈⠁⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠋⠲⣄⠀⠀
⠀⠀⠀⠀⣠⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠂⠀
⠀⠀⠀⢀⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⢱⠀⠀⠀⠀⠀⠀⠀⠐⠺⡄⠀⠀
⠀⡠⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡀⠀⢀⡼⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇⠀⠀
⢰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠈⠉⠁⡹⠀⠀⠀⣄⣀⡠⠟⢘⣯⣀⠀⠀
dot⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡷⠺⡍⠒⣿⣀⣠⡀⠀⠀⠀⠀⠀⠈⠀⠈⡷⠀
⠀⢸⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⠺⡁⠀⠙⠚⠀⠁⡏⢧⣀⡄⠀⠀⠀⠀⠐⠒⣇⠀
⠀st⣄⣀⣰⠀⠀⠀⠀⠀⠀⠲⣟⣿⡦⣷⠀⠀⠀⠀⢠⠁⣸⣿⣷⢶⡆⢀⣤⡀⣠⡾⠁
⠀⠀⠀⠀⠱⣀⠀⢀⡱⠄⠤⠜⠋⠻⡄⠀⠀⠀⠀⠀⣸⣴⡿⣏⠀⢀⣭⣁⣀⡽⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠸⠀⠀⠀⠀⠀⣿⡼⠁⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡆⠀⠀⠀⠀⢿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ╔╦╗┬─┐┌─┐┌─┐  ┬┌┐┌┌┬┐┌─┐  ┌─┐┬ ┬┌─┐┌┬┐┌─┐┬ ┬
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣧⠀⠀⠀⠀⠸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ║ ├┬┘├┤ ├┤   ││││ │ │ │  └─┐├─┤├─┤ │││ ││││
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠁⠀⠀⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ╩ ┴└─└─┘└─┘  ┴┘└┘ ┴ └─┘  └─┘┴ ┴┴ ┴─┴┘└─┘└┴┘
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠒⢋⣁⡀⠀⠀⠀⠀⠀⠘⠢⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠁⠉⠙⠒⠤⣘⣗⠒⠒⠒⠚⠛⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    '''
    print(logo)


def clean_line(line):
    line = re.sub(r"^├──\s+|^└──\s+|^│  \s+|^└──\s+", "", line)
    line = line.replace("│  ", "").replace("├──", "").replace("└──", "")
    return line.strip()


def rebuild_shadow(input_file, output_file=None, show_content=False):
    try:
        with open(input_file, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"[-] Error: File '{input_file}' not found.")
        sys.exit(1)

    reconstructed = []
    current_username = None
    current_hash_parts = []

    for line in lines:
        raw_line = line.strip()

        if not raw_line or raw_line.startswith("/etc/shadow"):
            continue
        if "directory" in raw_line and "file" in raw_line:
            continue

        cleaned = clean_line(line)
        if not cleaned:
            continue

        if ":" in cleaned and not cleaned.startswith("$"):
            if current_username and current_hash_parts:
                full_hash = "/".join(current_hash_parts)
                reconstructed.append(f"{current_username}:{full_hash}")
                current_username = None
                current_hash_parts = []

            parts = cleaned.split(":", 1)
            user = parts[0]
            rest = parts[1]

            if rest.startswith("$"):
                current_username = user
                current_hash_parts.append(rest)
            else:
                reconstructed.append(cleaned)
        else:
            if current_username:
                current_hash_parts.append(cleaned)

    if current_username and current_hash_parts:
        full_hash = "/".join(current_hash_parts)
        reconstructed.append(f"{current_username}:{full_hash}")

    output_content = "\n".join(reconstructed) + "\n"

    if output_file:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(output_content)
        print(f"[+] Successfully reconstructed shadow file saved to: {output_file}\n")
        if show_content:
            print(output_content)
    else:
        print(output_content)


if __name__ == "__main__":
    logo()
    parser = argparse.ArgumentParser(
        description="Reconstruct /etc/shadow from broken 'tree --fromfile' output."
    )
    parser.add_argument(
        "-i",
        "--input",
        required=True,
        help="Path to the broken tree output file",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Path to save the reconstructed shadow file (optional)",
    )
    parser.add_argument(
        "-s",
        "--show",
        action="store_true",
        help="Print full reconstructed shadow content to terminal even if output file is specified",
    )

    args = parser.parse_args()
    rebuild_shadow(args.input, args.output, args.show)
