#!/bin/bash

parent_dir=$(pwd)
installation_dir=/tmp/bin

mkdir -p $installation_dir
cd $installation_dir || exit

nodejs_version=v20.12.0
nvm_installation_script_url=https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh

if ! command -v npm &> /dev/null; then

    # shellcheck disable=SC2059
    printf "\nnpm not available. installing nodejs$nodejs_version using nvm...\n"
    nodejs_installation_dir=$installation_dir/nodejs

    if ! command -v node &> /dev/null; then

#       TODO: Fork this script, save nvm to /tmp/bin and all other dependencies to this directory, then install node and npm to this directory as well
        curl -o- "$nvm_installation_script_url" | bash

        # shellcheck disable=SC1090
        source ~/.bashrc

        printf "\ninstalling nvm v0.39.3\n"
        nvm install "$nodejs_version"

#        curl -o "$nodejs_installation_dir/$nodejs_version" $nodejs_download_url
#
#        mkdir -p $nodejs_installation_dir
#        tar -xf "$nodejs_installation_dir/$nodejs_version" -C $nodejs_installation_dir --strip-components=1

    fi

    NODE_HOME=$nodejs_installation_dir
    PATH="$NODE_HOME/bin:$PATH"

fi

# Function to check and install a command if missing
install_if_missing() {
  if ! command -v "$1" &> /dev/null; then
    printf "\n%s missing. installing...\n" "$1"
    pip install -U "$2"
  fi
}

if ! command -v pip &> /dev/null; then
  printf "\npip not installed. exiting...\n"
  exit 1
fi

install_if_missing reloadium reloadium

cd "$parent_dir" || exit

# Setup githooks
printf "\nsetting up git hooks\n"
. ./.githooks/prepare-hook.sh

printf "\nsetting up git commit message template\n"
git config commit.template ./.gitmessage
git config commit.cleanup strip

# Check installation if Docker & docker-compose not available
if ! command -v docker &> /dev/null; then
  printf "\nDocker not available. please install Docker & docker-compose for containerized dev env.\n"
fi
