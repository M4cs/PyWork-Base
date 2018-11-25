# Create a help menu using Terminal Tables #
# We can call helpmenu.run() in main.py to display our help menu #
def run():
    # Import terminaltables style SingleTable #
    from terminaltables import SingleTable
    helptable = [
        ['Command', 'Description'],
        ['help', 'Display this menu'],
        ['module1', 'Run module1'],
        ['module2', 'Run module2'],
        ['exit', 'Exit framework']
    ]
    table = SingleTable(helptable, "Help Menu") # Create our terminaltable data. SingleTable(table_name, "Table title")
    print(table.table) # Print our help table