import subprocess
import os
import sqlite3

# filepath = os.path.join(os.getcwd() + "\\upload", "audiofile.mp3")
# wavpath = os.path.join(os.getcwd() + "\\upload", "audiofile.wav")
# subprocess.call(['ffmpeg', '-i', filepath, wavpath])

# filename to form database
file = "Sqlite3.db"

try:
    conn = sqlite3.connect(os.getcwd() + "\\openapi_server\\database\\cvscanner.db")
    print("Database Sqlite3.db formed.")
except Exception as ex:
    print("Database Sqlite3.db not formed.")
    print(ex)