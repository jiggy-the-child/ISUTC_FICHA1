"""
Alright: here we're converting the speed from km/h to m/s as you can see in the exercises .pdf file, so, you might be wondering  
where does the 5/18 comes from, so, let me tell you, 1km/1h == 1000m/3600s (now it can get a little strange):
1000/200 == 5 and 3600/200 = 18, so there's where the 5/18 comes from.
"""

# now going to the exercise, I defined a variable called 'velocidade' as you can see, that receives a user input of a speed in km/h
# as a float and of course "abs" -- only accepts positive speeds.
# things like f' strings I already explained in the first exercise resolution.
velocidade = abs(float(input('Introduza a velocidade do veículo: '))) * (5/18)
print(f'A velocidade do veículo em m/s será: {velocidade}m/s.')