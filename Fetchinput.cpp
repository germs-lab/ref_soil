// usage:  g++ Fetchinput.cpp -o Fetchinput ;gcc NCBIinput.cpp -o NCBIinput 
// ./Fetchinput inputFile outputFile
// ./Fetchinput RefSoilListJin.csv RefSoilListJin.txt
#include <stdio.h>
#include <iostream>
#include <string>
#include <fstream>
#include <stdlib.h>

#define maxFilename 40

using namespace std;

int main(int argc, char *argv[])
{
int OpenFile(FILE **filePoint, string fileInput);
void CloseFile(FILE **filePoint);
void PrintFileContents(FILE **filePoint);

FILE *sourcefp;
string fileInput = argv[1];
printf("Start NCBI input\n");

OpenFile(&sourcefp,fileInput);

char info[100];
string read;
string delimiter = ",";
string token;
size_t pos = 0;
int delflag=0;

ofstream myfile;
myfile.open (argv[2]);
fscanf(sourcefp,"%s",info);

	while ((fscanf(sourcefp,"%s",info)) != EOF)
	{
		read = info;
		delflag=1;
		while ((pos = read.find(delimiter)) != string::npos) {
    		token = read.substr(0, pos);
    		if(delflag != 1 && token.length() != 0){myfile<<token+"\n";}
    		delflag++;
    		read.erase(0, pos + delimiter.length());
		}//while
	}//while

CloseFile(&sourcefp);	
myfile.close();
   
return 0;
}


// open file for reading
int OpenFile(FILE **filePoint, string fileInput)
{
    const char *file = fileInput.c_str();
    *filePoint = fopen (file,"r");
    
    if (filePoint == NULL){
    	printf ("File could not be opened\n");
    }else{
    	printf ("File opened\n");
    }
	return 0;
}

// close file
void CloseFile(FILE **filePoint)
{
	fclose(*filePoint); 	
}
