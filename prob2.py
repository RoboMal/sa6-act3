fish = ["shark", "guppy", "swordfish", "carp", 
        "tigerfish", "oarfish", "marlin"]


strings_sorted = sorted(fish, key = lambda x: (len(x), x)) 

print(f"Before Sort: {fish}\n")
print(f"After Sort: {strings_sorted}")

'''
Breakdown: 
Sort by Alphabet: strings_sorted = sorted(fish, key = lambda x: x)
Sort by length: string_sorted = sorted(fish, key = lambda x: len(x))

By combining the two into what is seen on Line 5,
I essentially set the key such that it sorts by length FIRST and
alphabet SECOND.


Alt. Test Cases
lords = ["Gwyn", "Seath", "Nito", "Four Kings", "Izalith"]
demigods = ["Godrick", "Mohg", "Ranni", "Rykard",
 "Radahn", "Morgott", "Miquella", Melania"]
'''