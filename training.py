import pandas as pd
from matplotlib import pyplot as plt

def	readFile(fileName):
	data = pd.read_csv(fileName)
	return data["km"], data["price"]

def     writeFile(theta0, theta1):
	data = pd.DataFrame({"theta0": [theta0], "theta1": [theta1]})
	data.to_csv("theta.csv")

def	normalize(val):
	tmp = []
	for i in range(len(val)):
		tmp.append(val[i] / max(val))
	return tmp

def	h_theta(theta0, theta1, x):
	return theta0 + theta1 * x

def	tab_h_theta(theta0, theta1, x):
	return theta0 + theta1 * x

def	j_theta(x, y, theta0, theta1):
	cost = 0
	m = len(x)
	for i in range(m):
		cost += (h_theta(theta0, theta1, x[i]) - y[i]) ** 2
	cost /= 2 * m
	return cost

def	gradientDescent(x, y):
	x = normalize(x)
	y = normalize(y)
	history_cost = []
	alpha = 0.1
	theta0 = theta1 = 0
	m = len(x)
	iteration = 10000
	for i in range(iteration):
		tmp_sum0 = tmp_sum1 = 0
		for j in range(m):
			tmp_sum0 += h_theta(theta0, theta1, x[j]) - y[j]
			tmp_sum1 += (h_theta(theta0, theta1, x[j]) - y[j]) * x[j]
		theta0 -= (alpha * tmp_sum0) / m
		theta1 -= (alpha * tmp_sum1) / m
		if i % 10 == 0:
            		history_cost.append(j_theta(x, y, theta0, theta1))
	return theta0, theta1, history_cost

def	plot(x, y, theta0, theta1, history_cost):
	fig, axs = plt.subplots(2,2, figsize=(10,10))
	axs[0,0].plot(x)
	axs[0,0].set_ylabel("Kilometer", fontsize=10, fontweight = 'bold')
	axs[0,0].set_title("Kilometer data", color = 'green', fontsize=10, fontweight='bold')
	axs[0,1].plot(y)
	axs[0,1].set_ylabel("Price", fontsize=10, fontweight = 'bold')
	axs[0,1].set_title("Price data", color = 'green', fontsize=10, fontweight='bold')
	# linear regression
	axs[1,0].scatter(x, y, c='r', s=50, label="data")
	axs[1,0].plot(x, tab_h_theta(theta0, theta1, x), label="linear regression", marker="+")
	axs[1,0].legend(fancybox=True, framealpha=1, shadow=True, borderpad=1)
	axs[1,0].set_xlabel("Kilometer", fontsize=10, fontweight = 'bold')
	axs[1,0].set_ylabel("Price", fontsize=10, fontweight = 'bold')
	axs[1,0].set_title("Price of cars based on their metrage", fontsize=10, color='green', fontweight='bold')
	# Cost per iteration
	axs[1,1].plot(history_cost, label='Cost')
	axs[1,1].legend(fancybox=True, framealpha=1, shadow=True, borderpad=1)
	axs[1,1].set_xlabel("Iteration", fontsize=10, fontweight = 'bold')
	axs[1,1].set_ylabel("Cost", fontsize=10, fontweight = 'bold')
	axs[1,1].set_title("cost per iteration J(θ0, θ1)", fontsize=10, color='green', fontweight='bold')
	# linear regression 3D
	fig = plt.figure(2)
	ax = fig.add_subplot(111, projection='3d')
	ax.scatter(x, y, tab_h_theta(theta0, theta1, x), c='r', s=50, label="data")
	ax.plot_trisurf(x, y, tab_h_theta(theta0, theta1, x), alpha=0.2, label="linear regression")
	ax.set_xlabel('Kilometer', fontsize=10, fontweight = 'bold')
	ax.set_ylabel('Price', fontsize=10, fontweight = 'bold')
	ax.set_zlabel('h(θ)', fontsize=10, fontweight = 'bold')
	ax.set_title("Price of cars based on their metrage in 3D", fontsize=10, color='green', fontweight='bold')
	#show
	plt.show()

def	rmse(y, y_pred, size):
	return (sum((y - y_pred) **2) / size) **0.5

def	main():
	x, y = readFile("data.csv")
	theta0, theta1, history_cost = gradientDescent(x, y)
	theta0 = theta0 * max(y)
	theta1 = theta1 * max(y) / max(x)
	y_pred = tab_h_theta(theta0, theta1, x)
	# Evaluate the performance of the algorithm
	result = rmse(y, y_pred, len(x))
	print("Root Mean Squared Error (RMSE) = {:.10f}".format(result))
	# Save in file
	writeFile(theta0, theta1)	
	# Graphics
	plot(x, y, theta0, theta1, history_cost)

if __name__ == "__main__":
	main()
