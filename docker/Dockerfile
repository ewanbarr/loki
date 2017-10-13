FROM python:2.7

RUN pip install setuptools redis
RUN git clone https://github.com/ewanbarr/loki.git &&\ 
    cd loki && \
    python setup.py install
