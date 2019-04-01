from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame
import numpy as np
from math import *

angle = 0
x = 0
x_ball = 0
forward = True
forward_ball = True
car_z = 0

def myInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(65, 1, 0.1, 85)
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
    glRotate(90, 0, 1, 0)
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

    glBegin(GL_POLYGON)
    glColor(1, 1, 1)
    glVertex(11, 0, 0.5)
    glVertex(20.5, 0, 0.5)
    glVertex(20.5, 0, 1.25)
    glVertex(11, 0, 1.25)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(1, 1, 1)
    glVertex(22, 0, 0.5)
    glVertex(32, 0, 0.5)
    glVertex(32, 0, 1.25)
    glVertex(22, 0, 1.25)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(1, 1, 1)
    glVertex(33.5, 0, 0.5)
    glVertex(50, 0, 0.5)
    glVertex(50, 0, 1.25)
    glVertex(33.5, 0, 1.25)
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

def arrowKeys(key, x, y):
    global car_z
    if key == GLUT_KEY_LEFT:
        car_z = car_z - 1
    elif key == GLUT_KEY_RIGHT:
        car_z = car_z + 1

def draw():
    global angle
    global x
    global x_ball
    global forward
    global forward_ball
    global car_z
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClearColor(0.6,0.8,0.8,0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    drawbody()
    #drawAxis()

    glLoadIdentity()

    ## ball ##
    glColor(1, 0, 0)
    glRotate(90, 0, 1, 0)
    glTranslate(-x_ball,0,0)
    glutSolidSphere(1, 20, 20)
    glLoadIdentity()

    glColor(1,0,0)
    glRotate(90, 0, 1, 0)
    glTranslate(x,0,car_z)
    glScale(1,0.25,0.5)
    glutSolidCube(5)

    glLoadIdentity()
    glColor(0,0,0)
    glRotate(90, 0, 1, 0)
    glTranslate(x,5*0.25,car_z)
    glScale(0.5, 0.25, 0.5)
    glutSolidCube(5)

    glLoadIdentity()
    glColor(0.9, 0.9, 0)
    glRotate(90, 0, 1, 0)
    glTranslate(x + 2.5, -2.5 * 0.25, 2.5 * 0.5 + car_z)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.25, 0.5, 12, 8)

    #glLoadIdentity()
    #glRotate(90, 0, 1, 0)
    #glTranslate(x + 2.5, -2.5 * 0.25, -2.5 * 0.5)
    #glRotate(angle, 0, 0, 1)
    #glColor(0.9, 0.9, 0)
    #glutWireTorus(0.25, 0.5, 12, 8)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(x + -2.5, -2.5 * 0.25, 2.5 * 0.5 + car_z)
    glRotate(angle, 0, 0, 1)
    glColor(0.9, 0.9, 0)
    glutWireTorus(0.25, 0.5, 12, 8)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(x + -2.5, -2.5 * 0.25, -2.5 * 0.5 + car_z)
    glRotate(angle, 0, 0, 1)
    glColor(0.9, 0.9, 0)
    glutWireTorus(0.25, 0.5, 12, 8)


    if forward:
        angle -= 0.1
        x += 0.0025
        if x > 30:
            forward = False
    else:
        angle += 0.1
        x -= 0.0025
        if x < -6:
            forward = True

    if forward_ball:
        x_ball += 0.008
        if x_ball > 9:
            forward_ball = False
    else:
        x_ball -= 0.008
        if x_ball < -40:
            forward_ball = True

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(500, 500)
glutCreateWindow(b"Moving car")
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutSpecialFunc(arrowKeys)
myInit()
glutMainLoop()
