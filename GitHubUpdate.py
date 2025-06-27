import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"Command failed: {command}")
        exit(1)


# Step 1: Add all changes
run_command("git add .")

# Step 2: Commit with a default message (or customize it)
commit_message = input("Enter a commit message: ")
run_command(f'git commit -m "{commit_message}"')

# Step 3: Push to GitHub
run_command("git push")