# Vstupni_data
TEXTS = ['''Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.''']

# Pomocne
oddelovac1 = 80 * "="
oddelovac2 = 80 * "-"
uvitani = "Welcome to the app,"

# Uzivatele
users = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}

print(oddelovac2)
print("Please, log in.")
print(oddelovac2)

# Vstupni_data_uzivatele
user = input("Username: ")
heslo = input("Password: ")

# Overeni_jmena_a_hesla
if users.get(user) == heslo:
    print(oddelovac2)
    print(uvitani, user.title())
else:
    print("Username or password is wrong! "
          "Please check your credentials and try again.")
    exit()

# Vstupni_data_pro_analyzu
print(f"We have {len(TEXTS)} texts to be analyzed.")
print(oddelovac2)
text_num = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")


if text_num.isalpha():
    print(f"Input must be number between 1 and {len(TEXTS)}. End app!")
    exit()

elif text_num.isnumeric():
    if int(text_num) >= 1 and int(text_num) <= 3:
        text_num = int(text_num)
        print(oddelovac2)
        print(f"You chose text number {str(text_num)}.")
        print(f"The selected text is:\n{TEXTS[text_num-1]}")
    else:
        print(f"Number must be between 1 and {len(TEXTS)}. End app!")
        exit()
else:
    print(f"Input must be number between 1 and {len(TEXTS)}. End app!")
    exit()

ch_text = TEXTS[text_num-1]
cl_word = []

for word in ch_text.split():
    cl_word.append(word.strip('.,;/:"!?'))

#analyza_textu
total_words = len(cl_word)
total_title = 0
total_lower = 0
total_upper = 0
total_numeric = 0
total_sum = 0

for i in cl_word:
    if i.istitle():
        total_title += 1
    elif i.isupper():
        total_upper += 1
    elif i.islower():
        total_lower += 1
    elif i.isnumeric():
        total_numeric += 1
        total_sum += int(i)

#vysledky
print(oddelovac2)
print(f"There are {str(total_words)} words in the selected text.")
print(f"There are {str(total_title)} titlecase words.")
print(f"There are {str(total_upper)} uppercase words.")
print(f"There are {str(total_lower)} lowercase words.")
print(f"There are {str(total_numeric)} numeric strings.")
print("The sum of all the numbers: ", str(total_sum))

#vysledek_LEN_grafu
delka = {}
for i in cl_word:
    delka[(len(i))] = delka.setdefault((len(i)), 0) + 1

klice = []

for i in delka.keys():
    klice.append(i)
    klice.sort()

print(oddelovac2)
print("LEN".rjust(5), "|", "OCCURENCES".ljust(20),"|", "NR.")
print(oddelovac2)
for j in klice:
    print(str(j).rjust(5), "|", ("*" * delka.get(j)).ljust(20),"|", delka.get(j))
print(oddelovac2)


print(oddelovac1)
print("Thank you very much for using our services. Goodbye " + str(user.title()) + "!")
print(oddelovac1)
