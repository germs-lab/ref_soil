//This script make a file that
// usage:  g++ GetResultHMM.cpp -o GetResultHMM
// ./GetResultHMM outputfilename resultfilename
// ./GetResultHMM RefSeq16sHMM.output RefSeq16sHMM.txt
#include <stdio.h>
#include <iostream>
#include <string>
#include <fstream>
#include <stdlib.h>
#include <dirent.h>
#include <vector>
#include <sstream>

using namespace std;
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
int main(int argc, char *argv[])
{
int checkFile(ifstream &input); 
void printMatrix(vector <vector <string> > &dad);

//****************************//
// Read output file of HMM    //
//****************************//
//file for input
ifstream input;
string s;

input.open(argv[1]);
checkFile(input);
vector <vector <string> > data;
while(getline(input,s))
{
	if(s.substr(0,2)==">>"){
		for(int i=0 ; i < 4 ; i++){
		istringstream ss (s);
		//this add data into the column (second number)
		vector <string> record;
		while (ss)
		{
			string s1;
			if(!getline(ss,s1,' ')) break;
			if(s1!=""){
				record.push_back(s1);
			}
		}
		//this add data into the row (first number)
		data.push_back(record);
		getline(input,s);
		}
	}//if
}//while

input.close();

//****************************//
// Write result file          //
//****************************//
//file for result
ofstream myfile;
myfile.open (argv[2]);
string token;
	for (int i=0;i<data.size();i++){
		myfile << data[i][1] +";" + data[i+3][12] +";" + data[i+3][13]+"\n";
		i=i+3;	
	}

myfile.close();
return 0;
}
//this is end of main


// check openfile
int checkFile(ifstream &input)
{
	if(input.fail()){                           //    Check open
       cerr << "Can't open file\n";
       exit(EXIT_FAILURE);
       //return 1;
	}else{return 0;}
}

void printMatrix(vector <vector <string> > &dad){
	for (int i=0;i<dad.size();i++){
		for (int j=0;j<dad[i].size();j++){
			cout<<dad[i][j]+" "<<flush;
		}
	cout<<endl<<flush;
	}
}