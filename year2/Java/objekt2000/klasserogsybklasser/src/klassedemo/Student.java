package klassedemo;

public class Student extends Person {
    String studieprogram;

    public Student(String navn, String adresse, int fodselsaar, String studieprogram) {
        super(navn, adresse, fodselsaar);
        this.studieprogram = studieprogram;
    }

    @Override
    public String toString() {
        return "Student{" +
                "studieprogram='" + studieprogram + '\'' +
                "} " + super.toString();
    }
}
