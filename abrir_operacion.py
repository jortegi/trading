#!/usr/bin/python

import argparse

pct_riesgo = 0.02

parser = argparse.ArgumentParser()
parser.add_argument('--size', help='trading account size', required=True)
parser.add_argument('--price', help="buy price", required=True)
parser.add_argument('--stop', help="stop loss", required=True)
args = parser.parse_args()

cuenta = args.size
entrada = args.price
stop_loss = args.stop

riesgo_total = float(float(cuenta) * pct_riesgo)
riesgo_por_accion = float(float(entrada) - float(stop_loss))

numero_de_acciones = riesgo_total / riesgo_por_accion

print(numero_de_acciones)
