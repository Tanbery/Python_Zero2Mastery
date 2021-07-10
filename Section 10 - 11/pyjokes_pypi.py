#pip install pyjokes ==> must be done before using it
#import pyjokes as pj

from pyjokes import  get_joke, get_jokes
joke = get_joke()
print("A Joke: ", joke)

jokes = get_jokes()
print("All Jokes: ")
i=1
for joke in jokes:
    print( i,"\t:", joke)
    i+=1