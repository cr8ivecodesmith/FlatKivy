

from kivy.uix.widget import Widget
from kivy.lang import Builder

from flatapp import FlatApp


Builder.load_string('''
<RootWidget>:
    GridLayout:
        cols: 3
        pos: root.pos
        size: root.size
        padding: '5dp'
        spacing: '5dp'
        canvas.before:
            Color:
                rgb: .1,.1,.1
            Rectangle:
                pos: self.pos
                size: self.size

        FlatButton:
            text: 'button'
            theme: ('green', 'accent')

        FlatIconButton:
            text: 'icon button'
            icon: 'fa-tree'
            theme: ('green', 'accent')

        FlatToggleButton:
            text: 'toggle button 1'
            group: 'toggle'
            theme: ('green', 'accent')

        FlatToggleButton:
            text: 'toggle button 2'
            group: 'toggle'
            theme: ('green', 'accent')

        CheckBoxListItem:
            text: 'check 1'
            group: 'check'
            theme: ('green', 'accent')

        CheckBoxListItem:
            text: 'check 2'
            group: 'check'
            theme: ('green', 'accent')

        FlatCard:
            image_source: 'AstroPic1.jpg'
            text: 'the card'
            color_tuple: ('Gray', '0000')

        FlatTextInput:

        BoxLayout:
            orientation: 'vertical'
            FlatLabel:
                text: 'FlatScrollView'
                size_hint_y: None
                height: '35dp'
                theme: ('green', 'main')

            FlatScrollView:
                do_scroll_x: False

                BoxLayout:
                    orientation: 'vertical'
                    height: '400dp'
                    size_hint_y: None
                    FlatLabel:
                        text: '1'
                    FlatLabel:
                        text: '2'
                    FlatLabel:
                        text: '3'
                    FlatLabel:
                        text: '4'
                    FlatLabel:
                        text: '5'
                    FlatLabel:
                        text: '6'

        FlatButton:
            text: 'popup'
            theme: ('green', 'accent')
            on_release: popup_demo.open()
            popup_demo: popup_demo.__self__

        FlatPopup:
            id: popup_demo
            title: 'Flat Popup Demo'
            size_hint: .6,.6
            on_parent: if self.parent: self.parent.remove_widget(self)

            FlatButton:
                text: 'just a button in here'
                theme: ('green', 'main')

        FlatSlider:
            id: hor_slider
            orientation: 'horizontal'
            value: ver_slider.value

        FlatSlider:
            id: ver_slider
            orientation: 'vertical'
            value: hor_slider.value

        FlatSlider:
            value: hor_slider.value
            orientation: 'horizontal'
            disabled: True
''')


class RootWidget(Widget):
    pass


class MyFlatApp(FlatApp):
    def build(self):
        return RootWidget()

    def setup_themes(self):
        main = {
            'FlatButton': {
                'color_tuple': ('Gray', '0000'),
                'font_color_tuple': ('LightGreen', '800'),
                'style': 'Button',
                },
            'FlatLabel': {
                'style': 'Button',
                },
            }

        accent = {
            'FlatButton': {
                'color_tuple': ('LightGreen', '500'),
                'font_color_tuple': ('Gray', '1000'),
                'style': 'Button',
                },
            'FlatIconButton': {
                'color_tuple': ('LightGreen', '500'),
                'font_color_tuple': ('Gray', '1000'),
                'style': 'Button',
                'icon_color_tuple': ('Gray', '1000')
                },
            'FlatToggleButton': {
                'color_tuple': ('LightGreen', '500'),
                'font_color_tuple': ('Gray', '1000'),
                'style': 'Button',
                },
            'FlatCheckBox': {
                'color_tuple': ('Gray', '0000'),
                'check_color_tuple': ('LightGreen', '500'),
                'outline_color_tuple': ('Gray', '1000'),
                'style': 'Button',
                'check_scale': .7,
                'outline_size': '10dp',
                },
            'CheckBoxListItem': {
                'font_color_tuple': ('Gray', '0000'),
                'check_color_tuple': ('LightGreen', '500'),
                'outline_color_tuple': ('Gray', '800'),
                'style': 'Button',
                'check_scale': .7,
                'outline_size': '10dp',
                },
            }

        self.theme_manager.add_theme('green', 'main', main)
        self.theme_manager.add_theme('green', 'accent', accent)


if __name__ == '__main__':
    MyFlatApp().run()
