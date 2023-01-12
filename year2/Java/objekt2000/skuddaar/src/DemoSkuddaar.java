import javax.swing.*;

public class DemoSkuddaar {
    public static void main(String[] args) {
        int aarstall = Integer.parseInt(JOptionPane.showInputDialog("Skriv et årstall: "));
        //Kaller metoden sjekkAar():
        boolean erskuddaar =sjekkAar(aarstall);
        if(erskuddaar) JOptionPane.showMessageDialog(null,"Året "+ aarstall +" er et skuddår");
        else JOptionPane.showMessageDialog(null,"Året "+aarstall+" er ikke et skuddår");

    }

    //Metode for å sjekke om vi har et skuddår:
    public static boolean sjekkAar(int aar){
        boolean ok;
        //Oversetter flytdiagrammet til kode:
        ok = (aar % 4 == 0 && aar % 100 != 0) || (aar % 400 == 0);
        return ok;
    }
}
