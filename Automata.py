
from PySimpleAutomata import DFA, automata_IO

class Automata:

    def __ini__(self, words):
        self._words = words

    def __init__(self) -> None:
        pass

    _dfa_assigned = {
        'alphabet': {'', 'a', 'b', 'c', 'd'},
        'states': {'q0', 'q1', 'q2', 'q3', 'q4'},
        'initial_state': 'q0',
        'accepting_states': {'q0', 'q2', 'q4'},
        'transitions': {
            ('q0', 'b'): 'q1',
            ('q1', 'a'): 'q2',
            ('q2', 'b'): 'q1',
            ('q4', 'd'): 'q4',
            ('q0', 'd'): 'q4',
            ('q4', 'c'): 'q3',
            ('q3', 'd'): 'q4',
            ('q0', 'c'): 'q3',
            ('q3', 'c'): 'q3',
            ('q2', 'c'): 'q3',
            ('q3', 'd'): 'q2'
        }
    }

    def generateGraph(self):
        graph = automata_IO.dfa_to_dot(self._dfa_assigned, 'grafo', path='./source')
        return graph

    def getWord(self):
        return self._words

    def setWord(self, words):
        if not type(words) is str:
            raise TypeError("Only integers are allowed")
        else:
            self._words = words

    def validateWords(self):
        words = DFA.dfa_word_acceptance(self._dfa_assigned, self._words)

        if words:
            return f'Aceptada'
        else:
            return f'Rechazada'

    def toString(self):
        return f'Words: {self._words}'

