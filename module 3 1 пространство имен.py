calls = 0


def count_calls():
    global calls
    calls = calls + 1


def string_info(string):
    global calls
    calls = calls + 1
    print((len(string), string.upper(), string.lower()))


def is_contains(string,list_to_search):
    global calls
    calls = calls + 1
    list_to_search_lower = [word.lower() for word in list_to_search]
    if string.lower() in list_to_search_lower:
        print(True)
    else:
        print(False)


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
