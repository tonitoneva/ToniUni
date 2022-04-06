from inheritance_ex.project3ex.elf import Elf


class MuseElf(Elf):
    def __init__(self, username, level):
        super().__init__(username, level)