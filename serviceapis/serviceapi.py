# -*- coding: utf-8 -*-
'''
Copyright © 2017, ACM@UIUC
FoodButton is open source software, released under the University of
Illinois/NCSA Open Source License.  You should have received a copy of
this license in a file with the distribution.
'''

import abc

class ServiceAPI(abc.ABC):
    @abc.abstractmethod
    def __init__(self, cfg):
        '''
        Initialize the API connection 
        '''
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return 

    @abc.abstractmethod
    def post(self, img, text):
        '''
        Post an image (PIL Image) and text (string)
        '''
        pass
