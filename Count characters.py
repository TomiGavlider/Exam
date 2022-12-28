def counter(character):
    counts = dict()
    file = open('da_vinci_code.txt','r')
    c = file.read()
    for characters in c:
        if characters in counts:
            counts[characters] += 1
        else:
            counts[characters] = 1
    for key in counts:
        return {character: counts.get(character)}






print(counter('0'))
