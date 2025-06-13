paragraph1 = 'This is paragraph'
paragraph2 = 'This is paragraph two'
paragraph3 = 'This is paragraph three'
paragraph4 = 'This is paragraph four'

def paragraph_html(paragraph):
    paragraph1_html = f'<p> {paragraph} </p>'
    return paragraph1_html
paragraph_html1 = paragraph_html(paragraph1)
paragraph_html2 = paragraph_html(paragraph2)
paragraph_html3 = paragraph_html(paragraph3)
paragraph_html4 = paragraph_html(paragraph4)

print(paragraph_html1)
print(paragraph_html2)
print(paragraph_html3)
print(paragraph_html4)

def h2_html(text):
    h2 = f'<h2> {text.title()} </h2>'
    return h2
print(h2_html('Top 10 product review'))
