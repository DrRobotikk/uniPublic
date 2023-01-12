package Multiplikasjonstabell.src.no.usn.braadland.Multiplikasjon;

import javax.swing.JOptionPane;

public class MultiProgram {

	public static void main(String[] args) {
		//Sp�r etter startverdi:
		int start = Integer.parseInt(JOptionPane.showInputDialog("Skriv startverdi:"));
		//Leser sluttverdi:
		int slutt = Integer.parseInt(JOptionPane.showInputDialog("Skriv sluttverdi:"));
		//Vi trenger to l�kker:
		//En ytre l�kke som g�r fra startverdi til sluttverdi.
		//En indre l�kke som g�r fra 1 til 10.
		//Ytre l�kke:
		for(int i = start; i < slutt+1; i++) {
			System.out.println();
			System.out.println(i + " gangen:");
			//Indre l�kke:
			for(int j = 1; j < 11; j++) {
				//i-telleren fra ytre l�kke ganges med j-telleren fra indre l�kke:
				System.out.println(i + " x " + j + " = " + i*j);
			}
		}

	}

}
