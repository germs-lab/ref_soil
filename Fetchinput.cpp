// usage:  g++ Fetchinput.cpp -o Fetchinput ;gcc NCBIinput.cpp -o NCBIinput 
// ./Fetchinput inputFile outputFile
// ./Fetchinput RefSoilListJinUnix.csv RefSoilListJin.txt
#include <stdio.h>
#include <iostream>
#include <string>
#include <fstream>
#include <stdlib.h>
#include <dirent.h>
#include <vector>
#include <sstream>
#define maxFilename 40

using namespace std;
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
int main(int argc, char *argv[])
{

int checkFile(ifstream &input);

//file for input
ifstream inputTable;
string table;
inputTable.open(argv[1]);
vector <vector <string> > data;
checkFile(inputTable);

//file for result
ofstream myfile;
myfile.open (argv[2]);

while(getline(inputTable,table))
{
	istringstream ss (table);
		
	//this add data into the column (second number)
	vector <string> record;

		while (ss)
		{
			string s1;
			if(!getline(ss,s1,',')) break;
			
			record.push_back(s1);
		}
		//this add data into the row (first number)
		data.push_back(record);

}//while
inputTable.close();

//output
for (int i=1;i<data.size();i++){
	for (int j=1;j<data[i].size();j++){
		if(data[i][j].length() > 0){
			myfile<<data[i][j]+"\n";
		}
	}
}

	
myfile.close();
   
return 0;
}


// check openfile
int checkFile(ifstream &input)
{
	if(input.fail()){                           //    Check open
       cerr << "Can't open file\n";
       exit(EXIT_FAILURE);
       //return 1;
	}else{return 0;}
}