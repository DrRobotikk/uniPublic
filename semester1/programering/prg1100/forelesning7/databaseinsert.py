# PRG1100-2022-innsetting TUI og data i cursor

import mysql.connector


mindatabase = mysql.connector.connect(
    host='localhost', port=3306, user='Lagersjefen2022', passwd='lagerpw', db='heltnydatabase')


settinn_markor = mindatabase.cursor()
markor = mindatabase.cursor()


settinn_markor.execute('INSERT INTO Vare'
                       '(VNr,Betegnelse,Pris,KatNr,Antall,Hylle)'
                       'VALUES("9999","Testvare",99.99,999,99,"T99")')

mindatabase.commit()
settinn_markor.execute("INSERT INTO Vare"
                       "(VNr,Betegnelse,Pris,KatNr,Antall,Hylle)"
                       "VALUES('8888','endaentestvare',88.88,888,88,'T88')")
mindatabase.commit()

markor.execute('SELECT * FROM Vare')

for row in markor:
    print(row)

settinn_markor.close()
markor.close()

mindatabase.close()
