#Generated by libmep version 2023.3.29.0-beta

import math

def mepx(x, outputs):
  prg = [0] * 12
  prg[0] = x[4]
  prg[1] = x[1]
  prg[2] = x[5]
  prg[3] = math.log(prg[2])
  prg[4] = math.pow(prg[0], prg[3])
  prg[5] = x[0]
  prg[6] = prg[1] + prg[5]
  prg[7] = x[1]
  prg[8] = x[6]
  prg[9] = prg[4] / prg[6]
  prg[10] = prg[9] / prg[8]
  prg[11] = prg[10] / prg[7]

  if prg[11] <= 72.321900:
    outputs[0] = 0
  else:
    outputs[0] = 1

#example of utilization ...

x = [
0.200000, 0.100000, 0.100000, 0.100000, 0.200000, 0.100000, 0.200000, 0.100000, 0.100000]

outputs = [0]

mepx(x, outputs)

print("class = ", int(outputs[0]))
