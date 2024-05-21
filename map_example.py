def capitalize_and_Ascii_sum(word:str):
    return sum(ord(x)for x in word.capitalize())

aniamls = ['cat','dog','cow']
#normal way

# for animal in aniamls :
#     asci_val =capitalize and 
animal_output = list(map(capitalize_and_Ascii_sum(aniamls)))
print(animal_output)