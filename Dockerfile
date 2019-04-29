FROM python:3.6
COPY . .
RUN pip install -r requirements.txt
RUN python ageg.py
RUN python finissante.py