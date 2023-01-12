package robin.tangen;

public class Testklient {
    //En testklient skal teste ut alle valgene:
    //som skal kunne foretas i et fremtidig grensesnitt
    public static void main(String[] args) {
        Oppgaveoversikt oversikt = new Oppgaveoversikt();
        //oppretter to studenter
        Student student = new Student("Lise", 2);


        boolean ok = oversikt.nyStudent(student);
        if(!ok) System.out.println("kune ikke legge til student");
        student = new Student("ole",0);
        oversikt.nyStudent(student);
        //Sorterer
        oversikt.sorter();
        //
        Student stud = oversikt.finnStudent("ole");
        if(stud != null) System.out.println(stud.toString());
        else System.out.println("Studenten er ikke registrert");
        //Søker på en vi vet ikke finnes:
        stud = oversikt.finnStudent("Petter");
        if(stud != null) System.out.println(stud.toString());
        else System.out.println("Studenten er ikke registrert");


    }
}
