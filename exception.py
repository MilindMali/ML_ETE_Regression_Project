from flask import Flask
from src.logger import logging
from src.exception import CustomException
import os, sys

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])

def index():

    try:
        raise Exception("we are testing our exception file")
    except Exception as e:
        ML=CustomException(e, sys)
        logging.info(ML.error_message)

    logging.info("we are testing our logging file")

    return "welcome to one more end to end ML project pipeline"


if __name__=="__main__":
    app.run(debug=True)
