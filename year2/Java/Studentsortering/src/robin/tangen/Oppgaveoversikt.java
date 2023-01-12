package robin.tangen;

import java.util.Arrays;

public class Oppgaveoversikt {
    //Denne skal holde rede på studentene
    //Hver student holder rede på egne godkjente oppgaver

    private Student[] studenter = new Student[2];
    private int antallStudenter = 0;

    //Metode forå sette inn en ny student

    public  boolean nyStudent(Student student){
        //Tester på om det er plass til et objekt til:
        if(antallStudenter < studenter.length){
            studenter[antallStudenter] = student;
            antallStudenter++;
            return true;
        }
        //Hvis ikke det er plass
        else return false;
    }

    public void sorter(){
        //Bruker hjelpeklassen Arrays:
        Arrays.sort(studenter);
    }

    //Meotde for linjært søk på student:
    public Student finnStudent(String søkenavn){
        String navn;
        for (int i = 0; i < antallStudenter; i++) {
            navn = studenter[i].getNavn();
            if (søkenavn.equals(navn)) return studenter[i];



        }
        // ikke funnet:
        return null;
    }




}
