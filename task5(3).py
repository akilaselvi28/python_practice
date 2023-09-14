season=input("Enter season:")
a=['September','October','November']
b=['December','January','February']
c=['March','April','May']
if season in a:
    print(season,"is the Autumn season")
elif season in b:
    print(season,"is the Winter season")
elif season in c:
    print(season,"is the Spring season")
else:
    print(season,"is the Summer season")