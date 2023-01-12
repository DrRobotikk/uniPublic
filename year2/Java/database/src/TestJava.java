import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.ResultSet;
import java.sql.PreparedStatement;
public class TestJava {


        private final String url = "jdbc:postgresql://localhost/dvdrental";
        private final String user = "postgres";
        private final String password = "Intensifique99!";

        public Connection connect() throws SQLException{
            return DriverManager.getConnection(url,user,password);
        }
    public TestJava(){

    }
        public static void main(String[] args) {
            TestJava t = new TestJava();
            t.selectData();



        }

        public void selectData(){
            try {
                Connection conn = connect();
                System.out.println("Connected");
                String SQL = "SELECT category_id,name FROM category";
                PreparedStatement pstmt = conn.prepareStatement(SQL);
                ResultSet rs = pstmt.executeQuery();
                while (rs.next()){
                    System.out.println(rs.getString("category_id")+"\t"+rs.getString("name"));
                }

            } catch (SQLException e){
                System.out.println(e.getMessage());
            }
        }
    }



