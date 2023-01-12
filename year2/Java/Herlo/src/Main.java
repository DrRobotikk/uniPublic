import javax.swing.*;

public class Main  {
    public static void main(String[] args) {

        String navn = JOptionPane.showInputDialog("Skriv et navn");
        String navn1 = JOptionPane.showInputDialog("Skriv et navn");


        Person p1 = new Person(navn,"Vei 1");
        Person p2 = new Person(navn1,"vei 2");
        System.out.println(p1.toString());
        System.out.println(p2.toString());
    }
}