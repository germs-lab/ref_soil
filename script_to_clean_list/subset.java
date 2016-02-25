//this script make subset list
//java subset originallist.txt willberemoved.txt 
import java.io.*;
import java.util.*;

class subset {
    public static void main(String[] args){
	//read to be removed
	HashSet <String> removed = new HashSet<String>();
	File reFile = new File(args[1]);
	try{
	    Scanner reFile_scan = new Scanner(reFile);
	    while(reFile_scan.hasNextLine()){
		String line = reFile_scan.nextLine();
		//System.out.println(line);
		removed.add(line);
	    }
	}catch (FileNotFoundException e){
	    e.printStackTrace();
	}

	//read list
	File liFile = new File(args[0]);
        try{
            Scanner liFile_scan = new Scanner(liFile);
            while(liFile_scan.hasNextLine()){
                String line = liFile_scan.nextLine();
		String[] splt = line.split("\t",0);
		//System.out.println(splt[0]);
		String[] nodot = splt[0].split("\\.",0);
		//System.out.println(nodot[0]);
		if (!removed.contains(nodot[0])){
		  System.out.println(line);
		}
            }
        }catch (FileNotFoundException e){
            e.printStackTrace();
        }
    }
}
