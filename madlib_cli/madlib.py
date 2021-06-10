import re
from typing import Counter

def print_salutation():
    print('''\n *****************************************************************************
    Wlecome to our Madlib Game :)
    Our funny game basied on your creativity in chosing phrases !!
    let's get start !! \n *****************************************************************************''')

if __name__ == "__main__": 
    print_salutation()
    


def read_template(path):
    '''
    A functon that read a text from a file 

    input : optional argument with defult value of file path

    return : the whole text in file 
    '''
    with open(path) as file:
        text = file.read()
    return text   


    
def parse_template(text):

    '''
    A function make analysis on a text so it will find any word in {} like:
    '{hi}' 

    input : an optinal aregument with defult value of text

    retutn : 1. a formated text ready to be print '{hi}' => '{}'
             2. the words where in the braces => hi
    '''

    regex = r"\{(.*?)\}"
    matches = re.findall(regex, text)
    text_to_print =  re.sub( r"\{(.*?)\}", '{}', text)
    return  [text_to_print , tuple(matches)]


def prompt_inputs(matches):
    
    '''
    A function to take the user inputs to be replaced 

    '''
    input_array = []
    print(' \n    Please answer the below: \n ' )
    for x in range(len(matches)):
        input_array += [input( f'{matches[x]} :')]
    print('\n \n')
    return tuple(input_array)
counter_template = 1
def merge(text_to_print , inputs):

    '''
    A function merge a stripped text with text parts '{}' + 'hi' => '{hi}' 

    input : 1. optional argument with defult value of stripped text
            2. optional argument with defult value of text parts

    retutn : the merged text parts & stripped text
    '''
    completed_text = text_to_print.format( *inputs )
    with open('assets/result.txt', 'w') as completed:
        completed.write(completed_text)
    
    return completed_text

def run_code():
    read = read_template('assets/template.txt')
    pars = parse_template(read)
    prompt = prompt_inputs(pars[1])
    result = merge(pars[0] , prompt)
    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
    print(result)
    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
    



if __name__ == "__main__": # if running this as a script using $ python topics.py
    run_code()