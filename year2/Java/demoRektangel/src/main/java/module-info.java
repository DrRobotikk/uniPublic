module com.example.demorektangel {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.demorektangel to javafx.fxml;
    exports com.example.demorektangel;
}