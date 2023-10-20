

class vowels_upper_lower_count:
    def __init__(self, msg):
        self.msg = msg
        self.count_vowels = 0
        self.count_upper = 0
        self.count_lower = 0
        self.count_space = 0  
        self.count_digit = 0
        self.count_symbol = 0

    def countvowels(self):
        for i in self.msg:
            if i in 'aeiouAEIOU':
                self.count_vowels += 1
        return self.count_vowels
    
    def countupper(self):
        for i in self.msg:
            if i.isupper():
                self.count_upper += 1
        return self.count_upper
    
    def countlower(self):
        for i in self.msg:
            if i.islower():
                self.count_lower += 1
        return self.count_lower
    
    def countspace(self):
        for i in self.msg:
            if i.isspace():
                self.count_space += 1
        return self.count_space


    def countdigit(self):
        for i in self.msg:
            if i.isdigit():
                self.count_digit += 1
        return self.count_digit
    
    def countsymbol(self):
        for i in self.msg:
            if i.isupper():
                pass
            elif i in 'aeiouAEIOU':
                pass
            elif i.islower():
                pass
            elif i.isdigit():
                pass
            elif i.isspace():
                pass
            else:
                self.count_symbol += 1
        return self.count_symbol


    def call_all(self):
        self.countvowels()
        self.countupper()
        self.countlower()
        self.countspace()
        self.countdigit()
        self.countsymbol()

    def print_value(self):
        print(f"Length of massage: {len(self.msg)}")
        print(f"Vowels in string: {self.count_vowels}")
        print(f"UpperCase in string: {self.count_upper}")
        print(f"LowerCase in string: {self.count_lower}")
        print(f"Space in string: {self.count_space}")
        print(f"Digits in string: {self.count_digit}")
        print(f"Symbols in string: {self.count_symbol}")



stmsg= input('Enter the srting: ')
st = vowels_upper_lower_count(stmsg)
st.call_all()
st.print_value()
