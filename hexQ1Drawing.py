from tkinter import *

# hexagon puzzle, a large hexagon with 24 inner triangles that also form 7 sub-hexagons
# hexagon is a string with each triangle as an index len 24
# notes for self:
# just pretend they're numbered 1 - 24 r-l u-d
# lets say the 6 labels are A, B, C, D, E, F
# ........................ start puzzle
# inner hexagons are indexes:
# TL: 0, 1, 2, 6, 7, 8
# TR: 2, 3, 4, 8, 9, 10
# ML: 5, 6, 7, 12, 13, 14
# MC: 7, 8, 9, 14, 15, 16
# MR: 9, 10, 11, 16, 17, 18
# BL: 13, 14, 15, 19, 20, 21
# BR: 15, 16, 17, 21, 22, 23


startPzl = '........................'  # each for an empty triangle
setOfChoices = {'A', 'B', 'C', 'D', 'E', 'F'}  # possible labels

def copies(tpl): # checks for copies within subhexagons
    seen = set()
    for label in tpl:
        if label != '.':
            if label in seen:
                return True  # true if it finds a copied label
            else:
                seen.add(label)
    return False  # otherwise it's still valid

def isInvalid(hexPzl):  # returns true if pzl is invalid, rewrite later maybe but idk
    hexTL = (hexPzl[0], hexPzl[1], hexPzl[2], hexPzl[6], hexPzl[7], hexPzl[8])
    hexTR = (hexPzl[2], hexPzl[3], hexPzl[4], hexPzl[8], hexPzl[9], hexPzl[10])
    hexML = (hexPzl[5], hexPzl[6], hexPzl[7], hexPzl[12], hexPzl[13], hexPzl[14])
    hexMC = (hexPzl[7], hexPzl[8], hexPzl[9], hexPzl[14], hexPzl[15], hexPzl[16])
    hexMR = (hexPzl[9], hexPzl[10], hexPzl[11], hexPzl[16], hexPzl[17], hexPzl[18])
    hexBL = (hexPzl[13], hexPzl[14], hexPzl[15], hexPzl[19], hexPzl[20], hexPzl[21])
    hexBR = (hexPzl[15], hexPzl[16], hexPzl[17], hexPzl[21], hexPzl[22], hexPzl[23])

    if copies(hexTL) or copies(hexTR) or copies(hexML) \
            or copies(hexMC) or copies(hexMR) or copies(hexBL) or copies(hexBR):
        return True  # true if the overall puzzle contains a subhex with copies, meaning its invalid

def bruteForce(pzl):  # find a solution through bruteForcing recursively
    if isInvalid(pzl):  # throw it out if it's invalid
        return ''
    if '.' not in pzl:  # if there are no empty spaces and it's not thrown out, it's solved
        return pzl

    nextOpenIndex = pzl.find('.')
    for choice in setOfChoices:
        # make a new pzl with the next empty choice filled with a possible label
        subPzl = pzl[0:nextOpenIndex] + choice + pzl[nextOpenIndex + 1:]
        result = bruteForce(subPzl)
        if result != '': # if it didn't fail, return it!
            return result

    return ''  # failure

solution = bruteForce(startPzl)
print(solution)

# displaying makes it easy to check visually
window = Tk()
window.title('Hexagon Problem 1')
hexPhoto = PhotoImage(file='hexagon.gif')
pW, pH = hexPhoto.width(), hexPhoto.height()
window.geometry('{}x{}'.format(pW, pH))
canvas = Canvas(window, width=pW, height=pH)
canvas.pack()
canvas.create_image(pW/2, pH/2, image=hexPhoto)

slnR1, slnR2 = solution[0:5], solution[5:12],
slnR3, slnR4 = solution[12:19], solution[19:24]

for index, label in enumerate(slnR1):
    canvas.create_text(105+57*index, 60, text=label)
for index, label in enumerate(slnR2):
    canvas.create_text(50+57*index, 155, text=label)
for index, label in enumerate(slnR3):
    canvas.create_text(50+57*index, 245, text=label)
for index, label in enumerate(slnR4):
    canvas.create_text(105+57*index, 340, text=label)

window.mainloop()
