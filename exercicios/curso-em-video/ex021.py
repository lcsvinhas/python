# Exercício Python 021: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

# IMPORTAR PYGAME COM PIP INSTALL PYGAME
import pygame

pygame.init()
pygame.mixer.music.load('testando.mp3')
pygame.mixer.music.play()
pygame.event.wait
