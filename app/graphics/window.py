from PyQt5 import QtWidgets
from .control_panel import ControlPanel


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, canvas, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # init central widget and layout
        central_widget = QtWidgets.QWidget()
        main_layout = QtWidgets.QHBoxLayout()
        
        # init canvas
        self.canvas = canvas
        main_layout.addWidget(self.canvas.canvas.native)

        # init panel
        self.control_panel = ControlPanel(self.canvas.system)
        main_layout.addWidget(self.control_panel)
        
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.setWindowTitle(self.canvas.system.name)