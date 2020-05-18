# coding: utf-8

import pandas as pd

def	openFile():
	data = pd.read_csv("theta.csv")
	return (float(data.theta0), float(data.theta1))

def	findPrice(theta0, theta1):
	km = input("Please enter kilometer : ")
	try:
		km = float(km)
		price = theta0 + theta1 * km
		print("{:.3f} euros".format(price))
	except:
		print("Oops! Enter a valid number")
		findPrice(theta0, theta1)

def	main():
	theta0 = theta1 = 0
	try:
		theta0, theta1 = openFile()
	except:
		print("Not yet learned")
	findPrice(theta0, theta1)

if __name__ == "__main__":
	main()
