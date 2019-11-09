FROM python:3

COPY . /usr/src/app
ENV HOME=/usr/src/app
WORKDIR /usr/src/app

RUN mkdir -p ~/.pip/
RUN cp pip.conf ~/.pip/
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["app.py"]
