# now we're starting to introduce the concepts of methods or functions.
# in Python, this is how you start a method with the 'def' keyword followed by the name of the function 'CalculaSegundos'
# and finally you'll end a function definition with parenthesis and colon. Inside the the parenthesis you can use parameters, but that's
# something we'll to learn about.

# this exercise, was a little bit of a brainstorming, had to seat for hours to figure out what was happenig here, I was even 
# importing some nonsense things that I ended up not using them, so, if you feel me, I'm not really in the mood to explain right now
# in the next commit I will explain every thing happening in these two functions. 

# TODO: explain the logic ASAP.
def CalculaSegundos(seg):
    hour = int(seg / (60 * 60))
    minute = int(seg - (hour * 60 * 60) / 60)
    second = int(seg - (hour * 60 * 60) - (minute * 60))
    return ('{}:{}:{}').format(hour, minute, second)

def massa():
    initial_mass = float(input('Introduza a massa inicial: '))
    final_mass = initial_mass
    sec = 0

    while final_mass > 0.05:
        final_mass /= 2
        seg += 50
    
    print(f'Massa Inicial: {initial_mass};\nMassa Final: {final_mass};\nSegundos: {CalculaSegundos(sec)}')

massa()