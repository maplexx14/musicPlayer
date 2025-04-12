import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class YandexMusicUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.playing = False
        self.setWindowTitle("Yandex Music Clone")
        self.setGeometry(100, 100, 1280, 720)
        self.setupUI()
        self.applyCustomStyles()


    def setupUI(self):
        # Главный контейнер
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Верхняя панель
        self.createTopBar(main_layout)

        # Основной контент
        content_widget = QWidget()
        content_layout = QHBoxLayout(content_widget)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)

        # Боковая панель
        self.createSidebar(content_layout)

        # Основная область
        self.createMainContent(content_layout)

        main_layout.addWidget(content_widget)

        # Нижний плеер
        self.createPlayerBar(main_layout)

    def createTopBar(self, parent):
        top_bar = QWidget()
        top_bar.setFixedHeight(56)
        top_bar.setStyleSheet("background: #0F0F0F;")
        top_layout = QHBoxLayout(top_bar)
        top_layout.setContentsMargins(16, 0, 16, 0)
        top_layout.setSpacing(24)

        # Тема
        theme_btn = QPushButton()
        theme_btn.setIcon(QIcon("pics/icons8-sun(1).svg"))
        theme_btn.setIconSize(QSize(32, 32))
        theme_btn.setCursor(Qt.PointingHandCursor)
        theme_btn.setStyleSheet("""
            QPushButton{
                background: transparent;
                border: none;
                stroke: #FFF;
                fill: #FFF;
                padding: 8px;
            }
        """)
        # Профиль
        profile_btn = QPushButton()
        profile_btn.setIcon(QIcon(":icons/profile.png"))
        profile_btn.setIconSize(QSize(32, 32))
        profile_btn.setCursor(Qt.PointingHandCursor)

        # Поисковая строка
        search = QLineEdit()
        search.setPlaceholderText("Поиск")
        search.setFixedWidth(600)
        search.setAlignment(Qt.AlignLeft)
        search.setStyleSheet("""
            QLineEdit {
                background: #282828;
                border: 1px solid #404040;
                border-radius: 10px;
                padding: 8px;
                color: #FFF;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 1px solid #FFF;
            }
        """)
        search.addAction(QIcon(":icons/search.png"), QLineEdit.LeadingPosition)

        top_layout.addWidget(profile_btn)
        top_layout.addStretch()
        top_layout.addWidget(search)

        top_layout.addStretch()
        top_layout.addWidget(theme_btn)
        parent.addWidget(top_bar)

    def createSidebar(self, parent_layout):
        sidebar = QWidget()
        sidebar.setFixedWidth(264)
        sidebar.setStyleSheet("background: #000000;")
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(8, 16, 8, 16)
        sidebar_layout.setSpacing(8)

        # Основные разделы
        sections = [
            ("Главная", "library"),
            ("Создать плейлист", "add_playlist"),
            ("Любимые треки", "favorites")
        ]

        for text, icon in sections:
            btn = QPushButton(text)
            btn.setIcon(QIcon(f":icons/{icon}.png"))
            btn.setStyleSheet("""
                QPushButton {
                    text-align: left;
                    padding: 12px 16px;
                    font-size: 14px;
                    color: #B3B3B3;
                    border-radius: 4px;
                }
                QPushButton:hover {
                    color: #FFF;
                    background: #282828;
                }
            """)
            sidebar_layout.addWidget(btn)

        # Разделитель
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setStyleSheet("border-color: #282828;")
        sidebar_layout.addWidget(separator)

        # Плейлисты
        sidebar_layout.addWidget(QLabel("Плейлисты", styleSheet="color: #B3B3B3; padding: 8px 16px;"))
        playlists = QListWidget()
        playlists.setStyleSheet("""
            QListWidget {
                background: transparent;
                border: none;
                color: #B3B3B3;
                font-size: 14px;
            }
            QListWidget::item {
                padding: 12px 16px;
                border-radius: 4px;
            }
            QListWidget::item:hover {
                background: #282828;
                color: #FFF;
            }
        """)
        playlists.addItems(["Ваш микс дня"])
        sidebar_layout.addWidget(playlists)

        parent_layout.addWidget(sidebar)

    def toggle_cat(self):
        self.playing = not self.playing
        if self.playing:
            print("Starting animation")
            self.label.setMovie(self.gif)
            self.gif.start()
            self.btn.setIcon(QIcon("pics/pause.png"))
        else:
            print("Pausing animation")
            self.gif.jumpToFrame(0)  # Возвращаем к первому кадру
            self.gif.setPaused(True)
            self.label.setPixmap(self.gif.currentPixmap())
            self.btn.setIcon(QIcon("pics/play.png"))
        # Обновляем изображение


    def createMainContent(self, parent_layout):
        content_widget = QWidget()
        layout = QVBoxLayout(content_widget)
        layout.setAlignment(Qt.AlignCenter)
        # Создаем объекты как атрибуты класса
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)

        # Инициализируем анимацию
        self.gif = QMovie("pics/oia-uia.gif")
        self.gif.setCacheMode(QMovie.CacheAll)
        self.gif.setSpeed(100)
        self.gif.start()
        self.gif.setPaused(True)

        # Создаем кнопку
        self.btn = QPushButton('')
        self.btn.setIconSize(QSize(50, 50))
        self.btn.setIcon(QIcon("pics/play.png"))
        self.btn.setFixedSize(200, 200)
        self.btn.clicked.connect(self.toggle_cat)
        self.btn.setStyleSheet("""
            QPushButton {
                border: none;
                border-radius: 50%;
                background: #282828;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            QPushButton:hover {
                background: #404040;
            }
        }""")
        # Начальное состояние
        self.playing = False
        self.gif.jumpToFrame(0)

        self.label.setPixmap(self.gif.currentPixmap())

        layout.addWidget(self.label)
        layout.addWidget(self.btn)

        parent_layout.addWidget(content_widget)
    def createPlayerBar(self, parent):
        player = QWidget()
        player.setFixedHeight(100)
        player.setStyleSheet("background: #000;")
        layout = QHBoxLayout(player)
        layout.setContentsMargins(16, 8, 16, 8)
        layout.setSpacing(32)

        # Текущий трек
        track_info = QWidget()
        track_layout = QHBoxLayout(track_info)
        track_layout.setSpacing(12)

        cover = QLabel()
        cover.setPixmap(QPixmap("pics/icons8-sun(1).svg").scaled(56, 56, Qt.KeepAspectRatio))


        text_info = QWidget()

        text_layout = QVBoxLayout(text_info)
        title = QLabel("Название трека")
        title.setStyleSheet("color: #FFF; font-size: 14px;")
        artist = QLabel("Исполнитель")
        artist.setStyleSheet("color: #B3B3B3; font-size: 12px;")
        text_layout.addWidget(title)
        text_layout.addWidget(artist)

        track_layout.addWidget(cover)
        track_layout.addWidget(text_info)
        layout.addWidget(track_info)

        # Управление воспроизведением
        controls = QWidget()
        ctrl_layout = QVBoxLayout(controls)
        ctrl_layout.setContentsMargins(0, 0, 0, 0)

        # Кнопки управления
        btn_row = QWidget()

        btn_layout = QHBoxLayout(btn_row)

        btn_row.setFixedSize(200, 50)


        prev_btn = QPushButton()
        prev_btn.setIcon(QIcon("pics/icons8-previous-64.png"))
        prev_btn.setIconSize(QSize(32, 32))
        prev_btn.setCursor(Qt.PointingHandCursor)
        prev_btn.setStyleSheet("background: transparent; border-radius: 4px;")

        play_btn = QPushButton()
        play_btn.setIcon(QIcon("pics/icons8-play-50.png"))
        play_btn.setIconSize(QSize(32, 32))
        play_btn.setCursor(Qt.PointingHandCursor)
        play_btn.setStyleSheet("background: transparent; border-radius: 4px;")

        next_btn = QPushButton()
        next_btn.setIcon(QIcon("pics/icons8-next-64.png"))
        next_btn.setIconSize(QSize(32, 32))
        next_btn.setCursor(Qt.PointingHandCursor)
        next_btn.setStyleSheet("background: transparent; border-radius: 4px;")

        btn_layout.addWidget(prev_btn)
        btn_layout.addWidget(play_btn)
        btn_layout.addWidget(next_btn)
        ctrl_layout.addWidget(btn_row)
        # Прогресс-бар
        progress = QSlider(Qt.Horizontal)
        progress.setRange(0, 100)
        progress.setValue(35)
        progress.setStyleSheet("""
            QSlider {
                padding: 0;
            }
            QSlider::groove:horizontal {
                height: 3px;
                background: #404040;
                border-radius: 4px;
                
            }
            QSlider::handle:horizontal:hover {
                background: #FFF;
            }
            QSlider::handle:horizontal {
                background: transparent;
                width: 12px;
                margin: -4px 0;
                border-radius: 6px;
            }
            QSlider::sub-page:horizontal {
                background: #1ED760;
            }
        """)

        time_labels = QWidget()
        time_layout = QHBoxLayout(time_labels)



        ctrl_layout.addWidget(btn_row, alignment=Qt.AlignHCenter)
        ctrl_layout.addWidget(progress)
        ctrl_layout.addWidget(time_labels)
        layout.addWidget(controls, stretch=2)

        # Громкость
        volume = QWidget()
        vol_layout = QHBoxLayout(volume)
        vol_layout.setSpacing(8)
        vol_btn = self.createIconButton(QStyle.SP_MediaVolume, 24, "#B3B3B3")
        vol_slider = QSlider(Qt.Horizontal)
        vol_slider.setRange(0, 100)
        vol_slider.setValue(75)
        vol_slider.setFixedWidth(100)
        vol_slider.setStyleSheet(progress.styleSheet())
        vol_layout.addWidget(vol_btn)
        vol_layout.addWidget(vol_slider)
        layout.addWidget(volume)

        parent.addWidget(player)

    def createIconButton(self, icon, size, color):
        btn = QPushButton()
        btn.setIcon(self.style().standardIcon(icon))
        btn.setIconSize(QSize(size, size))
        btn.setCursor(Qt.PointingHandCursor)
        btn.setStyleSheet(f"""
            QPushButton {{
                background: transparent;
                border: none;
                color: {color};
            }}
            QPushButton:hover {{
                opacity: 0.8;
            }}
        """)
        return btn

    def applyCustomStyles(self):
        self.setStyleSheet("""
            QWidget {
                background: #181818;
                color: #FFF;
                font-family: 'Arial';
            }
            QScrollBar:vertical {
                background: #181818;
                width: 6px;
            }
            QScrollBar::handle:vertical {
                background: #404040;
                min-height: 20px;
                border-radius: 3px;
            }
            QScrollBar::add-line:vertical, 
            QScrollBar::sub-line:vertical {
                height: 0;
            }
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("fusion")

    window = YandexMusicUI()
    window.show()
    sys.exit(app.exec_())