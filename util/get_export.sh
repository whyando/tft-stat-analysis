#!/bin/bash

cat remote_generate_export.sh | ssh whyando.com
ssh whyando.com 'tar -cf - export.txt | gzip -9' > /tmp/export.tar.gz
tar -xvzf /tmp/export.tar.gz
rm /tmp/export.tar.gz