import subprocess
import sys

def check_poetry_virtualenvs_create():
    try:
        # Run the Poetry command to get the current value of virtualenvs.create
        result = subprocess.run(
            ["poetry", "config", "virtualenvs.create"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
            shell=True
        )
        
        # Capture the output and strip any extra whitespace
        value = result.stdout.strip()
        
        # Convert the value to a boolean
        if value.lower() == "true":
            return True
        elif value.lower() == "false":
            return False
        else:
            raise ValueError(f"Unexpected value returned: {value}")
    
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e.stderr}")
        sys.exit()
    
def set_poetry_virtualenvs_create(value):
    try:
        # Set the value of virtualenvs.create
        subprocess.run(
            ["poetry", "config", "virtualenvs.create", str(value).lower()],
            check=True,
            shell=True
        )
        print(f"Poetry virtualenvs.create has been set to {value}.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while setting the value: {e.stderr}")
        sys.exit()
        

def install_dependencies():
    try:
        subprocess.run(
            ["poetry", "install"],
            check=True,
            shell=True
        )
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing the project: {e.stderr}")
        sys.exit()

if __name__ == "__main__":
    is_virtualenvs_create_enabled = check_poetry_virtualenvs_create()
    switch_back = False
    if not is_virtualenvs_create_enabled:
        set_poetry_virtualenvs_create(True)
        switch_back = True
    install_dependencies()
    if switch_back:
        set_poetry_virtualenvs_create(False)

    print(f"FIN is ready to use.")