module com.example.democheckbox {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.democheckbox to javafx.fxml;
    exports com.example.democheckbox;
}