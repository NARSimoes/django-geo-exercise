
FROM ubuntu:bionic

RUN mkdir -p /usr/src/geo_exercise
WORKDIR /usr/src/geo_exercise/
ADD . /usr/src/geo_exercise
# to delete after dev
RUN mkdir -p /geo_exercise

# set default environment variables
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

# some projects vars
ENV PORT=8000
ENV HOME /usr/src/geo_exercise/

RUN apt-get update && apt-get install -y --no-install-recommends \
	    tzdata \
        python3-setuptools \
        python3-pip \
        python3-dev \
        python3-venv \
        gunicorn \
		postgresql-client libpq-dev \
        python-gdal python-psycopg2 \
        python-dev libgdal-dev gcc musl-dev \
        fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 \
        libnspr4 libnss3 lsb-release xdg-utils libxss1 libdbus-glib-1-2 \
        curl unzip wget \
        xvfb \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# install environment dependencies
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade --no-cache-dir --src /usr/src -r requirements.txt

RUN GECKODRIVER_VERSION=`curl https://github.com/mozilla/geckodriver/releases/latest | grep -Po 'v[0-9]+.[0-9]+.[0-9]+'` && \
    wget https://github.com/mozilla/geckodriver/releases/download/$GECKODRIVER_VERSION/geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz && \
    tar -zxf geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz -C /usr/src/geo_exercise && \
    chmod +x /usr/src/geo_exercise/geckodriver && \
    rm geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz

# Firefox
#=========
ARG FIREFOX_VERSION=latest
RUN FIREFOX_DOWNLOAD_URL=$(if [ $FIREFOX_VERSION = "latest" ] || [ $FIREFOX_VERSION = "nightly-latest" ] || [ $FIREFOX_VERSION = "devedition-latest" ]; then echo "https://download.mozilla.org/?product=firefox-$FIREFOX_VERSION-ssl&os=linux64&lang=en-US"; else echo "https://download-installer.cdn.mozilla.net/pub/firefox/releases/$FIREFOX_VERSION/linux-x86_64/en-US/firefox-$FIREFOX_VERSION.tar.bz2"; fi) \
  && apt-get update -qqy \
  && apt-get -qqy --no-install-recommends install firefox libavcodec-extra \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/* \
  && wget --no-verbose -O /tmp/firefox.tar.bz2 $FIREFOX_DOWNLOAD_URL \
  && apt-get -y purge firefox \
  && rm -rf /opt/firefox \
  && tar -C /opt -xjf /tmp/firefox.tar.bz2 \
  && rm /tmp/firefox.tar.bz2 \
  && mv /opt/firefox /opt/firefox-$FIREFOX_VERSION \
  && ln -fs /opt/firefox-$FIREFOX_VERSION/firefox /usr/bin/firefox

RUN chmod a+x /usr/src/geo_exercise/entrypoint.sh

WORKDIR /geo_exercise/
