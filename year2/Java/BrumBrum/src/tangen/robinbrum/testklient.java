package tangen.robinbrum;

public class testklient {
    public static void main(String[] args) {
        kontroll kontroll = new kontroll();
        kontroll.nyttKjøretøy(new Personbil("AB12345", "Volvo", "V70", 2005, 5));
        kontroll.nyttKjøretøy(new Personbil("CD12345", "Volvo", "V70", 2005, 5));
        kontroll.nyttKjøretøy(new Personbil("EF12345", "Volvo", "V70", 2005, 5));
        kontroll.nyttKjøretøy(new Personbil("GH12345", "Volvo", "V70", 2005, 5));
        kontroll.nyttKjøretøy(new Personbil("IJ12345", "Volvo", "V70", 2005, 5));
        kontroll.nyttKjøretøy(new Personbil("KL12345", "Volvo", "V70", 2005, 5));
        kontroll.nyttKjøretøy(new Personbil("MN12345", "Volvo", "V70", 2005, 5));
        kontroll.nyttKjøretøy(new Personbil("OP12345", "Volvo", "V70", 2005, 5));
        kontroll.nyttKjøretøy(new Personbil("QR12345", "Volvo", "V70", 2005, 5));
        kontroll.nyttKjøretøy(new Personbil("ST12345", "Volvo", "V70", 2005, 5));
        kontroll.nyttKjøretøy(new Personbil("UV12345", "Volvo", "V70", 2005, 5));
        kontroll.nyttKjøretøy(new Personbil("WX12345", "Volvo", "V70", 2005, 5));
        kontroll.nyttKjøretøy(new Personbil("YZ12345", "Volvo", "V70", 2005, 5));
        kontroll.nyttKjøretøy(new Personbil("AB12346", "Volvo", "V70", 2005, 5));


        if (kontroll.finnKjøretøy("CD12345") != null) {
            System.out.println(kontroll.finnKjøretøy("CD12345").toString());
        } else {
            System.out.println("Kjøretøyet er ikke registrert");
        }
    }
}
