package com.example.demokomboplayer;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.ComboBox;
import javafx.scene.layout.BorderPane;
import javafx.stage.Stage;

import java.io.IOException;

public class HelloApplication extends Application {
    ComboBox<String> liste;

    String[] alternativer = {"mandag", "tirsdag", "onsdag", "torsdag", "fredag", "lørdag", "søndag"};
    @Override
    public void start(Stage stage) throws IOException {

        liste = new ComboBox<String>();
        liste.getItems().addAll(alternativer);
        //Setter overskriften til boksen
        liste.setValue("ukedag");
        //Knytter komboboksen til lytteren
        liste.setOnAction(e -> behandleValg());

        BorderPane root = new BorderPane();
        root.setCenter(liste);
        Scene scene = new Scene(root, 320, 240);
        stage.setTitle("Hello!");
        stage.setScene(scene);
        stage.show();

    }

    //En lytter som skriver ut valget ukedagen

    public void behandleValg() {
        //leser hvilken dag det ble klikket på
        String valg = liste.getValue();
        //Skriver ut i konsolet
        System.out.println("Du valgte " + valg);
    }

    public static void main(String[] args) {
        launch();
    }
}