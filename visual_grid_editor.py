
import pygame
import pyperclip
import numpy as np
import math
import copy
pygame.init()

width = 1000
height = 600
realwidth = 1000
canvas = pygame.display.set_mode((width, height))
pygame.display.set_caption("Shape Drawer")
font1 = pygame.font.SysFont("Calibri", 30)
FramePerSec = pygame.time.Clock()

jumpx = 2
jumpy = 1
maxjumplength = 5
jumpstring = "01234567"

def generatenewboard(size, jumps):
    board = []
    for i in range(size):
        board.append(["."] * size)
    return [board, jumps, [0, 0], [], "", 0]

def displayboard2(myboard):
    board = myboard[0]
    jumpstring = myboard[4]
    pos = myboard[2][:]
    jumps = myboard[1]
    for i in range(len(jumpstring)):
        board[pos[0]][pos[1]] = jumpstring[i]
        move = int(jumpstring[i])
        if move == 0:
            pos[1] += jumps[0]
        elif move == 1:
            pos[0] -= jumps[1]
            pos[1] += jumps[0]
        elif move == 2:
            pos[0] -= jumps[1]
        elif move == 3:
            pos[0] -= jumps[1]
            pos[1] -= jumps[0]
        elif move == 4:
            pos[1] -= jumps[0]
        elif move == 5:
            pos[0] += jumps[1]
            pos[1] -= jumps[0]
        elif move == 6:
            pos[0] += jumps[1]
        elif move == 7:
            pos[0] += jumps[1]
            pos[1] += jumps[0]
    board[pos[0]][pos[1]] = "*"
    return board

def generatejumps(myboard):
    pass  # Placeholder for logic if needed

def text_advanced(text, localfont, text_color, xpos, ypos):
    if text_color == "red":
        text_color = (255, 0, 0)
    textimage = localfont.render(text, True, text_color)
    textimagerect = textimage.get_rect()
    textimagerect.center = (xpos, ypos)
    canvas.blit(textimage, textimagerect)

def draw_text(text, localfont, text_color, xpos, ypos):
    textimage = localfont.render(text, True, text_color)
    canvas.blit(textimage, (xpos, ypos))

def closest_value(input_list, input_value):
    arr = np.asarray(input_list)
    i = (np.abs(arr - input_value)).argmin()
    return arr[i]

def findcursorpos():
    cursorx = cursorpos[0]
    pos = 0
    tempjumplist = copy.copy(visiblejumplist)
    tempjumplist.append(" ")
    candidatepositions = []
    for element in tempjumplist:
        textwidth = 20 + pygame.font.SysFont("Calibri", 20).render("".join(tempjumplist[0:pos]), 1, (0, 0, 0)).get_width()
        candidatepositions.append(textwidth)
        pos += 1
    mindist = 1000
    pos = 0
    for each in candidatepositions:
        if abs(int(each) - int(cursorx)) < mindist:
            mindist = abs(int(each) - int(cursorx))
        pos += 1
    pos = 0
    for each in candidatepositions:
        if abs(int(each) - int(cursorx)) == mindist:
            cursorx = each
            cursorposinlist = pos
        pos += 1
    return [cursorposinlist, cursorx]

def drawstring(jumpstring, jumpx, jumpy):
    bnum = len(jumpstring) + 1
    myboard = generatenewboard(2 * max(jumpx, jumpy) * (bnum + 1) + 1, [jumpx, jumpy])
    mid = int((2 * max(jumpx, jumpy) * (bnum + 1) + 1 + 1) / 2) - 1
    myboard[4] = str(jumpstring)
    generatejumps(myboard)
    myboard[2] = [mid, mid]
    myboard = displayboard2(myboard)

    shapesize = [len(myboard), len(myboard[0])]
    blockwidth = min(float((width - 100)) / float(shapesize[1]), float((width - 100)) / float(shapesize[0]))
    blockwidth = abs(math.floor(blockwidth))
    leftmargin = (width - (blockwidth * shapesize[1])) / 2
    return [myboard, shapesize, blockwidth, leftmargin]

visiblejumplist = [char for char in jumpstring]
cursorpos = [0, 0]

# Simplified loop just to show grid and allow exiting
running = True
while running:
    canvas.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    values = drawstring("".join(visiblejumplist), jumpx, jumpy)
    myboard, shapesize, blockwidth, leftmargin = values

    currentpos = [leftmargin, 50]
    for row in myboard:
        for block in row:
            if block != ".":
                pygame.draw.rect(canvas, (120, 120, 120), (currentpos[0], currentpos[1], blockwidth, blockwidth))
                if blockwidth > 12:
                    text_advanced(block, pygame.font.SysFont('Nunito', min(blockwidth // 2, blockwidth - 2)), (255, 255, 255),
                                  currentpos[0] + blockwidth / 2, currentpos[1] + blockwidth / 2)
            currentpos[0] += blockwidth
        currentpos[1] += blockwidth
        currentpos[0] = leftmargin

    pygame.display.update()
    FramePerSec.tick(30)

pygame.quit()
