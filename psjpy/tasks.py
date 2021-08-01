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

