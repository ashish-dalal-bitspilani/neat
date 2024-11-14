def roman_to_int(roman_numeral:str)->int:

    roman_to_int_map = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }

    value = 0
    previous = 0

    for numeral in reversed(roman_numeral):

        current = roman_to_int_map[numeral]

        if current < previous:
            value -= current
        else:
            value += current

        previous = current

    print(value)
    return value

roman_to_int('XXI')
roman_to_int("MCMXCIV")