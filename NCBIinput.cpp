// usage:  g++ NCBIinput.cpp -o NCBIinput ;gcc NCBIinput.cpp -o NCBIinput
// ./NCBIinput
#include <stdio.h>
#include <iostream>
#include <string>
#define maxFilename 40

using namespace std;

int main()
{
int OpenFile(FILE **filePoint, string fileInput);
void CloseFile(FILE **filePoint);
void PrintFileContents(FILE **filePoint);

//char userFile[maxFilename];
FILE *sourcefp;
string fileInput = "INSDC.csv";
printf("Start NCBI input\n");

OpenFile(&sourcefp,fileInput);

PrintFileContents(&sourcefp);

CloseFile(&sourcefp);	
	
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

//print 
void PrintFileContents (FILE **filePoint)
{
	char info[20];
	while ((fscanf(*filePoint,"%s",info)) != EOF)
	{
		printf("%s\n",info);
	}
}

