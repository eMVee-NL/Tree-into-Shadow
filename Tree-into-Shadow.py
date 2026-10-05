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
⠸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡷⠺⡍⠒⣿⣀⣠⡀⠀⠀⠀⠀⠀⠈⠀⠈⡷⠀
⠀⢸⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⠺⡁⠀⠙⠚⠀⠁⡏⢧⣀⡄⠀⠀⠀⠀⠐⠒⣇⠀
⠀⠸⣄⣀⣰⠀⠀⠀⠀⠀⠀⠲⣟⣿⡦⣷⠀⠀⠀⠀⢠⠁⣸⣿⣷⢶⡆⢀⣤⡀⣠⡾⠁
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
    line = re.sub(r"^├──\s+|^└──\s+|^│  \s+|^└──\s+|^│\s+", "", line)
    line = line.replace("│  ", "").replace("├──", "").replace("└──", "").replace("│", "")
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
    current_buffer = []

    for line in lines:
        raw_line = line.strip()

        if not raw_line or raw_line.startswith("/etc/shadow"):
            continue
        if "directory" in raw_line and "file" in raw_line:
            continue

        cleaned = clean_line(line)
        if not cleaned:
            continue

        if ":" in cleaned and not (cleaned.startswith("$") or cleaned.startswith("*") or cleaned.startswith("!")):
            if current_username:
                full_raw_string = "".join(current_buffer)
                reconstructed.append(f"{current_username}:{full_raw_string}")
                current_username = None
                current_buffer = []

            parts = cleaned.split(":", 1)
            current_username = parts[0]
            current_buffer.append(parts[1])
        else:
            if current_username:
                if not current_buffer[-1].endswith("/") and not cleaned.startswith(":"):
                    current_buffer.append("/" + cleaned)
                else:
                    current_buffer.append(cleaned)
            else:
                if ":" in cleaned:
                    reconstructed.append(cleaned)

    if current_username:
        full_raw_string = "".join(current_buffer)
        reconstructed.append(f"{current_username}:{full_raw_string}")

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
