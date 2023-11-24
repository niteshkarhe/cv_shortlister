import subprocess
import os

filepath = os.path.join(os.getcwd() + "\\upload", "audiofile.mp3")
wavpath = os.path.join(os.getcwd() + "\\upload", "audiofile.wav")
subprocess.call(['ffmpeg', '-i', filepath, wavpath])