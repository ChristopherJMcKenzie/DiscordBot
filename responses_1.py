import random

def handle_response(message: str) -> str:
    user_message = message.lower()
    keywords = ['office hours', 'instructor info', 'course grading', 'lab policy', 'test policy', 'prerequisites', 'topic', 'lecture policy', 'plagiarism policy', 'accommodations policy' ]


    if 'office hours' in user_message:
        user_message = user_message.replace('office hours', '').strip()
        print(user_message)
        return 'The office hours for CSCI 1620 are\nWednesday (11am- 1pm)\nLocated at PKI 285B\n\n' + handle_response(user_message)

    if 'instructor info' in user_message:
        user_message = user_message.replace('instructor info', '').strip()
        return 'Instructor name: Agatha Orowa\nEmail: aowora@unomaha.edu\n\n' + handle_response(user_message)
                
    if 'course grading' in user_message:
        user_message = user_message.replace('course grading', '').strip()
        return '100-97: A+   96-93: A   93-90: A-\n89-87: B+   86-83: B   82-80: B-\n79-77: C+   76-73: C   72-70: C-\n69-67: D+   66-63: D   62-60: D-\n59-0: F\n\n12-labs-30%\n10-tests-50%\n1-project-20%\n\n' + handle_response(user_message)

    if 'lab policy' in user_message:
        user_message = user_message.replace('lab policy', '').strip()
        return '''You are allowed to work individually, or in groups of 2.\nIf you choose to work in a group, only 1 person needs to make a submission (make sure you include your groupmates name in the comment section)
Late work will receive a grade of 0\nPlease check submission for correct files, and use correct file names\nYou can use office hours, class sessions, and lab sessions to receive feedback before submission\n\n''' + handle_response(user_message)

    if 'test policy' in user_message:
        user_message = user_message.replace('test policy', '').strip()
        return '''Tests are open note, with a time limit. They should be done individually, and be completed before the deadline.\nYou will be required to use lockdown browser, and have your webcam on during the test.\n
You are only allowed to use printed paper notes for the test.\n you will receive a 0 for the first time you are caught cheating, and a failing grade and administrative follow up for your second offense.\n\n''' + handle_response(user_message)

    if 'prerequisites' in user_message:
        user_message = user_message.replace('prerequisites', '').strip()
        return 'CIST 1400 (with a grade of C or better).\n\n' + handle_response(user_message)

    if 'topic' in user_message:
        user_message = user_message.replace('topic', '').strip()
        return 'Below is a list of topics that will be covered in the CIST-1620\n1. Programming Structures\n2. Data Structures\n3. Modules\n4. Files\n5. Exceptions\n6. Algorithm Analysis\n7. Recursion\n8. Searching and Sorting\n9. Object Oriented Programming\n10. Graphical User Interfaces\n11. Testing\n12. Documentation\n' + handle_response(user_message)

    if 'lecture policy' in user_message or 'class material policy' in user_message:
        user_message = user_message.replace('lecture policy', '').strip()
        user_message = user_message.replace('class material policy', '').strip()
        return """1.) Complete weekly tasks in the order they are listed in Canvas.\n2.) The lecture videos explain the notes provided.\n3.) Some topics have review questions provided for practice.
4.) The discord server will be used as a discussion platform where announcements, resources, and answers to any questions asked regarding the class material will be posted. Anyone can respond to a question posted to the server\n\n""" + handle_response(user_message)

    if 'plagiarism rules' in user_message:
        user_message = user_message.replace('plagiarism rules', '').strip()
        print(user_message)
        return "1.) if it is discovered you uploaded lab/test questions publicly to the internet, you will receive a failing grade for this class with administrative follow-up.\n 2.) If it is discovered you copied lab/test answers from the internet, or represented someone else's project idea as your own, you will receive 0 the first time and a failing grade for this class with administrative follow-up the second time.\n\n" + handle_response(user_message)

    if 'accommodations policy' in user_message:
        user_message = user_message.replace('accommodations policy', '').strip()
        return "1.) if you have any accommodations I need to be aware of, please reach out to the accessibility office before the end of the first week, to get official documentation.\n2.) To get an accommodation for a missed lab, test, or project, you must send an email to the accessibility office. They are the responsible for validating any documentation you might have (doctor's note etc.) and reaching out to me to formally ask for an accommodation on your behalf.\n\n" + handle_response(user_message)


    
    
    for words in range(len(keywords)):
        if keywords[words] not in user_message:
            return ''






























































































    # if user_message == "hello" or user_message == 'hi' or user_message == 'hey':
    #     return 'Hi there, I am the project bot made by Zidan and CJ.\nTo get a list of my commands, just do $help!'
    
    # #help message
    # if user_message == '$help':
    #     return 'My commands are:\n$d (number of sides you want dice to be)\n$rps (Rock Paper Scissors)\n$cf (Coin Flip)\n$bms (hehe)'
    


    # #explaining how to use dice
    # if user_message == '$d':
    #     return 'To use the dice command, type $d followed by the number of dice sides you want!\nExample $d 100'

    # #dice logic
    # if user_message.startswith('$d '):
    #     dice_sides = int(user_message.split()[1])
    #     return random.randint(1,dice_sides)
    


    # if user_message == '$cf':
    #     val = random.randint(1,2)
    #     if val == 1:
    #         return 'Heads'
    #     elif val == 2:
    #         return 'Tails'
    


    # #explaining how to use rock paper scissors
    # if user_message == '$rps':
    #     return 'To perform rock paper scissors, type $rps followed by what you want to throw!\nExample: $rps scissors.'
    
    # #rock paper scissors logic
    # if user_message.startswith('$rps '):
    #     choices = ['rock', 'paper', 'scissors']
    #     user_throw = user_message.split()[1]
    #     bot_throw = choices[random.randint(0,2)]
    #     if bot_throw == user_throw:
    #        return 'Tie'
    #     elif bot_throw == 'rock':
    #         if user_throw == 'paper':
    #             return 'I throw rock, and you win!'
    #         elif user_throw == 'scissors':
    #             return 'I throw rock, and you lose!'
            
    #     elif bot_throw == 'paper':
    #         if user_throw == 'rock':
    #             return 'I throw paper, and you lose!'
    #         elif user_throw == 'scissors':
    #             return 'I throw paper, and you win!'
            
    #     elif bot_throw == 'scissors':
    #         if user_throw == 'rock':
    #             return 'I throw scissors, and you win!'
    #         elif user_throw == 'paper':
    #             return 'I throw scissors, and you lose!'




    if user_message == '$bms':
        return 'https://cdn.discordapp.com/attachments/315582255386853376/1103874389734346802/buckle_me_shoe.mp4'


    

    