# Create a user function
# We can call cfg.checkuser() to see if the user has a config file. If not it creates one using cfg.createuser()
def createuser():
    from configparser import ConfigParser
    config = ConfigParser()
    config['DEFAULT'] = { # Create our configuration dictionary
        'configkey1': '',
        'configkey2': '',
        'configkey3': 'default value'
    }
    print("No Config File Found!".center(45, " "))
    print("Please Create A New Configuration".center(45, " "))
    print("Enter Value For Configkey1") # Get values for config keys
    configkey1 = str(input("> "))
    print("Enter Value For Configkey2")
    configkey2 = str(input("> "))
    print("Enter Value For Configkey3")
    configkey3 = str(input("> "))
    config['DEFAULT']['configkey1'] = configkey1
    config['DEFAULT']['configkey2'] = configkey2
    config['DEFAULT']['configkey3'] = configkey3
    with open('configuration/config.cfg', 'w') as f: # Must use paths from the root of the framework
        config.write(f)

# Check for configfile and then if it isn't there use the create function.
def checkuser():
    import os # Needed to check for path
    if os.path.exists('configuration/config.cfg') == True:
        pass
    else:
        createuser()
