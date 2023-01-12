package databasa;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class TestJava {
        private final String url = "jbcd:postgresql://localhost/dvdrental";
        private final String user = "postgres";
        private final String password = "Intensifique99!";

        public Connection connect() throws SQLException{
            return DriverManager.getConnection(url,user,password);
        }
    public TestJava(){

    }
        public static void main(String[] args) {
            TestJava t = new TestJava();
            try {
                t.connect();
                System.out.println("Connected to PostgreSQL server succsesfully.");
            }
            catch (SQLException e){
                e.printStackTrace();
            }


        }
    }
