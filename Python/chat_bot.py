# question : answer
import time
now = time.ctime()
qna = {
    'Hii' : '>Hey',
    'How are you' : ">I am fine.",
    'What is your name' : '>My name is Jarvis.',
    'How old are you'  : '>I am one year older than you.',
    'What is the time now' :now,
    'Speak up!' : '>I am worried about everything.',
    'How long have you worried about everything' : '>Since I came to LPU.',
    'Why did you came to MIT' : '>I wish I knew.',
    'Why did you say "I wish I knew"' : '>Stupid computer',
    'How much is 2 plus 2' : '>Does the number 2 have special significance for you.',
    'I am worried about my students ' : '>How long have you been worried about MY STUDENTS',
    'What should I tell them about the quizzes' : '>Tell them you feel their pain',
    'They say the eat Hamantashen at TEAL' : '>TEAL must be a place where fun goes to die.'
    }

while True:
    qs = input()
    if (qs == 'quit'):
        break
    else:
        print(qna[qs])
