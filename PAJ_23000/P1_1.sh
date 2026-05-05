#!/bin/bash
while true; do
  ping -c 1 8.8.8.8 | grep "time="
  sleep 1
done

# ini file praktikum 1.1 saya 
