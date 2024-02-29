import nltk 
from nltk.chat.util import Chat, reflections
  
pairs =[
    ['my name is (.*)', ['Hello !']],
    ['(hi|hello|hey|holla|hola)', ['Hey there !', 'Hi there !', 'Hey !']],
    ['(.*) your name ?', ['My name is chitty']],
    ['(.*) do you do ?', ['Making robo army !']],
    ['(.*) created you ?', ['--- nobody created me i am the creator']]
]
  
chat = Chat(pairs, reflections)
chat.converse()