# Important Stuff

### Python output in file not showing (redirect output)

This is due to python buffering the output first, disable by python -u.
Check this [link](https://unix.stackexchange.com/questions/45913/is-there-a-way-to-redirect-nohup-output-to-a-log-file-other-than-nohup-out)

<br> 

### Bash
Get PID and kill process:
>ps u, then kill PID1 PID2 ...\
>Check GPU ones with nvidia-smi, kill PID

See memory consumption:
>du -sh /dir 

List all files:
> ls -a to see all files (also dotfiles)

Get 5 biggest directories (with size):

>du -Sh | sort -rh | head -5  

>du - h to see size of directories


Time of creation of file:
> stat ./file

Disk space:
> df -H is disk space
> ls dir | wc -l



Remove without question 
> rm -r -f miniconda3/
  
Search in terminal 
> ctrl + r 
  
  Download and unzip:
> wget to download a file in current dir 
> unpack /zip-file

<br> 

### Conda 

List packages and remove:
> conda list \
> conda remove


>conda info --all 


Recreate conda env on new computer:
> conda env export > environment.yml

> conda env create -f environment.yml


Where are the packages?

Definetly after installation in local/pathi619/miniconda3/.pkgs - there also cache \
Also in Env/lib/... (here is also everything)

Solution:

> conda config --append pkgs_dirs /local/data1/pathi619/Packages # Add path to Package folder (here packages are saved) \
> conda info 

Afterwards everything newly installed will be added to new dir.


### Github setup
> git remote remove origin \
> git remote add origin https://<TOKEN>@github.com/<USERNAME>/<REPO>.git


We can unpack a list of args with \*!

