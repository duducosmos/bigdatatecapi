#!/bin/bash
curl -H "Accept: application/json" \
    -H "Content-type: application/json;charset=UTF-8"\
    -X POST    \
    -d "@Dados/curlSendTest.json" \
    http://35.167.223.76/init/default/api/sent.json
