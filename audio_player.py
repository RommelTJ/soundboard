import subprocess


def play(filename):
    subprocess.run(["cvlc", "--play-and-exit", filename])
    return
