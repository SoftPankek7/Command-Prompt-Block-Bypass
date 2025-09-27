import os
import sys


settings = {
    "usecustombatchrunner": "true",
    "usecustomcdsystem": "false"
}

os.system("title Command Prompt")
print("Microsoft Windows [Based on Version 10.0.19044.6216]\n(c) Microsoft Corporation. All Rights Reserved.\n")


def get_arguments():
    _ = sys.argv
    if len(_) == 1:
        return 0
    else:
        for i in range(len(_)):
            if _[i].lower() == "-k":
                os.system(_[len((_)-1)])
                return 0
            elif _[i].lower() == "-c":
                os.system(_[len((_)-1)])
                exit(0)
            elif _[i].lower() == "-q":
                os.system("@echo off")
                return 0
            elif _[i].lower()[0:3] == "-t:":
                os.system("color "+_[i].lower()[3:5])
            elif _[1].lower() == "/?" or _[1].lower() == "-h":
                print('Starts a new instance of the Windows command interpreter\n\nCMD [/A | /U] [/Q] [/D] [/E:ON | /E:OFF] [/F:ON | /F:OFF] [/V:ON | /V:OFF]\n    [[/S] [/C | /K] string]\n/C      Carries out the command specified by string and then terminates\n/K      Carries out the command specified by string but remains\n/S      Modifies the treatment of string after /C or /K (see below)\n/Q      Turns echo off\n/D      Disable execution of AutoRun commands from registry (see below)\n/A      Causes the output of internal commands to a pipe or file to be ANSI\n/U      Causes the output of internal commands to a pipe or file to be\n        Unicode\n/T:fg   Sets the foreground/background colors (see COLOR /? for more info)\n/E:ON   Enable command extensions (see below)\n/E:OFF  Disable command extensions (see below)\n/F:ON   Enable file and directory name completion characters (see below)\n/F:OFF  Disable file and directory name completion characters (see below)\n/V:ON   Enable delayed environment variable expansion using ! as the\n        delimiter. For example, /V:ON would allow !var! to expand the\n        variable var at execution time.  The var syntax expands variables\n        at input time, which is quite a different thing when inside of a FOR\n        loop.\n/V:OFF  Disable delayed environment expansion.\n\nNote that multiple commands separated by the command separator "&&"\nare accepted for string if surrounded by quotes.  Also, for compatibility\nreasons, /X is the same as /E:ON, /Y is the same as /E:OFF and /R is the\nsame as /C.  Any other switches are ignored.\n\nIf /C or /K is specified, then the remainder of the command line after\nthe switch is processed as a command line.')

def change_directory(path):
    if settings["usecustomcdsystem"].lower() == "true":
        _ = open(os.abspath(__file__))
        _2 = open(path + "\\cmd.py", "wt")
        own = _.readlines()
        for i in range(len(own)):
            _2.write(own[i])
        os.system("python "+path+"\\cmd.py")

def bat_runner(path):
    if settings["usecustombatchrunner"].lower() == "true":
        try:
            file = open(path)
            runlist = file.readlines()
            try:
                runlist.remove("\n")
            except ValueError:
                pass
            for i in range(len(runlist)):
                os.system(runlist[i])
        except FileNotFoundError:
            print("'"+path+"' is not recognized as an internal or external command, operable program or batch file.")
        except KeyboardInterrupt:
            return 0
    else:
        os.system(path)

get_arguments()
while True:
    try:
        command = input(os.getcwd()+">")
        if command[-4:].lower() == ".bat" or command[-4:].lower() == ".cmd":
            bat_runner(command)
        elif command.lower() == "menu":
            try:
                while True:
                    print("-=<{ MENU }>=-\n\nPress CTRL+C To stop.\nHere are the list of settings:\n")
                    print(settings)
                    _ = input("Key:  ").lower()
                    _2 = input("Value:  ")
                    settings[_] = _2
            except KeyboardInterrupt:
                print()
                continue
        elif command.lower()[0:1] == "cd":
            change_directory(command[3:])
        else:
            os.system(command)
    except KeyboardInterrupt:
        pass
    except EOFError:
        pass