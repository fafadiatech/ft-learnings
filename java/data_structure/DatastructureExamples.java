import java.io.*;
import java.util.*;

public class DatastructureExamples{
	public static void main(String[] args){
		// Example usage of HashMap
		HashMap<String, String> favColors = new HashMap<String, String>();
		favColors.put("Sidharth", "Red");
		favColors.put("Vyoma", "Pink");

		for(Map.Entry<String, String> entry: favColors.entrySet()){
			System.out.println(entry.getKey() + " -> " + entry.getValue());
		}

		// Example useage of ArrayList
		ArrayList<Inte

	}
}