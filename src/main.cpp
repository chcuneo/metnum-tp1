#include "algoritmos.h"
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <chrono>

/*
param 1 = input file
param 2 = output file
param 3 = method 
	0: Eliminacion Gaussiana banda, 
	1: Factorizacion LU explotando la propiedad banda y utilizando forward/back substitution
	2: Algoritmo de eliminacion de sanguijuela simple
	3: Algoritmo de eliminaci ́on de sanguijuela mejorado, usando la formula de Sherman–Morrison cuando sea posible
*/
int main(int argc, char *argv[]){

	std::ifstream input;
	input.open(argv[1]);

	//Cargar datos de input
	double widthp;
	double heightp;
	int nsangui;
	double h, trash;

	input >> widthp;
	input >> heightp;	
	if (argc == 5){
		std::stringstream out;
		out << argv[4];
		out >> h;
		input >> trash;
	} else {
		input >> h;
	}
	input >> nsangui;

	//Cargar datos de sanguijuelas

	sanguijuela* sanguiList = new sanguijuela[nsangui];
	for (int i = 0; i < nsangui; i++){
		input >> sanguiList[i].coord.y;
		input >> sanguiList[i].coord.x;
		input >> sanguiList[i].r;
		input >> sanguiList[i].t;
		//printf("Sangui: %i - Coord(%3.2lf,%3.2lf) - Radio:%lf - Temp=%lf\n", i, sanguiList[i].coord.y, sanguiList[i].coord.x, sanguiList[i].r, sanguiList[i].t);
	}
	input.close();

	//Inicializar Discretizacion de Parabrisas
	//int nw = (int)(widthp/h);
	//int nh = (int)(heightp/h);
	//double parabrisas[(int)nw][(int)nh];
	//for (int x = 1; x < nw - 1; x++){
	//	for (int y = 1; y < nh - 1; y++){
	//			parabrisas[x][y] = -200;
	//	}
	//}
	//for (int i = 0; i < nw; i++){
	//	parabrisas[i][0] = -100;
	//	parabrisas[i][nh-1] = -100;
	//}
	//for (int i = 0; i < nh; i++){
	//	parabrisas[0][i] = -100;
	//	parabrisas[nw-1][i] = -100;
	//}

	Matriz *test = new Matriz;
	GenerarMatriz(test, (heightp / h) + 1, (widthp / h) + 1, h, sanguiList, nsangui);
	int mejorsangui = -1;
	int i;

	//Tiempo:
	std::chrono::high_resolution_clock::time_point t1 = std::chrono::high_resolution_clock::now();

	switch(atoi(argv[3])){
		case(0):
			eliminacionGauseana(test);
			backwardSubstitution(test);
			mostrarF(test, argv[2]);
			break;
		case(1):
			descomposicionLU(test);
			fordwardSubstitution(test);
			backwardSubstitution(test);
			mostrarF(test, argv[2]);
			break;
		case(2):
			eliminacionGauseana(test);
			backwardSubstitution(test);
			// mostrarSolucion(test);
			mejorsangui = ultimaEsperanza(test, sanguiList, nsangui, heightp, widthp);
			// mostrarSolucion(test);
			mostrarF(test, argv[2]);
			break;
		case(3):
			descomposicionLU(test);
			fordwardSubstitution(test);
			backwardSubstitution(test);
			mejorsangui = superLastHope(test, sanguiList, nsangui, heightp, widthp);
			mostrarF(test, argv[2]);
			break;
		case(4):
			descomposicionLU(test);
			fordwardSubstitution(test);
			backwardSubstitution(test);
			mostrarSolucion(test);
			while (true){
				std::cin >> i;
				regenerarSinSangui(test, i);
				//eliminacionGauseana(test);
				//backwardSubstitution(test);
				descomposicionLU(test);
				fordwardSubstitution(test);
				backwardSubstitution(test);
				mostrarSolucion(test);
			}
			mostrarMF(test);
			break;
	}
	std::chrono::high_resolution_clock::time_point t2 = std::chrono::high_resolution_clock::now();
	auto duration = std::chrono::duration_cast<std::chrono::microseconds>(t2 - t1).count();

	// if (atoi(argv[3]) == 2 or atoi(argv[3]) == 3){
	// 	std::cout << "La mejor sanguijela a sacar con el limpiaparabrisas es la numero: " << mejorsangui << "\n";
	// 	std::cout << "Sangui " << mejorsangui << " - X: " << sanguiList[mejorsangui].coord.x << "  Y: " << sanguiList[mejorsangui].coord.y
	// 	<< "  Radio: " << sanguiList[mejorsangui].r << "  Temp: " << sanguiList[mejorsangui].t << "C" << "\n";
	// }

	std::cout << duration << "," << test->solution[(test->n / 2)] << "," << mejorsangui ;

	delete test;
	delete[] sanguiList;
	return 0;
}


