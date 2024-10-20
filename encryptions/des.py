class Des:
    def __init__(self, main_window):
        self.main_window = main_window

        self.main_window.des_ecb_button.clicked.connect(lambda: self.switch_des_page(0))
        self.main_window.des_cbc_button.clicked.connect(lambda: self.switch_des_page(1))
        self.main_window.des_ofb_button.clicked.connect(lambda: self.switch_des_page(2))
        self.main_window.des_cfb_button.clicked.connect(lambda: self.switch_des_page(3))


    def switch_des_page(self, index):
        self.main_window.stackedWidget_des.setCurrentIndex(index)
