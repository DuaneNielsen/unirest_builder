cat /tmp/names | tr -d , | xargs -n1 ./template.py $.database-status.status-properties.rate-properties.rate-detail value > /tmp/frag.json
cat header.json /tmp/frag.json footer.json > /tmp/marklogic_schema.json
