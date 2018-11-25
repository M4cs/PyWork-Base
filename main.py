#!/usr/bin/python3
# First Thing Is First... Import your third-party modules #
from configparser import ConfigParser # Used for configuration reading and writing
import os, sys
# Import our first-party modules from configuration, modules and core
from core.displays import helpmenu, welcome # Call with helpmenu.function() or welcome.function()
from core.modules import module1, module2 # Call with module1.function() or module2.function()
from configuration import cfg # Call with cfg.function()

# Check for configuration on startup #
cfg.checkuser() # We only have to call checkuser because if they dont pass then they create one
# Load user config #
config = ConfigParser()
config.read('configuration/config.cfg')
# We can now call any key with config['DEFUALT']['keyname']
welcome.run() # Display welcome banner from core/displays/welcome.py
helpmenu.run() # Display Help Menu
# Create our user i/o environment and call it main()
terminalname = "[pywork] " # This will be the equivalent to PS1 in bash.
def main():
    terminal = input(terminalname) # Create our input
    if terminal[0:7] == "module1": # If the first 7 characters are equal to module1 then it will run module1
        module1.run()
        main() # Restart terminal after
    elif terminal[0:7] == "module2": # If the first 7 characters are equal to module2 then it will run module2
        module2.run()
        main()
    elif terminal[0:4] == "help": # If the first 4 characters are equal to help it will display the help menu
        helpmenu.run()
        main()
    elif terminal[0:4] == "exit": # If the first 4 characters are equal to exit it will exit
        sys.exit(2)
    else: # If it's not a command we say not a command and retry
        print("Error! Command %s Unrecognized. Use 'help' to display help menu." % terminal)
        main()

# Call main to start our "shell" after doing what we need to in the first place.
main()
