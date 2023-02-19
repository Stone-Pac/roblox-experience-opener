import webbrowser

# Prompt the user to input the Universal ID
universal_id = input("Enter the Universal ID of the Roblox experience: ")

# Construct the URL for the Roblox experience using the Universal ID
url = f"https://create.roblox.com/creations/experiences/{universal_id}/overview"

# Open the URL in the default web browser
webbrowser.open(url)
