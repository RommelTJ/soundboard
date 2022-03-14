import subprocess


def play(filename):
    subprocess.run(["vlc", filename])
