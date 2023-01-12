package com.example.democheckbox;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.CheckBox;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

import java.io.IOException;

public class HelloApplication extends Application {
    CheckBox boks1,boks2,boks3;
    @Override
    public void start(Stage stage) throws IOException {

        BorderPane root = new BorderPane();
        Scene scene = new Scene(root, 320, 240);
        //Lager en Vbox
        VBox knappePanel = new VBox();
        //LeggeVboxen inn i venstre del av rotpanelet
        root.setLeft(knappePanel);
        //Oppretter avkryssningsboksene
        boks1 = new CheckBox("OBJ2000");
        boks2 = new CheckBox("OAD2000");
        boks3 = new CheckBox("OBJ2100");
        //Legger avkryssningsboksene inn i Vboxen
        knappePanel.getChildren().addAll(boks1,boks2,boks3);
        //Knytter avkryssningsboksene til lytteren
        boks1.setOnAction(e -> behandlebox1());
        boks2.setOnAction(e -> behandlebox2());
        boks3.setOnAction(e -> behandlebox3());

        stage.setTitle("Hello!");
        stage.setScene(scene);
        stage.show();

    }

    public void behandlebox1() {
        //leser hvilken dag det ble klikket på
        //Skriver ut i konsolet
        System.out.println("Du valgte OBJ2000");
    }

    public void behandlebox2() {
        //leser hvilken dag det ble klikket på
        //Skriver ut i konsolet
        System.out.println("Du valgte OAD2000");
    }

    public void behandlebox3() {
        //leser hvilken dag det ble klikket på
        //Skriver ut i konsolet
        System.out.println("Du valgte OBJ2100");
    }

    public static void main(String[] args) {
        launch();
    }
}