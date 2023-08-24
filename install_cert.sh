#!/usr/bin/env bash
mkcert -install \
    -cert-file cert.pem \
    -key-file key.pem \
    localhost

directory_path="node_modules/webpack-dev-server/ssl"

if [ ! -d "$directory_path" ]; then
    mkdir -p "$directory_path"
    echo "Directory created: $directory_path"
else
    echo "Directory already exists: $directory_path"
fi
cat cert.pem key.pem > $directory_path/server.pem
rm cert.pem key.pem

sleep 1