import json
import requests
import random
import re
import pymsteams

# Get joke from API
response = requests.get("https://api.chucknorris.io/jokes/random")
data = json.loads(response.text)
joke = data["value"]
print(joke)

# List of names
list_of_names = ['Joanna Palmer', 'Tara Armstrong', 'Brian Davidson', 'Jay Hamilton', 'Thomas Rice', 'Ricky Morris', 'Gloria Myers', 'James Harrell', 'Natasha Mata', 'Thomas Bailey']

# Let's choose a random name to "Norrize" 
chosen_name = random.choice(list_of_names)
splitted_name = chosen_name.split()
norrized_name = splitted_name[0] + " Norris " + splitted_name[1]

# Let's substitute it in our joke
pattern = "Chuck Norris"
customized_joke = re.sub(pattern, norrized_name, joke )

# You must create the connectorcard object with the Microsoft Webhook URL
myTeamsMessage = pymsteams.connectorcard("Insert_Here_Your_MS_Teams_Webhook_URL")

# Add text to the message.
myTeamsMessage.text(customized_joke)

# send the message.
myTeamsMessage.send()