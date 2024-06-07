FROM selenium/standalone-chrome

USER root
RUN apt-get update && apt-get install python3-distutils -y
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py
RUN python3 -m pip install selenium
RUN apt-get update 
RUN apt-get install -y xvfb python3-tk python3-dev

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirement.txt

# Run script
CMD [ "python3", "index.py" ]