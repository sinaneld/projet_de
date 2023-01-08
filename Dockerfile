FROM python:3.10.8

WORKDIR /app
ENV STREAMLIT_SERVER_PORT=80

RUN apt-get update

# cv2 dependencies
RUN apt-get install ffmpeg libsm6 libxext6  -y

# Matplotlib setup
# setuptool takes a lot of time so we decided to put matplotlb
RUN pip install --upgrade setuptools
RUN pip install matplotlib


COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["streamlit", "run", "/app/app.py"]
