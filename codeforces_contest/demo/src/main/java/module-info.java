module java {
    requires javafx.controls;
    requires javafx.fxml;

    opens java to javafx.fxml;
    exports java;
}
