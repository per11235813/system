from invoke import task
from invoke.context import Context
from pathlib import Path
import datetime as dt
import os
import subprocess
from pathlib import Path
import zipfile

@task
def count_py(c, docs=False, bytecode=False, extra=''):
    cwd = Path(".")
    py_files = list(cwd.glob("**/*.py"))
    print(f"Number of python files: {len(py_files)}")


@task
def hello(c):
    import sys
    for line in sys.stdin.readlines():
        print(f"PyInvoke: {line}", end="")


@task
def split_semi(c, sep=";"):
    import sys
    for line in sys.stdin.readlines():
        for entry in line.split(sep):
            print(entry)


@task
def backup(c):
    home = Path.home()
    backup_dir = home / "OneDrive - MAN Energy Solutions SE" / "adm" / "backup"
    backup_prefix = dt.datetime.now().isoformat()[:10]
    backup_file = backup_dir / f"{backup_prefix} backup.zip"

    backup_lists = [
        home / ".ssh",
        home / "AppData" / "Local" / "Temp" / "URLOBDXLS",
        home / ".gitconfig",
        r"C:\Users\d6bqr00\Documents\repo\python\.env",
        r"C:\Users\d6bqr00\Documents\repo\bwcph\src\.env",
        r"C:\Users\d6bqr00\AppData\Local\Microsoft\Edge\User Data\Default\Bookmarks",

    ]
    with zipfile.ZipFile(backup_file, "w") as zf:
        for loc in backup_lists:
            if Path(loc).exists():
                print(f"Backup up {loc}")
                zf.write(loc)
            else:
                print(f"File location '{loc}' does not exist")



@task
def nbclean(c, f=None, a=False, r=False):
    #if name and name.split(".")[-1] == "ipynb" and not ".ipynb_checkpoints" in path:
    #    subprocess.run( ["jupyter",  "nbconvert",  "--ClearOutputPreprocessor.enabled=True",  "--inplace", os.path.join(path, name)], shell=True )
    cwd = Path(os.getcwd())
    nb_list = []

    if f is not None:
        p = Path(f)
        if p.exists():
            nb_list.append(Path(f))
        else:
            raise ValueError(f"File {f} does not exist")
    elif f is None and a is True:
        nb_list = cwd.glob("*.ipynb")
    elif f is None and r is True:
        nb_list = [nb for nb in  cwd.glob("*.ipynb") if ".ipynb_checkpoints" not in nb.parts]
    else:
        raise ValueError(f"Invalid arguments: {f} {a} {r}")

    for nb in nb_list:
        print(f"Cleaning notebook: {nb}, size {nb.stat().st_size:_}")
        subprocess.run( ["jupyter",  "nbconvert",  "--ClearOutputPreprocessor.enabled=True",  "--inplace", str(nb)], shell=True )
    

        
