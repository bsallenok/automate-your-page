#!DOCTYPE html
#--Project Stage 2-->
#Bonnie's Notes
def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)

EXAMPLE_LIST_OF_CONCEPTS = [ ['How the Web Works', 'A user opens a browser such as Firefox and requests a URL'],
                             ['Hypertext Markup Language', 'Hypertext Markup Language or HTML for short'],
                             ['Why Programmers are so Smart', 'Programmers have to be smart because computers are stupid!'],
                             ['Programmers Vocabulary', 'In programming language there are tag, element and attribute definitions.'],
                             ['Udacity Image', 'This image was borrowed from Udacity Intro to Programming lesson one to illustrate img tag.'],
                             ['Developer Tools Inline and Block', 'HTML elements are inline or block.'],
                             ['HTML Structuring and CSS Styling', 'HTML and Cascading Style Sheets are two languages used to create web pages.'],
                             ['Text Editors for Programming', 'Text editors like Scratchpad, Codepen and Sublime make writing code easier.'],
                             ['Adding Style with CSS', 'Programmers use CSS to add style to their HTML structure.'],
                             ['The Box Model and Avoiding Repetition with CSS', 'Programmers define boxes around their content with "div" tags.'],
                             ['Code-Test-Refine', 'Perfect practice calls for code, test, and refine behavior.'],
                             ['Computers and Computer Programs', 'The computer by itself does not know what to do; it has limited functionality.'],
                             ['Programming Languages', 'Programming languages tell the computer what steps to take.'],
                             ['Python and its Grammar Rules', 'The computer language,Python, was named from the Monty Python series.'],
                             ['Variables', 'Python allows the programmer to use variables to keep track of numbers via the Assignment Statement.'],
                             ['They are called Variables because they Vary', 'In Python the = sign means assignment'],
                             ['Strings', 'Strings are a sequence of characters surrounded by quotes.'],
                             ['What is a Function?', 'A function takes input, does something to that input, and then produces output.'],
                             ['Making versus Using a Function', 'Functions are made by starting a line of code with a keyword: def.'],
                             ['How do Functions help Programmers Avoid Repetition?', 'Functions are tools that programmers can create and reuse forever!'],
                             ['What happens when a Function does not have a Return', 'Without a Return, Pyton will produce special output: None'],
                             ['What is an if statement?', 'We can use the if statement on a test expression and make a decision based on comparisons.'],
                             ['While Loops', 'While will loop and execute 0 to an infinite number of times as long as the test expression is TRUE.'],
                             ['Debugging', 'Debugging is a necessary skill to master if you want to become a good programmer.'],
                             ['What is a list?', 'A list is a sequence of not just characters but also numbers, strings, and other lists.'],
                             ['Loops on Lists: for', 'Python provides a simpler way to loop through lists via the for loop'],
                             ['Problem Solving', 'Approach the problem systematically by writing small bits of code, testing them and knowing what they do.']] 


def make_HTML_for_many_concepts(list_of_concepts):
    HTML = ""
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML

print make_HTML_for_many_concepts(EXAMPLE_LIST_OF_CONCEPTS)

    