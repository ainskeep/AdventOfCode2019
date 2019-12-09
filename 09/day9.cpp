//
// Created by ainskeep on 12/2/19.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

const string filePath = "./testInput.txt";

long long runProgram (){
    string line, code;
    ifstream inFile (filePath);
    getline(inFile, line); //get the first line

    stringstream ss(line);

    long long arraySize = 0;
    while ( getline(ss, code, ',') ){ //find how many numbers there are in the array
        arraySize++;
    }

    ss.str(line); //reset the string stream
    ss.clear();

    long long array[arraySize*10]; //create an array of just the right size

    int i = 0;
    while ( getline(ss, code, ',') ){
        array[i] = strtoll(code);
        i++;
    }

    //main program
    int opCode = 0;
    unsigned int instruction = 0;
    long long opPosition = 0;

    int paramMode1 = -1;
    int paramMode2 = -1;
    int paramMode3 = -1;

    long long param1 = 0;
    long long param2 = 0;
    long long param3 = 0;

    long long inputInt = 0;
    long long relativeBase = 0;

    bool breakLoop = false;
    while( !breakLoop ){

        instruction = array[opPosition];
        opCode = instruction % 100;

        paramMode1 =  instruction/100 % 10;
        paramMode2 = instruction/1000 % 10;
        paramMode3 = instruction/10000 % 10;

        switch(paramMode1){
            case 0:
                // position mode
                param1 = array[array[opPosition+1]];
                break;
            case 1:
                // imediate mode
                param1 = array[opPosition+1];
                break;
            case 2:
                // relative mode
                param1 = array[ relativeBase + array[opPosition+1]];
                break;
        };
        switch(paramMode2){
            case 0:
                // position mode
                param2 = array[array[opPosition+2]];
                break;
            case 1:
                // imediate mode
                param2 = array[opPosition+2];
                break;
            case 2:
                // relative mode
                param2 = array[ relativeBase + array[opPosition+2]];
                break;
        };
        switch(paramMode3){
            case 0:
                // position mode
                param1 = array[array[opPosition+3]];
                break;
            case 1:
                // imediate mode
                param1 = array[opPosition+3];
                break;
            case 2:
                // relative mode
                param1 = array[ relativeBase + array[opPosition+3]];
                break;
        };


        switch(opCode){
            case 1:
                param3 = array[opPosition+3]; // never immediate mode

                array[param3] = param1 + param2;
                opPosition += 4;

                break;
            case 2:
                param3 = array[opPosition+3]; // never immediate mode

                array[param3] = param1 * param2;
                opPosition += 4;
                break;
            case 3:
                cout << "Enter a  value: " << endl;;
                cin >> inputInt;
                cout << "You entered: " << inputInt << endl;

                param1 = array[opPosition+1];

                array[param1] = inputInt;

                opPosition += 2;
                break;

            case 4:
                cout << param1 << endl;
                opPosition += 2;
                break;

            case 5:
                if (param1 != 0){
                    opPosition = param2;
                }else {
                    opPosition +=3;
                }
                break;
            case 6:

                if (param1 == 0){
                    opPosition = param2;
                }else {
                    opPosition +=3;
                }
                break;
            case 7:
                param3 = array[opPosition+3]; // never immediate mode

                if (param1 < param2) {
                    array[param3] = 1;
                } else{
                    array[param3] = 0;
                }

                opPosition += 4;
                break;
            case 8:
                param3 = array[opPosition+3]; // never immediate mode

                if (param1 == param2) {
                    array[param3] = 1;
                } else{
                    array[param3] = 0;
                }

                opPosition += 4;
                break;
            case 9:
                param1 = paramMode1 == 1 ? array[opPosition+1] :  array[array[opPosition+1]];

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
    long long ans = runProgram();

    return 0;
}