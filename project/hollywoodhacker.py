import sys
import random
from pathlib import Path

def main():
    if len(sys.argv) != 2:
        print("Usage: hacker.py <filename> ",file=sys.stderr)
        sys.exit(1)

    file = sys.argv[1]
    p = Path(file)

    if not p.exists():
        print(f"Cannot open \"{file}\".")
        sys.exit(1)

    try:
        with open(file) as f:
            lines = f.readlines()

        with open("hacking_session.txt","w") as f:
            f.write("[INITIATING NEURAL LINK...]\n")
            f.write(f"Connecting to 192.168.{random.randint(0,255)}.{random.randint(0,255)}... OK\n")
            f.write("Bypassing firewall"+"."*random.randint(6,14)+" [DONE]\n")
            f.write("Injecting payload"+"."*random.randint(6,14)+" [DONE]\n\n")

            for line in lines:
                line = line.strip()
                if line:
                    f.write("> ")
                    for c in line:
                        f.write(c+" ")
                        if random.randint(1,12)==1:
                            f.write(" ")
                    f.write("\n")
                f.write("\n")

            f.write("Scanning memory sectors... "+str(random.randint(70,99))+"% complete\n")
            f.write("Random packet flood sent to "+str(random.randint(1,255))+"."+str(random.randint(0,255))+"."+str(random.randint(0,255))+"."+str(random.randint(0,255))+"\n")
            f.write("ACCESS GRANTED\n")
            f.write("Encryption keys dumped\n")
            f.write("Root privileges obtained\n")

        print(f"Hacking session saved to \"hacking_session.txt\"")

    except:
        print(f"Cannot open \"{file}\".")
        sys.exit(1)

if __name__ == "__main__":
    main()