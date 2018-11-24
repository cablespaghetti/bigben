FROM python:3-alpine

RUN pip install toot==0.19.0 && apk add --no-cache gettext bash && mkdir -p /root/.config/toot
WORKDIR /bong
COPY config.json.tmpl /bong/config.json.tmpl 
COPY images /bong/images
COPY bong.sh /bong

CMD cat config.json.tmpl | envsubst > /root/.config/toot/config.json && bash bong.sh
