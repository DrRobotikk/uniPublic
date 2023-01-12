package robin.tangengeneric;

public class TestKlient {
    public static void main(String[] args) {
        GeneriskStack<String> stakken = new GeneriskStack<>();
        //Setter inn noen bynavn:
        stakken.push("Kongsberg");
        stakken.push("Drammen");
        stakken.push("Hønefoss");

        //Tester på hva som igger øversti stakken:
        System.out.println("Øverst i stakken ligger: " + stakken.peep());
        //Skrive ut hele stakken:
        Object[] byliste = stakken.getInnhold();
        for(int i = byliste.length - 1; i > -1; i--){
            System.out.println(byliste[i]);
        }

        //FJerner øverse objekt
        System.out.println("Fjerner øverste by: " + stakken.pop());

        //skriver ut på nytt
        System.out.println("Stakken ser slik ut nå:");
        byliste = stakken.getInnhold();
        for(int i = byliste.length -1; i > -1; i--){
            System.out.println(byliste[i]);
        }

    }
}
