class Pokemon:

    def __init__(self, data):
        rensad = data.strip()
        splitlista = rensad.split(",")
        self.number = splitlista[0]
        self.name = splitlista[1]
        self.type1 = splitlista[2]
        self.type2 = splitlista[3]
        self.total = splitlista[4]
        self.hp = splitlista[5]
        self.attack = splitlista[6]
        self.defense = splitlista[7]
        self.spatk = splitlista[8]
        self.spdef = splitlista[9]
        self.speed = splitlista[10]
        self.generation = splitlista[11]
        self.legendary = splitlista[12]

    def __str__(self):
        lgnd = ""
        if self.legendary == "True":
            lgnd = " LEGENDARY!"
        return self.number + ". " + self.name + " HP:" + self.hp + " ATD:" + self.attack + lgnd

    def __lt__(self, other):
        print("Har ", self.name, " mindre HP än ", other.name, "?")
        if int(self.hp) < int(other.hp):
            return True
        else:
            return False

    def __gt__(self, other):
        print("Har ", self.name, " högre attackdamage än ", other.name, "?")
        if int(self.attack) > int(other.attack):
            return True
        else:
            return False

    def attackincrease(self):
        newattack = int(self.attack) + 1
        self.attack = str(newattack)

        return self.name + " har ny ATD: " + self.attack
def search_pokemon(inp,lista):
    for i in lista:
        if inp.lower() == i.name.lower():
            return "Resultat: \n-> " + i.number + ". " + i.name + " HP:" + i.hp + " ATD:" + i.attack
    return "Inga resultat"

def readpokemons():
    with open("pokemon.csv") as pokemonfil:
        pokemonfil.readline()

        pokemonlist = []
        for dataline in pokemonfil:
            newpokemon = Pokemon(dataline)
            pokemonlist.append(newpokemon)
    return pokemonlist

def main():
    pokemonlist = readpokemons()
    print("1-----")
    print(pokemonlist[162])
    print(pokemonlist[170])
    print("2-----")
    print(pokemonlist[162] < pokemonlist[170])
    print("3-----")
    print(pokemonlist[162] > pokemonlist[170])
    print("4-----")
    print(pokemonlist[162].attackincrease())
    print("5-----")
    searchinp = input("Mata in namnet på den pokemon du vill söka på:")
    print(search_pokemon(searchinp,pokemonlist))




main()