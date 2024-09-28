import subprocess

with open('requirements.txt', 'r') as f:
    packages = [line.strip() for line in f.readlines()]

for package in packages:
    try:
        subprocess.check_call(['pip', 'install', package])
    except subprocess.CalledProcessError:
        print(f"Skipping {package} due to installation failure")
        continue