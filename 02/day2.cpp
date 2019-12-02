//
// Created by ainskeep on 12/2/19.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

const string filePath = "./input.txt";

int runProgram (int noun, int verb){
    string line, code;
    ifstream inFile (filePath);
    getline(inFile, line); //get the first line

    stringstream ss(line);

    int arraySize = 0;
    while ( getline(ss, code, ',') ){ //find how many numbers there are in the array
        arraySize++;
    }

    ss.str(line); //reset the string stream
    ss.clear();

    int array[arraySize]; //create an array of just the right size

    int i = 0;
    while ( getline(ss, code, ',') ){
        array[i] = stoi(code);
        i++;
    }

    // Restore state
    array[1] = noun;
    array[2] = verb;

    //main program
    int opCode = 0;
    int opPosition = 0;
    int ansLoc = 0;
    bool breakLoop = false;
    while( !breakLoop ){
        opCode = array[opPosition];

        switch(opCode){

            case 1:
                ansLoc = array[opPosition+3];
                if (ansLoc > arraySize) {
                    cout << "ansLoc will go out of array bounds" << "\n";
                }
                array[ansLoc] = array[array[opPosition+1]] + array[array[opPosition+2]];
                break;
            case 2:
                ansLoc = array[opPosition+3];
                if (ansLoc > arraySize) {
                    cout << "opPosition+3 will go out of array bounds" << "\n";
                }
                array[ansLoc] = array[array[opPosition+1]] * array[array[opPosition+2]];
                break;
            case 99:
                // cout << "\nopCode 99 hit. position 0: " << array[0] << "\n";
                breakLoop = true;
                break;

            default:
                cout << "\nSomething went wrong. Unknow opCode: " << opCode << "\n";
        }

        opPosition += 4;
        if (opPosition+3 > arraySize && !breakLoop){
            cout << "opPosition will go out of array bounds" << "\n";
            breakLoop = true;
        }
    }
    return array[0];
}



int main()
{
    cout << "\nPart One Ans: " << runProgram(12, 2) << endl;

    for(int noun = 0; noun <= 99; noun++){
        for(int verb = 0; verb <= 99; verb++){
            int ret = runProgram(noun, verb);
            if (ret == 19690720){
                cout << "Part Two Ans: Noun: " << noun << " Verb: " << verb << " Code: " << 100 * noun + verb << endl;
                return 0;
            }
        }
    }

    return 0;
}