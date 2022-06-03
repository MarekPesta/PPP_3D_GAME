# Python 3D Game

![image](https://user-images.githubusercontent.com/54101971/171924121-929097e0-aee1-4f03-a613-9ed6a7e1cba5.PNG)

## Introduction

This is a repository of simple 3D game written in python.
It is the second part of the PPP classes project.
The goal is to create some FPS games.

## Libraries and Tools

* Python 3.10.2
* [rich](https://github.com/Textualize/rich)
* ursina

## Instalation

1. Install python 3.10.2
2. Install needed modules with `pip`

```sh
python -m pip install rich
python -m pip install ursina
```

3. Run main.py

```sh
python main.py
```

## Overview

This game is a simple FPS arena shooter.
There are three types of weapons available.
Each weapon has unlimited ammo.
There are three types of enemies.
Currently, the player plays in "God mode" (enemies cannot kill you).

## Keybindings

* '1' - handgun
* '2' - rifle
* '3' - railgun
* '0' - no weapon

* 'W' - move forward
* 'S' - move backwards
* 'A' - move left
* 'D' - move right

* 'space' - jump
* 'shift' - sprint

* 'left mouse button' - shoot

* 'G' - spawn monsters
* 'enter' - start/pause

* 'esc' - quit game
