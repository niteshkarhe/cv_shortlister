'''
Created on Nov 22, 2023

@author: NKarhe
'''

from openapi_server.app_context import get_logger
from timeit import default_timer as timer

start_time = timer()


def log_entering(func, *args):
    """ Pre function logging """
    global start_time
    start_time = timer()

    logger = get_logger()

    logger.info("Entered %s", func.__name__)


def log_exiting(func):
    """ Post function logging """

    logger = get_logger()

    global start_time
    logger.info("Exited %s %g seconds", func.__name__, timer() - start_time)
