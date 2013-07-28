from ps3a import *
import time
from perm import *


#
#
# Problem #6A: Computer chooses a word
#
#
def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    # TO DO...
    for i in xrange(0,len(hand)):
        perms=get_perms(hand,len(hand)-i)
        for j in xrange(0,len(perms)):
            if perms[j] in word_list:
                return perms[j]
    return ''

                             
                             
            
    
#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    # TO DO ...    
    print 'Present hand: '
    display_hand(hand)
    score=0
    done=0
    while done!=1:
        word=comp_word=comp_choose_word(hand,word_list)
        ##check for null case
        ##check for valid word
        ##else compute score and update hand & display hand
        ##break if hand is null
        if word=='':
            print 'No word(s) found quitting'
            break
        if not(is_valid_word(word,hand,word_list)):
            print 'That is not a valid word'
        else:
            print 'Computer word chosen: ' + str(word)
            score+=get_word_score(word,HAND_SIZE)
            print 'Score: ' + str(score)
            hand=update_hand(hand,word)
            display_hand(hand)
        if hand=={}:
            raw_input('No solutions left. Press any key to quit')    
            break
#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    # TO DO...
    old_hand={}
    hand={}
    done=0
    while done !=1:
        print "Input 'n' to play a new random hand."
        print "Input 'r' to play the last hand again."
        print "Input 'e' to exit the game."
        user_prompt1=raw_input('Please enter your selection: ')
        
        if user_prompt1=='n':
            hand=deal_hand(HAND_SIZE)
            old_hand=hand
        elif user_prompt1=='r':
            if old_hand=={}:
                print 'You must have played at least one hand before replaying'
            else:
                hand=old_hand
        elif user_prompt1=='e':
            break
        else:
            print 'Please enter a valid command'
        while done !=1:
            print "Input 'u' to enable user chosen words."
            print "Input 'c' to enable computer chosen words."
            user_prompt2=raw_input('Please enter your selection: ')
            print str((user_prompt2!="c") or (user_prompt2!="u"))
            if (user_prompt2!="c") and (user_prompt2!="u"):
                print 'Please enter a valid command'
            else:
                break
        if hand !={}:
            if user_prompt2=='u':
                play_hand(hand,word_list)
            if user_prompt2=='c':
                comp_play_hand(hand,word_list)
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

    
