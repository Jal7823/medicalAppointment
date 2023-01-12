import random
from random import randint
import datetime
from datetime import timedelta



def createNumberMembership():
    """should be create a number membership for new associated user
    """    
    numbreCard = random.randint(0,9999_9999_9999_9999)
    traspast = str(numbreCard)
    separator = '{} {} {} {}'.format(traspast[:4],traspast[4:8],traspast[8:12],traspast[12:])

createNumberMembership()