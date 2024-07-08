# Use the official Ubuntu image as the base image
FROM public.ecr.aws/ubuntu/ubuntu:22.04_stable

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt update \
    && apt install -y \
        sudo \
        curl \
        wget \
        unzip \
        gnupg \
        apt-transport-https \
        software-properties-common \
        at-spi2-core \
        libatk1.0-0 \
        libgtk-3-0 \
        libxtst6 \
        libxcomposite1 \
        libxrandr2 \
        xdg-utils \
        fonts-liberation \
        x11-xserver-utils \
        libxcursor1 \
        libxdamage1 \
        libxfixes3 \
        libxi6 \
        libxrender1 \
        libpangocairo-1.0-0 \
        libfreetype6 \
        fontconfig \
        dbus \
        libvulkan1 \
        mesa-utils \
        dbus-x11 \
        libdbus-glib-1-2 \
        libasound2 \
        libgconf-2-4 \
        libcups2 \
        libxkbcommon0 \
        libnss3 \
        libxshmfence-dev \
        libxss1 \
        libatk-bridge2.0-0 \
        libgbm1 \
        alsa-base \
        alsa-utils \
        adwaita-icon-theme \
        libatk-adaptor \
        gtk2-engines-pixbuf \
        x11-xkb-utils \
        libasound2-dev \
        python3 \
        python3-pip \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

# Add Google Chrome repository and install Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list' \
    && apt update \
    && apt install -y google-chrome-stable \
    && sudo rm -rf /var/lib/apt/lists/*

# Install ChromeDriver
RUN wget https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.126/linux64/chromedriver-linux64.zip \
    && sudo unzip chromedriver-linux64.zip \
    && sudo rm chromedriver-linux64.zip \
    && sudo mv chromedriver-linux64 /usr/local/bin/chromedriver \
    && sudo chmod +x /usr/local/bin/chromedriver

# Python Libs
RUN python3 -m pip install selenium

# Set environment variables
ENV PATH="/usr/local/bin/chromedriver:$PATH"
# ENV CHROME_PATH="/usr/bin/google-chrome"

# Copy the function code
COPY app.py /usr/src/app/app.py

# Set the working directory
WORKDIR /usr/src/app

# Set the CMD to execute the Python script
CMD ["python3", "app.py"]
