import inflect

p = inflect.engine()

def timeInWords(h, m):
    if m == 0:
        return f"{p.number_to_words(h)} o' clock"
    elif m == 15:
        return f"quarter past {p.number_to_words(h)}"
    elif m == 30:
        return f"half past {p.number_to_words(h)}"
    elif m == 45:
        return f"quarter to {p.number_to_words((h % 12) + 1)}"
    elif m < 30:
        minute_word = "minute" if m == 1 else "minutes"
        return f"{p.number_to_words(m).replace('-', ' ')} {minute_word} past {p.number_to_words(h)}"
    else:
        to_minutes = 60 - m
        minute_word = "minute" if to_minutes == 1 else "minutes"
        return f"{p.number_to_words(to_minutes).replace('-', ' ')} {minute_word} to {p.number_to_words((h % 12) + 1)}"


print(timeInWords(5, 47))