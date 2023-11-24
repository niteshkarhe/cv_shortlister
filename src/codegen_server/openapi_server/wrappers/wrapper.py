'''
Created on Nov 22, 2023

@author: NKarhe
'''

def wrap(pre, post):
    """ Wrapper """

    def decorate(func):
        """ Decorator """

        def call(*args, **kwargs):
            """ Actual wrapping """
            pre(func, *args)
            result = func(*args, **kwargs)
            post(func)
            return result

        return call

    return decorate
