from greeting import Greeting
from welcome import Welcome 

welcome_1 = Welcome("Hello!", "James")
welcome_2 = Welcome("Hola!", "Sarah")
welcome_3 = Welcome("Bonjour!")

greeting_1 = Greeting("Hiya")
greeting_2 = Greeting("Wassap")
greeting_3 = Greeting("Greetings!")

messages = [welcome_1, welcome_2, welcome_3, greeting_1, greeting_2, greeting_3]

for message in messages:
    print(message.display())
    print()