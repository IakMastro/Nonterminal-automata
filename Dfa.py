class Automata:
    instructions: dict
    sum_of_states: int
    alphabet: dict
    curr_state: str
    final_state: dir

    def set_states(self, lines):
        self.sum_of_states = lines[0]
        self.alphabet = lines[1].split()
        self.curr_state = lines[2]
        self.final_state = lines[3].split()

        self.instructions = {}
        for i in range(4, len(lines)):
            line = lines[i].rsplit(" ", 1)
            self.instructions[line[0]] = line[1]

    def change_state(self, answer):
        self.curr_state = self.instructions[self.curr_state + " " + answer]
        print(f"Current state changed to: {self.curr_state}")


if __name__ == '__main__':
    automata = Automata()

    with open("Dfa.txt", "r") as file:
        automata.set_states(lines=file.read().split("\n"))

    print(f"Information:\nSum of states: {automata.sum_of_states}")
    print(f"Alphabet: {automata.alphabet}")
    print(f"Initial State: {automata.curr_state}")
    print(f"Final State: {automata.final_state}")

    print("Instructions: ")
    for instruction in automata.instructions:
        print(f"From state {instruction[0]} and answer {instruction[2]} goes to {automata.instructions[instruction]}")

    for i in range(10):
        answer = input("Give next state: ")
        while answer not in automata.alphabet:
            answer = input(f"Give correct value from {automata.alphabet}: ")

        automata.change_state(answer)

    if automata.curr_state in automata.final_state:
        print("Ended successfully!")

    else:
        print("The library is wrong")
