#!/bin/bash
while true; do
  ping -c 1 8.8.8.8 | grep "time="
  sleep 1
done
