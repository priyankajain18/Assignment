import os, sys


def solve_jumble_word(jumble_word):

    result = {}

    lower_jumble_word = jumble_word.strip().lower()

    # Sort lower_jumble_word to check if sorted_jumble_word exists as a key in jumble_dict
    sorted_jumble_word = ''.join(sorted(lower_jumble_word))

    try:
        f_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dictionary.txt')
        f = open(f_path, 'r')
        jumble_dict = {}

        while True:
            for line in f:
                # Remove whitespace characters and then convert it to lowercase
                word = line.strip().lower()

                # Check if length of word is equal to length of sorted_jumble_word
                if len(word) == len(sorted_jumble_word):
                    # Sort word to make it as a key in jumble_dict
                    sorted_word = ''.join(sorted(word))

                    if sorted_word.startswith(sorted_jumble_word[0]) and sorted_word.endswith(sorted_jumble_word[-1]):
                        # Make sorted_word as a key in jumble_dict with empty list as a value
                        # If it already exists then append its value with word
                        jumble_dict.setdefault(sorted_word, []).append(word)
            f.close()
            break

        # Check if sorted_jumble_word exists as a key in jumble_dict
        if sorted_jumble_word in jumble_dict:
            result["words"] = jumble_dict[sorted_jumble_word]
        else:
            result["message"] = "Sorry! No word is present for %s" % jumble_word

    except IOError:
        result["message"] = "Oops! File doesn't exist."

    return result


if __name__ == '__main__':

    jumble_word = ''

    try:
        jumble_word = sys.argv[1]
        response = solve_jumble_word(jumble_word)

        if "message" in response:
            print response["message"]

        if "words" in response:
            print "Words for %s:" % jumble_word
            for word in response["words"]:
                print word

    except IndexError:
        print "Oops! Please enter a Jumble Word."
