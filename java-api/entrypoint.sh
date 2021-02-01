#!/bin/bash
set -e

# This entry point runs two processes, a continuous java api build and a continuous serve of a springboot application
#cd /home/gradle/src
cd /app

# Spawn bash if we're booting in console mode
if [ "$1" = 'bash' ]; then
    /bin/bash
    exit
fi

# if [ "$1" = 'build' ]; then
#   echo "beginning continuous build..."
#   gradle build --continuous --no-daemon
# fi

if [ "$1" = 'development_server' ]; then
  # echo "Beginning continuous build..."
  # gradle build --continuous --no-daemon &
  echo "Beginning server..."
  pwd
  ls
  # gradle bootRun --debug-jvm --no-daemon
  gradle bootRun --no-daemon
fi

if [ "$1" = 'deployment' ]; then
  echo "Beginning production serve"
  java -XX:+UnlockExperimentalVMOptions -XX:+UseCGroupMemoryLimitForHeap -Djava.security.egd=file:/dev/./urandom -jar /app.jar
fi
