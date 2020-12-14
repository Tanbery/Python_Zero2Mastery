import pyjokes as pj

joke = pj.get_joke()
print("A Joke:", joke)

jokes = pj.get_jokes()
print("All Jokes: ")
i=1
for joke in jokes:
    print( i,":", joke)
    i+=1