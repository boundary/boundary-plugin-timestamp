#!/usr/bin/env python
"""
This script generates metrics with timestamps
Changing sha

    timestamp.py

"""
import json
import time
import socket
import random
import sys

class Timestamp():

  def __init__(self):
     self.pollInterval = None
     self.hostname = socket.gethostname()

  def get_configuration(self):
    '''
    1) Reads the param.json file that contains the configuration of the plugin.
    2) Sets the values to member variables of the class instance.
    '''
    with open('param.json') as f:
      parameters = json.loads(f.read())
      self.pollInterval = float(parameters['pollInterval'])/1000.0

  def run(self):
    '''
    Outputs a random metric value at a give duration specified by the poll interval
    '''
    while True:
      print("{0} {1} {2} {3}".format("BOUNDARY_TIMESTAMP_METRIC",str(random.randrange(0,99)),self.hostname,str(int(time.time()*1000))))
      sys.stdout.flush()
      time.sleep(float(self.pollInterval))

if __name__ == "__main__":
  # Timestamp instance
  t = Timestamp()
  # Load configuration
  t.get_configuration()
  # execute plugin
  t.run()
