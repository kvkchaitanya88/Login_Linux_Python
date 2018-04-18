#!/usr/pkg/bin/python

#Importing modules
import paramiko
import sys
import time
import os
import subprocess

#setting parameters like host IP, username, passwd
HOST = "127.0.0.1"
USER = "root"
PASS = "root"
ITERATION = 1

#A function that logins and execute commands
def fn():
  client1=paramiko.SSHClient()
  #Add missing client key
  client1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  client1.connect(HOST,username=USER,password=PASS)
  print "SSH connection to %s established" %HOST
  os.linesep
  f = open('hello.txt','w')
  f.write('hello world')
  f.close()
  client1.close()
  print"Logged out of device %s" %HOST

#for loop to call above fn x times. Here x is set to 1
for x in xrange(ITERATION):
  fn()
  print "%s Iteration/s completed" %(x+1)
  print "********"
  time.sleep(1) #sleep for 5 seconds
