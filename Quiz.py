
from gpiozero import Button
from time import sleep

import random

button11 = Button(23)
button12 = Button(16)
button13 = Button(15)
button14 = Button(14)
button21 = Button(22)
button22 = Button(10)
button23 = Button(9)
button24 = Button(11)
button31 = Button(6)
button32 = Button(13)
button33 = Button(19)
button34 = Button(26)

class QA:
  def __init__(self, question, correctAnswer, otherAnswers):
    self.question = question
    self.corrAnsw = correctAnswer
    self.otherAnsw = otherAnswers


qaList = []

Lista1 = [QA("Sose felejtsd el ki vagy, a világ nem fogja. Viseld pancelkent és akkor sosem fordithatjak ellened. - Ki mondta?", "Tyrion Lannister", ["Daenerys Targaryen", "Jorah Mormont", "Tarth-i Brienne"]),
QA("Kit kotozott ki es vetkoztetett mesztelenre Melissandre?", "Gendryt", ["Havas Jont", "Davost", "Stannis Baratheont"]),
QA("Ki tamasztja fel Havas Jont a halala utan?", "Melissandre", ["Missandei", "Arya", "Benjen Stark"]),
QA("Hogy hivtak Robb Stark feleseget?", "Talisa", ["Orisa", "Myrcella", "Missandei"]),
QA("Melyik sarkany hatan repult Havas Jon?", "Rhaegal", ["Viserion", "Drogon", "Smaug"]),
QA("Hanyszor hazasodott meg Sansa Stark?", "Ketszer", ["Haromszor", "Negyszer", "Egyszer sem"]),
QA("Sok idom volt azon gondolkodni, hogy milyen jol tudtam jonak tunni. - Ki mondta?", "Margaery Tyrell", ["Sansa Stark", "Szegfu", "Tyrion Lannister"]),
QA("Jo szived van Havas Jon. Emiatt fogunk mind meghalni. - Ki mondta?", "Alliser Thorne", ["Aemon Targaryen", "Daenerys Targaryen", "Ygritte"]),
QA("Szurke Fereg es Missandei Daenerys szovetsegeseive valnak miutan felszabaditjak a varosukat. Melyik varos ez?", "Astapor", ["Meereen", "Braavos", "Essos"]),
QA("Ki gyozi meg Ned Starkot, hogy megtartsak a remfarkasokat?", "Havas Jon", ["Catelyn", "Robb", "Arya"]),
QA("Mi a neve a csatanak, amit Havas Jonek Deres visszaszezeseert vivtak a Boltonok ellen?", "A Fattyak csataja", ["Az eszaki tronok harca", "Arvak kuzdelme", "Halalthozok csataja"]),
QA("Mivel aknaztatta ala Kiralyvarat II. Aerys Targaryen?", "Futotuzzel", ["Dinamittal", "Sarkanytuzzel", "Fustbombaval"]),
QA("Ki adja ki a parancsot a Voros Naszra?", "Walder Frey", ["Roose Bolton", "Havas Ramsay", "Joffrey Baratheon"]),
QA("Kivel nem halt Daenerys?", "Tyrion Lannisterrel", ["Daario Naharisszal", "Khal Drogoval", "Havas Jonnal"]),
QA("Ki volt Margaery Tyrell elso ferje?", "Renly Baratheon", ["Tommen Baratheon", "Joffrey Baratheon", "Stannis Bartheon"]),
QA("Ki volt a legfiatalabb Stark-testver?", "Rickon", ["Bran", "Sansa", "Arya"]),
QA("Hogy talalkozik Jon eloszor Ygritte-tel", "Ygritte Jon fogsagaba kerul, de keptelen kivegezni a lanyt.", ["Gilly mutatja be oket egymasnak.", "A vadak meglatogatjak az Ejjeli Orseget.", "Ugyanarra az allatra vadasztak az erdoben."]),
QA("Kik Havas Jon igazi szulei?", "Rhaegal Targaryen, Lyanna Stark", ["Oberyn Martell, Lyanna Stark", "Ned Stark, Catelyn Stark", "Ned Stark, Elia Martell"]),
QA("Kinek a beceneve A Hegy?", "Gregor Clegane", ["Oberyn Martell", "Sandor Clegane", "Tywin Lannister"]),
QA("Kitol kapja ajandekba Tut Arya?", "Havas Jontol", ["Ned Starktol", "Robert Baratheontol", "Robb Starktol"])]

Lista2 = [QA("Hany karika van a kviddicspalyan?", "6", ["12", "2", "8"]),
QA("Mennyibe kerult Harry palcaja?", "7 galleon", ["90 knut", "5 galleon", "15 galleon"]),
QA("Ki tanitotta meg Harryt varazslosakkozni?", "Ron", ["Dumbledore", "McGalagony", "Hermione"]),
QA("Ki a legidosebb Weasley-fiu?", "Bill", ["Charlie", "Percy", "Ron"]),
QA("Melyik horcruxot pusztitottak el eloszor?", "A naplot", ["A medalt", "A gyurut", "A diademot"]),
QA("Mi Luna Lovegood patronusa?", "Macska", ["Nyul", "Vidra", "Pillango"]),
QA("Hany eves volt Nicholas Flamel, mikor meg kellett semmisitenie a Bolcsek Kovet?", "665", ["498", "521", "599"]),
QA("Mi nem Haloweenkor tortent?", "Harry megkapja a Tekergok terkepet", ["Lily es James meggyilkolasa", "Sirius Black betort a Griffendel klubhelyisegbe", "Trollt talalnak a pinceben"]),
QA("Milyen tipusu Lucius Malfoy palcaja?", "Szilfa, sarkanyszivhur mag", ["Cseresznyefa, vela haj mag", "Nyarfa, unikornisszor mag", "Rozsafa, fonixtoll mag"]),
QA("Kicsoda Florean Fortescue?", "Fagyizoja van az Abszol uton", ["A Varazslastan alapfokon szerzoje", "A Szarnyas Vadkan kocsmarosa", "Auror a Magiaugyi Miniszteriumnal"]),
QA("Hogy hivjak az amerikai varazsloiskolat?", "Ilvermorny", ["Beauxbattons", "Durmstrang", "Castelobruxo"]),
QA("Hol talalhato a Szukseg szobaja?", "Hetedik emelet, baloldali folyoso", ["Otodik emelet, ket pancel kozott", "Harmadik emeleti folyoso, jobb oldali resze", "Alagsor, a Hugrabug klubhelyiseggel szemben"]),
QA("Hogy lehet bejutni a roxforti konyhaba?", "Meg kell csiklandozni az ajto festmenyen a kortet", ["Palcaval meg kell bokni a szobor mogotti gyumolcskosar-kepet", "Ha ehes vagy, automatikusan megjelenik a kulcs", "Jelszoval"]),
QA("Milyen hatása van a Colloportus varázslatnak?", "Bezarja magikusan az ajtot, igy azt mugli modszerrel nem tudjak kinyitni", ["Varazslenyomat eltunteto bubaj", "Emberkimutato bubaj, ami megmutatja van-e ember a varazsiget hasznalo korul", "Ez egy atok, aminek hatasara az illeto labai megbenulnak"]),
QA("Mi a Lumos vilagito varazslat ellentete?", "Nox", ["Obscuro", "Alohomora", "Imperio"]),
QA("Milyen magikus kepessege nincs Dumbledornak?", "Parszaszaju", ["Patronus bubajjal tud uzenetet kuldeni masoknak", "Lathatatlan tud lenni lathatatlanna tevo koponyeg nelkul is", "Beszel koboldul"]),
QA("Miota tartanak Kviddics vilagbajnoksagot?", "1473", ["1120", "1666", "1766"]),
QA("Mi Bimba professzor keresztneve?", "Pomona", ["Patricia", "Luna", "Poppy"]),
QA("Melyik roxforti hazba jar Susan Bones?", "Hugrabug", ["Hollohat", "Mardekar", "Griffendel"]),
QA("Milyen alnevet mondott Harry a Kobor Grimbuszon?", "Neville Longbottom", ["Dean Thomas", "Dudley Dursley", "Seamus Finnigan"])]

Lista3 = [QA("Mikor volt az elso (modern kori) nyari olimpia?", "1986", ["1908", "1900", "1920"]),
QA("Mit szimbolizal az olimpiai otkarika?", "Ot kontinenst", ["Okori olmpiak ot sportagat", "Beke, szabadsag, kitartas, egyenloseg, szorgalom", "Nincs jelentese"]),
QA("Milyen szin nins a karikak kozott?", "Feher", ["Fekete", "Sarga", "Kek"]),
QA("Ki a legerdmenyesebb magyar olimpikon a tortenelemben?", "Gerevich Aladar", ["Egerszegi Krisztina", "Gyarmati Dezso", "Keleti Agnes"]),
QA("Hany aranyat nyertek a magyarok Londonban?", "8", ["10", "12", "16"]),
QA("Ki volt a magyar zaszlovivo a londoni jatekokon?", "Biros Peter", ["Szilagyi Aron", "Kovacs Katalin", "Risztov Eva"]),
QA("Mikor szereztuk a legtobb ermet a jatekokon?", "1952, Helsinki", ["1988, Szöul", "1956, Melbourne", "1996, Atlanta"]),
QA("Megkapta-e valaha Budapest az olimpia rendezesi jogat?", "Igen", ["Nem", "Soha nem is igenyelte", "Meg nem biraltak el"]),
QA("Hany magyar versenyzo vehetett reszt a rioi olimpian?", "159", ["213", "115", "190"]),
QA("Hogy hivtak a rioi olimpia kabalaallatat?", "Vinicius", ["Waldy", "Hodori", "Izzy"]),
QA("Ki szerezte az elso magyar olimpiai ermet?", "Hajos Alfred 100 meteres gyorsuszasban", ["Hajos Alfred 100 meter mellen", "Gerevich Aladar, vivasban", "Elek Ilona, torvivasban"]),
QA("Ki nyerte az elso noi olimpiai aranyermet?", "Elek Ilona, torvivasban", ["Keleti Agnes talajon", "Rejto Ildiko torvivasban", "Egerszegi Krisztina melluszasban"]),
QA("Melyik sportolo vett reszt a legtobb olimpiai jatekon?", "Gerevich Aladar, vivo", ["Hajos Alfred, uszo", "Tarics Sandor, vizilabdazo", "Hegedus Csaba, birkozo"]),
QA("Melyik sportolono vett reszt a legtobb olimpian?", "Rejto Ildiko, torvivo", ["Egerszegi Krisztina, uszo", "Nagy Timea, barbajtorozo", "Keleti Agnes tornasz"]),
QA("Ki szerzett legidosebben olimpiai aranyat?", "Gerevich Aladar, vivo", ["Tarics Sandor, vizilabdazo", "Keleti Agnes tornasz", "Hajos Andras, uszo"]),
QA("Ki szerezte a legtobb aranyermet?", "Egerszegi Krisztina, Keleti Agnes", ["Hajos Andras, Hosszu Katinka", "Keleti Andrea, Gerevich Aaldar", "Nagy Time, Tarics Sandor"]),
QA("Melyik olimpia volt szamunkra a legeredmenyesebb?", "Helsinki", ["London", "Sydney", "Peking"]),
QA("Ki nyerte a 100. magyar aranyermet?", "Hegedus Csaba", ["Hosszu Katinka", "Nagy Timea", "Egerszegi Krisztina"]),
QA("Hany magyar erem szuletett eddig?", "480", ["450", "390", "415"]),
QA("Az eddigi eredmenyek alapjan hanyadik helyen all Magyarorszag?", "8.", ["10.", "6.", "11."])]

Lista4 = [QA("Ki nyerte a 2019-es evadnyito Ausztral Nagydijat??", "Bottas", ["Hamilton", "Vettel", "Verstappen"]),
QA("Kinek volt a 2. legtobb gyors kore a legutobbi Ausztral Nagydijon?", "Leclerc",["Bottas", "Hamilton", "Vettel"]),
QA("Melyik Nagydijon szerezte meg elso gyozelmet a Ferrari 2019-ben?", "Belga", ["Olasz", "Szingapuri", "Magyar"]),
QA("Hany kulonbozo versenyzo vezette a bajnoksagot 2019-ben?", "2", ["1", "3", "4"]),
QA("1981-ben ki maradt le egyetlen ponttal a bajnoki cimrol?", "Carlos Reutemann", ["Alain Prost", "Alan Jones", "Gilles Villeneuve"]),
QA("1976-os balesete utan mennyit hagyott ki Niki Lauda?", "2 futamot", ["2 honapot", "1977-ben tert vissza", "12 honapot"]),
QA("Ki volt az elso konstruktori bajnok 1958-ban?", "Vanwall", ["Ferrari", "Lotus-Climax", "Cooper-Climax"]),
QA("1982-ben hany futamgyozelme volt Keke Rosbergnek?", "1", ["3", "5", "7"]),
QA("Ki nem indult soha versenyzokent is F1-es versenyhetvegen a csapattulajdonosok kozul?", "Ron Dennis", ["Bruce McLaren", "Bernie Ecclestone", "Jack Brabham"]),
QA("Hanyszor vegzett dobogon Jos Verstappen?", "2", ["0", "5", "10"]),
QA("Hany futambol allt az elso, 1950-es szezon?", "7", ["5", "10", "16"]),
QA("Mikor szuletett Ayron Senna?", "1960.03.21.", ["1959.03.20.", "1962.05.01.", "1961.04.21."]),
QA("Ki nem szállított soha motort versenyhetvegere a MCLarennek?", "Lamborghini", ["Alfa Romeo", "Ford", "Peugeot"]),
QA("Mely csapatnal debutalt Michael Schumacher?", "Jorden", ["Benetton", "Tyrell", "Minardi"]),
QA("Kit beceztek Mr. Monaconak??", "Gragham Hill", ["Michael Schumacher", "Alain Prost", "Ayrton Senna"]),
QA("Mely szponzor nem szerepelt soha a Lotus autoin?", "Rothmans", ["Camel", "John Player Special", "Gold Leaf"]),
QA("Milyen markaju volt az elso Safety Car?", "Porsche", ["Mercedes", "Opel", "Lamborghini"]),
QA("Mely csapat epitett hat kereku autot, mely versenyen is indult?", "Tyrell", ["Lotus", "Ligier", "Williams"]),
QA("Mit abrazolt a Hesketh Racing logoja?", "Pluss macit", ["Koronat", "Oroszlant", "Pezsgos uveget"]),
QA("Hany kozepcsapat allt fel a dobogora 2019-ben?", "2", ["4", "1", "3"])]


print("Nyomd meg a távirányító megfelelő sorszámú gombját, annak függvényében, hogy hányan akartok játszani!")

wait_for_press()
if button11.when_pressed:
  JatekosDb = 1
elif button12.when_pressed:
  JatekosDb = 2
elif button13.when_pressed:
  JatekosDb = 3
else:
  JatekosDb = 4

#pause()

while not (JatekosDb == 1 or JatekosDb == 2 or JatekosDb == 3):
  print("Nem megfelelő gombot nyomtatok meg! Csak 1, 2, vagy 3 játékos lehet! Adjátok meg ismét, hányan szeretnétek játszani!")
  wait_for_press()
  if button11.when_pressed:
    JatekosDb = 1
  elif button12.when_pressed:
    JatekosDb = 2
  elif button13.when_pressed:
    JatekosDb = 3
  else:
    JatekosDb = 4

  #pause()


print("Válasszatok egy témakört, a megfelelő szám beírásával!")
print("1. Filmek, sorozatok")
print("2. Sport")
print("A választott témakör sorszáma:")

wait_for_press()
if button11.when_pressed:
  Temakor = 1
elif button12.when_pressed:
  Temakor = 2
else:
  Temakor = 3

#pause()

while not (Temakor == 1 or Temakor == 2):
  print("Nem megfelelő gombot nyomtatok meg! Adjátok meg ismét, melyik témakört választjátok, az 1. vagy a 2. gomb megnyomásával!")
  wait_for_press()
  if button11.when_pressed:
    Temakor = 1
  elif button12.when_pressed:
    Temakor = 2
  else:
    Temakor = 3

  #pause()

print("")

if Temakor == 1:
  print("Most válasszatok egy témát ezen a témakörön belül, a megfelelő szám beírásával!")
  print("1. Trónok harca")
  print("2. Harry Potter")
  print("A választott téma sorszáma:")

  wait_for_press()
  if button11.when_pressed:
    Tema = 1
  elif button12.when_pressed:
    Tema = 2
  else:
    Tema = 3

  #pause()

  while not (Tema == 1 or Tema == 2):
    print("Nem megfelelő gombot nyomtatok meg! Adjátok meg ismét, melyik témát választjátok, az 1. vagy a 2. gomb megnyomásával!")
    wait_for_press()
    if button11.when_pressed:
      Tema = 1
    elif button12.when_pressed:
      Tema = 2
    else:
      Tema = 3

    #pause()

  print("")

  if Tema == 1:
    qaList = Lista1
    print("1/1")  # majd ez mar nem kell
    print("")
  elif Tema == 2:
    qaList = Lista2
    print("1/2")  # majd ez mar nem kell
    print("")

elif Temakor == 2:
  print("Most válasszatok egy témát ezen a témakörön belül, a megfelelő szám beírásával!")
  print("Olimpia")
  print("Forma 1")
  print("A választott téma sorszáma:")

  wait_for_press()
  if button11.when_pressed:
    Tema = 1
  elif button12.when_pressed:
    Tema = 2
  else:
    Tema = 3

  #pause()

  while not (Tema == 1 or Tema == 2):
    print("Nem megfelelő gombot nyomtatok meg! Adjátok meg ismét, melyik témát választjátok, az 1. vagy a 2. gomb megnyomásával!")
    wait_for_press()
    if button11.when_pressed:
      Tema = 1
    elif button12.when_pressed:
      Tema = 2
    else:
      Tema = 3

    #pause()

  print("")

  if Tema == 1:
    qaList = Lista3
    print("2/1")  # majd ez mar nem kell
    print("")
  elif Tema == 2:
    qaList = Lista4
    print("2/2")  # majd ez mar nem kell
    print("")

db = 0
corrCountA = 0
corrCountB = 0
corrCountC = 0
random.shuffle(qaList)

for qaItem in qaList:
  db += 1
  if db == 11:
    break
  print(qaItem.question)
  print("A lehetséges válaszok:")
  possible = qaItem.otherAnsw + [qaItem.corrAnsw]  # square brackets turn correct answer into list for concatenating with other list
  random.shuffle(possible)
  count = 0  # list indexes start at 0 in python
  while count < len(possible):
    print(str(count+1) + ": " + possible[count])
    count += 1
  print("")

  print("1. játékos: Kérlek írd be a szerinted helyes válasz sorszámát:")

  wait_for_press()
  if button11.when_pressed:
    userAnsw = 1
  elif button12.when_pressed:
    userAnsw = 2
  elif button13.when_pressed:
    userAnsw = 3
  elif button14.when_pressed:
    userAnsw = 4
  else:
    userAnsw = 0

  #pause()

  if possible[userAnsw-1] == qaItem.corrAnsw:

    corrCountA += 1

  print("")

  if JatekosDb > 1:
    print("2. játékos: Kérlek írd be a szerinted helyes válasz sorszámát:")

    wait_for_press()
    if button21.when_pressed:
      userAnsw = 1
    elif button22.when_pressed:
      userAnsw = 2
    elif button23.when_pressed:
      userAnsw = 3
    elif button24.when_pressed:
      userAnsw = 4
    else:
      userAnsw = 0

    #pause()

    if possible[userAnsw - 1] == qaItem.corrAnsw:

      corrCountB += 1

    print("")

  if JatekosDb > 2:
    print("3. játékos: Kérlek írd be a szerinted helyes válasz sorszámát:")

    wait_for_press()
    if button31.when_pressed:
      userAnsw = 1
    elif button32.when_pressed:
      userAnsw = 2
    elif button33.when_pressed:
      userAnsw = 3
    elif button34.when_pressed:
      userAnsw = 4
    else:
      userAnsw = 0

    #pause()

    if possible[userAnsw - 1] == qaItem.corrAnsw:

      corrCountC += 1

    print("")


print("1. játékos: Gratulálok! " + str(corrCountA) + " pontot szereztél.")  #str(len(qaList))
if JatekosDb > 1:
  print("2. játékos: Gratulálok! " + str(corrCountB) + " pontot szereztél.")  #str(len(qaList))
if JatekosDb > 2:
  print("3. játékos: Gratulálok! " + str(corrCountC) + " pontot szereztél.")  #str(len(qaList))
