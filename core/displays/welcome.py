# We can call welcome.run() in main.py now to print our welcome display.
def run():
    # Import any modules needed #
    from fabulous import image # Using fabulous to display welcome logo in terminal (Doesn't work on Windows)
    # Create a welcome banner. Here is a simple version. #
    print(image.Image('core/displays/images/example.png')) # Anytime we call a path we have to act as if we are in the root directory of the framework
    print("PyWork Framework Base".center(45, " ")) # Center our text
    print("")
    print("Framework Designed by @maxbridgland".center(45, " "))
    print("Link: https://github.com/M4cs/PyWorkBase".center(45, " "))
