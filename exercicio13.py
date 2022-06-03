# as the exercise says, whe have 45 students, but we don't have the ages neither the heights of these students, it seems like 
# we'll have to create them... as we now, is a little bit hard to think or create data for 45 students, and given the exercise, 
# it won't be only 45, it has to be 90 because of the ages and the heights, so... let's see:

# imported random and we already now that it serves to generate random numbers for us, or make random choices if we want.
import random

# a variable that will contain the list of students, with the heights and ages.
students_list = []

for _ in range(45):
    # this loop is doing nothing more than iterate 45 times and creating random heights and ages for us, the heights take float or 
    # real numbers as type and the ages, integers, but now, they're doing it in a different way, let me explain:
    students_list.append({
        'altura': round(random.uniform(1, 2), 2), # here, if it was a "normal" random generator, you wouldn't be seeing this much parameters, so
        # basically, what I'm doing is: inside the uniform, I'm giving the boundaries to the heights that I want randomly created: a person in a university
        # class (if the person is not deficient), usually is between 1 meter and 2 meters. But, we still can see another number 2! What's that for?
        # Okay the other number 2, is from the round method, and what we telling is: hey, create a float number for me with the given parameters, but it 
        # can only have 2 decimal places, so we can't see heights like: 1.8937463774653746, or 1.3476385873752486297486863, otherwise, what we'll 
        # see is: 1.93 or 1.34 and that's it. 
        'idade': random.randint(16, 40), # and here still the same, these numbers as parameters inside the randint are just boundaries, we are telling 
        # the random method to create random integer numbers between 16 and 40
    })
    # and it will do it 45 times.

    # UFA... muita explicação envolvida aqui. Nem escrevo bem inglês mas vou praticar convosco.

# these two variables don't need explanation...
soma_idades = 0 
count_idade = 0
soma_alturas = 0
count_altura = 0
# aqui pode azedar, mas lá vamos nós:
for i in range(len(students_list)):

    # Okay... we didn't create a simple list, it was a dictionary list (hope you search about it in the python docs and here goes the link: TODO: put a link here)
    # so, we have a list with a dictionary inside the list, with key and value pairs, 
    # (e.g: 'idade' as key and round(random.uniform(1, 2), 2) as value and they must be separated by ':', but we'll have opportunity to talk about this later on)
    # so, we created a list with a dictionary inside, and we gave values to this dictionary keys. So what we are doing here is,
    # we're getting the value from the list at the [i] index... and what we found there?! a dictionary with 'key: value' pair, and then, what do we do?
    # we '.get' the ('value') by the name 'altura' or whatever it is, it could be 'name' or 'country' or even 'id' -- is the most popular, but in this case is 'altura'
    # so, we grab 'altura' and check if it's lower than 1.70 it could be 1.7 too because the zero doesn't make a lotta difference
    if students_list[i].get('altura') < 1.70:
        # o resto, é resto!
        count_idade +=1
        soma_idades += students_list[i].get('idade')
    if students_list[i].get('idade') > 20:
        count_altura +=1
        soma_alturas += students_list[i].get('altura')
idade_media = round(soma_idades / count_idade, 2)
media_altura = round(soma_alturas / count_altura, 2)
print(f'A média das idades para os alunos com menos de 1.70m é: {idade_media}')
print(f'A média das alturas para os alunos com mais de 20 anos de idade é: {media_altura}')