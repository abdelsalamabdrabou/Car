from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame
import numpy as np
from math import *

angle = 0
x = 0
forward = True

def myInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(65, 1, 0.1, 50)
    gluLookAt(8, 9, 10, 0,0,0, 0,1,0)

def drawAxis():
    glBegin(GL_LINES)
    glColor(1, 0, 0)
    glVertex(10, 0, 0)
    glVertex(-10, 0, 0)
    glEnd()

    glBegin(GL_LINES)
    glColor(0, 0, 1)
    glVertex(0, 10, 0)
    glVertex(0, 0, 0)
    glEnd()

    glBegin(GL_LINES)
    glColor(0, 1, 0)
    glVertex(0, 0, 10)
    glVertex(0, 0, -10)
    glEnd()

def drawbody():
    glBegin(GL_POLYGON)
    glColor(0, 0, 0)
    glVertex(-100, 0, -2.5)
    glVertex(100, 0, -2.5)
    glVertex(100, 0, 3.5)
    glVertex(-100, 0, 3.5)
    glEnd()
    ############
    glBegin(GL_POLYGON)
    glColor(1, 1, 1)
    glVertex(-19.5, 0, 0.5)
    glVertex(-14.5, 0, 0.5)
    glVertex(-14.5, 0, 1.25)
    glVertex(-19.5, 0, 1.25)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(1, 1, 1)
    glVertex(-13.5, 0, 0.5)
    glVertex(-8.5, 0, 0.5)
    glVertex(-8.5, 0, 1.25)
    glVertex(-13.5, 0, 1.25)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(1, 1, 1)
    glVertex(-7.5, 0, 0.5)
    glVertex(-2.5, 0, 0.5)
    glVertex(-2.5, 0, 1.25)
    glVertex(-7.5, 0, 1.25)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(1, 1, 1)
    glVertex(-1.5, 0, 0.5)
    glVertex(3.5, 0, 0.5)
    glVertex(3.5, 0, 1.25)
    glVertex(-1.5, 0, 1.25)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(1, 1, 1)
    glVertex(4.5, 0, 0.5)
    glVertex(9.5, 0, 0.5)
    glVertex(9.5, 0, 1.25)
    glVertex(4.5, 0, 1.25)
    glEnd()
    #########3
    glBegin(GL_POLYGON)
    glColor(0.5, 0.8, 0.1)
    glVertex(-100, 0, 3.5)
    glVertex(100, 0, 3.5)
    glVertex(100, 0, 100)
    glVertex(-100, 0, 100)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(0.5, 0.8, 0.1)
    glVertex(-100, 0, -2.5)
    glVertex(100, 0, -2.5)
    glVertex(100, 0, -10)
    glVertex(-100, 0, -10)
    glEnd()

def draw():
    global angle
    global x
    global forward
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClearColor(0.6,0.8,0.8,0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    drawbody()

    glColor(1,0,0)
    glTranslate(x,0,0)
    glScale(1,0.25,0.5)
    glutSolidCube(5)

    glLoadIdentity()
    glColor(0,0,0)
    glTranslate(x,5*0.25,0)
    glScale(0.5, 0.25, 0.5)
    glutSolidCube(5)

    glLoadIdentity()
    glColor(0.9, 0.9, 0)
    glTranslate(x+2.5, -2.5 * 0.25, 2.5 * 0.5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.25, 0.5, 12, 8)

    glLoadIdentity()
    glTranslate(x+2.5, -2.5 * 0.25, -2.5 * 0.5)
    glRotate(angle, 0, 0, 1)
    glColor(0.9, 0.9, 0)
    glutWireTorus(0.25, 0.5, 12, 8)

    glLoadIdentity()
    glTranslate(x+-2.5, -2.5 * 0.25, 2.5 * 0.5)
    glRotate(angle, 0, 0, 1)
    glColor(0.9, 0.9, 0)
    glutWireTorus(0.25, 0.5, 12, 8)


    if forward:
        angle -= 0.1
        x += 0.0019
        if x > 5:
            forward = False
    else:
        angle += 0.1
        x -= 0.0019
        if x < -5:
            forward = True

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(500, 500)
glutCreateWindow(b"hello world!")
glutDisplayFunc(draw)
glutIdleFunc(draw)
myInit()
glutMainLoop()