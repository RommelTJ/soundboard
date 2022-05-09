import subprocess

BASE_PATH = "/home/pi/Desktop/soundboard"

def play(filename):
    file = BASE_PATH + "/sounds/" + filename
    subprocess.run(["cvlc", "--play-and-exit", file])
    return
