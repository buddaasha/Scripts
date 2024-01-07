import subprocess


result = subprocess.run(['pwd'], stdout=subprocess.PIPE, text=True)
print(result)

# Check if the command was successful (return code 0)
if result.returncode == 0:
    current_directory = result.stdout.strip()
    print(f"Current directory: {current_directory}")
else:
    print(f"Error: {result.stderr}")