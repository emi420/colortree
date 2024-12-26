# -*- coding: utf-8 -*-.
 
import argparse
import random

colors = ["red", "green", "normal"]
tree_chars = ["•","⏺","܍"]
trunk_chars = ["░","▒"]

def printColor(color, text):
    if color == "red":
        print("\033[91m{}\033[00m" .format(text))
    elif color == "green":
        print("\033[92m{}\033[00m" .format(text))
    print(text)

def symbol():
    return random.choice(tree_chars)

def print_tree(size):
    trunk_v = size/1.5

    for i in range(0, size):
        line = []
        n = size - i
        for j in range(0, size*2):
            v = j - n
            line.append(symbol() if (v > 0 and v < i * 2) else " ")
        printColor(random.choice(colors), (" ".join(line)))

    for i in range(0, 1):
        line = []
        for j in range(0, size*2):
            line.append(random.choice(trunk_chars) if (j > trunk_v and (j < trunk_v + trunk_v)) else " ")
        print("\033[40m{}\033[00m" .format(" ".join(line)))

def main():
    args = argparse.ArgumentParser()
    args.add_argument("--size", "-s", help="Size of the tree", type=int, default=10)
    args = args.parse_args()

    if args.size > 2:
        print("")
        print_tree(args.size)
        print("")
    else:
        print("Size must be at least 3")

if __name__ == "__main__":
    main()