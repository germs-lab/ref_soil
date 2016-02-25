//java present_in_refseq archaea bacteria fungi id

import java.io.*;
import java.util.*;

class present_in_refseq {
    public static void main(String[] args){
	//read archaea
	HashSet <String> archaea = new HashSet<String>();
	File arFile = new File(args[0]);
	try{
	    Scanner arFile_scan = new Scanner(arFile);
	    while(arFile_scan.hasNextLine()){
		String line = arFile_scan.nextLine();
		String[] parts = line.split("\t");
		archaea.add(parts[0]);
	    }
	}catch (FileNotFoundException e){
	    e.printStackTrace();
	}
	//read bacteria
	HashSet <String> bacteria = new HashSet<String>();
        File bacFile = new File(args[1]);
        try{
            Scanner bacFile_scan = new Scanner(bacFile);
            while(bacFile_scan.hasNextLine()){
                String line = bacFile_scan.nextLine();
                String[] parts = line.split("\t");
                bacteria.add(parts[0]);
            }
        }catch (FileNotFoundException e){
            e.printStackTrace();
        }

	// read fungi
	HashSet <String> fungi = new HashSet<String>();
        File funFile = new File(args[2]);
        try{
            Scanner funFile_scan = new Scanner(funFile);
            while(funFile_scan.hasNextLine()){
                String line = funFile_scan.nextLine();
                String[] parts = line.split("\t");
                fungi.add(parts[0]);
            }
        }catch (FileNotFoundException e){
            e.printStackTrace();
        }

	//read id to find
	File idFile = new File (args[3]);
	try{
            Scanner idFile_scan = new Scanner(idFile);
            while(idFile_scan.hasNextLine()){
                String line = idFile_scan.nextLine();
                if(archaea.contains(line)||bacteria.contains(line)||fungi.contains(line)){
		    //System.out.println("present");
		}else{
		    System.out.println(line);
		}
            }
        }catch (FileNotFoundException e){
            e.printStackTrace();
        }
			    
    }
}
