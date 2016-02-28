# Sarah Sedky and Corinne Druhan
#
#
#

from hmc_urllib import getHTML

def mtcURL(url):
    L = textCloud(url)
    s = ''
    for i in range(len(L)):
        COUNT = L[i][0]
        NUMBER = COUNT * 70
        WORD = L[i][1]
        s = s + '<abbr title = ' + str(COUNT) + ' style = "font-size:' + str(NUMBER) + '%">' + str(WORD) + '</abbr> &nbsp; &nbsp;\n'
    return s

def textCloud(url):
    depth = 3
    maxwords = 50
    if depth == 0:
        wordFrequencies(url)
    elif depth < 0 or depth > 10:
        return "Please enter a depth between 0 and 10."
    else:
       L = URLList(url, depth)
       L4 = []
       for x in L:
            L = createList(x)
            L2 = clean(L)
            L3 = stem(L2)
            L4 += L3
    L = count(L4, maxwords)
    return L
    
       

def URLList(url, depth):
    L = [url]
    if depth == 0:
        return L
    else:
        C = getHTML(url)[1]
        for x in C:
            New_L = URLList(x, depth-1)
            L += New_L
            removeRepeats(L)
    return L

def removeRepeats(L):
    if L:
        L.sort()
        last = L[-1]
        for i in range(len(L)-2, -1, -1):
            if last == L[i]:
                del L[i]
            else:
                last = L[i]

def wordFrequencies(url):
    """ wordFrequencies creates a list of frequently occurring words on some 
    webpage. """
    L = createList(url)
    L2 = clean(L)
    L3 = stem(L2)
    count(L3)
    
def createList(url):
    """ createList returns a list of all of the words on a given webpage."""
    return str.split(getHTML(url)[0])

def removeAll(L, x):
    """ removeAll removes all undesired words from a list of words."""
    return [word for word in L if word != x]

def clean(L):
    """ clean removes unimportant words and punctuation from a list of words."""
    S = ['the', 'of', 'to', 'and', 'a', 'in', 'is', 'it', 'you', 'that', 'he', 'was', 'for', 'on', 'are', 'with', 'as', 'i', 'his', 'they', 'be', 'at', 'one', 'have', 'this', 'from', 'or', 'had', 'by', 'but', 'some', 'what', 'there', 'we', 'can', 'out', 'other', 'were', 'all', 'your', 'when', 'up', 'an']
    L2 = []
    for x in L:
        x = x.strip(',.?!:;\"-&$%(\')0123456789')
        if x != '':
            L2 += [x]
        for y in L2:
            if y in S:
                L2 = removeAll(L2, y)
    return L2

def stem(L):
    """ stem removes suffixes from words and returns just the stems of the 
    words."""
    L2 = []
    for w in L:
        E = ['number', 'sly', 'ply', 'fly', 'wily', 'ugly', 'rely', 'lily', 'july', 'holy', 'ally', 'jelly', 'jolly', 'zed', 'wed', 'ted', 'red', 'ned', 'led', 'fed', 'bed', 'vied', 'sped', 'sled', 'shed', 'fred', 'fled', 'coed', 'bred', 'bled', 'unwed', 'embed', 'per', 'her', 'veer', 'tier', 'pier', 'peer', 'over', 'leer', 'jeer', 'ever', 'deer', 'beer', 'water','wafer', 'viper', 'utter', 'usher', 'under', 'ulcer', 'udder', 'tower', 'tiger', 'tater', 'taper', 'super', 'steer', 'sober', 'sneer', 'sheer', 'sever', 'ruler', 'peter', 'roger', 'otter', 'other', 'order', 'offer', 'niger', 'miser', 'meter', 'liver', 'liter', 'lever', 'leper', 'layer', 'later','laser', 'lager', 'infer', 'hover', 'fiber', 'ember', 'enter', 'ether', 'elder', 'eager', 'cower', 'cover', 'cider', 'cheer', 'ceder', 'cater', 'caper', 'brier', 'anger', 'after', 'yonder', 'wonder', 'supper', 'summer', 'somber', 'solder', 'soccer', 'sliver', 'sister', 'silver', 'shower', 'roster', 'proer', 'prefer', 'prayer', 'powder', 'poster', 'pewter', 'pepper', 'pander', 'pamper', 'oyster', 'oliver', 'nether', 'mutter', 'muster', 'murder', 'mother', 'mister', 'member', 'meager', 'matter', 'manger', 'master', 'lumber', 'loiter', 'litter', 'limber', 'lawyer', 'latter', 'lather', 'ladder', 'kosher', 'jitter', 'jigger', 'jasper', 'isomer', 'heifer', 'hammer', 'ginger', 'foster', 'former', 'folder', 'fodder', 'flower', 'filter', 'drawer', 'diaper', 'dexter', 'denver', 'danger', 'damper', 'dagger', 'cypher', 'crater', 'corner', 'copper', 'clover', 'butter', 'butler', 'burger', 'bummer', 'buffer', 'broker', 'booger', 'bitter', 'blazer', 'better', 'beaver', 'batter', 'barter', 'barber', 'banter', 'banner', 'badger', 'antler', 'answer', 'whoever', 'whisper', 'weather', 'uncover', 'twitter', 'trigger', 'tamper', 'trailer', 'toddler', 'thunder', 'theater', 'terrier', 'swelter', 'sweater', 'sticker', 'sputter', 'snicker', 'sneaker', 'smother', 'smolder', 'slumber', 'slobber', 'slither', 'slender', 'slather', 'slander', 'shudder', 'shelter', 'shatter', 'seltzer', 'scamper', 'saunter', 'rooster', 'reorder', 'reenter', 'recover' ,'quarter', 'prosper', 'premier', 'plunder', 'pitcher', 'pioneer', 'neither', 'meander' ,'lobster', 'leather', 'lacquer', 'jupiter', 'juniper', 'integer', 'however', 'holster', 'hipster', 'heather', 'hamster', 'glitter', 'glimmer', 'glacier', 'power', 'empower', 'feather', 'farther', 'critter', 'courier', 'coaster', 'clutter', 'clatter', 'chipper', 'checker', 'chashier', 'butcher', 'boulder', 'blooper', 'bolster', 'blister', 'another', 'holler', 'painkiller', 'stroller', 'barrier', 'administer', 'cluster', 'headmaster', 'wistful', 'awful', 'witness', 'lioness', 'highness', 'fitness', 'less', 'bless', 'unless', 'nonetheless', 'prism', 'deism', 'theism', 'schism', 'sadism', 'autism', 'baptism', 'optimism', 'nihlism', 'atheism', 'altruism', 'exorcism', 'hypnotism', 'communism', 'embolism', 'vies', 'ties', 'pies', 'lies', 'dies', 'rabies', 'scabies', 'rookies', 'potpies', 'barbies', 'belies', 'bookies', 'brownies', 'collies', 'cooties', 'hippies', 'magpies', 'meanies', 'newbies', 'movies', 'pixies', 'panties', 'smoothies', 'sweeties', 'townies', 'zombies', 'sing', 'ring', 'ding', 'king', 'zing', 'bring', 'wing', 'viking', 'icing', 'thing', 'sling', 'wring', 'cling', 'string', 'during', 'affable', 'abominable', 'capable', 'able', 'cable', 'viable', 'stable', 'constable', 'culpable', 'liable', 'delect', 'malleable', 'despicable', 'disable', 'mutable', 'satiable', 'table', 'incapable', 'unable', 'probable', 'amicable', 'arguable', 'vulnerable', 'amiable', 'vegetable', 'venerable', 'unusable']
        if w[-1] == 's' and w[-3:] != 'ies'and w[-2:] != 'ss' and w[-2:] != 'us':
            w = w[:-1] 
        elif w not in E:
            if w[-4:] == 'able':
                w = w[:-4]
                if w[-1] == w[-2]:
                    w = w[:-1]
                elif w in ['acquir', 'ador', 'believ', 'contru', 'configur', 'confus', 'consum', 'continu', 'creat', 'cur', 'customiz', 'decid', 'declar', 'decompos', 'defin', 'degrad', 'desir', 'dispos', 'dispens', 'distribut', 'lov', 'los', 'recogniz', 'recycl', 'refut', 'sav', 'solv', 'tun', 'us', 'writ']:
                    w = w + 'e'
            elif w[-3:] == 'ing':
                w = w[:-3]
                if w[-1] == w[-2]:
                    w = w[:-1]
            elif w[-3:] == 'ies':
                w = w[:-3] + 'y'
            elif w[-3:] == 'ism':
                w = w[:-3]
                if w in ['hol', 'pacif', 'anarch']:
                    w = w + 'y'
                elif w in ['nud', 'pur', 'tru', 'escap', 'separat']:
                    w = w + 'e'
            elif w[-2:] == 'er':
                w = w[:-2]
                if w[-1] == w[-2]:
                    w = w[:-1]
                if w[-1] == 'i':
                    w = w[:-1] + 'y'
            elif w[-4:] == 'less' and w != 'less':
                w = w[:-4]
                if w[-1] == 'i':
                    w = w[:-1] + 'y'
            elif w[-2:] == 'ed':
                w = w[:-2]
                if w[-1] == w[-2]:
                    w = w[:-1]
                if w[-1] == 'i':
                    w = w[:-1] + 'y'
            elif w[-4:] == 'ness':
                w = w[:-4]
                if w[-1] == 'i':
                    w = w[:-1] + 'y'
            elif w[-3:] == 'ful':
                w = w[:-3]
                if w[-1] == 'i':
                    w = w[:-1] + 'y'
            elif w[-2:] == 'ly':
                w = w[:-2]
            L2 += [w]
        else:
            for x in L:
                if x in E:
                    L2 += [x]
    return L2

def count(L, m):
    """ count gives the frequency of words on a given webpage in decending 
    order."""
    freq_dic = {}
    for word in L:
        try:
            freq_dic[word] += 1
        except:
            freq_dic[word] = 1
    freq_list = freq_dic.items()
    freq_list.sort()
    freq_list2 = [(val, key) for key, val in freq_dic.items()]
    freq_list2.sort(reverse = True)
    freq_list2 = freq_list2[:m]
    for freq, word in freq_list2:
        word, freq
    return freq_list2
        
    
        
