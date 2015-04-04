//This script make a file that list of file in the directory
// usage:  g++ getFileList.cpp -o getFileList 
// ./getFileList case2 ListOfFile.txt
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

//file for result
ofstream myfile;
myfile.open (argv[2]);
string token;

//get list of file
DIR *dir;
struct dirent *ent;
string dirname= argv[1];
char const* ca = dirname.c_str();
if ((dir = opendir (ca)) != NULL) {
  /* print all the files and directories within directory */
  while ((ent = readdir (dir)) != NULL) {
 	string filenameDIR=dirname+"/"+ent->d_name;
 	cout<<filenameDIR<<endl<<flush;
 	token = ent->d_name;
 	token = token.substr(0,10);
	myfile<<token+"\n";

  }
  closedir (dir);
} else {
  /* could not open directory */
  perror ("");
  return EXIT_FAILURE;
}
myfile.close();
return 0;
}
//this is end of main