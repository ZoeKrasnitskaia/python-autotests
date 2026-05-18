class Lead:
    def __init__(self, name):
        self.name = name

def change_name(lead):
        lead.name = 'name2'

lead_name = Lead("Имя")

change_name(lead_name)

print(lead_name.name)
