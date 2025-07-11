import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"Command failed: {command}")
        exit(1)


# Step 1: pull updates
run_command("git pull")

