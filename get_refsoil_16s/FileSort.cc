// usage:  g++ FileSort.cc -o FileSort
// ./FileSort fileinput directory case1 case2
// ./FileSort RefSoilListJinUnix.csv ../RefSoil16s case1 case2
// ./FileSort RefSoilListJinUnix.csv genbank-files case1 case2
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
size_t getFilesize(const std::string& filename);
int checkFile(ifstream &input); 
string searchSize(string &st,vector <vector <string> > &da);
void printMatrix(vector <vector <string> > &dad);
void checkDir (string &direc);


//arguments
//string fileInput = argv[1];
string dirname = argv[2];
//case 1 don't need work
string newdirname1= argv[3];
//case 2 need HMM
string newdirname2= argv[4];

//*********************************************************
//read full table of RefSoil list and put into matrix
//*********************************************************
//file for input
ifstream inputTable;
string table;
inputTable.open(argv[1]);
vector <vector <string> > data;
checkFile(inputTable);

while(getline(inputTable,table))
{
	istringstream ss (table);
	//this add data into the column (second number)
	vector <string> record;
		while (ss)
		{
			string s1;
			if(!getline(ss,s1,',')) break;
			if(s1!=""){
				record.push_back(s1);
			}
		}
		//this add data into the row (first number)
		data.push_back(record);

}//while
inputTable.close();

//run into directory to figure out

//***********************
//get file matrix
//***********************
DIR *dir;
struct dirent *ent;
char const* ca = dirname.c_str();
vector <vector <string> > Filedata;
if ((dir = opendir (ca)) != NULL) {
  /* print all the files and directories within directory */
	while ((ent = readdir (dir)) != NULL) {
 		vector <string> record;
		string filenameDIR=dirname+"/"+ent->d_name;
		string file = ent->d_name;
		if(file.substr(0,1)!="."){
			record.push_back(ent->d_name);
			char const* fica = filenameDIR.c_str();
			size_t size = getFilesize(fica);	
			int convertdata = static_cast<int>(size);
			ostringstream ostr;
			ostr << convertdata;
			string filesize = ostr.str();
			record.push_back(filesize);
			Filedata.push_back(record);
		}
  }//while
  closedir (dir);
} else {
  /* could not open directory */
  perror ("");
  return EXIT_FAILURE;
}
//printMatrix(data);

//***********************
// compare
//***********************
for(int i=1;i<data.size();i++){
	for(int j=0;j<data[i].size();j++){
		//search file size
		if(searchSize(data[i][j],Filedata)=="0"){
			cout<<data[i][j]<<endl<<flush;
			//go throurth row
			int flag=0;
			for (int l=0; l<data[i].size();l++){
				//search file size
				if((searchSize(data[i][l],Filedata)!="0") && (searchSize(data[i][l],Filedata)!="")){
					flag=1;
				}
			}//for
			string oldFilename = dirname + "/" + data[i][j] + ".gbk.16S.fa";
			char const* oname = oldFilename.c_str();
			if(flag==1){
				cout<<"case1"<<endl<<flush;
				checkDir (newdirname1);
				string newfilename1 = newdirname1 + "/" + data[i][j] + ".gbk.16S.fa";
				char const* nname1 = newfilename1.c_str();
				rename(oname,nname1);
			}else{
				cout<<"case2"<<endl<<flush;
				checkDir (newdirname2);
				string newfilename2 = newdirname2 + "/" + data[i][j] + ".gbk.16S.fa";
				char const* nname2 = newfilename2.c_str();
				rename(oname,nname2);
				
			}//if
		}else if(searchSize(data[i][j],Filedata)==""){
			//cout<<"no file"<<endl<<flush;
		}else{
			//cout<<"looks good"<<endl<<flush;
		}//if search file size
	}//for j
}//for i
	
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

// check openfile
int checkFile(ifstream &input)
{
	if(input.fail()){                           //    Check open
       cerr << "Can't open file\n";
       exit(EXIT_FAILURE);
       //return 1;
	}else{return 0;}
}

string searchSize(string &st,vector <vector <string> > &da){
	string size="";
	for (int k=0;k<da.size();k++){
		if(st+".gbk.16S.fa"==da[k][0]){
			size = da[k][1];
		}
	}
	return size;
}

void printMatrix(vector <vector <string> > &dad){
	for (int i=0;i<dad.size();i++){
		for (int j=0;j<dad[i].size();j++){
			cout<<dad[i][j]+" "<<flush;
		}
	cout<<endl<<flush;
	}
}

void checkDir (string &direc){
	DIR *dir;
	struct dirent *ent;
	char const* ca = direc.c_str();
	if ((dir = opendir (ca)) != NULL) {
		closedir (dir);
	} else {
  		/* could not open directory */
  		string mkdir = "mkdir "+direc;
  		char const* run = mkdir.c_str();
  		system(run);
	}
}