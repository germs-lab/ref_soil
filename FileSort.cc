// usage:  g++ FileSort.cc -o FileSort
// ./FileSort fileinput directory case1 case2
// ./FileSort RefSoilListJinUnix.csv ../RefSoil16s case1 case2
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
int OpenFile(FILE **filePoint, string fileInput);
void CloseFile(FILE **filePoint);
void PrintFileContents(FILE **filePoint);
size_t getFilesize(const std::string& filename); 

string fileInput = argv[1];
string dirname= argv[2];
//case 1 don't need wokr
string newdirname1= argv[3];
//case 2 need HMM
string newdirname2= argv[4];

FILE *sourcefp;

OpenFile(&sourcefp,fileInput);

char info[100];
string read;
string delimiter = ",";
string token;
size_t pos = 0;
int delflag=0;
//open file
fscanf(sourcefp,"%s",info);
//read file
typedef string MATRIX[1181][4];
MATRIX list;
MATRIX filename;
vector<string> vlist;
vector<string> vfilename;

int countraw=0;
int countcol=0;
	//read until end
int colnum=0;
	while ((fscanf(sourcefp,"%s",info)) != EOF)
	{
		read = info;
		delflag=1;
		
		countraw++;
		colnum=0;
		while ((pos = read.find(delimiter)) != string::npos) {
    		token = read.substr(0, pos);

    		if(delflag>countcol){countcol=delflag;}
    		list[countraw][colnum]=token;			
    	
    		colnum++;
    		delflag++;
    		read.erase(0, pos + delimiter.length());
		}//while
	}//while

////close file
CloseFile(&sourcefp);	



//get file matrix
DIR *dir;
struct dirent *ent;
int filenamenum=0;

char const* ca = dirname.c_str();
if ((dir = opendir (ca)) != NULL) {
  /* print all the files and directories within directory */
  while ((ent = readdir (dir)) != NULL) {
 
   string filenameDIR=dirname+"/"+ent->d_name;
   filename[filenamenum][0]=filenameDIR;
   filename[filenamenum][2]=ent->d_name;
   
   vfilename.push_back(filenameDIR);
  
   char const* fica = filenameDIR.c_str();

	size_t size = getFilesize(fica);

  int convertdata = static_cast<int>(size);
	//string filesize = to_string(convertdata);
	//string filesize = lexical_cast<string>(convertdata);
	ostringstream ostr;
	ostr << convertdata;
	string filesize = ostr.str();

	filename[filenamenum][1]=filesize;
	filenamenum++;

  }
  closedir (dir);
} else {
  /* could not open directory */
  perror ("");
  return EXIT_FAILURE;
}


for (int i=0; i<1181;i++){
	if (filename[i][1]=="0"){
		for(int j=0;j<1065;j++){
			if(list[j][1]+".gbk.16S.fa"==filename[i][2]||list[j][2]+".gbk.16S.fa"==filename[i][2]||list[j][3]+".gbk.16S.fa"==filename[i][2]){
				string newfilename1 = newdirname1 + filename[i][2];
				string newfilename2 = newdirname2 + filename[i][2];
				char const* oname = filename[i][0].c_str();
				char const* nname1 = newfilename1.c_str();
				char const* nname2 = newfilename2.c_str();
				
				if(list[j][2]==""){
					cout<<"alone-> case2 "+filename[i][2]<<endl<<flush;
					rename(oname,nname2);
				
				}else{
					cout<<"case1 "+filename[i][2]<<endl<<flush;
					rename(oname,nname1);
				}
			}
		}

	}
}

   
return 0;
}
//this is end of main

//file size
size_t getFilesize(const std::string& filename) {
    struct stat st;
    if(stat(filename.c_str(), &st) != 0) {
        return 0;
    }
    return st.st_size;   
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
