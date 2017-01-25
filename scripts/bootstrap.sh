#!/bin/bash

if [ "$1" = "--dev" ]; then
    echo -e "\e[32mInstall Requirements\e[0m"
    pip install -r requirements/dev.txt
    if [ ! -f ./settings/local.py ]; then
        echo -e "\e[32mCreating local settings file\e[0m"
        cp ./settings/local.default.py ./settings/local.py
    fi
    echo -e "\e[32mGit Init\e[0m"
    git init
    echo -n -e "\e[32mMigrate\e[0m"
    python manage.py migrate
    echo -n -e "\e[32mDo you want to create a superuser now? (y/n)?\e[0m"
    read answer
    if echo "$answer" | grep -iq "^y" ;then
        export ENVIRONMENT=local && python manage.py createsuperuser
    fi
elif [ "$1" = "--prod" ]; then
    pip install -r requirements/prod.txt
else
    echo "argument needed (--dev, --prod)"
fi
