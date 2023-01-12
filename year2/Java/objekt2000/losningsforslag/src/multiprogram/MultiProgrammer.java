package multiprogram;

import javax.swing.*;

public class MultiProgrammer {
    public static void main(String[] args) {
        //Spør etter start verdi:
        int start = Integer.parseInt(JOptionPane.showInputDialog("Skriv startverdi"));
        //Leser sluttverdi:
        int slutt = Integer.parseInt(JOptionPane.showInputDialog("Skriv sluttverdi"));
        //Vi trenger to løkker:
        //en ytre løkke som går fra startverdi til sluttverdi
        //En indre løkke som går fra 1 til 10:
        //Ytre løkke:
        for (int i=start;i<slutt+1;i++){
            System.out.println();
            System.out.println(i + " gangen:");
            //indre løkke:
            for (int j = 1;j<11;j++){
                //i-tellern fra ytre løkke ganges med j-tellern fra indre løkke
                System.out.println(i+" x "+j + " = " + i*j);
            }
        }
    }
}
