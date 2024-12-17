import os 
import logging
logger = logging.getLogger()
try:
    start = int(os.environ["START"]) 
    end = int(os.environ["END"])
except Exception as e: 
    logger.error(e)
if start >= end:
    logger.error("start must be bigger than end number start="+str(start)+" end="+str(end))   
else:    
    for x in range(start,end):
        print (str(x))
