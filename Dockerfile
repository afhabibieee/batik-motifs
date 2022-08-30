FROM python:3.8.0-slim

CMD mkdir /batik
COPY . /batik

WORKDIR /batik

EXPOSE 8501

RUN pip3 install -r requirements.txt

CMD streamlit run app.py --server.port $PORT