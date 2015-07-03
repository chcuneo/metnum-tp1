import os
from pylab import *
#TODO Pasar datos a otro directorio asi no se reprocesa

plotdir = "./plots/"
if not os.path.exists(plotdir):
    os.makedirs(plotdir)
indef = open("resultsDef.csv", "r")
next(indef)

xgrantemp = []
test1temp0 = []
test1temp1 = []
test1temp2 = []
test1temp3 = []

test2temp0 = []
test2temp1 = []
test2temp2 = []
test2temp3 = []

test7temp0 = []
test7temp1 = []
test7temp2 = []
test7temp3 = []

xgran = []
xgrantime = []
test1time0 = []
test1time1 = []
test1time2 = []
test1time3 = []

test2time0 = []
test2time1 = []
test2time2 = []
test2time3 = []

test7time0 = []
test7time1 = []
test7time2 = []
test7time3 = []

while True:
	try:
		test1met0 = next(indef)
		test1met1 = next(indef)
		test1met2 = next(indef)
		test1met3 = next(indef)
		test2met0 = next(indef)
		test2met1 = next(indef)
		test2met2 = next(indef)
		test2met3 = next(indef)
		test7met0 = next(indef)
		test7met1 = next(indef)
		test7met2 = next(indef)
		test7met3 = next(indef)
	except(StopIteration):
		break
	test1met0 = test1met0.split(',') 
	test1met1 = test1met1.split(',') 
	test1met2 = test1met2.split(',') 
	test1met3 = test1met3.split(',') 
	test2met0 = test2met0.split(',') 
	test2met1 = test2met1.split(',') 
	test2met2 = test2met2.split(',') 
	test2met3 = test2met3.split(',') 
	test7met0 = test7met0.split(',') 
	test7met1 = test7met1.split(',') 
	test7met2 = test7met2.split(',') 
	test7met3 = test7met3.split(',') 

	xgran.append(float(test1met0[2]))
	nowgran = float(test1met0[2])
	if (float(test1met1[2]) != nowgran) or (float(test1met2[2]) != nowgran) or (float(test1met3[2]) != nowgran) or (float(test2met0[2]) != nowgran) or(float(test2met1[2]) != nowgran) or (float(test2met2[2]) != nowgran) or (float(test2met3[2]) != nowgran) or (float(test7met0[2]) != nowgran) or(float(test7met1[2]) != nowgran) or (float(test7met2[2]) != nowgran) or (float(test7met3[2]) != nowgran):
		print("wtf!!!!")
		quit()
	if ((nowgran) > 1.6 ):
		xgrantime.append(float(test1met0[2]))
		test1time0.append(int(test1met0[3]))
		test1time1.append(int(test1met1[3]))
		test1time2.append(int(test1met2[3]))
		test1time3.append(int(test1met3[3]))
		test2time0.append(int(test2met0[3]))
		test2time1.append(int(test2met1[3]))
		test2time2.append(int(test2met2[3]))
		test2time3.append(int(test2met3[3]))
		test7time0.append(int(test7met0[3]))
		test7time1.append(int(test7met1[3]))
		test7time2.append(int(test7met2[3]))
		test7time3.append(int(test7met3[3]))

	if ((float(test1met0[4]) != -100) and (float(test1met1[4]) != -100) and (float(test1met2[4]) != -100) and (float(test2met0[4]) != -100) and(float(test2met1[4]) != -100) and (float(test2met2[4]) != -100) and (float(test7met0[4]) != -100) and(float(test7met1[4]) != -100) and (float(test7met2[4]) != -100)):
		xgrantemp.append(float(test1met0[2]))
		test1temp0.append(float(test1met0[4]))
		test1temp1.append(float(test1met1[4]))
		test1temp2.append(float(test1met2[4]))
		test1temp3.append(float(test1met2[4]))
		test2temp0.append(float(test2met0[4]))
		test2temp1.append(float(test2met1[4]))
		test2temp2.append(float(test2met2[4]))
		test2temp3.append(float(test2met2[4]))
		test7temp0.append(float(test7met0[4]))
		test7temp1.append(float(test7met1[4]))
		test7temp2.append(float(test7met2[4]))
		test7temp3.append(float(test7met2[4]))

print("vamo lo pi")

plot(xgrantemp, test1temp0, color='red', lw=2, label='test1', marker="o")
plot(xgrantemp, test2temp0, color='green', lw=2, label='test2', marker="o")
plot(xgrantemp, test7temp0, color='blue', lw=2, label='test7', marker="o")
legend(loc='upper right')
xlabel('Granularidad')
ylabel('Temperatura Punto Critico (C)')
title('Metodo 0')
grid(True)
savefig("granTempMet0.png")
clf()

plot(xgrantemp, test1temp1, color='red', lw=2, label='test1', marker="o")
plot(xgrantemp, test2temp1, color='green', lw=2, label='test2', marker="o")
plot(xgrantemp, test7temp1, color='blue', lw=2, label='test7', marker="o")
legend(loc='upper right')
xlabel('Granularidad')
ylabel('Temperatura Punto Critico (C)')
title('Metodo 1')
grid(True)
savefig("granTempMet1.png")
clf()

plot(xgrantemp, test1temp2, color='red', lw=2, label='test1', marker="o")
plot(xgrantemp, test2temp2, color='green', lw=2, label='test2', marker="o")
plot(xgrantemp, test7temp2, color='blue', lw=2, label='test7', marker="o")
legend(loc='upper right')
xlabel('Granularidad')
ylabel('Temperatura Punto Critico (C)')
title('Metodo 2')
grid(True)
savefig("granTempMet2.png")
clf()

plot(xgrantemp, test1temp3, color='red', lw=2, label='test1', marker="o")
plot(xgrantemp, test2temp3, color='green', lw=2, label='test2', marker="o")
plot(xgrantemp, test7temp3, color='blue', lw=2, label='test7', marker="o")
legend(loc='upper right')
xlabel('Granularidad')
ylabel('Temperatura Punto Critico (C)')
title('Metodo 3')
grid(True)
savefig("granTempMet3.png")
clf()

plot(xgrantime, test1time0, color='red', lw=2, label='Metodo 0', marker="o")
plot(xgrantime, test1time1, color='green', lw=2, label='Metodo 1', marker="o")
legend(loc='upper right')
xlabel('Granularidad')
ylabel('Tiempo de computo (microsegundos)')
title('Test1')
grid(True)
savefig("granTimetest1.png")
clf()

plot(xgrantime, test2time0, color='red', lw=2, label='Metodo 0', marker="o")
plot(xgrantime, test2time1, color='green', lw=2, label='Metodo 1', marker="o")
legend(loc='upper right')
xlabel('Granularidad')
ylabel('Tiempo de computo (microsegundos)')
title('Test2')
grid(True)
savefig("granTimetest2.png")
clf()

plot(xgrantime, test7time0, color='red', lw=2, label='Metodo 0', marker="o")
plot(xgrantime, test7time1, color='green', lw=2, label='Metodo 1', marker="o")
legend(loc='upper right')
xlabel('Granularidad')
ylabel('Tiempo de computo (microsegundos)')
title('Test7')
grid(True)
savefig("granTimetest7.png")
clf()

plot(xgrantime, test1time2, color='red', lw=2, label='Metodo 3', marker="o")
plot(xgrantime, test1time3, color='green', lw=2, label='Metodo 4', marker="o")
legend(loc='upper right')
xlabel('Granularidad')
ylabel('Tiempo de computo (microsegundos)')
title('Test1')
grid(True)
savefig("granTempTest1.png")
clf()

plot(xgrantime, test2time2, color='red', lw=2, label='Metodo 3', marker="o")
plot(xgrantime, test2time3, color='green', lw=2, label='Metodo 4', marker="o")
legend(loc='upper right')
xlabel('Granularidad')
ylabel('Tiempo de computo (microsegundos)')
title('Test2')
grid(True)
savefig("granTempTest2.png")
clf()

plot(xgrantime, test7time2, color='red', lw=2, label='Metodo 3', marker="o")
plot(xgrantime, test7time3, color='green', lw=2, label='Metodo 4', marker="o")
legend(loc='upper right')
xlabel('Granularidad')
ylabel('Tiempo de computo (microsegundos)')
title('Test7')
grid(True)
savefig("granTempTest7.png")
clf()