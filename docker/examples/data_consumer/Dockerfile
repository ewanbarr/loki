FROM python:2.7

RUN pip install setuptools redis && \
    git clone https://github.com/ewanbarr/loki.git &&\ 
    cd loki && \
    python setup.py install

COPY script.py script.py
eCMD ['/usr/local/bin/python','script.py']