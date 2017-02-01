#!/bin/bash
curl -H "Accept: application/json" \
    -H "Content-type: application/json;charset=UTF-8"\
    -X POST    \
    -d "@Dados/curlSendTest.json" \
    http://api.bigdatatec.com/init/default/api/sent.json
