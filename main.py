import sys
import os

import math
import shutil
from PyQt5 import QtWidgets, QtCore, Qt, QtGui, QtPrintSupport
from PIL import Image
from PyQt5.QtWidgets import QMessageBox
from GUI import mainwindow, newitca, redactionitca, pic_dialog, printitca
import fnmatch
import yaml
import pdfrw

from datetime import datetime

DIRECTORY_PATH = os.getcwd()
FOLDER_ITCA = DIRECTORY_PATH + "//itca"
FOLDER_PIC = DIRECTORY_PATH + "//GUI//pic"
FOLDER_PIC_TEMP = DIRECTORY_PATH + "//GUI//pic_temp"
ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'


def write_fillable_pdf(input_pdf_path, output_pdf_path, data_dict):
    template_pdf = pdfrw.PdfReader(input_pdf_path)
    template_pdf.Root.AcroForm.update(pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))
    annotations = template_pdf.pages[0][ANNOT_KEY]
    for annotation in annotations:
        if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
            if annotation[ANNOT_FIELD_KEY]:
                key = annotation[ANNOT_FIELD_KEY][1:-1]
                if key in data_dict.keys():
                    annotation.update(
                        pdfrw.PdfDict(V='{}'.format(data_dict[key]))
                    )
    pdfrw.PdfWriter().write(output_pdf_path, template_pdf)


def get_data_from_yaml(filename):
    data = dict()
    try:
        with open(filename, encoding='utf-8') as stream:
            data = yaml.safe_load(stream)
    except Exception as e:
        print(e)
    return data


class NewItca(QtWidgets.QDialog):
    def __init__(self, parent=None):
        # First, call the higher constructor in the hierarchy (QtWidgets.QMainWindow)
        super(NewItca, self).__init__()
        self.ui = newitca.Ui_Dialog()  # call constructor of the MainWindow file
        self.ui.setupUi(self)  # setup all items of the windows in their default values
        self.adjustSize()
        self.dict_data = {}
        self.add_menu()
        self.data_menu = {}

    def _set_widget(self, key: str, values=None, combobox=None):
        if values is None:
            values = []
        if key == "list":
            menu = QtWidgets.QComboBox()
            menu.addItem("")
            for value in values:
                menu.addItem(str(value))
        elif key == "line":
            menu = QtWidgets.QLineEdit()
        elif key == "date":
            menu = QtWidgets.QDateEdit(calendarPopup=True)
            menu.setDateTime(QtCore.QDateTime.currentDateTime())
        elif key == "button":
            menu = QtWidgets.QPushButton(str(values))
            menu.clicked.connect(lambda: self._file_save(combobox))
        else:
            menu = QtWidgets.QLabel(key)
            menu.setAlignment(Qt.Qt.AlignCenter)
        return menu

    @staticmethod
    def _get_pic():
        if os.path.exists(FOLDER_PIC):
            return os.listdir(FOLDER_PIC)
        return []

    def _file_save(self, combobox):
        src = QtWidgets.QFileDialog.getOpenFileName(self, "Picture selection", "./", "Image Files(*.png *.jpg *.bmp)")
        if not src[0]:
            return
        basename = os.path.basename(src[0])
        if basename in os.listdir(FOLDER_PIC):
            ret = QMessageBox.question(self, 'Warning', "Il existe déjà une image du même nom, voulez-vous l'écraser?",
                                       QMessageBox.Yes | QMessageBox.No)
            if ret == QMessageBox.No:
                i = 0
                while basename in os.listdir(FOLDER_PIC):
                    filename, file_extension = os.path.splitext(basename)
                    filename = filename if i == 0 else filename[:-2]
                    basename = filename + f"_{i}" + file_extension
                    i += 1
        name = FOLDER_PIC + "//" + basename
        shutil.copyfile(src[0], name)
        img = Image.open(src[0])
        img.thumbnail((600, 400))
        img.save(name, img.format)

        if isinstance(combobox, QtWidgets.QComboBox):
            combobox.clear()
            new_value = ""
            combobox.addItem(new_value)
            for value in self._get_pic():
                combobox.addItem(str(value))
                if value in basename:
                    new_value = value
            combobox.setCurrentText(new_value)

    def add_menu(self):
        if not os.path.isfile("GUI/menu.yaml"):
            return
        data_menu = get_data_from_yaml("GUI/menu.yaml")
        i, j = 0, 1
        for key, values in data_menu.items():
            w1, w2 = None, None
            label = self._set_widget(key)
            self.ui.gridLayout.addWidget(label, j, i)
            if isinstance(values, list):
                widget = self._set_widget("list", values)
            elif isinstance(values, dict):
                widget = QtWidgets.QHBoxLayout()
                for k, v in values.items():
                    w2 = self._set_widget(k)
                    if v:
                        w1 = self._set_widget(v)
                        widget.addWidget(w1)
                        widget.addWidget(w2)
                    else:
                        widget = w2

            elif str(values) == "line":
                widget = self._set_widget("line")
            elif str(values) == "date":
                widget = self._set_widget("date")
            elif str(values) == "photo":
                widget = QtWidgets.QHBoxLayout()
                w1 = self._set_widget("list", self._get_pic())
                w2 = self._set_widget("button", "add", combobox=w1)
                widget.addWidget(w1, 2)
                widget.addWidget(w2, 1)
            else:
                widget = self._set_widget("None")
            if w1 and w2:
                self.dict_data.update({key: {widget: [w1, w2]}})
            else:
                self.dict_data.update({key: {widget: None}})
            if isinstance(widget, QtWidgets.QHBoxLayout):
                self.ui.gridLayout.addLayout(widget, j + 1, i)
            else:
                self.ui.gridLayout.addWidget(widget, j + 1, i)
            i += 1
            if i > 1:
                i = 0
                j += 2

    def get_data(self):
        data_return = dict()
        for key, value in self.dict_data.items():
            sub_key = list(value.keys())[0]
            sub_value = value[sub_key]
            if not sub_value:
                sub_value = [sub_key]
            v = ""
            for sub_sub_value in sub_value:
                if isinstance(sub_sub_value, (QtWidgets.QLabel, QtWidgets.QDateEdit, QtWidgets.QLineEdit)):
                    v += sub_sub_value.text()
                elif isinstance(sub_sub_value, QtWidgets.QComboBox):
                    v += str(sub_sub_value.currentText())
                elif isinstance(sub_sub_value, QtWidgets.QPushButton):
                    pass
                else:
                    v = None
            data_return.update({key: v})
        self.data_menu = data_return
        self.accept()

    def get_data_menu(self):
        self.show()
        if self.exec_():
            return self.data_menu


class RedactionItca(QtWidgets.QDialog):
    def __init__(self, parent=None):
        # First, call the higher constructor in the hierarchy (QtWidgets.QMainWindow)
        super(RedactionItca, self).__init__()
        self.ui = redactionitca.Ui_Dialog()  # call constructor of the MainWindow file
        self.ui.setupUi(self)  # setup all items of the windows in their default values
        self.adjustSize()
        self.data = dict()
        self.page = 1
        self.redact_max = 4
        for _ in range(2):
            self.add_redaction_widget()

    def get_data_menu(self):
        self.show()
        if self.exec_():
            self.clear_layout(self.ui.verticalLayout_page)
            return self.data

    def clear_layout(self, layout, page=None):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                if isinstance(child.widget(), QtWidgets.QLabel):
                    try:
                        int(child.widget().text())
                        page = child.widget().text()
                    except ValueError:
                        pass
                elif isinstance(child.widget(), QtWidgets.QPlainTextEdit) and page:
                    if int(page) in self.data:
                        self.data[int(page)].update({"text": child.widget().toPlainText()})
                child.widget().deleteLater()
            elif child.layout():
                page = self.clear_layout(child.layout(), page)
        return page

    def add_redaction_widget(self):
        name = len(self.data) + 1
        self.data.update({name: {}})
        if (name - 1) / self.page == self.redact_max:
            self.next_page()
        else:
            self.add_layout(name)

    def add_layout(self, name, text="", photo=0):
        layout_v = QtWidgets.QVBoxLayout()
        layout_h = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel(f"{name}")
        label.setMinimumWidth(50)
        label.setStyleSheet("font: bold 14px;")
        verticalSpacer = QtWidgets.QSpacerItem(500, 40, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        label_pic = QtWidgets.QLabel(f"Photo(s): {photo}")
        button = QtWidgets.QPushButton("add pictures")
        button.clicked.connect(lambda: self.picture(name, label_pic))
        del_button = QtWidgets.QPushButton("X")
        del_button.clicked.connect(lambda: self.del_redact(name))
        for i in [label, label_pic, button, del_button, verticalSpacer]:
            if isinstance(i, QtWidgets.QSpacerItem):
                layout_h.addItem(i)
            else:
                layout_h.addWidget(i)
        plain_text = QtWidgets.QPlainTextEdit()
        plain_text.setPlainText(text)
        layout_v.addLayout(layout_h)
        layout_v.addWidget(plain_text)
        self.ui.verticalLayout_page.addLayout(layout_v)

    def del_redact(self, redact):
        if len(self.data) == 1:
            return
        self.data.pop(int(redact))
        i, data = 1, dict()
        for value in self.data.values():
            data.update({i: value})
            i += 1
        self.data = data
        self.add_widget_page()

    def picture(self, name, label):
        pic = self.data[int(name)].setdefault("pic", [])
        manage_pic = PicItca(name, pic)
        manage_pic.show()
        if manage_pic.exec_():
            self.data[int(name)].update({"pic": manage_pic.pic})
        label.setText(f"Photo(s): {len(self.data[int(name)]['pic'])}")

    def set_page(self):
        redact = len(self.data)
        nbr_pages = math.floor(redact / (self.redact_max + 1)) + 1
        self.ui.pushButton_previous.setEnabled(self.page > 1)
        self.ui.pushButton_previous.setText(f"< {self.page - 1}")
        self.ui.pushButton_next.setEnabled(nbr_pages > self.page)
        self.ui.pushButton_next.setText(f"{self.page + 1} >")

    def add_widget_page(self):
        start = (self.page - 1) * self.redact_max
        if start + 1 > len(self.data):
            self.previous_page()
        else:
            self.set_page()
            self.clear_layout(self.ui.verticalLayout_page)
            for i in range(start + 1, start + 5):
                if i not in self.data:
                    break
                self.add_layout(i, self.data[i].get("text", ""), len(self.data[i].get("pic", "")))

    def next_page(self):
        self.page += 1
        self.add_widget_page()

    def previous_page(self):
        self.page -= 1
        self.add_widget_page()


class PicItca(QtWidgets.QDialog):
    def __init__(self, name=None, list_pic=None):
        # First, call the higher constructor in the hierarchy (QtWidgets.QMainWindow)
        super(PicItca, self).__init__()
        if list_pic is None:
            list_pic = []
        self.ui = pic_dialog.Ui_Dialog()  # call constructor of the MainWindow file
        self.ui.setupUi(self)  # setup all items of the windows in their default values
        self.adjustSize()
        if name:
            self.ui.labelname.setText(f"Redact {name}")
            self.ui.labelname.setStyleSheet("font: bold 14px;")
        self.pic = list_pic
        self.add_pic_list(list_pic)

    def add_pic_list(self, items):
        for item in items:
            self.ui.listWidget.addItem(str(item))
            item = self.ui.listWidget.item(self.ui.listWidget.count() - 1)
            item.setFlags(Qt.Qt.ItemIsUserCheckable | Qt.Qt.ItemIsEnabled)
            item.setCheckState(Qt.Qt.Unchecked)

    def show_selected(self):
        for i in range(self.ui.listWidget.count()):
            if self.ui.listWidget.item(i).checkState():
                item = self.ui.listWidget.item(i).text()
                img = Image.open(item)
                img.show()

    def add_picture(self):
        path = QtWidgets.QFileDialog.getOpenFileNames(self, "Picture selection", "./",
                                                      "Image Files(*.png *.jpg *.bmp)")[0]
        if not path:
            return
        for file in path:
            if file in self.pic:
                QMessageBox.question(self, 'Warning', f"L'image {file} est déjà séléctionnée")
                continue
            basename = os.path.basename(file)
            name = FOLDER_PIC_TEMP + "//" + basename
            shutil.copyfile(file, name)
            img = Image.open(file)
            img.thumbnail((400, 400))
            img.save(name, img.format)
            self.add_pic_list([basename])
            self.pic.append(basename)

    def delete_selected(self):
        for i in range(self.ui.listWidget.count()):
            if self.ui.listWidget.item(i).checkState():
                self.pic.remove(self.ui.listWidget.item(i).text())
        self.ui.listWidget.clear()
        self.add_pic_list(self.pic)


class PrintItca(QtWidgets.QDialog):
    def __init__(self, data=None):
        # First, call the higher constructor in the hierarchy (QtWidgets.QMainWindow)
        super(PrintItca, self).__init__()
        if data is None:
            data = {}
        self.ui = printitca.Ui_Dialog()  # call constructor of the MainWindow file
        self.ui.setupUi(self)  # setup all items of the windows in their default values
        self.adjustSize()
        self.ui.pushButton_itca.clicked.connect(self.save_itca)
        self.ui.pushButton_pdf.clicked.connect(self.save_pdf)

        self.data_correlation = {"NOM DU SERVICE": self.ui.label_moms, "N° ITCA": self.ui.label_itca_number,
                                 "EMETTEUR": self.ui.label_emetteur, "QUALITE": self.ui.label_qualite,
                                 "DATE": self.ui.label_visa, "TYPE D'INTERVENTION": self.ui.label_intervention,
                                 "REF DOC": self.ui.label_ref_doc, "ETAPE": self.ui.label_etape,
                                 "MOT": self.ui.label_mot, "NOM DU LRU": self.ui.label_lru,
                                 "POSITION": self.ui.label_position_mot, "N° SUPPORT": self.ui.label_av}
        self.add_data(data)
        self.data = data

    def add_data(self, data):
        for key, value in self.data_correlation.items():
            if data.get(key):
                if key == "NOM DU LRU":
                    pixmap = QtGui.QPixmap(FOLDER_PIC + "//" + data[key])
                    self.ui.label_pixmap.setPixmap(pixmap)
                value.setText(str(data[key]))
        self.add_redact(data)

    def add_redact(self, data):
        scroll = QtWidgets.QScrollArea()
        layout_v = QtWidgets.QVBoxLayout()
        for i in range(len(data)):
            if i not in data:
                continue
            layout_v.addLayout(self.add_layout(i, data[i].get("text"), data[i].get("pic")))
        widget = QtWidgets.QWidget()
        widget.setLayout(layout_v)
        scroll.setWidgetResizable(True)
        scroll.setWidget(widget)
        self.ui.verticalLayout_data.addWidget(scroll)

    def add_layout(self, name, text="", photo=None):
        if not photo:
            photo = []
        layout_v = QtWidgets.QVBoxLayout()
        label = QtWidgets.QLabel(f"{name}")
        label.setMinimumWidth(50)
        label.setStyleSheet("font: bold 14px;")
        plain_text = QtWidgets.QPlainTextEdit()
        plain_text.setPlainText(text)
        plain_text.setEnabled(False)
        layout_v.addWidget(label)
        layout_v.addWidget(plain_text)
        layout_g = QtWidgets.QGridLayout()
        x, y = 0, 0
        for i in photo:
            if x >= 3:
                x = 0
                y += 1
            file = FOLDER_PIC_TEMP + "//" + i
            label_pixmap = QtWidgets.QLabel("")
            pixmap = QtGui.QPixmap(file)
            label_pixmap.setPixmap(pixmap)
            # label_pixmap.setMaximumSize(200, 200)
            layout_g.addWidget(label_pixmap, y, x)
            x += 1
        layout_v.addLayout(layout_g)
        return layout_v

    def save_itca(self):
        name = f"ITCA{datetime.now().strftime('%y%m%d-%H%M')}"
        while True:
            text, ok = QtWidgets.QInputDialog.getText(self, 'Name of the ITCA', 'Name of the ITCA to save:', text=name)
            path = FOLDER_ITCA + "//" + text + ".itca"
            if os.path.exists(path):
                QMessageBox.warning(self, 'Warning', f"Le nom {text} existe déjà.")
            else:
                break
        if ok:
            try:
                with open(path, 'w') as file:
                    yaml.safe_dump(self.data, file, default_flow_style=True)
            except EOFError as e:
                print(e)

    def save_pdf(self):
        src = QtWidgets.QFileDialog.getSaveFileName(self, "ITCA save", "./", "Image Files(*.pdf)")
        if not src[0]:
            return
        nom_lru = self.data.get("NOM DU LRU", "")
        nom_lru2 = nom_lru.split(".")
        self.data.update({"TITRE": "ITCA", "NOM DU LRU": nom_lru2[0], "IMAGE LRU": FOLDER_PIC + "\\" + nom_lru,
                          "PAGE": "PAGE N°1"})
        write_fillable_pdf("GUI\\cartouche-1-form.pdf", src[0], self.data)


class MyWindow(QtWidgets.QMainWindow):
    """
    this is the main class. The GUI control the action of the script. The parameters and the action is defined by the
    GUI.

    .. seealso::
        For more details for the variables and functions see the source code

    .. warnings also::
        No specific warning.

    Here below is the results of the functions docstring:

    """

    def __init__(self):
        # First, call the higher constructor in the hierarchy (QtWidgets.QMainWindow)
        super(MyWindow, self).__init__()
        self.ui = mainwindow.Ui_MainWindow()  # call constructor of the MainWindow file
        self.ui.setupUi(self)  # setup all items of the windows in their default values
        self.show()
        self.adjustSize()
        self.element = []
        self.get_itca_config()
        self.check_thread_timer = QtCore.QTimer()
        self.check_thread_timer.setInterval(1000)
        self.check_thread_timer.timeout.connect(self.get_itca_config)
        self.check_thread_timer.start()

    def get_itca_config(self):
        # self.ui.listWidget.clear()
        if os.path.exists(FOLDER_ITCA):
            items_text_list = [str(self.ui.listWidget.item(i).text()) for i in range(self.ui.listWidget.count())]
            for element in os.listdir(FOLDER_ITCA):
                # to have the files csv and format
                if fnmatch.fnmatch(element, f"*.itca") and element not in items_text_list:
                    self.ui.listWidget.addItem(element)

    def launch(self):

        selected_item = self.ui.listWidget.selectedItems()[0].text() if self.ui.listWidget.selectedItems() else []

        if not selected_item:
            dia = NewItca()
            data_menu = dia.get_data_menu()
            if not data_menu:
                print("canceled")
                return
            dia2 = RedactionItca()
            data_menu2 = dia2.get_data_menu()
            if not data_menu2:
                print("canceled")
                return

            data_menu.update(data_menu2)
        else:
            data_menu = get_data_from_yaml(FOLDER_ITCA + "//" + selected_item)

        print_itca = PrintItca(data_menu)
        print_itca.show()
        print_itca.exec_()


def global_path():
    print("My current directory is : " + DIRECTORY_PATH)
    folder_name = os.path.basename(DIRECTORY_PATH)
    print("My directory name is : " + folder_name)
    os.mkdir(FOLDER_ITCA) if not os.path.isdir(FOLDER_ITCA) else print(f"{FOLDER_ITCA} exist already")
    os.mkdir(FOLDER_PIC) if not os.path.isdir(FOLDER_PIC) else print(f"{FOLDER_PIC} exist already")
    os.mkdir(FOLDER_PIC_TEMP) if not os.path.isdir(FOLDER_PIC_TEMP) else print(f"{FOLDER_PIC_TEMP} exist already")


if __name__ == "__main__":
    global_path()
    try:
        app_gui = QtWidgets.QApplication(sys.argv)
        app_gui.setStyle('Fusion')
        print(QtWidgets.QStyleFactory.keys())
        window = MyWindow()

        sys.exit(app_gui.exec_())
        # status = app_gui.exec_()
    except Exception as exc:
        print(exc)
        with open("error.log", "w") as f:
            f.write(str(exc))
        os._exit(0)
