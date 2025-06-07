#!/usr/bin/env python
import os
import subprocess
import sys

def run_command(command):
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"Command failed: {command}")
        sys.exit(1)

def main():
    print("Starting build process...")
    
    # Install dependencies
    run_command("pip install -r requirements.txt")
    
    # Collect static files
    run_command("python manage.py collectstatic --noinput --clear")
    
    print("Build completed successfully!")

if __name__ == "__main__":
    main()