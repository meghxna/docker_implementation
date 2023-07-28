FROM continuumio/anaconda3
WORKDIR /test
COPY . /test
EXPOSE 5000

RUN pip install -r requirements.txt
RUN pip install -r requirements1.txt
CMD  ["python", "untitled1.py"]