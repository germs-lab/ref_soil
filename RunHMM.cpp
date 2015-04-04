//This script make a file that list of file in the directory
// usage:  g++ RunHMM.cpp -o RunHMM
// ./RunHMM directory
// ./RunHMM FullGenomeForHMM
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
string dirname= argv[1];
string token;
string runHMM;
char const* ca = dirname.c_str();
if ((dir = opendir (ca)) != NULL) {
  /* print all the files and directories within directory */
  while ((ent = readdir (dir)) != NULL) {
 	string filenameDIR=dirname+"/"+ent->d_name;
 	cout<<filenameDIR<<endl<<flush;
 	token = ent->d_name;
 	token = token.substr(0,10);
	runHMM = "hmmsearch ssu.hmm "+filenameDIR+" > output/"+token+".out";
	//cout<<runHMM<<endl<<flush;
	if (token.substr(0,1)!="."){
	 char const* run = runHMM.c_str();
	 system(run);
	}
  }
  closedir (dir);
} else {
  /* could not open directory */
  perror ("");
  return EXIT_FAILURE;
}


//system ("hmmsearch");
return 0;
}
//this is end of main