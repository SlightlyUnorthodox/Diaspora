# Test for python system initiative class

from __future__ import print_function
from nltk.chat.util import reflections
import StateBasedDialogue

states = ()

def demo():
    test_chatbot = StateBasedDialogue(states)
    test_chatbot.start_dialogue()

if __name__ == "__main__":
    demo()