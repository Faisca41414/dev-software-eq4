import subprocess

# Define the commands for backend and frontend
backend_commands = [
    "fastapi dev main.py"
]

frontend_commands = [
    "cd frontend",
    "npm install",
    "npm run dev"
]

# Function to run a list of commands in a separate process
def run_commands(commands):
    process = subprocess.Popen(" && ".join(commands), shell=True)
    return process

# Run backend and frontend commands in separate processes
backend_process = run_commands(backend_commands)
frontend_process = run_commands(frontend_commands)

# Wait for both processes to complete
backend_process.wait()
frontend_process.wait()