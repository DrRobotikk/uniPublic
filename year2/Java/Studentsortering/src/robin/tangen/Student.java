package robin.tangen;

public class Student implements Comparable<Student> {
    private String navn;
    private int antallOppgaver;

    public Student(String navn, int antallOppgaver) {
        this.navn = navn;
        this.antallOppgaver = antallOppgaver;
    }

    public String getNavn() {
        return navn;
    }

    public void setNavn(String navn) {
        this.navn = navn;
    }

    public int getAntallOppgaver() {
        return antallOppgaver;
    }

    public void setAntallOppgaver(int antallOppgaver) {
        this.antallOppgaver = antallOppgaver;
    }

    @Override
    public String toString() {
        return "Student{" +
                "navn='" + navn + '\'' +
                ", antallOppgaver=" + antallOppgaver +
                '}';
    }

    public int compareTo(Student student) {
        return this.navn.compareTo(student.getNavn());
    }

    public boolean equals(Student s) {
        return this.navn.equals(s.getNavn());

    }
}
