from config import test_directory
import subprocess
import os

for filename in os.listdir(test_directory):
    if filename.endswith(".spec.js"):
        print("Running test: " + filename)
        subprocess.run(["npx", "playwright", "test", test_directory + "/" + filename])
    else:
        continue