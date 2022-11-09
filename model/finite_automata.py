def display_menu():
    print("\n 1 - Display the set of states")
    print("2 - Display the alphabet")
    print("3 - Display the transitions")
    print("4 - Display the initial state")
    print("5 - Display the final state\n")


class FA:
    def __init__(self):
        self.states = []
        self.alphabet = []
        self.transitions = []
        self.initial_state = 0
        self.final_states = []
        self.fileFA = open("files/FA.in", "r")
        self.read_file()
        self.cmds = {'1': self.display_states(), '2': self.display_alphabet(), '3': self.display_transitions(),
                     '4': self.display_initial(), '5': self.display_final()}

    def display_states(self):
        print("Set of states: \n")
        for state in self.states:
            print(state)

    def display_alphabet(self):
        print("The alphabet: \n")
        for letter in self.alphabet:
            print(letter)

    def display_transitions(self):
        print("The transitions: \n")
        for tran in self.transitions:
            print(tran)

    def display_initial(self):
        print("Initial state: \n")
        print(self.initial_state)

    def display_final(self):
        print("Final states: \n")
        for state in self.final_states:
            print(state)

    def read_file(self):
        self.states = self.fileFA.readline().split(" ")
        self.alphabet = self.fileFA.readline().split(" ")
        self.transitions = self.fileFA.readline().split(";")
        self.initial_state = self.fileFA.readline().strip().split(" ")
        self.final_states = self.fileFA.readline().split(" ")

    def start(self):

        display_menu()

        while True:
            cmd = input().strip().lower()
            if cmd == 'exit':
                return
            if cmd not in self.cmds:
                print("\nBad command")
            try:
                self.cmds[cmd]()
            except ValueError as ve:
                print("error - " + str(ve))
