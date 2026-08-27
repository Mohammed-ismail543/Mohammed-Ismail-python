# match-case statement

def month_name(month):
    match month:
        case 1:
            return "It is January"
        case 2:
            return "It is February"
        case 3:
            return "It is March"
        case 4:
            return "It is April"
        case 5:
            return "It is May"
        case 6:
            return "It is June"
        case 7:
            return "It is July"
        case 8:
            return "It is August"
        case 9:
            return "It is September"
        case 10:
            return "It is October"
        case 11:
            return "It is November"
        case 12:
            return "It is December"
        case _:
            return "Not a valid month"

print(month_name(10))