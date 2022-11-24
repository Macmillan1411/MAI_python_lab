from string import ascii_uppercase

class Alphabet:

    def __init__(self,lang,letters):
        self.lang = lang
        self.letters = list(letters) 

    def print(self):
         print(self.letters)

    def letters_num(self):
        print(f"количество букв в алфавите: {len(self.letters)}")

class EngAlphabet(Alphabet):

    _letters_num = 26
    
    def __init__(self, lang='En', letters=ascii_uppercase):
        super().__init__(lang='En', letters=ascii_uppercase)
        self.lang = lang
        self.letters = list(letters) 

    def is_en_letter(self,let):
        self.let = let.upper()
        if self.let in self.letters:
            return True
        return False    

    def letters_num(self):
        return self._letters_num

    @staticmethod
    def example():
        return "Any text in English!"


#test object
en = EngAlphabet()

#tests 
en.print()
print(f"Количества букв в алфавиту: {en.letters_num()}")
print(f"Буква F относится к англискому алфавиту: { en.is_en_letter('F') }")
print(f"Буква Щ относится к англискому алфавиту: { en.is_en_letter('Щ') }")
print(en.example())

print("-------------------------------------------------------------------")



'''
#test russian alphabet
ru = Alphabet("Ру",'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ')

#tests for russian keyboard
ru.print()
print(f"Количества букв в алфавиту: {ru.letters_num()}")

'''









