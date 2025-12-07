# Hollywood Hacker – Terminal Hacking Simulator

A tongue and cheek Python script that turns any boring text file into proper movie-style hacking.

## What it actually does
- Takes a text file (defaults to `target.txt` if you don’t tell it otherwise)  
- Prints the whole thing char-by-char with the classic slow typewriter effect  
- Throws in fake “connecting to network” messages, random IPs, firewall bypass nonsense, payload injection lines – all the stuff you see in films  
- Spits out random tech-sounding gibberish between sections for extra drama  
- At the end it dumps the entire session into `hacking_session.txt` so it looks like a real log  
- Works on Windows, Mac and Linux (clears screen properly)  
- Pauses at the end so the window doesn’t just disappear

## How to run it

### Easy way (uses target.txt)
Just double-click `hollywoodhacker.py` or  
```bash
python hollywoodhacker.py