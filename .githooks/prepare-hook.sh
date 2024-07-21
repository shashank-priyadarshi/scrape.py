#!/bin/bash

parent_dir=$(pwd)
installation_dir=/tmp/bin

cd "$parent_dir" || exit

if ! command -v commitlint &> /dev/null; then
  printf "\ncommitlint not available. installing latest commitlint globally...\n"
  npm install --global @commitlint/cli
fi

printf "\nsetting up npm repository for commitlint\n"
npm init -y &> /dev/null
printf "\ninstalling commit lint as dev dependency\n"
npm install --save-dev @commitlint/config-conventional &> /dev/null

install_if_missing() {
  if ! command -v "$1" &> /dev/null; then
    printf "\n%s missing. installing...\n" "$1"
    pip install -U "$2"
  fi
}

install_if_missing prospector prospector
install_if_missing mypy mypy
install_if_missing radon radon
install_if_missing bandit bandit
install_if_missing isort isort

printf "\nall git hook dependencies installed/available. proceeding with setup...\n"

cp "$parent_dir/.githooks/commit-msg" "$parent_dir/.git/hooks/"
chmod +x "$parent_dir/.git/hooks/commit-msg"

cp "$parent_dir/.githooks/pre-commit" "$parent_dir/.git/hooks/pre-commit"
chmod +x "$parent_dir/.git/hooks/pre-commit"

printf "\nsetup hook dependencies and local hooks\n"
