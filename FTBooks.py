import sqlite3
import time

from PyQt5 import QtCore, QtGui, QtWidgets




class Ui_FTBooks(object):

    def __init__(self):

        self.get_network()


    def get_network(self):

        self.network = sqlite3.connect("database.db")
        self.cursor = self.network.cursor()
        self.cursor.execute("Create Table If not exists Books(Author TEXT,Book TEXT)")
        self.network.commit()


    def Add_Book(self):

        author = self.author_name.text()
        book = self.book_name.text()

        if len(author) == 0 or len(book) == 0:
            self.book_text.setText("Please write Author and Book!")

        else:

            self.cursor.execute("Select * from Books where Author = ? and Book = ?",(author,book))
            data = self.cursor.fetchall()

            if  len(data) != 0:
                self.book_text.setText("This book has already existed!\n\n\n")

            else:

                self.cursor.execute("Insert into Books Values(?,?)",(author,book))

                self.network.commit()

                self.book_text.setText("Book is added successfully!\n\n\n")

                self.author_name.setText("")
                self.book_name.setText("")




    def Show_Books(self):

        author = self.author_filter.text()
        book = self.book_filter.text()

        if (len(author) != 0 and len(book) != 0) or (len(author) != 0 and len(book) == 0) or (len(author) == 0 and len(book) != 0):

            file = open("search.txt","w",encoding="utf-8")

            self.cursor.execute("Select * from Books where Author LIKE ? and Book LIKE ?", ("%{}%".format(author), "%{}%".format(book)))
            data = self.cursor.fetchall()

            data.sort()

            if len(data) == 0:
                file.write("There isn't any book like that!\n\n\n")

            for i in data:
                file.write("Author:        {}\nBook:           {}\n\n".format(i[0],i[1]))

            file.close()

            file = open("search.txt", "r", encoding="utf-8")

            self.book_text.setText(file.read())

            file.close()



        else:

            file = open("search.txt", "w", encoding="utf-8")

            self.cursor.execute("Select * from Books")
            data = self.cursor.fetchall()

            data.sort()

            if len(data) == 0:
                file.write("There isn't any book here!\n\n\n")

            for i in data:
                file.write("Author:        {}\nBook:           {}\n\n".format(i[0],i[1]))

            file.close()

            file = open("search.txt", "r", encoding="utf-8")

            self.book_text.setText(file.read())

            file.close()



    def setupUi(self, FTBooks):
        FTBooks.setObjectName("FTBooks")
        FTBooks.setWindowModality(QtCore.Qt.ApplicationModal)
        FTBooks.resize(1124, 826)
        palette = QtGui.QPalette()
        gradient = QtGui.QConicalGradient(1.0, 0.528, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 71, 97, 175))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        gradient = QtGui.QConicalGradient(1.0, 0.528, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 71, 97, 175))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QConicalGradient(1.0, 0.528, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 71, 97, 175))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        gradient = QtGui.QConicalGradient(1.0, 0.528, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 71, 97, 175))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        gradient = QtGui.QConicalGradient(1.0, 0.528, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 71, 97, 175))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QConicalGradient(1.0, 0.528, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 71, 97, 175))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        gradient = QtGui.QConicalGradient(1.0, 0.528, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 71, 97, 175))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        gradient = QtGui.QConicalGradient(1.0, 0.528, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 71, 97, 175))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QConicalGradient(1.0, 0.528, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 71, 97, 175))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        FTBooks.setPalette(palette)
        FTBooks.setWindowOpacity(1.0)
        FTBooks.setLayoutDirection(QtCore.Qt.LeftToRight)
        FTBooks.setStyleSheet("background-color: qconicalgradient(cx:1, cy:0.528, angle:0, stop:0 rgba(0, 71, 97, 175), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 14pt \"Comic Sans MS\";\n"
"")
        self.logo = QtWidgets.QLabel(FTBooks)
        self.logo.setGeometry(QtCore.QRect(30, 20, 431, 101))
        self.logo.setStyleSheet("font: 40pt \"Tw Cen MT Condensed Extra Bold\";\n"
"background-color: qconicalgradient(cx:0.515, cy:1, angle:0, stop:0 rgba(164, 164, 164, 255), stop:1 rgba(255, 255, 255, 255));")
        self.logo.setObjectName("logo")
        self.logo_info = QtWidgets.QLabel(FTBooks)
        self.logo_info.setGeometry(QtCore.QRect(30, 120, 431, 41))
        self.logo_info.setStyleSheet("background-color: qconicalgradient(cx:0.515, cy:1, angle:0, stop:0 rgba(164, 164, 164, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 18pt \"Tw Cen MT Condensed Extra Bold\";")
        self.logo_info.setObjectName("logo_info")
        self.add_book = QtWidgets.QPushButton(FTBooks)
        self.add_book.setGeometry(QtCore.QRect(30, 330, 221, 51))
        self.add_book.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_book.setStyleSheet("background-color: qconicalgradient(cx:0.5199, cy:1, angle:0, stop:0 rgba(133, 133, 133, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(170, 0, 0);\n"
"font: 20pt \"Tw Cen MT Condensed Extra Bold\";\n"
"")
        self.add_book.setObjectName("add_book")
        self.show_books = QtWidgets.QPushButton(FTBooks)
        self.show_books.setGeometry(QtCore.QRect(710, 20, 281, 41))
        self.show_books.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.show_books.setStyleSheet("background-color: qconicalgradient(cx:0.5199, cy:1, angle:0, stop:0 rgba(133, 133, 133, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(170, 0, 0);\n"
"font: 20pt \"Tw Cen MT Condensed Extra Bold\";\n"
"")
        self.show_books.setObjectName("show_books")
        self.quit = QtWidgets.QPushButton(FTBooks)
        self.quit.setGeometry(QtCore.QRect(1020, 20, 81, 41))
        self.quit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.quit.setStyleSheet("font: 17pt \"Tw Cen MT Condensed Extra Bold\";\n"
"background-color: qconicalgradient(cx:0.5, cy:1, angle:0, stop:0 rgba(134, 86, 86, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.quit.setObjectName("quit")
        self.author = QtWidgets.QLabel(FTBooks)
        self.author.setGeometry(QtCore.QRect(30, 400, 121, 41))
        self.author.setStyleSheet("font: 18pt \"Tw Cen MT Condensed Extra Bold\";\n"
"background-color: qconicalgradient(cx:0.504975, cy:1, angle:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(218, 218, 218);")
        self.author.setObjectName("author")
        self.book = QtWidgets.QLabel(FTBooks)
        self.book.setGeometry(QtCore.QRect(30, 450, 121, 41))
        self.book.setStyleSheet("font: 18pt \"Tw Cen MT Condensed Extra Bold\";\n"
"background-color: qconicalgradient(cx:0.504975, cy:1, angle:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(218, 218, 218);")
        self.book.setObjectName("book")
        self.author_name = QtWidgets.QLineEdit(FTBooks)
        self.author_name.setGeometry(QtCore.QRect(150, 400, 311, 41))
        self.author_name.setStyleSheet("background-color: qconicalgradient(cx:0.515, cy:1, angle:0, stop:0 rgba(164, 164, 164, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 15pt \"Tw Cen MT Condensed Extra Bold\";\n"
"")
        self.author_name.setText("")
        self.author_name.setObjectName("author_name")
        self.book_name = QtWidgets.QLineEdit(FTBooks)
        self.book_name.setGeometry(QtCore.QRect(150, 450, 311, 41))
        self.book_name.setStyleSheet("background-color: qconicalgradient(cx:0.515, cy:1, angle:0, stop:0 rgba(164, 164, 164, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 15pt \"Tw Cen MT Condensed Extra Bold\";\n"
"")
        self.book_name.setText("")
        self.book_name.setObjectName("book_name")
        self.author_filter = QtWidgets.QLineEdit(FTBooks)
        self.author_filter.setGeometry(QtCore.QRect(710, 80, 281, 31))
        self.author_filter.setStyleSheet("background-color: qconicalgradient(cx:0.515, cy:1, angle:0, stop:0 rgba(164, 164, 164, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 15pt \"Tw Cen MT Condensed Extra Bold\";\n"
"")
        self.author_filter.setText("")
        self.author_filter.setObjectName("author_filter")
        self.book_filter = QtWidgets.QLineEdit(FTBooks)
        self.book_filter.setGeometry(QtCore.QRect(710, 120, 281, 31))
        self.book_filter.setStyleSheet("background-color: qconicalgradient(cx:0.515, cy:1, angle:0, stop:0 rgba(164, 164, 164, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 15pt \"Tw Cen MT Condensed Extra Bold\";\n"
"")
        self.book_filter.setText("")
        self.book_filter.setObjectName("book_filter")
        self.book_2 = QtWidgets.QLabel(FTBooks)
        self.book_2.setGeometry(QtCore.QRect(620, 120, 91, 31))
        self.book_2.setStyleSheet("font: 16pt \"Tw Cen MT Condensed Extra Bold\";\n"
"background-color: qconicalgradient(cx:0.504975, cy:1, angle:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(218, 218, 218);")
        self.book_2.setObjectName("book_2")
        self.author_2 = QtWidgets.QLabel(FTBooks)
        self.author_2.setGeometry(QtCore.QRect(620, 80, 91, 31))
        self.author_2.setStyleSheet("font: 16pt \"Tw Cen MT Condensed Extra Bold\";\n"
"background-color: qconicalgradient(cx:0.504975, cy:1, angle:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(218, 218, 218);")
        self.author_2.setObjectName("author_2")
        self.filter = QtWidgets.QLabel(FTBooks)
        self.filter.setGeometry(QtCore.QRect(620, 20, 91, 41))
        self.filter.setStyleSheet("font: 16pt \"Tw Cen MT Condensed Extra Bold\";\n"
"background-color: qconicalgradient(cx:0.5199, cy:1, angle:0, stop:0 rgba(133, 133, 133, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.filter.setObjectName("filter")
        self.book_text = QtWidgets.QTextBrowser(FTBooks)
        self.book_text.setGeometry(QtCore.QRect(500, 180, 601, 621))
        self.book_text.setStyleSheet("font: 15pt \"Tw Cen MT Condensed Extra Bold\";\n"
"background-color: qconicalgradient(cx:0.515, cy:1, angle:0, stop:0 rgba(164, 164, 164, 255), stop:1 rgba(255, 255, 255, 255));")
        self.book_text.setText("")
        self.book_text.setObjectName("book_text")

        self.frhtas = QtWidgets.QLabel(FTBooks)
        self.frhtas.setGeometry(QtCore.QRect(30, 770, 131, 31))
        self.frhtas.setStyleSheet("font: 9pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(61, 61, 61);")
        self.frhtas.setObjectName("frhtas")


        self.retranslateUi(FTBooks)
        QtCore.QMetaObject.connectSlotsByName(FTBooks)



    def retranslateUi(self, FTBooks):
        _translate = QtCore.QCoreApplication.translate
        FTBooks.setWindowTitle(_translate("FTBooks", "FTBooks"))
        self.logo.setText(_translate("FTBooks", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#aa0000;\">FT</span><span style=\" font-weight:600;\">Books</span></p></body></html>"))
        self.logo_info.setText(_translate("FTBooks", "<html><head/><body><p align=\"center\">Read the book and save it here!</p></body></html>"))
        self.add_book.setText(_translate("FTBooks", "Add New Book"))
        self.show_books.setText(_translate("FTBooks", "Show My Books"))
        self.quit.setText(_translate("FTBooks", "Quit"))
        self.author.setText(_translate("FTBooks", "<html><head/><body><p align=\"center\">Author</p></body></html>"))
        self.book.setText(_translate("FTBooks", "<html><head/><body><p align=\"center\">Book</p></body></html>"))
        self.book_2.setText(_translate("FTBooks", "<html><head/><body><p align=\"center\">Book</p></body></html>"))
        self.author_2.setText(_translate("FTBooks", "<html><head/><body><p align=\"center\">Author</p></body></html>"))
        self.filter.setText(_translate("FTBooks", "<html><head/><body><p align=\"center\">Filters</p></body></html>"))
        self.frhtas.setText(_translate("FTBooks", "<html><head/><body><p align=\"center\">made by <span style=\" font-size:11pt; color:#ffaa00;\">frhtas</span></p></body></html>"))


        self.quit.clicked.connect(self.Quit)

        self.add_book.clicked.connect(self.Add_Book)

        self.show_books.clicked.connect(self.Show_Books)

    def Quit(self):
        QtWidgets.qApp.quit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FTBooks = QtWidgets.QWidget()
    ui = Ui_FTBooks()
    ui.setupUi(FTBooks)
    FTBooks.show()
    sys.exit(app.exec_())

