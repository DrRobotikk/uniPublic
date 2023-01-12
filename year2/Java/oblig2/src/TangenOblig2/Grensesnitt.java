package TangenOblig2;

import javax.swing.*;
import java.util.ArrayList;
import java.util.Collections;

public class Grensesnitt {
    Kontroll kontroll = new Kontroll();
    private final String[] ALTERNATIVER = {"register hare","registrer gaupe","gjenfangsthare","gjenfangst gaupe","finn dyr","list alle dyr","avslutt"};


    public int lesvalg(){
        int valg = JOptionPane.showOptionDialog(
                null,
                "Ta et valg",//Ledetekst
                "Dyrregister",//Tittel på vinduet
                JOptionPane.DEFAULT_OPTION,//Klassekonstant
                JOptionPane.PLAIN_MESSAGE,//Klassekonstant
                null,
                ALTERNATIVER,//Valgene
                ALTERNATIVER[0]);//Default option
        return valg;
    }

    public void meny(){
        boolean fortsette = true;
        while (fortsette){
        int valg = lesvalg();
            switch (valg){
                case 0: registrerHare();
                    break;
                case 1: registrerGaupe();
                    break;
                case 2: registrerGjenfangstHare();
                    break;
                case 3: registrerGjenfangstGaupe();
                    break;
                case 4: finnDyr();
                    break;
                case 5: finnAlleDyr();
                    break;


                default: fortsette = false;
            }
        }
    }


    public void registrerHare(){
        ArrayList<Hare> hareListe = kontroll.getHareListe();
        String id = "H" + (hareListe.size()+1);
        String kjonn = JOptionPane.showInputDialog("Hva er kjønnet til dyret?");
        float lengde = Float.parseFloat(JOptionPane.showInputDialog("Hva er lengden til dyret?"));
        float vekt = Float.parseFloat(JOptionPane.showInputDialog("Hva er vekten til dyret?"));
        String type = JOptionPane.showInputDialog("Hva er type dyret?");
        String farge = JOptionPane.showInputDialog("Hva er fargen til dyret?");
        String sted = JOptionPane.showInputDialog("Hvor ble dyret observert?");
        String dato = JOptionPane.showInputDialog("Hvilket dato ble dyret observert?");
        ArrayList<GjenfangstHare> haregjenfangst = new ArrayList<>();
        Hare hare = new Hare(id,kjonn,lengde,vekt,sted,dato,type,farge,haregjenfangst);

        kontroll.registrerHare(hare);
    }

    public void registrerGaupe(){
        ArrayList<Gaupe> gaupeListe = kontroll.getGaupeListe();
        String id = "G" + (gaupeListe.size()+1);
        String kjonn = JOptionPane.showInputDialog("Hva er kjønnet til dyret?");
        float lengde = Float.parseFloat(JOptionPane.showInputDialog("Hva er lengden til dyret?"));
        float vekt = Float.parseFloat(JOptionPane.showInputDialog("Hva er vekten til dyret?"));
        float lengdeorer = Float.parseFloat(JOptionPane.showInputDialog("Hva er lengden på dyrets ører?"));
        String sted = JOptionPane.showInputDialog("Hvor ble dyret observert?");
        String dato = JOptionPane.showInputDialog("Hvilket dato ble dyret observert?");
        ArrayList<GjenfangstGaupe> gaupegjenfangst = new ArrayList<>();
        Gaupe gaupe = new Gaupe(id,kjonn,lengde,vekt,sted,dato,lengdeorer,gaupegjenfangst);

        kontroll.registrerGaupe(gaupe);
    }

    public void finnDyr(){
        String id = JOptionPane.showInputDialog("Hva er id til dyret?");
        String dyret = kontroll.finnDyr(id);
        System.out.println(dyret);
    }

    public void finnAlleDyr(){
        ArrayList<Gaupe> gaupe = kontroll.getGaupeListe();
        ArrayList<Hare> hare = kontroll.getHareListe();
        Collections.sort(gaupe);
        Collections.sort(hare);
        System.out.println(gaupe);
        System.out.println(hare);

    }

    public void registrerGjenfangstHare(){
        String id = JOptionPane.showInputDialog("Hva er id til dyret?");
        String sted = JOptionPane.showInputDialog("Hvor ble dyret observert?");
        String dato = JOptionPane.showInputDialog("Hvilket dato ble dyret observert?");
        float vekt = Float.parseFloat(JOptionPane.showInputDialog("Hva er vekten til dyret?"));
        float lengde = Float.parseFloat(JOptionPane.showInputDialog("Hva er lengden til dyret?"));
        String farge = JOptionPane.showInputDialog("Hva er fargen til dyret?");
        GjenfangstHare  hare = new GjenfangstHare( id, dato, vekt,lengde,sted, farge);
        kontroll.registrerGjenfangstHare(hare);
    }

    public void registrerGjenfangstGaupe(){
        String id = JOptionPane.showInputDialog("Hva er id til dyret?");
        String sted = JOptionPane.showInputDialog("Hvor ble dyret observert?");
        String dato = JOptionPane.showInputDialog("Hvilket dato ble dyret observert?");
        float vekt = Float.parseFloat(JOptionPane.showInputDialog("Hva er vekten til dyret?"));
        float lengde = Float.parseFloat(JOptionPane.showInputDialog("Hva er lengden til dyret?"));
        float lengdeorer = Float.parseFloat(JOptionPane.showInputDialog("Hva er lengden på dyrets ører?"));
        GjenfangstGaupe gaupe = new GjenfangstGaupe(id, dato, vekt,lengde,sted, lengdeorer);
        kontroll.registrerGjenfangstGaupe(gaupe);
    }


}
