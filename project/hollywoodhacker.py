import sys
import random
from pathlib import Path
import time
import os

def main():
    if len(sys.argv) == 1:
        file = "target.txt"
        print("No file → using target.txt")
    elif len(sys.argv) != 2:
        print("Usage: hollywoodhacker.py <filename> ", file=sys.stderr)
        sys.exit(1)
    else:
        file = sys.argv[1]

    p = Path(file)
    if not p.exists():
        print(f"Cannot open \"{file}\".")
        sys.exit(1)

    try:
        with open(file) as f:
            lines = f.readlines()

        # Clear screen for extra drama (optional but cool)
        os.system('cls' if os.name == 'nt' else 'clear')

        with open("hacking_session.txt", "w") as f:
            def typewrite(text, delay=0.03):
                for char in text:
                    print(char, end='', flush=True)
                    f.write(char)
                    time.sleep(delay)
                print()
                f.write("\n")

            typewrite("[INITIATING NEURAL LINK...]", 0.05)
            time.sleep(0.8)
            typewrite(f"Connecting to 192.168.{random.randint(0,255)}.{random.randint(0,255)}... OK", 0.03)
            typewrite("Bypassing firewall" + "."*random.randint(8,16) + " [DONE]", 0.08)
            typewrite("Injecting payload" + "."*random.randint(8,16) + " [DONE]", 0.08)
            time.sleep(1)
            print()

            for line in lines:
                line = line.strip()
                if line:
                    typewrite("> ", 0.1)
                    for c in line:
                        print(c, end=' ', flush=True)
                        f.write(c + " ")
                        time.sleep(random.uniform(0.05, 0.15))
                    print()
                    f.write("\n")
                print()
                f.write("\n")
                time.sleep(0.5)

            time.sleep(1)
            typewrite("Scanning memory sectors... ", 0.05)
            typewrite(f"{random.randint(70,99)}% complete", 0.03)
            typewrite(f"Random packet flood sent to {random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}", 0.03)
            time.sleep(0.8)
            typewrite("ACCESS GRANTED", 0.15)
            typewrite("Encryption keys dumped", 0.1)
            typewrite("Root privileges obtained", 0.1)

        print(f"\nHACKING COMPLETE → check \"hacking_session.txt\"")
        input("\nPress Enter to exit...")

    except Exception as e:
        print(f"Error: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()