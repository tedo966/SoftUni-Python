class Party:
    def __init__(self):
        self.people = []


party = Party()

while True:
    name = input()

    if name == "End":
        break

    party.people.append(name)

result = ", ".join(party.people)
print(f"Going: {result}")
print(f"Total: {len(party.people)}")