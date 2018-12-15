
# hexagon puzzle, a large hexagon with 24 inner triangles that also form 7 sub-hexagons
# hexagon is a string with the four corners missing
# lets say the 6 labels are A, B, C, D, E, F
# hexagon puzzle is 4x7 grid w/o corners
# 1 is a corner 0 is an unlabeled triangle
# 1000001000000000000001000001 start puzzle
# inner hexagons are indexes:
# TL: 1, 2, 3, 8, 9, 10
# TR: 3, 4, 5, 10, 11, 12
# ML: 7, 8, 9, 14, 15, 16
# MC: 9, 10, 11, 16, 17, 18
# MR: 11, 12, 13, 18, 19, 20
# BL: 15, 16, 17, 22, 23, 24
# BR: 17, 18, 19, 24, 25, 26

startPzl = '1000001000000000000001000001'
setOfChoices = {'A', 'B', 'C', 'D', 'E', 'F'}

def copies(tpl):
    seen = set()
    for label in tpl:
        if label != '0':
            if label in seen:
                return True  # true if labels in subhex aren't unique
            else:
                seen.add(label)
    return False  # otherwise it's still valid

def isInvalid(hexPzl):  # find out better way this isn't nice
    hexTL = (hexPzl[1], hexPzl[2], hexPzl[3], hexPzl[8], hexPzl[9], hexPzl[10])
    hexTR = (hexPzl[3], hexPzl[4], hexPzl[5], hexPzl[10], hexPzl[11], hexPzl[12])
    hexML = (hexPzl[7], hexPzl[8], hexPzl[9], hexPzl[14], hexPzl[15], hexPzl[16])
    hexMC = (hexPzl[9], hexPzl[10], hexPzl[11], hexPzl[16], hexPzl[17], hexPzl[18])
    hexMR = (hexPzl[11], hexPzl[12], hexPzl[13], hexPzl[18], hexPzl[19], hexPzl[20])
    hexBL = (hexPzl[15], hexPzl[16], hexPzl[17], hexPzl[22], hexPzl[23], hexPzl[24])
    hexBR = (hexPzl[17], hexPzl[18], hexPzl[19], hexPzl[24], hexPzl[25], hexPzl[26])

    if copies(hexTL) or copies(hexTR) or copies(hexML) \
            or copies(hexMC) or copies(hexMR) or copies(hexBL) or copies(hexBR):
        return True  # true if the overall puzzle contains a subhex with copies, meaning its invalid

def bruteForce(pzl):
    if isInvalid(pzl):
        return ''
    if '0' not in pzl and not isInvalid(pzl):
        return pzl

    nextOpenIndex = pzl.find('0')
    for choice in setOfChoices:
        subPzl = pzl[0:nextOpenIndex] + choice + pzl[nextOpenIndex + 1:]
        bf = bruteForce(subPzl)
        if bf != '':
            return bf

    return ''  # failure

print(bruteForce(startPzl))
