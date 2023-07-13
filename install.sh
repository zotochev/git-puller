#!/usr/bin/env bash

# export IFS=":"
# sentence="$PATH"
INSTALLATION_DIR="$HOME/.local/bin"

if [[ $PATH == *"$INSTALLATION_DIR"* ]]; then
  # echo "EXISTS IN PATH!"
  :
else
  for word in $sentence; do
    if [[ $word == *"local"* ]]; then
      INSTALLATION_DIR="$word"
      break
    fi
  done
fi

if [ ! -d "$INSTALLATION_DIR" ]; then
  # echo "NO such directory"
  mkdir -p "$INSTALLATION_DIR"
fi


SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

cp "$SCRIPT_DIR/git-puller" "$INSTALLATION_DIR"

