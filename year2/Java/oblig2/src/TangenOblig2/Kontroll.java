package TangenOblig2;

import java.util.ArrayList;

public class Kontroll {

    private ArrayList<Hare> hare = new ArrayList<>();
    private ArrayList<Gaupe> gaupe = new ArrayList<>();
    private ArrayList<Object> dyr = new ArrayList<>();


    public ArrayList<Hare> getHareListe() {
        return hare;
    }

    public ArrayList<Gaupe> getGaupeListe() {
        return gaupe;
    }

    public void registrerHare(Hare harepus) {
        hare.add(harepus);
        dyr.add(harepus);
    }

    public String finnDyr(String raseid) {
        for (Object dyr : dyr) {
            if (dyr instanceof Hare) {
                if (((Hare) dyr).getRaseid().equals(raseid)) {
                    return dyr.toString();
                }
            }
            if (dyr instanceof Gaupe) {
                if (((Gaupe) dyr).getRaseid().equals(raseid)) {
                    return dyr.toString();
                }
            }
        }
        return "Fant ikke dyret";
    }

    public void registrerGaupe(Gaupe gaupen) {
        gaupe.add(gaupen);
        dyr.add(gaupen);
    }


    public void registrerGjenfangstHare(GjenfangstHare harepus) {
        for (Hare hare : hare) {
            if (hare.getRaseid().equals(harepus.getRaseid())) {
                hare.getGjenfangst().add(harepus);
                dyr.add(harepus);
            }

        }
    }

    public void registrerGjenfangstGaupe(GjenfangstGaupe gaupen) {
        for (Gaupe gaupe : gaupe) {
            if (gaupen.getRaseid().equals(gaupe.getRaseid())) {
                gaupe.getGjenfangst().add(gaupen);
                dyr.add(gaupe);
            }

        }
    }
}
