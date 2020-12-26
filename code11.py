#Build the list of syllables
allSyllables = set()
def addSyllables():
    #vowels
    allSyllables.add("aa")
    allSyllables.add("ae")
    allSyllables.add("ah")
    allSyllables.add("ao")
    allSyllables.add("aw")
    allSyllables.add("ax")
    allSyllables.add("ay")
    allSyllables.add("ea")
    allSyllables.add("eh")
    allSyllables.add("er")
    allSyllables.add("ey")
    allSyllables.add("ia")
    allSyllables.add("ih")
    allSyllables.add("iy")
    allSyllables.add("oh")
    allSyllables.add("ow")
    allSyllables.add("oy")
    allSyllables.add("ua")
    allSyllables.add("uh")
    allSyllables.add("uw")
    #consonants
    allSyllables.add("p")
    allSyllables.add("b")
    allSyllables.add("t")
    allSyllables.add("d")
    allSyllables.add("f")
    allSyllables.add("v")
    allSyllables.add("th")
    allSyllables.add("dh")
    allSyllables.add("s")
    allSyllables.add("z")
    allSyllables.add("sh")
    allSyllables.add("zh")
    allSyllables.add("ch")
    allSyllables.add("jh")
    allSyllables.add("k")
    allSyllables.add("ng")
    allSyllables.add("g")
    allSyllables.add("m")
    allSyllables.add("n")
    allSyllables.add("l")
    allSyllables.add("r")
    allSyllables.add("w")
    allSyllables.add("y")
    allSyllables.add("hh")
addSyllables()

#Build the list of vowels
vowels = set()
def addVowels():
    allSyllables = vowels
    allSyllables.add("aa")
    allSyllables.add("ae")
    allSyllables.add("ah")
    allSyllables.add("ao")
    allSyllables.add("aw")
    allSyllables.add("ax")
    allSyllables.add("ay")
    allSyllables.add("ea")
    allSyllables.add("eh")
    allSyllables.add("er")
    allSyllables.add("ey")
    allSyllables.add("ia")
    allSyllables.add("ih")
    allSyllables.add("iy")
    allSyllables.add("oh")
    allSyllables.add("ow")
    allSyllables.add("oy")
    allSyllables.add("ua")
    allSyllables.add("uh")
    allSyllables.add("uw")
addVowels()

#Build Dictionary to compare consonants
likeConsonants = {}
def addLikeConsonants():
    #p
    p = set()
    p.add("p")
    p.add("b")
    p.add("f")
    likeConsonants["p"] = p
    #b
    b = set()
    b.add("p")
    b.add("b")
    likeConsonants["b"] = b
    #t 
    t = set()
    t.add("t")
    t.add("d")
    t.add("th")
    t.add("dh")
    likeConsonants["t"] = t
    #d 
    d = set()
    d.add("t")
    d.add("d")
    d.add("th")
    d.add("dh")
    likeConsonants["d"] = d
    #f 
    f = set()
    f.add("p")
    f.add("f")
    likeConsonants["f"] = f
    #v 
    v = set()
    v.add("b")
    v.add("v")
    v.add("w")
    likeConsonants["v"] = v
    #th, dh
    th = set()
    th.add("t")
    th.add("d")
    th.add("th")
    th.add("dh")
    likeConsonants["th"] = th
    likeConsonants["dh"] = th
    #s, z, sh, zh, ch
    s = set()
    s.add("s")
    s.add("z")
    s.add("sh")
    s.add("zh")
    s.add("ch")
    likeConsonants["s"] = s 
    likeConsonants["z"] = s
    likeConsonants["sh"] = s
    likeConsonants["zh"] = s
    likeConsonants["ch"] = s
    #k, g
    k = set() 
    k.add("k")
    k.add("g")
    likeConsonants["k"] = k
    likeConsonants["g"] = k
    #ng, m, n
    ng = set()
    ng.add("ng")
    ng.add("m")
    ng.add("n")
    likeConsonants["ng"] = ng
    likeConsonants["m"] = ng
    likeConsonants["n"] = ng
    #l
    l = set() 
    l.add("l")
    l.add("r")
    l.add("y")
    likeConsonants["l"] = l
    #r 
    r = set() 
    r.add("l")
    r.add("r")
    likeConsonants["r"] = r
    #w 
    w = set()
    w.add("v")
    w.add("w")
    #y 
    likeConsonants["y"] = vowels 
    #hh 
    hh = set()
    hh.add("hh")
    likeConsonants["hh"] = hh
addLikeConsonants()
    
#The database of jokes
database = []

#The joke class
class Joke:
    def __init__(self, punchline, syllables):
        for syllable in syllables:
            if syllable not in allSyllables: raise NameError(syllable + " not a valid syllable")
        self.punchline = punchline 
        self.syllables = syllables
        database.append(self)
        
#Add some jokes 
def starterJokes():
    Joke('suck on deez nuts', ['s','uh','k','oh','n','d','iy','s','n','uh','t','s'])
    Joke('bite on deez nuts', ['b','ay','t','oh','n','d','iy','s','n','uh','t','s'])
starterJokes()

#Look up the inputted setup, see if there's a joke it fits into
def findJoke(setup):
    for joke in database:
        found = False
        for jokeVar in variations(joke.syllables):
            if anyCompatible(setup, jokeVar):
                yield joke.punchline
                found = True
                break 
        if not found:
            for setupVar in variations(setup):
                if anyCompatible(setupVar, joke.syllables):
                    yield joke.punchline
                    break 

#Takes list of syllables, yield all variations of the list (one consonant may be removed)
def variations(input):
    yield input 
    for i in range(len(input)):
        if input[i] not in vowels:
            yield input[:i] + input[i + 1:] 
    
#Sees if setup fits into punchine, and return T/F
def anyCompatible(setup, punchline): #setup and punchline are lists of syllables
    for i in range(len(punchline) - len(setup) + 1):
        if compatible(setup, punchline[i:]):
            return True 
    return False 

#Sees if the setup fits into the start of the punchline, returns T/F
def compatible(setup, punchline):
    for i in range(len(setup)):
        if not similarSyllable(setup[i], punchline[i]):
            return False 
    return True

#Takes two syllable paramters, return if they are comparable and can be substituted for one another
def similarSyllable(a, b):
    if a in vowels and b in vowels: return True
    elif (a in vowels and b not in vowels) or (a not in vowels and b in vowels): return False
    else: return b in likeConsonants[a]

#Obtain the list of syllables representing the punchline, a desired # of jokes, and print out candidate accordingly
def getJokes():
    setup = []
    nextSyllable = "start"
    while nextSyllable != "done":
        nextSyllable = input("Add the next syllable. Type 'done' once finished: ").rstrip("\n")
        if nextSyllable not in allSyllables:
            if nextSyllable == "done":
                break
            print("Not a valid syllable")
        else:
            setup.append(nextSyllable)
        print("Current syllables: " + str(setup))
    yieldCount = int(input("How many jokes to get? Response: "))
    currentCount = 0
    for joke in findJoke(setup):
        print(joke)
        currentCount+=1
        if currentCount >= yieldCount: break 
    print("Total jokes found: " + str(currentCount))
                

