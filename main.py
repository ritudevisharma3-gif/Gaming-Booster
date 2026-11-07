import os
import platform

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

Window.clearcolor = (0.02, 0.02, 0.08, 1)


class GamingBooster(App):

    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        layout.add_widget(Label(
            text="[b]GAMING BOOSTER[/b]",
            markup=True,
            font_size=30,
            color=(0, 1, 0.7, 1)
        ))

        self.info = Label(text="WELCOME GAMER!")
        layout.add_widget(self.info)

        self.add_button(layout, "GAMING MODE",
                        self.gaming)
        self.add_button(layout, "RAM INFORMATION",
                        self.ram)
        self.add_button(layout, "DEVICE INFORMATION",
                        self.device)
        self.add_button(layout, "GAMING TIPS",
                        self.tips)

        return layout

    def add_button(self, layout, name, action):
        btn = Button(
            text=name,
            background_color=(0.3, 0, 0.6, 1),
            font_size=18
        )
        btn.bind(on_press=action)
        layout.add_widget(btn)

    def gaming(self, *args):
        self.info.text = "GAMING MODE ACTIVATED!\nEnjoy Gaming!"

    def ram(self, *args):
        try:
            data = {}
            with open("/proc/meminfo") as f:
                for line in f:
                    k, v = line.split(":")
                    data[k] = int(v.split()[0])

            total = data["MemTotal"] / 1024
            free = data["MemAvailable"] / 1024
            used = total - free

            self.info.text = (
                f"RAM USED: {used:.0f} MB\n"
                f"TOTAL RAM: {total:.0f} MB"
            )
        except Exception:
            self.info.text = "RAM information unavailable"

    def device(self, *args):
        self.info.text = (
            f"DEVICE: {platform.machine()}\n"
            f"CPU CORES: {os.cpu_count()}"
        )

    def tips(self, *args):
        self.info.text = (
            "GAMING TIPS\n"
            "Use stable Wi-Fi\n"
            "Close unused apps\n"
            "Keep phone cool"
        )


GamingBooster().run()
