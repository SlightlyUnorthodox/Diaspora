# Main dialogue for initializing a chatbot

from collections import OrderedDict
from nltk import chat

class DialogueInterface():

    user_name = ''
    user_dialogue_choice = ''

    dialogue_catalogue = OrderedDict([
        ('1. NTLK: eliza', 'chat.eliza_chat()'),
        ('2. NLTK: iesha', 'chat.iesha_chat()'),
        ('3. NTLK: rude', 'chat.rude_chat()'),
        ('4. NLTK: suntsu', 'chat.suntsu_chat()'),
        ('5. NLTK: zen', 'chat.zen_chat()'),
        ('6. Preliminator', 'print("that\'s all for now")'),
    ])

    def start_dialogue(self):

        self.introduce_dialogue_system()
        self.get_user_name()
        self.get_user_dialogue_choice()
        self.start_user_dialogue()

    def introduce_dialogue_system(self):
        print("Hello! Welcome to the Diaspora 'dialogue catalogue'.")

    def get_user_name(self):
        self.user_name = str(raw_input("What is your name?\n"))
        if len(self.user_name) == 0:
            print("Please enter your name")
            self.get_user_name()

    def get_user_dialogue_choice(self):

        self.display_dialogue_options()
        self.user_dialogue_choice = str(raw_input("Please pick a dialogue to try out.\n"))

        if not self.valid_user_dialogue_choice(self.user_dialogue_choice):
            print("Please enter a valid choice")
            self.get_user_dialogue_choice()

    def display_dialogue_options(self):

        print("Your dialogue choices are...")
        for dialogue in self.dialogue_catalogue.keys():
            print(str(dialogue))

    def valid_user_dialogue_choice(self, user_choice):

        for key in self.dialogue_catalogue.keys():
            if str(key).find(str(user_choice)) >= 0:
                self.user_dialogue_choice = self.dialogue_catalogue[key]
                return True

        return False

    def start_user_dialogue(self):
        eval(str(self.user_dialogue_choice))


if __name__ == "__main__":
    dialogue_interface_instance = DialogueInterface()
    dialogue_interface_instance.start_dialogue()
