package com.example.demoradioknapper;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.RadioButton;
import javafx.scene.control.ToggleGroup;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

import java.io.IOException;

public class HelloApplication extends Application {
    //Et objekt av klassen ToggleGroup
    ToggleGroup gruppe = new ToggleGroup();
    RadioButton rb1,rb2,rb3;
    @Override
    public void start(Stage stage) throws IOException {
        VBox root = new VBox();
        //Oppretter en knapp
        rb1 = new RadioButton("OBJ2000");
        //Setter som default
        rb1.setSelected(true);
        rb2 = new RadioButton("OAD2000");
        rb3 = new RadioButton("OBJ2100");
        //Knytter kanppene til ToggleGroup
        rb1.setToggleGroup(gruppe);
        rb2.setToggleGroup(gruppe);
        rb3.setToggleGroup(gruppe);
        //Legger knappene inn i Vboxen
        root.getChildren().addAll(rb1,rb2,rb3);
        //En annen måte å håndtere hendelser på
        rb1.setOnAction(e-> {if (rb1.isSelected()) System.out.println("Du valgte OBJ2000");});
        rb2.setOnAction(e-> {if (rb2.isSelected()) System.out.println("Du valgte OAD2000");});
        rb3.setOnAction(e-> {if (rb3.isSelected()) System.out.println("Du valgte OBJ2100");});



        Scene scene = new Scene(root, 320, 240);
        stage.setTitle("Radioknapper");
        stage.setScene(scene);
        stage.show();
    }



    public static void main(String[] args) {
        launch();
    }
}