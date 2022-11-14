# Important stuff

**Python output in fiile not showing**

This is due to python buffering the output first, disable by python -u.
Check this [link](https://unix.stackexchange.com/questions/45913/is-there-a-way-to-redirect-nohup-output-to-a-log-file-other-than-nohup-out)

**Get PID and kill process**

ps u, then kill PID1 PID2 ...

conda list
conda remove

du -sh /dir to see memory consumption

conda info --all 
ls -a to see all files (also .conda)

du -Sh | sort -rh | head -5  # get 5 biggest directories with estimated size


**Where are the packages?**
Definetly after installation in local/pathi619/miniconda3/.pkgs - ther also cache
Also in Env/lib/... (here is also everything)


Solution:

conda config --append pkgs_dirs /local/data1/pathi619/Packages # Add path to Package folder (here packages are saved)
conda info 

Afterwards everything newly installed will be added to new dir


IMPORTANT: Check how the data is fed - channel before or after?

Sample new ones with the checkpoint.
https://github.com/openai/improved-diffusion