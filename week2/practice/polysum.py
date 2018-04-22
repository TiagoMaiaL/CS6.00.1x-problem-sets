#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 10:20:38 2018

@author: knowledgetemple
"""

import math

def polysum(sidesNumber, sidesLength):
    '''
    sidesNumber: number of sides of a polygon
    sidesLength: each side length, integer or float
    
    returns: the sum of the area with the square of the perimeter.
    '''
    
    area = (0.25 * sidesNumber * sidesLength ** 2) / math.tan(math.pi / sidesNumber)
    perimeter = sidesNumber * sidesLength

    return round(area + perimeter ** 2, 4)