import subprocess

BASE_PATH = "/home/pi"

def play(filename):
    file = BASE_PATH + "/sounds/" + filename
    subprocess.run(["cvlc", "--play-and-exit", file])
    return
