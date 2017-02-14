# Attempts to flip 'system initiative' NLTK Chat module design as a 'user initiative' design

from __future__ import print_function

import re
import time


# import random
# from nltk import compat


class Simple:
    def __init__(self, system_name, states, patterns):
        self.system_name = system_name
        self.states = states
        self.patterns = patterns

        self.current_state = 'start'
        self.system_utterance = states['start']

        self.quit = False
        self.match_found = True

        self.error_message = ''
        self.user_utterance = ''

    def start(self):
        while not self.quit:
            self.generate_system_utterance()
            self.wait_for_user_utterance()
            time.sleep(0.5)
            self.check_state()

    def check_state(self):
        for state_rule in self.patterns:
            if self.states_match(state_rule[0]):
                if self.patterns_match(state_rule):
                    self.current_state = state_rule[3]
                    return
                else:
                    self.error_message = state_rule[2]

    def states_match(self, pattern_state):
        return self.current_state == pattern_state

    def patterns_match(self, pattern_tupple):
        self.match_found = re.match(pattern_tupple[1], self.user_utterance)
        return self.match_found

    def generate_system_utterance(self):
        self.check_match_found()
        print(self.system_name + ": " + self.system_utterance + '\n')

    def check_match_found(self):
        if self.match_found:
            self.system_utterance = self.states[self.current_state]
        else:
            self.system_utterance = self.error_message

    def wait_for_user_utterance(self):
        self.user_utterance = str(raw_input("User: "))
        self.check_for_quit()

    def check_for_quit(self):
        if self.user_utterance.find('quit') >= 0:
            self.quit = True
