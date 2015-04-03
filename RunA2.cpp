//This script make a file that list of file in the directory
// usage:  g++ RunA2.cpp -o RunA2
// you need to run this in the working directory
// ./RunA2 DB queryDirectory
// example: ./RunA2 ../../RefSoilCompGenome
#include <stdio.h>
#include <iostream>
#include <string>
#include <fstream>
#include <stdlib.h>
#include <dirent.h>
#include <vector>

#define maxFilename 40

using namespace std;
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
int main(int argc, char *argv[])
{

//get list of file
DIR *dir;
struct dirent *ent;
string dirname=argv[1];
string token;
string runA2;
char const* ca = dirname.c_str();
if ((dir = opendir (ca)) != NULL) {
  /* print all the files and directories within directory */
	while ((ent = readdir (dir)) != NULL) {
		// print file-name 
 		string filenameDIR=dirname+"/"+ent->d_name;
 		cout<<filenameDIR<<endl<<flush;
 		token = ent->d_name;
		runA2 = "perl ../Scripts/MarkerScanner.pl -Bacteria -DNA "+filenameDIR;
		
		//run A2
		if (token.substr(0,1)!="."){
			char const* run = runA2.c_str();
			system(run);
		}//if
		
  	}//while
	closedir (dir);
} else {
  /* could not open directory */
  perror ("");
  return EXIT_FAILURE;
}//if

return 0;
}
//this is end of main