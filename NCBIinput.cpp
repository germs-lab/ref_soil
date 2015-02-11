// usage:  g++ NCBIinput.cpp -o NCBIinput ;gcc NCBIinput.cpp -o NCBIinput
// ./NCBIinput
#include <stdio.h>
#include <iostream>
#include <string>
#define maxFilename 40

using namespace std;

int main()
{
int OpenFile(string fileInput);
void CloseFile(string fileInput);
void PrintFileContents(FILE **filePoint);

char userFile[maxFilename];
FILE *sourcefp;
string fileInput = "INSDC.csv";

    printf("Start NCBI input\n");
    
	OpenFile(fileInput);
     
    
    
return 0;
}

// open file for reading
int OpenFile(string fileInput)
{
    FILE *my_stream;
    const char *file = fileInput.c_str();
    my_stream = fopen (file,"r");
    
    if (my_stream == NULL){
    	printf ("File could not be opened\n");
    }else{
    	printf ("File opened\n");
    }
    

return 0;
}

void CloseFile(string fileInput)
{
	const char *file = fileInput.c_str();
	fclose(file); 
	
}

void PrintFileContents (FILE **filePoint)
{
}

