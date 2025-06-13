from random import choice

"""
The iPhone is a cellular phone, allowing users to make and receive calls and send text.
The iPhone is a line of smartphones developed and marketed by Apple that run iOS.
The first-generation iPhone was announced by then–Apple CEO and co-founder Steve Jobs.
 """
sentence1 = [
    'As a cellular phone, the iPhone enables users to send and receive texts as well as make calls.',
    'The iPhone is a cellular phone that lets users send and receive texts as well as make and receive calls.',
    'Users can send and receive texts and make and receive calls on the iPhone, which is a cellular phone.',
    'The iPhone is a cellular phone, allowing users to make and receive calls and send text.'
]

sentence2 = [
    'The iPhone is a line of smartphones developed and marketed by Apple that run iOS.',
    'Apple created and markets the iPhone range of iOS-powered devices.',
    'Apple created and markets a range of iOS-powered cellphones called the iPhone.',
    'Developed and marketed by Apple, the iPhone is a line of iOS-powered cellphones.'
]

sentence3 = [
    'As a cellular phone, the iPhone enables users to send and receive texts as well as make calls.',
    'The iPhone is a cellular phone that lets users send and receive texts as well as make and receive calls.',
    'Users can send and receive texts and make and receive calls on the iPhone, which is a cellular phone.',
    'As a mobile phone, the iPhone enables users to send and receive texts as well as make and receive calls.'
]

# random selection form sentences
# concatenation of all sentences
# add html p tag

def paragraph_formation(s1, s2, s3):
    """
    This function will create random paragraph
    :param s1, s2, s3: list of sentences
    :return: A paragraph
    """
    paragraph = choice(s1) + ' ' + choice(s2) + ' ' + choice(s3)
    return f'<p> {paragraph} </p>'
print(paragraph_formation(sentence1, sentence2, sentence3))
print(paragraph_formation(sentence1, sentence2, sentence3))
print(paragraph_formation(sentence1, sentence2, sentence3))
print(paragraph_formation(sentence1, sentence2, sentence3))
