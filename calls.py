calls = 0


def count_calls(value):
    global calls
    calls += value

def string_info(string):
    count_calls(1)
    return (len(string), string.upper(), string.lower())


def contains(string, list_to_search):  #is_contians не верно
    found = False
    for i in list_to_search:
        if i.lower() == string.lower():
            found = True

    if found == True:
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBan
print(contains('cycle', ['recycle', 'cyclic']))  # No matches
print(calls)
