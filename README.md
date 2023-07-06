# highscore-micro-one

[![Open in Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=660674546&machine=standardLinux32gb&devcontainer_path=.devcontainer%2Fdevcontainer.json&location=EastUs)

A FastAPI ASGI microservice to query a high score list.

Backend is a NoSQL database deployed on Deta Space. (Cloud deployment shown via [GitHub Actions](https://github.com/bcorfman/highscore-micro-one/blob/main/.github/workflows/test-deploy.yml).)

I'm using this project to practice simple microservice design with Python.

# Prerequisites

* Click on the *Open with GitHub Codespaces* badge above to launch the project in a browser or on your desktop inside Visual Studio Code.

OR

* Install [Python](https://www.python.org) 3.9 or higher
* Install [Pipenv](https://pipenv.pypa.io/en/latest/)
* At a command prompt in the project directory, type `pipenv install` to set up project-level dependencies only, or `pipenv install --dev` to include dev dependencies as well

# Try out the live web service
It's hosted [on Deta Space](https://demofastapi-1-e9928521.deta.app/docs).
