#29
class MainClass:
    def __init__(self, text_field):
        self.text_field = text_field

    def set_text_field(self, text=None):
        if text is not None:
            self.text_field = text
        else:
            self.text_field = "Default Text"


class SubClass(MainClass):
    def __init__(self, text_field, numeric_field):
        super().__init__(text_field)
        self.numeric_field = numeric_field


if __name__ == "__main__":
    main_obj = MainClass("Initial Text")
    print("Main Class Text Field:", main_obj.text_field)

    main_obj.set_text_field("Updated Text")
    print("Main Class Text Field After Update:", main_obj.text_field)

    sub_obj = SubClass("Subclass Text", 42)
    print("Subclass Text Field:", sub_obj.text_field)
    print("Subclass Numeric Field:", sub_obj.numeric_field)

    sub_obj.set_text_field("Updated Subclass Text")
    print("Subclass Text Field After Update:", sub_obj.text_field)
#30
class MainClass:
    def __init__(self, text_field):
        self.text_field = text_field

    def set_text_field(self, text=None):
        if text is not None:
            self.text_field = text
        else:
            self.text_field = "Default Text"


class SubClass(MainClass):
    def __init__(self, text_field, numeric_field):
        super().__init__(text_field)
        self.numeric_field = numeric_field

if __name__ == "__main__":
    main_obj = MainClass("Initial Text")
    print("Main Class Text Field:", main_obj.text_field)

    main_obj.set_text_field("Updated Text")
    print("Main Class Text Field After Update:", main_obj.text_field)

    sub_obj = SubClass("Subclass Text", 42)
    print("Subclass Text Field:", sub_obj.text_field)
    print("Subclass Numeric Field:", sub_obj.numeric_field)

#34
class Roman:
    roman_numerals = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40,
                      'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500,
                      'CM': 900, 'M': 1000}

    def __init__(self, value):
        if isinstance(value, str):
            self.value = self.roman_to_int(value)
        elif isinstance(value, int):
            self.value = value
        else:
            raise ValueError("Invalid input. Must be a Roman numeral string or an integer.")

    def __str__(self):
        return self.int_to_roman(self.value)

    def __add__(self, other):
        if isinstance(other, Roman):
            return Roman(self.value + other.value)
        else:
            raise TypeError("Unsupported operand type. Must be Roman.")

    def __sub__(self, other):
        if isinstance(other, Roman):
            return Roman(self.value - other.value)
        else:
            raise TypeError("Unsupported operand type. Must be Roman.")

    def __mul__(self, other):
        if isinstance(other, Roman):
            return Roman(self.value * other.value)
        else:
            raise TypeError("Unsupported operand type. Must be Roman.")

    def __truediv__(self, other):
        if isinstance(other, Roman):
            return Roman(self.value // other.value)
        else:
            raise TypeError("Unsupported operand type. Must be Roman.")

    @staticmethod
    def roman_to_int(s):
        result = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i+2] in Roman.roman_numerals:
                result += Roman.roman_numerals[s[i:i+2]]
                i += 2
            else:
                result += Roman.roman_numerals[s[i]]
                i += 1
        return result

    @staticmethod
    def int_to_roman(num):
        result = ''
        for value, numeral in sorted(((value, numeral)
                                     for numeral, value in Roman.roman_numerals.items()), reverse=True):
            while num >= value:
                result += numeral
                num -= value
        return result


# Пример использования
if __name__ == "__main__":
    roman1 = Roman("XII")
    roman2 = Roman("IV")

    print(f"{roman1} + {roman2} = {roman1 + roman2}")
    print(f"{roman1} - {roman2} = {roman1 - roman2}")
    print(f"{roman1} * {roman2} = {roman1 * roman2}")
    print(f"{roman1} / {roman2} = {roman1 / roman2}")

