import subprocess

def run_flake8(filename):
    result = subprocess.run(["flake8", filename], capture_output=True, text=True)
    if result.returncode == 0:
        print("No se encontraron problemas de código.")
    else:
        print("Problemas de código encontrados:")
        print(result.stdout)

run_flake8(".\Simple_game.py")
