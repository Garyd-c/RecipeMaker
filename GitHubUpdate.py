import subprocess


def run_command(command, allow_empty_commit=False):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        # Check if it's the harmless "nothing to commit" case
        if allow_empty_commit and "nothing to commit" in result.stdout:
            print("No changes to commit.")
        else:
            print(f"Command failed: {command}")
            print(result.stdout)
            print(result.stderr)
            exit(1)
    else:
        print(result.stdout)


# Step 1: Add all changes
run_command("git add .")

# Step 2: Commit with a default message (or customize it)
commit_message = input("Enter a commit message: ")
run_command(f'git commit -m "{commit_message}"', allow_empty_commit=True)

# Step 3: Push to GitHub
run_command("git push")