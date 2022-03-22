FROM python:3.7.10

ENV HOST="0.0.0.0" \
    PORT="8000" \
    DATA_ROOT_PATH="/system/system/user_data"

WORKDIR /system

COPY ./ /system/

RUN apt update \
    && apt install -y --no-install-recommends \
        build-essential \
        python3-opencv \
    && pip3 install --upgrade --no-cache-dir pip setuptools wheel pipenv \
    && pipenv lock -r > requirements.txt \
    && pip3 --no-cache-dir install -r requirements.txt \
    && sed -i -e "1i #\! /usr/bin/env python3\n" converter/convert.py \
    && mv converter/convert.py /usr/local/sbin \
    && mv converter/config /usr/local/sbin \
    && ln /usr/local/sbin/convert.py /usr/local/sbin/tfconvert \
    && chmod +x /usr/local/sbin/tfconvert \
    && rm -rf converter/

VOLUME /system/system/user_date

ENTRYPOINT gunicorn --bind=$HOST:$PORT wsgi:app
