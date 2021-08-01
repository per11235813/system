
set pythonpath=%userprofile%\repo\python;%cd%\src;%cd%\tests;%cd%
set SHELL=cmd.exe

doskey ls=dir /B
doskey ll=dir
doskey jup=jupyter lab --ContentsManager.allow_hidden=True

call %userprofile%\venv\scripts\activate

