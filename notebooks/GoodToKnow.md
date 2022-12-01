# Important stuff

**Python output in fiile not showing**

This is due to python buffering the output first, disable by python -u.
Check this [link](https://unix.stackexchange.com/questions/45913/is-there-a-way-to-redirect-nohup-output-to-a-log-file-other-than-nohup-out)

**Get PID and kill process**

ps u, then kill PID1 PID2 ...
Check GPU ones with nvidia-smi, kill PID

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


**Github setup**
git remote remove origin
git remote add origin https://<TOKEN>@github.com/<USERNAME>/<REPO>.git


**Time of creation**
stat ./file

40 min per 10000 steps

df -H is disk space
ls dir | wc -l

We can unpack a list of args with *!
**Questions**
What does a step indicate? How many pictures per step? How many steps does it take to do one full epoch? How many of the images did the model see during training?
  
  
 Remove without question 
 rm -r -f miniconda3/
  
 ctrl + r = search in terminal 
  
wget to download a file in current dir 
unpack /zip-file 
