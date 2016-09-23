import json
import fileinput


morse_code = {}
code_morse = {}
with open('morse.json') as json_data:
    json_str = json_data.read()
    morse_code = json.loads(json_str)
    json_data.close()
    print("{}".format(morse_code))

for key, value in morse_code.iteritems():
    code_morse[value] = key


#for line in fileinput.input():
    #print line

APOSTROPHE = '.-....- -....- -....- -....- .'

sentence = ""
with open('in') as morse_in:
    for line in morse_in:
        for word in line.split("     "):
            print word
            if APOSTROPHE in word:
                words = word.split(APOSTROPHE)
                # parse first half
                for letter in words[0].split(" "):
                    if letter:
                        sentence += code_morse[letter.strip()]

                sentence += "'"

                # parse second half
                print ("words[1] = {}".format(words[1]))
                for letter in words[1].split(" "):
                    if letter and letter != '\n':
                        sentence += code_morse[letter]

                sentence += " "
                continue
            for letter in word.split(" "):
                if letter in code_morse:
                    sentence += code_morse[letter]
            sentence += " "
print sentence
