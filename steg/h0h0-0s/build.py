"""
Builder for H0H0-0S challenge.
"""

import os
import os.path
import shutil
import zipfile
import random

from folders import Lisp2Folders

FLAG = "FLAG-{y0u_s4v3d_th3_313v35}"
BUILD_FOLDER = "H0H0-0S"
SCRIPT = f"""
(dir bin
    (print (literal string The )))
(dir etc
    (print (literal string flag )))
(dir home
    (print (literal string is: )))
(dir root
    (print (literal string `{FLAG[:len(FLAG)//2]})))
(dir usr
    (print (literal string {FLAG[len(FLAG)//2:]}`)))
"""

TOYS = ["scarf", "toy-car", "teddy-bear", "santa", "elf", "gingerbread-man", "polar-bear", "sled", "reindeer", "snowman", "snow"]
EXTENSIONS = ["txt", "pdf", "png", "jpg"]

def main():
    if os.path.exists(f"./{BUILD_FOLDER}"):
        shutil.rmtree(f"./{BUILD_FOLDER}")

    lisp2folders = Lisp2Folders(f"./{BUILD_FOLDER}")
    lisp2folders.build(SCRIPT)

    with open(f"./{BUILD_FOLDER}/gr1nch.txt", "w") as h:
        h.write("Ftp Open - Lves Don't Even Remember Security\n\nI encrypted your whole drive with an uncrackable algorithm. You'll only be able to save Christmas if you find the key.\n\n- Gr1nch\n")

    for walk in os.walk(f"./{BUILD_FOLDER}"):
        directory = walk[0]

        if directory in [f"./{BUILD_FOLDER}"]:
            continue

        for toy in random.sample(TOYS, k=random.randrange(1, len(TOYS) // 3)):
            with open(directory + "/" + toy + "." + random.choice(EXTENSIONS), "w") as h:
                h.write("Gr1nch Encrypted")

if __name__ == "__main__":
    main()
