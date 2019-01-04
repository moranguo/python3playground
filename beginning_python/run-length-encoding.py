# State machine approach:

def run_length_encode(text):
    result = []

    # Keeps track of the letter we're in the midst of a run of
    current_letter = None
    # Keeps track of how many times we've seen that letter
    count = 0

    # Iterate over each letter in the string
    for letter in text:

        # If it's the same letter we're already tracking
        if letter == current_letter:
            count += 1
        else:
            # Unless it's the very start of the process
            if count > 0:
                result.append((current_letter, count))

            # Start tracking the new letter
            current_letter = letter
            count = 1

    # Without this, we'd fail to return the last letter
    result.append((current_letter, count))

    # At this point, result looks like [('A', 3), ('B', 2), ...]
    # This next line combines the letters and counts and then puts everything into a single string
    #return ''.join('{}{}'.format(letter, count) for letter, count in result)
    return result

def run_length_decode(result):
    string_result=''
    for letter, count in result:
        string_result += letter*count
    return string_result

result = run_length_encode('AAABBCCCDAAT')
print(''.join('{}{}'.format(letter, count) for letter, count in result))
print(run_length_decode(result))
#assert run_length_encode('AAABBCCCDAAT') == 'A3B2C3D1A2T1'

