//this script make subset list
//java subset originallist.txt willberemoved.txt 
import java.io.*;
import java.util.*;

class subset_full {
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
		if (!removed.contains(line)){
		  System.out.println(line);
		}
            }
        }catch (FileNotFoundException e){
            e.printStackTrace();
        }
    }
}
