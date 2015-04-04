// This program merge all files in the directory into one file
// usage:  g++ MergeFiles.cpp -o MergeFiles
// ./MergeFiles List16s(folder) Final16s.fa(file)
// ./MergeFiles ../RefSoil16s RefSoil16s.fa
#include <stdio.h>
#include <iostream>
#include <string>
#include <fstream>
#include <stdlib.h>
#include <dirent.h>

#define maxFilename 40

using namespace std;
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
int main(int argc, char *argv[])
{

//file for input
ifstream input;
string s;

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
	
	string file = ent->d_name;
 	if (file.substr(0,1)!="."){
 		char const* fin = filenameDIR.c_str();
 		input.open(fin);
 	
 	if(input.fail()){                           //    Check open
       cerr << "Can't open file\n";
       return 1;
     }//if
     
 	while (!input.eof())
	{
		getline(input,s);
		if(s!=""){
		myfile << s+"\n";
		}
	}//while

	input.close();

 	}//if

  }//while
  closedir (dir);
} else {
  /* could not open directory */
  perror ("");
  return EXIT_FAILURE;
}
myfile.close();
return 0;
}


