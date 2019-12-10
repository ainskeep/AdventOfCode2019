//
// Created by ainskeep on 12/2/19.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

const string filePath = "/home/ainskeep/github/AdventOfCode2019/09/input.txt";

long long int getParam(long long int *array, int paramMode, int paramNumber, int opPosition, int relativeBase){
    int param;
        switch(paramMode){
            case 0:
                // position mode
                param = array[opPosition+paramNumber];
                break;
            case 1:
                // imediate mode
                param = opPosition+paramNumber;
                break;
            case 2:
                // relative mode
                param = relativeBase + array[opPosition+paramNumber];
                break;
        };
    return param;
}

long long int runProgram (){
    string line, code;
    ifstream inFile (filePath);
    getline(inFile, line); //get the first line

    stringstream ss(line);

    long long int arraySize = 0;
    while ( getline(ss, code, ',') ){ //find how many numbers there are in the array
        arraySize++;
    }

    ss.str(line); //reset the string stream
    ss.clear();

    long long int array[arraySize * 10] = {0}; //create an array of just the right size

    char* pEnd;
    int i = 0;
    while ( getline(ss, code, ',') ){
        array[i] = strtoll(code.c_str(), &pEnd,10);
        i++;
    }

    //main program
    int opCode = 0;
    unsigned int instruction = 0;
    long long int opPosition = 0;

    int paramMode1 = -1;
    int paramMode2 = -1;
    int paramMode3 = -1;

    long long int param1 = 0;
    long long int param2 = 0;
    long long int param3 = 0;

    long long int inputInt = 0;
    long long int relativeBase = 0;

    bool breakLoop = false;
    while( !breakLoop ){

        instruction = array[opPosition];
        opCode = instruction % 100;

        paramMode1 =  instruction/100 % 10;
        paramMode2 = instruction/1000 % 10;
        paramMode3 = instruction/10000 % 10;

        switch(opCode){
            case 1:
                param1 = array[getParam(array, paramMode1, 1, opPosition, relativeBase)];
                param2 = array[getParam(array, paramMode2, 2, opPosition, relativeBase)];
                param3 = getParam(array, paramMode3, 3, opPosition, relativeBase); //unsure

                array[param3] = param1 + param2;
                opPosition += 4;

                break;
            case 2:
                param1 = array[getParam(array, paramMode1, 1, opPosition, relativeBase)];
                param2 = array[getParam(array, paramMode2, 2, opPosition, relativeBase)];
                param3 = getParam(array, paramMode3, 3, opPosition, relativeBase); //unsure

                array[param3] = param1 * param2;
                opPosition += 4;
                break;
            case 3:
                cout << "Enter a  value: " << endl;;
                cin >> inputInt;
                cout << "You entered: " << inputInt << endl;

                param1 = array[getParam(array, paramMode1, 1, opPosition, relativeBase)];

                array[param1] = inputInt;

                opPosition += 2;
                break;

            case 4:
                param1 = array[getParam(array, paramMode1, 1, opPosition, relativeBase)];

                cout << param1 << endl;
                opPosition += 2;
                break;

            case 5:
                param1 = array[getParam(array, paramMode1, 1, opPosition, relativeBase)];
                param2 = array[getParam(array, paramMode2, 2, opPosition, relativeBase)];

                if (param1 != 0){
                    opPosition = param2;
                }else {
                    opPosition +=3;
                }
                break;
            case 6:
                param1 = array[getParam(array, paramMode1, 1, opPosition, relativeBase)];
                param2 = array[getParam(array, paramMode2, 2, opPosition, relativeBase)];

                if (param1 == 0){
                    opPosition = param2;
                }else {
                    opPosition +=3;
                }
                break;
            case 7:
                param1 = array[getParam(array, paramMode1, 1, opPosition, relativeBase)];
                param2 = array[getParam(array, paramMode2, 2, opPosition, relativeBase)];
                param3 = getParam(array, paramMode3, 3, opPosition, relativeBase); //unsure


                if (param1 < param2) {
                    array[param3] = 1;
                } else{
                    array[param3] = 0;
                }

                opPosition += 4;
                break;
            case 8:
                param1 = array[getParam(array, paramMode1, 1, opPosition, relativeBase)];
                param2 = array[getParam(array, paramMode2, 2, opPosition, relativeBase)];
                param3 = getParam(array, paramMode3, 3, opPosition, relativeBase); //unsure

                if (param1 == param2) {
                    array[param3] = 1;
                } else{
                    array[param3] = 0;
                }

                opPosition += 4;
                break;
            case 9:
                param1 = getParam(array, paramMode1, 1, opPosition, relativeBase);
                relativeBase += param1;

                opPosition += 2;

                break;

            case 99:
                // cout << "\nopCode 99 hit. position 0: " << array[0] << "\n";
                breakLoop = true;
                break;

            default:
                cout << "\nSomething went wrong. Unknow opCode: " << opCode << "\n";
        }
    }
    return array[0];
}


int main()
{
    long long int ans = runProgram();

    return 0;
}