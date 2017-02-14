# Test for python system initiative class

from __future__ import print_function
from nltk.chat.util import reflections
import StateBasedDialogue
import re

# Make sure to include a 'start' and 'end' state
any_pattern = re.compile(".?")

states = {
    'start': 'Hello!',
    'middle': 'How are you?',
    'next': 'Why should I care?',
    'end': 'That\'s nice. Goodbye!',
}

patterns = (
    ('start', any_pattern, 'Enter any value', 'middle'),
    ('middle', any_pattern, 'Enter any value', 'next'),
    ('next', any_pattern, 'Enter any value', 'end'),
    ('end', any_pattern, 'Enter any value', 'end'),
)

def demo():
    test_chatbot = StateBasedDialogue.Simple('Test System', states, patterns)
    test_chatbot.start()

if __name__ == "__main__":
    demo()