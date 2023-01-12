import javax.swing.*;

public class personProgram {
    //Dette er selve programet


    public static void main(String [] args){
        String navn= JOptionPane.showInputDialog("oppgi navn");
        String navn1= JOptionPane.showInputDialog("Oppgi navn");


        Person p1 = new Person(navn,"vei 1");
        Person p2 = new Person(navn1,"Vei 3");
        System.out.println(p1.toString());
        System.out.println(p2.toString());

        JOptionPane.showMessageDialog(null,p1.toString());
        JOptionPane.showMessageDialog(null,p2.toString());
    }
}
