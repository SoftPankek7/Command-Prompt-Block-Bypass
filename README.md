# Command-Prompt-Block-Bypass
### How this works

This works by using the Python `os.system()` function from the Python OS library to bypass any Command Prompt blocking systems. The simplest and smallest way you could incorporate this is: 
```
import os
while True:
	os.system(input())
```

Or, if you wish to style it in a realistic way, you could choose to mix some stuff, for example:

```
import os
while True:
	os.system(input(os.getcwd()+">" if os.name == "nt" else "$ "))
```
##
### Problems / Issues

But you may notice there are some problems. Such as:

- You cannot change directory.
- You do not have administrative access.
- You may not run ``.bat``, and/or  ``.cmd`` files if Command Prompt is fully blocked (will not execute ``.bat`` files).
- Command Line Arguments to start up itself don't work (e.g: ``cmd.py -k echo boo``)

So, I have fixed some problems. Some cannot be fixed, e.g: ``You do not have administrative access.`` due to cybersecurity purposes.

However, I have fixed ``.bat`` and ``.cmd`` files by creating my own processor. It is a bit lacking, (theoretically loops will not work) - so do not get your hopes too high.

I also (*sort-of*) fixed the Command Line Arguments, but to be fair - you wouldn't really use CLI Args - because the shell is more than enough on its own.

Finally, I also theoretically fixed the ``cd`` command from not working (due to privileges being too low to change directory - or something like that)

**I also included a regedit-like settings tool that can be accessed by typing ``menu``.** 

##
### Cross compatibility

However, the main code for the repository (unlike the 2 examples above) are **focused for Microsoft Windows**, instead of Linux, MacOS and other UNIX/POSIX-based systems.

##
### Credit

[hippogriff](https://github.com/hippogriff101) for assisting my development (not really, just here because I - softpankek - felt empathy)
