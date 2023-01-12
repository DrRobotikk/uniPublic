module com.example.demoradioknapper {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.demoradioknapper to javafx.fxml;
    exports com.example.demoradioknapper;
}