FROM python:3.9

# Install Chrome and necessary dependencies
RUN apt-get update && \
    apt-get install -y wget gnupg2 && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable

# Download ChromeDriver - CHANGE VERSION IF NECESSARY
RUN wget -q -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/98.0.4758.48/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    chmod +x /usr/local/bin/chromedriver

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir selenium pyautogui requests

# Run script
CMD [ "python", "index.py" ]
