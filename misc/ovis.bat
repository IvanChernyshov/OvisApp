# parameters: change for your system
set root=C:\Programming\Anaconda3
set env=ncsd

# script
call %root%\Scripts\activate.bat %root%
call conda activate %env%
call python -m ovis && exit 0 || exit 1
