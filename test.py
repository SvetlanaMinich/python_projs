import time

def remove_double_letters(text):
    '''Alice knows that NSA agents use the following algorithm to cipher their messages.

        1. They delete all spaces and punctuation marks.
        2. They replace all successive identical letters with only one such letter.
        3. They insert two identical letters at an arbitrary place many times.

        Alice has intercepted some messages which are "meaningless" sequences of letters that NSA agent 
        Bob has sent to another NSA agent Caroline about Alice's possible location. She wants to be able 
        to restore the message as it was after step 2). Help Alice write a program in Python that removes 
        all pairs of identical letters from the message inserted in the third step.

        The program should be executed by calling “python alice.py path/to/file.txt” from the Unix shell 
        where "path/to/file.txt" is the path to the file with a ciphered message sent by Bob. The message 
        consists of lowercase English letters and its length is at most 100 000. Output the message after 
        step 2). The program should produce an answer in less than a few seconds.
        '''
    start_time = time.time()
    index = 0
    while len(text) != 0 and text[0] == text[1]:
        text = text[2:]
    while index < len(text)-1:
        if text[index] == text[index+1]:
            text = text[:index] + text[index+2:]
            index -= 1
            continue
        index += 1
    end_time = time.time()
    print(f"time: {end_time-start_time:.6f} seconds")
    return text

text_to_check = "wwaldnaandicffenn"
result_text = remove_double_letters(text_to_check)
print(result_text)