import markovify

inText = ''
infile = open('./Oathbringer.txt', 'r')
for line in infile:
    if line[0:1] != '<':
        if len(line) != 0:
            inText += line

text_model = markovify.Text(inText)


# Print five randomly-generated sentences
for i in range(5):
    print(text_model.make_sentence())
    print('')

# Print three randomly-generated sentences of no more than 140 characters
for i in range(3):
    print(text_model.make_short_sentence(140))
    print('')

