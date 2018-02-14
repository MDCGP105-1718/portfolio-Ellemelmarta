lyrics = """
You were my sun
You were my earth
But you didn't know all the ways I loved you no
So you took a chance
And made other plans
But I bet you didn't think that they would come crashing down no

You don't have to say what you did
I already know I found out from him
Now there's just no chance for you and me there'll never be
And don't it make you sad about it

You told me you loved me
Why did you leave me all alone
Now you tell me you need me
When you call me on the phone
Girl I refuse you must have me confused
With some other guy
Your bridges were burned and now it's your turn
To cry cry me a river
Cry me a river-er
Cry me a river
Cry me a river-er yea yea

I know that they say
That somethings are better left unsaid
It wasn't like you only talked to him and you know it
Don't act like you don't know it
All of these things people told me
Keep messing with my head
Messing with my head
You should've picked honesty
Then you may not have blown it
Yea

You don't have to say, what you did
Don't have to say what you did
I already know I found out from him
I already know uh
Now there's just no chance for you and me there'll never be
No chance you and me
And don't it make you sad about it

You told me you loved me
Why did you leave me all alone
All alone
Now you tell me you need me
When you call me on the phone
When you call me on the phone
Girl I refuse you must have me confused
With some other guy
I'm not like them baby
Your bridges were burned and now it's your turn
It's your turn
To cry cry me a river
Go on and just
Cry me a river-er
Go on and just
Cry me a river
Baby go on and just
Cry me a river-er yea yea

Oh
Oh
The damage is done
So I guess I be leaving
Oh
Oh
The damage is done
So I guess I be leaving
Oh
Oh
The damage is done
So I guess I be leaving
Oh
Oh
The damage is done
So I guess I be leaving

You don't have to say what you did
Don't have to say what you did
I already know I found out from him
I already know uh
Now there's just no chance for you and me there'll never be
No chance you and me
And don't it make you sad about it

Cry me a river
Go on and just
Cry me a river-er
Baby go on and just
Cry me a river
You can go on and just
Cry me a river-er, yea yea

Cry me a river
Baby go on and just
Cry me a river-er
Go on and just
Cry me a river
Cause I've already cried
Cry me a river-er yea yea
Ain't gonna cry no more yea-yea

Cry me a river
Cry me a river oh
Cry me a river oh
Cry me a river oh

Cry me a river oh
Cry me cry me
Cry me a river oh
Cry me cry me
Cry me a river oh
Cry me cry me
Cry me a river oh
Cry me cry me

Cry me a river oh
Cry me cry me
Cry me a river oh
Cry me cry me
Cry me a river
Cry me cry me
"""
lyrics_check = (lyrics.lower()).split()
#turned lyrics into lower case so it counts them all as the count was case sensitive so displayed slightly wrong

def freq_dict(lyrics_check):
    """
    Creates a dictionary with a count of the words within the song lyrics and returns that dictionary
    """
    count_lyrics = {}
    for w in lyrics_check:
        count_lyrics[w] = count_lyrics.get(w, 0) + 1
#goes through list if the word is the same as one thats come up before then +1 to value if not makes new entry with value 1)
    return count_lyrics

lyric_dict = freq_dict(lyrics_check)

most_commmon = max(lyric_dict, key=lyric_dict.get)
#making the max look at the highest value for the key and providing us with the dictionary input that goes with it
most_commmon_value = max(lyric_dict.values())

print (f"The word that appears the most is: '{most_commmon}', appearing: {most_commmon_value} times.")

#insert something to avoid the input error like with letters etc
word_repeat = int(input("Enter the number for finding words the repeated at least X amount of times: "))


def input_frequency(lyric_dict, word_repeat):
    """
    """
    lyric_dict_higher = {}
    for a in lyric_dict.keys():
        #to make sure it is using the key values
        if word_repeat <= lyric_dict[a]:
            lyric_dict_higher[a] = lyric_dict[a]
    return lyric_dict_higher
print (f"These are the words that repeat more than {word_repeat} times:", str(input_frequency(lyric_dict, word_repeat)).strip('{}'))
#.strip helps to remove the [] from the list created and print just the number


# ----------------------------------------------------------------------
## Excess code I created at the start of creating this which worked with lists not dictionary and was looking for
## how many times a word repeated that the user entered.
#
#word = (input("Please enter a word to find in the song in lowercase: "))
#
#def freq_dict_input(lyrics_check, word):
#    """
#    Checks how many times the user input is within the song lyrics
#    """
#    frequency = []
#    for x in lyrics_check:
#        if x in word:
#            frequency.append(lyrics_check.count(x))
#            break
#    if x not in word:
#        frequency = 0
#    return frequency
#
##without break it would keep going through counting the letter and adding it to frequency list which ends up as
##lots of the same number this way it just prints the count once
#
#print (f"This word can be found", str(freq_dict_input(lyrics_check, word)).strip('[]'), "times.")
