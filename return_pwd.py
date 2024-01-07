import subprocess

try:
    which_command = input("Enter your command: " )
    result = subprocess.run([which_command], stdout=subprocess.PIPE, text=True)
except subprocess.TimeoutExpired.stderr as e:
    print(f"could not find the path due to error:{e}")

if result.returncode == 0:
    current_directory = result.stdout.strip()
    print(f"Current directory: {current_directory}")
else:
    print(f"Error: {result.stderr}")