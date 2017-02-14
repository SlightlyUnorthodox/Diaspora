# Main dialogue for initializing a chatbot

from collections import OrderedDict
from nltk import chat
from lib import test
from lib import Preliminator

class DialogueInterface():

    def __init__(self):
        self._user_name = ''
        self._user_dialogue_choice = ''
        self._dialogue_catalogue = OrderedDict([
            ('1. NTLK: eliza', 'chat.eliza_chat()'),
            ('2. NLTK: iesha', 'chat.iesha_chat()'),
            ('3. NTLK: rude', 'chat.rude_chat()'),
            ('4. NLTK: suntsu', 'chat.suntsu_chat()'),
            ('5. NLTK: zen', 'chat.zen_chat()'),
            ('6. Preliminator', 'Preliminator.start()'),
            ('7. StateBasedChat: test', 'test.demo()'),
        ])

    def start(self):

        self._introduce_dialogue_system()
        self._get_user_name()
        self._get_user_dialogue_choice()
        self._start_user_dialogue()

    def _introduce_dialogue_system(self):
        print("Hello! Welcome to the Diaspora 'dialogue catalogue'.")

    def _get_user_name(self):
        self._user_name = str(raw_input("What is your name?\n"))
        if len(self._user_name) == 0:
            print("Please enter your name")
            self._get_user_name()

    def _get_user_dialogue_choice(self):

        self._display_dialogue_options()
        self._user_dialogue_choice = str(raw_input("Please pick a dialogue to try out.\n"))

        if not self._valid_user_dialogue_choice(self._user_dialogue_choice):
            print("Please enter a valid choice")
            self._get_user_dialogue_choice()

    def _display_dialogue_options(self):

        print("Your dialogue choices are...")
        for dialogue in self._dialogue_catalogue.keys():
            print(str(dialogue))

    def _valid_user_dialogue_choice(self, user_choice):

        for key in self._dialogue_catalogue.keys():
            if str(key).find(str(user_choice)) >= 0:
                self._user_dialogue_choice = self._dialogue_catalogue[key]
                return True

        return False

    def _start_user_dialogue(self):
        eval(str(self._user_dialogue_choice))

    def _exit_statement(self):
        print("That's all for now")


if __name__ == "__main__":
    dialogue_interface_instance = DialogueInterface()
    dialogue_interface_instance.start()
