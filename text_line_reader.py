import sys

try:
    if len(sys.argv) != 2:
        print("Usage: python line_counter.py <filename>")
        #sys.exit(1)

    filename = sys.argv[1]

    with open(filename, "r") as file:
        lines = file.readlines()
        count = len(lines)

    print(f"{filename} has {count} lines.")

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"An error occurred: {e}")
