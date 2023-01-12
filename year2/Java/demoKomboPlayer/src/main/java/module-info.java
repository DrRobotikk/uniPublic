module com.example.demokomboplayer {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.demokomboplayer to javafx.fxml;
    exports com.example.demokomboplayer;
}