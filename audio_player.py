import os
import subprocess

path = os.getcwd()


def play(filename):
    file = path + "/sounds/" + filename
    subprocess.run(["cvlc", "--play-and-exit", file])
    return
