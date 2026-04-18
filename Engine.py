from sqlalchemy import create_engine, Column, String, Integer, Boolean, Numeric, and_
from sqlalchemy.orm import sessionmaker, declarative_base
from map import Map
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from ui import Ui_MainWindow
from PySide6.QtGui import QIcon
import os

def resource_path(relative_path):
    """ Получает абсолютный путь к ресурсам, работает для разработки и для PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

Base = declarative_base()

class Printer(Base):
  __tablename__ = 'Printers'

  printer_id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
  model = Column(String(100), nullable=False)
  type = Column(String(50), nullable=False)
  color_printing = Column(Boolean, nullable=False)
  resolution = Column(Integer, nullable=False)
  price = Column(Numeric(10, 2))
  connection_type = Column(String(50))
  print_speed = Column(Integer)
  id_manufacturer = Column(Integer, nullable=False)

db_path = resource_path("mrPrinter.db")
engine = create_engine(f'sqlite:///{db_path}')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


class MrPrinter(QMainWindow):
    def __init__(self):
        super(MrPrinter, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        icon_path = resource_path(os.path.join("image", "ICON.ico"))
        self.setWindowIcon(QIcon(icon_path))

        self.submit_button = QPushButton("Подтвердить")
        self.ui.pushButton.clicked.connect(self.search)



    def search(self):

        ans_error = "Мы что-то напутали давайте еще раз"


        type_map = {
            "Профессиональное использование": "P",
            "Офисное использование": "O",
            "Домашнее использование": "H"
        }

        boolean_mapping = {
            "Да": "1",
            "Нет": "0"
        }


        def build_filter(criteria):
            filters = []
            for key, value in criteria.items():
                if isinstance(value, tuple):
                    operator, val = value
                    column = getattr(Printer, key)
                    if operator == ">":
                        filters.append(column > val)
                    elif operator == "<":
                        filters.append(column < val)
                    elif operator == ">=":
                        filters.append(column >= val)
                    elif operator == "<=":
                        filters.append(column <= val)
                    elif operator == "=":
                        filters.append(column == val)
                else:
                    column = getattr(Printer, key)
                    filters.append(column == value)
            return filters




        # print (get_printer_by_id(2))
        resolution_id = ""
        resolution_id += type_map[self.ui.comboBox.currentText()]
        resolution_id += boolean_mapping[self.ui.comboBox_2.currentText()]
        resolution_id += boolean_mapping[self.ui.comboBox_3.currentText()]
        resolution_id += boolean_mapping[self.ui.comboBox_7.currentText()]
        print (resolution_id)
        mapping = Map.get(resolution_id)

        # здесь передача фильтра
        if mapping:
            filter_crit = build_filter(mapping)
            printers = session.query(Printer).filter(and_(*filter_crit)).all()

            if printers:
                self.ui.textEdit.setText("Принтеры, которые подходят под ваши запросы:\n")

                for i , printer in enumerate (printers,start=1):
                    self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f'{str(i)} ) {printer.model};\n')
            else :
                self.ui.textEdit.setText("Принтер под ваш запрос не найден")
                print("Принтер под ваш запрос не найден")
        else:  print("Ошибка. Неверный код решения, обратитесь к разработчику")


if __name__ =="__main__":
  app = QApplication(sys.argv)

  window = MrPrinter()
  window.show()
  sys.exit(app.exec())
