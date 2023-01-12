package robin.tangen.modul;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.layout.BorderPane;
import javafx.stage.Stage;



public class demo extends Application {

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) {
        try{
            BorderPane root = new BorderPane();
            Scene scene = new Scene(root,400,400);
            Label hilsen = new Label();
            hilsen.setText("Hei");
            root.setCenter(hilsen);
            primaryStage.setScene(scene);
            primaryStage.show();

        }
        catch (Exception e){
            e.printStackTrace();
        }

    }
}
