from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.togglebutton import ToggleButton
import requests
import kivy
from kivy.core.window import Window
from kivy.config import Config
from kivy.metrics import sp,dp

kivy.require('2.1.0')
Config.set('graphics', 'density', '1')
LabelBase.register(
    name="NanumGothic", 
    fn_regular= "assets/font/NanumGothic.ttf"
)
default_dpi = 160
device_dpi = Window.dpi if Window.dpi > 0 else default_dpi
font_size = 32 * ( default_dpi / device_dpi)
button_width = 180 * (default_dpi / device_dpi)
button_height = 130 * (default_dpi / device_dpi)

주문금액 = 0
주문_이름 = ""

temp =''

count = 1

dic_coffee_sum = {"아메리카노" : 0, "에스프레소" : 0, "드립" : 0, "더치" : 0, "라떼" : 0, "더치라떼" : 0, "바닐라라떼" : 0, "민트라떼" : 0, "카푸치노" : 0,
           "콜드브루" : 0, "카페모카" : 0, "보리커피" : 0, "플렛화이트" : 0, "꼼빠냐" : 0, "아인슈페너" : 0}

dic_coffee_cup = {"아메리카노" : 0, "에스프레소" : 0, "드립" : 0, "더치" : 0, "라떼" : 0, "더치라떼" : 0, "바닐라라떼" : 0, "민트라떼" : 0, "카푸치노" : 0,
           "콜드브루" : 0, "카페모카" : 0, "보리커피" : 0, "플렛화이트" : 0, "꼼빠냐" : 0, "아인슈페너" : 0}

dic_beverage_sum = {"베리고" : 0, "망고스무디" : 0, "아보카도바나나" : 0, "망고바나나" : 0, "패션후르츠" : 0, "레몬에이드" : 0, "복숭아바질" : 0, "초코라떼" : 0,
                    "핫초코" : 0, "자두에이드" : 0, "유자민트티" : 0, "미숫가루" : 0, "밀크티" : 0, "딸기라떼" : 0, "애플민트스무디" : 0}

dic_beverage_cup = {"베리고" : 0, "망고스무디" : 0, "아보카도바나나" : 0, "망고바나나" : 0, "패션후르츠" : 0, "레몬에이드" : 0, "복숭아바질" : 0, "초코라떼" : 0,
                    "핫초코" : 0, "자두에이드" : 0, "유자민트티" : 0, "미숫가루" : 0, "밀크티" : 0, "딸기라떼" : 0, "애플민트스무디" : 0}

dic_menu_price = {"아메리카노" : 2500, "에스프레소" : 2500, "드립" : 4000, "더치" : 3500, "라떼" : 3000, "더치라떼" : 4000, "바닐라라떼" : 3500, "민트라떼" : 4000, "카푸치노" : 3000,
           "콜드브루" : 3000, "카페모카" : 3500, "보리커피" : 2500, "플렛화이트" : 3000, "꼼빠냐" : 3500, "아인슈페너" : 4000, "베리고" : 4000, "망고스무디" : 4000, "아보카도바나나" : 3500,
           "망고바나나" : 4000, "패션후르츠" : 3500, "레몬에이드" : 3500, "복숭아바질" : 3500, "초코라떼" : 3500,
                    "핫초코" : 3500, "자두에이드" : 3500, "유자민트티" : 4000, "미숫가루" : 3500, "밀크티" : 3000, "딸기라떼" : 3500, "애플민트스무디" : 3500}



class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = FloatLayout()
        
        self.password_input = TextInput(
            hint_text="비밀번호를 입력하세요",
            font_name="NanumGothic",
            password=True,
            multiline=False,
            size_hint=(0.6, 0.1),
            font_size=(font_size + 5),
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        layout.add_widget(self.password_input)

        login_button = Button(
            text="로그인",
            font_name="NanumGothic",
            size_hint=(0.4, 0.1),
            pos_hint={"center_x": 0.5, "y": 0.3}
        )

        login_button.bind(on_press=self.verify_login)
        layout.add_widget(login_button)
        
        self.message_label = Label(
            text="",
            font_name="NanumGothic",
            size_hint=(1, 0.2),
            font_size=35,
            color=(1, 0, 0, 1),  # 빨간색 텍스트
            pos_hint={"center_x": 0.5, "y": 0.5}
        )
        layout.add_widget(self.message_label)
        
        
        self.add_widget(layout)
        
    def verify_login(self, instance):
        password = self.password_input.text
        
        url = "http://15.165.161.106:5000/login_button_click"
        data = {
            "password": password
        }
        try : 
            response = requests.post(url, json=data)
        
            response_data = response.json()
            check_value = response_data.get("check")
        
            if check_value == 1:
                self.manager.current = "home"
            else:
                self.password_input.text = ""
                self.message_label.text = "비밀번호가 틀렸습니다!"
            
                Clock.schedule_once(self.clear_message, 2)
        
        except :
            self.password_input.text = ""
            self.message_label.text = "서버가 차단 되어있습니다."
                
            Clock.schedule_once(self.clear_message, 7)
            
            
    def clear_message(self, dt):
        self.message_label.text = ""
        

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
           
        주문_button = Button(
            text="주문하기",
            font_name="NanumGothic",
            size_hint = (0.2,0.2),
            width = button_width,
            height = button_height,
            pos_hint={"x": 0.25, "y": 0.45}
        )
        
        주문_button.bind(on_press = self.go_to_주문화면)
        layout.add_widget(주문_button)

        선물_button = Button(
            text="선물하기",
            font_name="NanumGothic",
            size_hint = (0.2,0.2),
            width = button_width,
            height = button_height,
            pos_hint={"x": 0.55, "y": 0.45}
        )
        
        선물_button.bind(on_press = self.go_to_선물화면)
        layout.add_widget(선물_button)
        
        self.add_widget(layout)
        
        
    
    def go_to_주문화면(self, instance):
        self.manager.current = 'name_choose'
    
    def go_to_선물화면(self, instance):
        self.manager.current = 'gift'
        
        
        
class NamechooseScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.items = ["오주현", "오세현", "김향", "박세범", "윤자", "송송이", "정태오","바태","고유진","고유빈","김서인","서윤구"]
        self.filtered_items = self.items

        # BoxLayout의 padding을 늘려서 화면에 여유 공간을 추가합니다.
        root_layout = BoxLayout(orientation="vertical", padding=[20, 70, 20, 20], spacing=10)  # 위쪽 padding을 50으로 추가

        # 검색창(TextInput)
        self.search_input = TextInput(
            hint_text="이름을 검색하세요",
            font_name="NanumGothic",
            size_hint=(0.6, 0.1),
            font_size=font_size,
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        
        self.search_input.bind(text=self.on_text_change)

        # 검색 결과를 보여줄 ScrollView + GridLayout
        self.scroll_view = ScrollView(size_hint=(1, 1))
        self.result_layout = GridLayout(cols=1, size_hint_y=None)
        self.result_layout.bind(minimum_height=self.result_layout.setter('height'))

        self.scroll_view.add_widget(self.result_layout)

        # root_layout에 추가
        root_layout.add_widget(self.search_input)  # 검색창을 추가
        root_layout.add_widget(self.scroll_view)  # 결과 목록 추가

        self.add_widget(root_layout)  # 화면에 UI 추가

    def on_text_change(self, instance, text):
        # 검색어에 맞는 항목 필터링
        self.filtered_items = [item for item in self.items if text in item]

        # 결과를 화면에 갱신
        self.update_search_results()

    def update_search_results(self):
        # 이전 결과를 지우고 새로 갱신
        self.result_layout.clear_widgets()

        # 일치하는 항목들을 Button으로 추가
        for item in self.filtered_items:
            button = Button(
                text=item,
                font_name="NanumGothic",
                font_size = (font_size-5),
                size_hint_y=None,
                height=200
            )
            button.bind(on_press=self.on_item_select)
            self.result_layout.add_widget(button)

    def on_item_select(self, instance):
        # 버튼을 클릭하면 해당 이름을 선택
        selected_name = instance.text
        global 주문_이름
        주문_이름 = selected_name
        self.search_input.text = ''
        self.manager.current = 'order'
        
        
        
    
        

class OrderScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        """
        root_layout = BoxLayout(
            orientation="vertical",  # 세로 방향으로 정렬
            size_hint=(1, 1),  # 부모 레이아웃 크기 고정
            padding=[20, 20, 20, 20],  # 여백 설정
        )
        """
        
        root_layout = FloatLayout()
        
        self.scroll_view = ScrollView(
            size_hint=(1, 0.7),  # 가로 전체, 세로 70%
            pos_hint={"center_x": 0.5, "top": 0.9},  # 화면 중앙, TextInput 아래
        )
        
        # 2. 메뉴 버튼 부분 (GridLayout + ScrollView 사용)
        menu_layout = GridLayout(
            cols=3,  # 3개의 열
            size_hint_y=None,  # 스크롤 가능하도록 높이 고정 해제
            spacing=[30, 30],
            padding=[42, 10, 10, 15],
        )
        menu_layout.bind(minimum_height=menu_layout.setter("height"))  # 내용에 따라 높이 조정
        
        
        menu_layout.add_widget(Label(text="coffee", font_name="NanumGothic", size_hint=(None, None), height=270, width = 310, font_size='20sp', bold=True))
        menu_layout.add_widget(Label(size_hint=(None, None), width=310, height=270))
        menu_layout.add_widget(Label(size_hint=(None, None), width=310, height=270))
        #menu_layout.add_widget(Label(size_hint=(None, None), width=310, height=270))
        
        
        아메리카노_button = Button(
            text="아메리카노\n\n\u20A92,500",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        아메리카노_button.bind(on_press =lambda instance, name="아메리카노": self.아메_open_popup(name,instance))
        menu_layout.add_widget(아메리카노_button)
        
        에스프레소_button = Button(
            text="에스프레소\n\n\u20A92,500",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        에스프레소_button.bind(on_press =lambda instance, name="에스프레소": self.에스_open_popup(name,instance))
        menu_layout.add_widget(에스프레소_button)
        
        드립_button = Button(
            text="(섭)드립\n\n\u20A94,000",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        드립_button.bind(on_press =lambda instance, name="드립": self.드립_open_popup(name,instance))
        menu_layout.add_widget(드립_button)
        
        더치_button = Button(
            text="더치\n\n\u20A93,500",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        더치_button.bind(on_press =lambda instance, name="더치": self.더치_open_popup(name,instance))
        menu_layout.add_widget(더치_button)
        
        라떼_button = Button(
            text="라떼\n\n\u20A93,000",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        라떼_button.bind(on_press =lambda instance, name="라떼": self.라떼_open_popup(name,instance))
        menu_layout.add_widget(라떼_button)
        
        더치라떼_button = Button(
            text="더치라떼\n\n\u20A94,000",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        더치라떼_button.bind(on_press =lambda instance, name="더치라떼": self.더치라떼_open_popup(name,instance))
        menu_layout.add_widget(더치라떼_button)
        
        바닐라라떼_button = Button(
            text="바닐라라떼\n\n\u20A93,500",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        바닐라라떼_button.bind(on_press =lambda instance, name="바닐라라떼": self.바닐라라떼_open_popup(name,instance))
        menu_layout.add_widget(바닐라라떼_button)
        
        민트라떼종류_button = Button(
            text="민트라떼\n\n\u20A94,000",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        민트라떼종류_button.bind(on_press =lambda instance, name="민트라떼": self.민트라떼종류_open_popup(name,instance))
        menu_layout.add_widget(민트라떼종류_button)
        
        카푸치노_button = Button(
            text="카푸치노\n\n\u20A93,000",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        카푸치노_button.bind(on_press =lambda instance, name="카푸치노": self.카푸치노_open_popup(name,instance))
        menu_layout.add_widget(카푸치노_button)
        
        콜드브루_button = Button(
            text="콜드브루\n\n\u20A93,000",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        콜드브루_button.bind(on_press =lambda instance, name="콜드브루": self.콜드브루_open_popup(name,instance))
        menu_layout.add_widget(콜드브루_button)
        
        카페모카_button = Button(
            text="카페모카\n\n\u20A93,500",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        카페모카_button.bind(on_press =lambda instance, name="카페모카": self.카페모카_open_popup(name,instance))
        menu_layout.add_widget(카페모카_button)
        
        보리커피_button = Button(
            text="보리커피\n\n\u20A92,500",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        보리커피_button.bind(on_press =lambda instance, name="보리커피": self.보리커피_open_popup(name,instance))
        menu_layout.add_widget(보리커피_button)
        
        플렛화이트_button = Button(
            text="플렛화이트\n\n\u20A93,000",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        플렛화이트_button.bind(on_press =lambda instance, name="플렛화이트": self.플렛화이트_open_popup(name,instance))
        menu_layout.add_widget(플렛화이트_button)
        
        꼼빠냐_button = Button(
            text="꼼빠냐\n\n\u20A93,500",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        꼼빠냐_button.bind(on_press =lambda instance, name="꼼빠냐": self.꼼빠냐_open_popup(name,instance))
        menu_layout.add_widget(꼼빠냐_button)
        
        아인슈페너_button = Button(
            text="아인슈페너\n\n\u20A94,000",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        아인슈페너_button.bind(on_press =lambda instance, name="아인슈페너": self.아인슈페너_open_popup(name,instance))
        menu_layout.add_widget(아인슈페너_button)
        
        #menu_layout.add_widget(Label(size_hint=(None, None), width=310, height=270))
        menu_layout.add_widget(Label(text="beverage", font_name="NanumGothic", size_hint=(None, None), height=270, width = 310, font_size='20sp', bold=True))
        menu_layout.add_widget(Label(size_hint=(None, None), width=310, height=270))
        menu_layout.add_widget(Label(size_hint=(None, None), width=310, height=270))
        #menu_layout.add_widget(Label(size_hint=(None, None), width=310, height=270))
        
        베리고_button = Button(
            text="베리고\n\n\u20A94,000",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        베리고_button.bind(on_press =lambda instance, name="베리고": self.베리고_open_popup(name,instance))
        menu_layout.add_widget(베리고_button)
        
        망고스무디_button = Button(
            text="망고스무디\n\n\u20A94,000",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        망고스무디_button.bind(on_press =lambda instance, name="망고스무디": self.망고스무디_open_popup(name,instance))
        menu_layout.add_widget(망고스무디_button)
        
        아보카도바나나_button = Button(
            text="아보카도바나나\n\n\u20A93,500",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        아보카도바나나_button.bind(on_press =lambda instance, name="아보카도바나나": self.아보카도바나나_open_popup(name,instance))
        menu_layout.add_widget(아보카도바나나_button)
        
        망고바나나_button = Button(
            text="망고바나나\n\n\u20A94,000",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        망고바나나_button.bind(on_press =lambda instance, name="망고바나나": self.망고바나나_open_popup(name,instance))
        menu_layout.add_widget(망고바나나_button)
        
        패션후르츠에이드_button = Button(
            text="패션후르츠\n\n\u20A93,500",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        패션후르츠에이드_button.bind(on_press =lambda instance, name="패션후르츠": self.패션후르츠_open_popup(name,instance))
        menu_layout.add_widget(패션후르츠에이드_button)
        
        레몬에이드_button = Button(
            text="레몬에이드\n\n\u20A93,500",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        레몬에이드_button.bind(on_press =lambda instance, name="레몬에이드": self.레몬에이드_open_popup(name,instance))
        menu_layout.add_widget(레몬에이드_button)
        
        ##여기까지## ##같은 메뉴에서, 메뉴의 갯수를 시간차를 두고 추가하는 경우, 찾아 들어가기"##
        복숭아바질에이드_button = Button(
            text="복숭아바질\n\n\u20A93,500",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        복숭아바질에이드_button.bind(on_press =lambda instance, name="복숭아바질": self.복숭아바질_open_popup(name,instance))
        menu_layout.add_widget(복숭아바질에이드_button)
        
        초코라떼_button = Button(
            text="초코라떼\n\n\u20A93,500",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        초코라떼_button.bind(on_press = self.go_to_초코라떼)
        menu_layout.add_widget(초코라떼_button)
        
        핫초코_button = Button(
            text="핫초코\n\n\u20A93,500",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        핫초코_button.bind(on_press = self.go_to_핫초코)
        menu_layout.add_widget(핫초코_button)
        
        자두에이드_button = Button(
            text="자두에이드\n\n\u20A93,500",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        자두에이드_button.bind(on_press = self.go_to_자두에이드)
        menu_layout.add_widget(자두에이드_button)
        
        유자민트티_button = Button(
            text="유자민트티\n\n\u20A93,000",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        유자민트티_button.bind(on_press = self.go_to_유자민트티)
        menu_layout.add_widget(유자민트티_button)
        
        미숫가루_button = Button(
            text="미숫가루\n\n\u20A93,500",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        미숫가루_button.bind(on_press = self.go_to_미숫가루)
        menu_layout.add_widget(미숫가루_button)
        
        밀크티_button = Button(
            text="밀크티\n\n\u20A93,000",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        밀크티_button.bind(on_press = self.go_to_밀크티)
        menu_layout.add_widget(밀크티_button)
        
        딸기라떼_button = Button(
            text="딸기라떼\n\n\u20A93,500",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        딸기라떼_button.bind(on_press = self.go_to_딸기라떼)
        menu_layout.add_widget(딸기라떼_button)
        
        애플민트스무디_button = Button(
            text="애플민트스무디\n\n\u20A93,500",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        애플민트스무디_button.bind(on_press = self.go_to_애플민트스무디)
        menu_layout.add_widget(애플민트스무디_button)
        
        #menu_layout.add_widget(Label(size_hint=(None, None), width=310, height=270))
        menu_layout.add_widget(Label(text="bear", font_name="NanumGothic", size_hint=(None, None), height=270, width = 310, font_size='20sp', bold=True))
        menu_layout.add_widget(Label(size_hint=(None, None), width=310, height=270))
        menu_layout.add_widget(Label(size_hint=(None, None), width=310, height=270))
        #menu_layout.add_widget(Label(size_hint=(None, None), width=310, height=270))
        
        제주누보_button = Button(
            text="제주누보\n\n\u20A93,000",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        제주누보_button.bind(on_press = self.go_to_제주누보)
        menu_layout.add_widget(제주누보_button)
        
        레몬사와_button = Button(
            text="레몬사와\n\n\u20A93,000",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        레몬사와_button.bind(on_press = self.go_to_레몬사와)
        menu_layout.add_widget(레몬사와_button)
        
        유자사와_button = Button(
            text="유자사와\n\n\u20A93,000",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        유자사와_button.bind(on_press = self.go_to_유자사와)
        menu_layout.add_widget(유자사와_button)
    
        아사히_button = Button(
            text="아사히\n\n\u20A93,000",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        아사히_button.bind(on_press = self.go_to_아사히)
        menu_layout.add_widget(아사히_button)
        
        menu_layout.add_widget(Label(size_hint=(None, None), width=310, height=270))
        menu_layout.add_widget(Label(size_hint=(None, None), width=310, height=270))
        menu_layout.add_widget(Label(text="etc", font_name="NanumGothic", size_hint=(None, None), height=270, width = 310, font_size='20sp', bold=True))
        menu_layout.add_widget(Label(size_hint=(None, None), width=310, height=270))
        menu_layout.add_widget(Label(size_hint=(None, None), width=310, height=270))
        #menu_layout.add_widget(Label(size_hint=(None, None), width=310, height=270))
        
        탄산수_button = Button(
            text="탄산수\n\n\u20A9500",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        탄산수_button.bind(on_press = self.go_to_탄산수)
        menu_layout.add_widget(탄산수_button)
        
        쌍화탕_button = Button(
            text="쌍화탕\n\n\u20A91,700",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        쌍화탕_button.bind(on_press = self.go_to_쌍화탕)
        menu_layout.add_widget(쌍화탕_button)
        
        포춘쿠키_button = Button(
            text="포춘쿠키\n\n\u20A91,000",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        포춘쿠키_button.bind(on_press = self.go_to_포춘쿠키)
        menu_layout.add_widget(포춘쿠키_button)
        
        튀일쿠키_button = Button(
            text="튀일쿠키\n\n\u20A92,000",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        튀일쿠키_button.bind(on_press = self.go_to_튀일쿠키)
        menu_layout.add_widget(튀일쿠키_button)
        
        브륄레_button = Button(
            text="브륄레\n\n\u20A93,000",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        브륄레_button.bind(on_press = self.go_to_브륄레)
        menu_layout.add_widget(브륄레_button)
        
        
        menu_layout.add_widget(Label(size_hint=(None, None), width=310, height=270))
        #menu_layout.add_widget(Label(size_hint=(None, None), width=310, height=270))
        #menu_layout.add_widget(Label(size_hint=(None, None), width=310, height=270))
        menu_layout.add_widget(Label(text="tea", font_name="NanumGothic", size_hint=(None, None), height=270, width = 310, font_size='20sp', bold=True))
        menu_layout.add_widget(Label(size_hint=(None, None), width=310, height=270))
        menu_layout.add_widget(Label(size_hint=(None, None), width=310, height=270))
        #menu_layout.add_widget(Label(size_hint=(None, None), width=310, height=270))
        
        캐모마일_button = Button(
            text="캐모마일\n\n\u20A92,500",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        캐모마일_button.bind(on_press = self.go_to_캐모마일)
        menu_layout.add_widget(캐모마일_button)
        
        루이보스_button = Button(
            text="루이보스\n\n\u20A92,500",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        루이보스_button.bind(on_press = self.go_to_루이보스)
        menu_layout.add_widget(루이보스_button)
        
        보이차_button = Button(
            text="보이차\n\n\u20A92,500",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        보이차_button.bind(on_press = self.go_to_보이차)
        menu_layout.add_widget(보이차_button)
        
        페퍼민트차_button = Button(
            text="페퍼민트\n\n\u20A92,500",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        페퍼민트차_button.bind(on_press = self.go_to_페퍼민트차)
        menu_layout.add_widget(페퍼민트차_button)
        
        레몬그라스_button = Button(
            text="레몬그라스\n\n\u20A92,500",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        레몬그라스_button.bind(on_press = self.go_to_레몬그라스)
        menu_layout.add_widget(레몬그라스_button)
        
        라벤더_button = Button(
            text="라벤더\n\n\u20A92,500",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        라벤더_button.bind(on_press = self.go_to_라벤더)
        menu_layout.add_widget(라벤더_button)
        
        


        self.scroll_view.add_widget(menu_layout)
        
        root_layout.add_widget(self.scroll_view)

        # 3. 주문 버튼 부분 (BoxLayout 사용)
        
        back_layout = BoxLayout(
            size_hint=(1, 0.1),  # 가로 전체, 세로 10%
            pos_hint={"left": 0.5, "top": 1},  # 화면 상단
            orientation="horizontal",
            padding=(5, 0, 5, 0),
            spacing=3,
        )
        
        뒤로_button = Button(
            text="뒤로",
            font_name="NanumGothic",
            size_hint=(None, 1),
            width=200,
        )
        뒤로_button.bind(on_press=self.go_to_뒤로)
        back_layout.add_widget(뒤로_button)
        
        order_layout = GridLayout(
            cols = 4,
            size_hint=(1, None),  # 가로 전체, 세로 10%
            height = (button_height * 2),
            #width = 150,
            pos_hint={"x": 0, "bottom": 0},
        )
        
        self.메뉴1_button = Button(
            text="",
            font_name="NanumGothic",
            size_hint=(1,None),
            height=button_height,
            text_size=(160 * (default_dpi / device_dpi), None),
            halign="center",
            valign="middle",
            font_size = (font_size-5),
        )
        self.메뉴1_button.bind(on_press =lambda instance : self.메뉴_open_popup("[장바구니] "+instance.text.split(" ")[0], instance))
        order_layout.add_widget(self.메뉴1_button)

        self.메뉴2_button = Button(
            text="",
            font_name="NanumGothic",
            size_hint=(1,None),
            text_size=(160 * (default_dpi / device_dpi), None),
            halign="center",
            valign="middle",
            font_size = (font_size-5),
            height=button_height,
        )
        
        self.메뉴2_button.bind(on_press =lambda instance : self.메뉴_open_popup("[장바구니] "+instance.text.split(" ")[0], instance))
        order_layout.add_widget(self.메뉴2_button)
        
        self.메뉴3_button = Button(
            text="",
            font_name="NanumGothic",
            size_hint=(1,None),
            text_size=(160 * (default_dpi / device_dpi), None),
            halign="center",
            valign="middle",
            font_size = (font_size-5),
            height=button_height,
        )
        
        self.메뉴3_button.bind(on_press =lambda instance : self.메뉴_open_popup("[장바구니] "+instance.text.split(" ")[0], instance))
        order_layout.add_widget(self.메뉴3_button)
        
        
        self.메뉴4_button = Button(
            text="",
            font_name="NanumGothic",
            size_hint=(1,None),
            text_size=(160 * (default_dpi / device_dpi), None),
            halign="center",
            valign="middle",
            font_size = (font_size-5),
            height=button_height,
        )
        
        self.메뉴4_button.bind(on_press =lambda instance : self.메뉴_open_popup("[장바구니] "+instance.text.split(" ")[0], instance))
        order_layout.add_widget(self.메뉴4_button)
        
        self.메뉴5_button = Button(
            text="",
            font_name="NanumGothic",
            size_hint=(1,None),
            text_size=(160 * (default_dpi / device_dpi), None),
            halign="center",
            valign="middle",
            font_size = (font_size-5),
            height=button_height,
        )
        
        self.메뉴5_button.bind(on_press =lambda instance : self.메뉴_open_popup("[장바구니] "+instance.text.split(" ")[0], instance))
        order_layout.add_widget(self.메뉴5_button)
        
        
        self.메뉴6_button = Button(
            text="",
            font_name="NanumGothic",
            size_hint=(1,None),
            text_size=(160 * (default_dpi / device_dpi), None),
            halign="center",
            valign="middle",
            font_size = (font_size-5),
            height=button_height,
        )
        
        self.메뉴6_button.bind(on_press =lambda instance : self.메뉴_open_popup("[장바구니] "+instance.text.split(" ")[0], instance))
        order_layout.add_widget(self.메뉴6_button)
        
        
        self.메뉴7_button = Button(
            text="",
            font_name="NanumGothic",
            size_hint=(1,None),
            text_size=(160 * (default_dpi / device_dpi), None),
            halign="center",
            valign="middle",
            font_size = (font_size-5),
            height=button_height,
        )
        
        self.메뉴7_button.bind(on_press =lambda instance : self.메뉴_open_popup("[장바구니] "+instance.text.split(" ")[0], instance))
        order_layout.add_widget(self.메뉴7_button)
        
        다음_button = Button(
            text="다음",
            font_name="NanumGothic",
            size_hint=(1,None),
            text_size=(160 * (default_dpi / device_dpi), None),
            halign="center",
            valign="middle",
            font_size = (font_size-5),
            height=button_height,
        )
        
        다음_button.bind(on_press=self.go_to_주문)
        order_layout.add_widget(다음_button)
        
        root_layout.add_widget(back_layout)
        root_layout.add_widget(order_layout)

        # 최종적으로 root_layout을 스크린에 추가
        self.add_widget(root_layout)
        
    def 아메_open_popup(self, menu_name, instance):
        # 팝업 내용 정의
        content = FloatLayout()
        content.add_widget(Label(font_name="NanumGothic",font_size=sp(26), pos_hint={'center_x': 0.5, 'y': 0.45}, text=menu_name))
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None),  # 크기를 고정
            size=(100, 50),  # 고정 크기 설정
            pos_hint={'center_x': 0.5, 'y': 0.3},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)

        self.따아_button = ToggleButton(
            text="핫!",
            font_name="NanumGothic",
            size_hint=(0.3, 0.07),  # 버튼 크기
            pos_hint={'x': 0.32, 'y': 0.6},  # y 값을 조정하여 버튼 위치 설정
            group='온도'
        )
        self.아아_button = ToggleButton(
            text="아이스!",
            font_name="NanumGothic",
            size_hint=(0.3, 0.07),
            pos_hint={'x': 0.52, 'y': 0.6},
            group='온도'
        )
        
        self.따아_button.bind(on_press=lambda instance: self.record_selection(instance))
        self.아아_button.bind(on_press=lambda instance: self.record_selection(instance))
        
        content.add_widget(self.따아_button)
        content.add_widget(self.아아_button)

        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.15, 0.15),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.15, 0.15), pos_hint={'x': 0.85, 'y': 0}, on_press=lambda _ : self.go_to_아메리카노(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7, 0.7),
                           auto_dismiss=False)
        self.popup.open()
        

    def 에스_open_popup(self, menu_name, instance):
        # 팝업 내용 정의
        content = FloatLayout()
        content.add_widget(Label(font_name="NanumGothic",font_size=sp(26), pos_hint={'center_x': 0.5, 'y': 0.45}, text=menu_name))
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.5},text="[수량]")
        content.add_widget(수량)
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None), 
            size=(100, 50),  
            pos_hint={'center_x': 0.5, 'y': 0.32},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)

        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_에스프레소(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def 드립_open_popup(self, menu_name, instance):
        # 팝업 내용 정의
        content = FloatLayout()
        content.add_widget(Label(font_name="NanumGothic",font_size=sp(26), pos_hint={'center_x': 0.5, 'y': 0.45}, text=menu_name))
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.5},text="[수량]")
        content.add_widget(수량)
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None), 
            size=(100, 50),  
            pos_hint={'center_x': 0.5, 'y': 0.32},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)

        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_드립(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()

    def 더치_open_popup(self, menu_name, instance):
        # 팝업 내용 정의
        content = FloatLayout()
        content.add_widget(Label(font_name="NanumGothic",font_size=sp(26), pos_hint={'center_x': 0.5, 'y': 0.45}, text=menu_name))
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.5},text="[수량]")
        content.add_widget(수량)
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None), 
            size=(100, 50),  
            pos_hint={'center_x': 0.5, 'y': 0.32},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)

        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_더치(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def 라떼_open_popup(self, menu_name, instance):
        # 팝업 내용 정의
        content = FloatLayout()
        content.add_widget(Label(font_name="NanumGothic",font_size=sp(26), pos_hint={'center_x': 0.5, 'y': 0.45}, text=menu_name))
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.5},text="[수량]")
        content.add_widget(수량)
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None), 
            size=(100, 50),  
            pos_hint={'center_x': 0.5, 'y': 0.32},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)

        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_라떼(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
               
    def 더치라떼_open_popup(self, menu_name, instance):
        # 팝업 내용 정의
        content = FloatLayout()
        content.add_widget(Label(font_name="NanumGothic",font_size=sp(26), pos_hint={'center_x': 0.5, 'y': 0.45}, text=menu_name))
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.5},text="[수량]")
        content.add_widget(수량)
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None), 
            size=(100, 50),  
            pos_hint={'center_x': 0.5, 'y': 0.32},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)

        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_더치라떼(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        

    def 바닐라라떼_open_popup(self, menu_name, instance):
        # 팝업 내용 정의
        content = FloatLayout()
        content.add_widget(Label(font_name="NanumGothic",font_size=sp(26), pos_hint={'center_x': 0.5, 'y': 0.45}, text=menu_name))
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.5},text="[수량]")
        content.add_widget(수량)
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None), 
            size=(100, 50),  
            pos_hint={'center_x': 0.5, 'y': 0.32},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)

        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_바닐라라떼(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def 민트라떼종류_open_popup(self, menu_name, instance):
        # 팝업 내용 정의
        content = FloatLayout()
        content.add_widget(Label(font_name="NanumGothic",font_size=sp(26), pos_hint={'center_x': 0.5, 'y': 0.45}, text=menu_name))
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.5},text="[수량]")
        content.add_widget(수량)
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None), 
            size=(100, 50),  
            pos_hint={'center_x': 0.5, 'y': 0.32},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)

        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_민트라떼종류(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def 카푸치노_open_popup(self, menu_name, instance):
        # 팝업 내용 정의
        content = FloatLayout()
        content.add_widget(Label(font_name="NanumGothic",font_size=sp(26), pos_hint={'center_x': 0.5, 'y': 0.45}, text=menu_name))
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.5},text="[수량]")
        content.add_widget(수량)
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None), 
            size=(100, 50),  
            pos_hint={'center_x': 0.5, 'y': 0.32},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)

        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_카푸치노(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
        
    def 콜드브루_open_popup(self, menu_name, instance):
        # 팝업 내용 정의
        content = FloatLayout()
        content.add_widget(Label(font_name="NanumGothic",font_size=sp(26), pos_hint={'center_x': 0.5, 'y': 0.45}, text=menu_name))
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.5},text="[수량]")
        content.add_widget(수량)
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None), 
            size=(100, 50),  
            pos_hint={'center_x': 0.5, 'y': 0.32},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)

        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_콜드브루(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()


    def 카페모카_open_popup(self, menu_name, instance):
        # 팝업 내용 정의
        content = FloatLayout()
        content.add_widget(Label(font_name="NanumGothic",font_size=sp(26), pos_hint={'center_x': 0.5, 'y': 0.45}, text=menu_name))
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.5},text="[수량]")
        content.add_widget(수량)
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None), 
            size=(100, 50),  
            pos_hint={'center_x': 0.5, 'y': 0.32},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)

        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_카페모카(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        

    def 보리커피_open_popup(self, menu_name, instance):
        # 팝업 내용 정의
        content = FloatLayout()
        content.add_widget(Label(font_name="NanumGothic",font_size=sp(26), pos_hint={'center_x': 0.5, 'y': 0.45}, text=menu_name))
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.5},text="[수량]")
        content.add_widget(수량)
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None), 
            size=(100, 50),  
            pos_hint={'center_x': 0.5, 'y': 0.32},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)

        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_보리커피(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()


    def 플렛화이트_open_popup(self, menu_name, instance):
        # 팝업 내용 정의
        content = FloatLayout()
        content.add_widget(Label(font_name="NanumGothic",font_size=sp(26), pos_hint={'center_x': 0.5, 'y': 0.45}, text=menu_name))
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.5},text="[수량]")
        content.add_widget(수량)
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None), 
            size=(100, 50),  
            pos_hint={'center_x': 0.5, 'y': 0.32},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)

        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_플렛화이트(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
        
    def 꼼빠냐_open_popup(self, menu_name, instance):
        # 팝업 내용 정의
        content = FloatLayout()
        content.add_widget(Label(font_name="NanumGothic",font_size=sp(26), pos_hint={'center_x': 0.5, 'y': 0.45}, text=menu_name))
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.5},text="[수량]")
        content.add_widget(수량)
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None), 
            size=(100, 50),  
            pos_hint={'center_x': 0.5, 'y': 0.32},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)

        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_꼼빠냐(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        

    def 아인슈페너_open_popup(self, menu_name, instance):
        # 팝업 내용 정의
        content = FloatLayout()
        content.add_widget(Label(font_name="NanumGothic",font_size=sp(26), pos_hint={'center_x': 0.5, 'y': 0.45}, text=menu_name))
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.5},text="[수량]")
        content.add_widget(수량)
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None), 
            size=(100, 50),  
            pos_hint={'center_x': 0.5, 'y': 0.32},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)

        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_아인슈페너(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
        
    def 베리고_open_popup(self, menu_name, instance):
        # 팝업 내용 정의
        content = FloatLayout()
        content.add_widget(Label(font_name="NanumGothic",font_size=sp(26), pos_hint={'center_x': 0.5, 'y': 0.45}, text=menu_name))
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.5},text="[수량]")
        content.add_widget(수량)
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None), 
            size=(100, 50),  
            pos_hint={'center_x': 0.5, 'y': 0.32},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)

        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_베리고(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def 망고스무디_open_popup(self, menu_name, instance):
        # 팝업 내용 정의
        content = FloatLayout()
        content.add_widget(Label(font_name="NanumGothic",font_size=sp(26), pos_hint={'center_x': 0.5, 'y': 0.45}, text=menu_name))
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.5},text="[수량]")
        content.add_widget(수량)
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None), 
            size=(100, 50),  
            pos_hint={'center_x': 0.5, 'y': 0.32},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)

        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_망고스무디(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
        
    def 아보카도바나나_open_popup(self, menu_name, instance):
        # 팝업 내용 정의
        content = FloatLayout()
        content.add_widget(Label(font_name="NanumGothic",font_size=sp(26), pos_hint={'center_x': 0.5, 'y': 0.45}, text=menu_name))
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.5},text="[수량]")
        content.add_widget(수량)
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None), 
            size=(100, 50),  
            pos_hint={'center_x': 0.5, 'y': 0.32},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)

        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_아보카도바나나(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()   
        
    def 망고바나나_open_popup(self, menu_name, instance):
        # 팝업 내용 정의
        content = FloatLayout()
        content.add_widget(Label(font_name="NanumGothic",font_size=sp(26), pos_hint={'center_x': 0.5, 'y': 0.45}, text=menu_name))
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.5},text="[수량]")
        content.add_widget(수량)
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None), 
            size=(100, 50),  
            pos_hint={'center_x': 0.5, 'y': 0.32},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)

        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_망고바나나(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open() 
        
    def 패션후르츠_open_popup(self, menu_name, instance):
        # 팝업 내용 정의
        content = FloatLayout()
        content.add_widget(Label(font_name="NanumGothic",font_size=sp(26), pos_hint={'center_x': 0.5, 'y': 0.45}, text=menu_name))
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.5},text="[수량]")
        content.add_widget(수량)
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None), 
            size=(100, 50),  
            pos_hint={'center_x': 0.5, 'y': 0.32},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)

        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_패션후르츠(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open() 
        
    def 레몬에이드_open_popup(self, menu_name, instance):
        # 팝업 내용 정의
        content = FloatLayout()
        content.add_widget(Label(font_name="NanumGothic",font_size=sp(26), pos_hint={'center_x': 0.5, 'y': 0.45}, text=menu_name))
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.5},text="[수량]")
        content.add_widget(수량)
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None), 
            size=(100, 50),  
            pos_hint={'center_x': 0.5, 'y': 0.32},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)

        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_레몬에이드(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def 복숭아바질_open_popup(self, menu_name, instance):
        # 팝업 내용 정의
        content = FloatLayout()
        content.add_widget(Label(font_name="NanumGothic",font_size=sp(26), pos_hint={'center_x': 0.5, 'y': 0.45}, text=menu_name))
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.5},text="[수량]")
        content.add_widget(수량)
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None), 
            size=(100, 50),  
            pos_hint={'center_x': 0.5, 'y': 0.32},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)

        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_복숭아바질(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def 메뉴_open_popup(self, menu_name, instance):
        # 팝업 내용 정의
        content = FloatLayout()
        content.add_widget(Label(font_name="NanumGothic",font_size=sp(26), pos_hint={'center_x': 0.5, 'y': 0.45}, text=menu_name))
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.5},text="[수량]")
        content.add_widget(수량)
        
        
        self.a = instance.text.split(" ")[0]
        self.b = 0
        if self.a in dic_coffee_sum.keys():
            self.b = dic_coffee_cup[self.a]
        elif self.a in dic_beverage_sum.keys():
            self.b = dic_beverage_cup[self.b]
            
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None), 
            size=(100, 50),  
            pos_hint={'center_x': 0.5, 'y': 0.32},  # y를 조정하여 버튼 아래로 위치
            text=str(self.b)
            )
        content.add_widget(self.cup)

        content.add_widget(Button(text="정정", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_정정(instance)))
        content.add_widget(Button(text="삭제", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_삭제(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus_2(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus_2(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def record_selection(self,instance):
        if instance.state == 'down':
            self.last_selected = instance.text
        else : 
            self.last_selected = None
    
    def plus_2(self, instance):
        global dic_beverage_cup,dic_coffee_cup
        if self.a in dic_beverage_cup.keys():
            dic_beverage_cup[self.a] += 1
            self.cup.text = str(dic_beverage_cup[self.a])
        elif self.a in dic_coffee_cup.keys():
            dic_coffee_cup[self.a] += 1
            self.cup.text = str(dic_coffee_cup[self.a])
            
    def minus_2(self, instance):
        global dic_beverage_cup,dic_coffee_cup
        if int(self.cup.text) > 1:
            if self.a in dic_beverage_cup.keys():
                dic_beverage_cup[self.a] -= 1
                self.cup.text = str(dic_beverage_cup[self.a])
            elif self.a in dic_coffee_cup.keys():
                dic_coffee_cup[self.a] -= 1
                self.cup.text = str(dic_coffee_cup[self.a])
        else:
            pass
    
    def plus(self,instance):
        global count
        count += 1
        self.cup.text = str(count)

    def minus(self,instance):
        global count
        if count > 1:
            count -= 1
            self.cup.text = str(count)
        else:
            pass
        
    def go_to_닫기(self,instance):
        global count
        count = 1
        self.popup.dismiss()
    
    def go_to_삭제(self,instance):
        if self.a in dic_beverage_cup.keys():
            dic_beverage_cup[self.a] = 0
            dic_beverage_sum[self.a] = 0
        elif self.a in dic_coffee_cup.keys():
            dic_coffee_cup[self.a] = 0
            dic_coffee_sum[self.a] = 0

        instance.text = ""
        for _ in range(6) :
            if _ == 0:
                if self.메뉴1_button.text == '':
                    self.메뉴1_button.text = self.메뉴2_button.text
                    self.메뉴2_button.text = ''
                else:
                    pass
            elif _ == 1:
                if self.메뉴2_button.text == '':
                    self.메뉴2_button.text = self.메뉴3_button.text
                    self.메뉴3_button.text = ''
                else :
                    pass

            elif _ == 2:
                if self.메뉴3_button.text == '':
                    self.메뉴3_button.text = self.메뉴4_button.text
                    self.메뉴4_button.text = ''
                else :
                    pass
                
            elif _ == 3:
                if self.메뉴4_button.text == '':
                    self.메뉴4_button.text = self.메뉴5_button.text
                    self.메뉴5_button.text = ''
                else :
                    pass
                
            elif _ == 4:
                if self.메뉴5_button.text == '':
                    self.메뉴5_button.text = self.메뉴6_button.text
                    self.메뉴6_button.text = ''
                else :
                    pass
                
            elif _ == 5:
                if self.메뉴6_button.text == '':
                    self.메뉴6_button.text = self.메뉴7_button.text
                    self.메뉴7_button.text = ''
                else :
                    pass

        self.popup.dismiss()

    def go_to_정정(self,instance):
        global dic_beverage_cup,dic_coffee_cup,dic_menu_price
        if self.a in dic_beverage_cup.keys():
            instance.text = instance.text.split(" ")[0] + " " + str(dic_beverage_cup[self.a])
            dic_beverage_sum[self.a] = dic_menu_price[self.a] * dic_beverage_cup[self.a]
            self.popup.dismiss()
            
        elif self.a in dic_coffee_cup.keys():
            instance.text = instance.text.split(" ")[0] + " " + str(dic_coffee_cup[self.a])
            dic_coffee_sum[self.a] = dic_menu_price[self.a] * dic_coffee_cup[self.a]
            self.popup.dismiss()
    
    def go_to_아메리카노(self,instance):
        global count,dic_coffee_sum,dic_coffee_cup
        dic_coffee_sum["아메리카노"] += (2500 * count)
        dic_coffee_cup["아메리카노"] += count
        #self.메뉴1_button.text = f"아메리카노 {아메리카노_잔수}"
        if self.메뉴1_button.text == "":
            self.메뉴1_button.text = f"아메리카노 {dic_coffee_cup["아메리카노"]}"
        elif self.메뉴2_button.text == "":
            self.메뉴2_button.text = f"아메리카노 {dic_coffee_cup["아메리카노"]}"
        elif self.메뉴3_button.text == "":
            self.메뉴3_button.text = f"아메리카노 {dic_coffee_cup["아메리카노"]}"
        elif self.메뉴4_button.text == "":
            self.메뉴4_button.text = f"아메리카노 {dic_coffee_cup["아메리카노"]}"
        elif self.메뉴5_button.text == "":
            self.메뉴5_button.text = f"아메리카노 {dic_coffee_cup["아메리카노"]}"
        elif self.메뉴6_button.text == "":
            self.메뉴6_button.text = f"아메리카노 {dic_coffee_cup["아메리카노"]}"
        elif self.메뉴7_button.text == "":
            self.메뉴7_button.text = f"아메리카노 {dic_coffee_cup["아메리카노"]}"
        count = 1
        self.popup.dismiss()
        self.cup.text = "1"
        print(f"{dic_coffee_sum["아메리카노"]} {dic_coffee_cup["아메리카노"]}")
        
    def go_to_에스프레소(self,instance):
        global count,dic_coffee_sum,dic_coffee_cup
        dic_coffee_sum["에스프레소"] += (2500 * count)
        dic_coffee_cup["에스프레소"] += count
        if self.메뉴1_button.text == "":
            self.메뉴1_button.text = f"에스프레소 {dic_coffee_cup["에스프레소"]}"
        elif self.메뉴2_button.text == "":
            self.메뉴2_button.text = f"에스프레소 {dic_coffee_cup["에스프레소"]}"
        elif self.메뉴3_button.text == "":
            self.메뉴3_button.text = f"에스프레소 {dic_coffee_cup["에스프레소"]}"
        elif self.메뉴4_button.text == "":
            self.메뉴4_button.text = f"에스프레소 {dic_coffee_cup["에스프레소"]}"
        elif self.메뉴5_button.text == "":
            self.메뉴5_button.text = f"에스프레소 {dic_coffee_cup["에스프레소"]}"
        elif self.메뉴6_button.text == "":
            self.메뉴6_button.text = f"에스프레소 {dic_coffee_cup["에스프레소"]}"
        elif self.메뉴7_button.text == "":
            self.메뉴7_button.text = f"에스프레소 {dic_coffee_cup["에스프레소"]}"
        count = 1
        self.popup.dismiss()
        self.cup.text = "1"
        print(f"{dic_coffee_sum["에스프레소"]} {dic_coffee_cup["에스프레소"]}")
            
    
    def go_to_드립(self,instance):
        global count,dic_coffee_cup,dic_coffee_sum
        dic_coffee_sum["드립"] += (4000 * count)
        dic_coffee_cup["드립"]+= count
        if self.메뉴1_button.text == "":
            self.메뉴1_button.text = f"드립 {dic_coffee_cup["드립"]}"
        elif self.메뉴2_button.text == "":
            self.메뉴2_button.text = f"드립 {dic_coffee_cup["드립"]}"
        elif self.메뉴3_button.text == "":
            self.메뉴3_button.text = f"드립 {dic_coffee_cup["드립"]}"
        elif self.메뉴4_button.text == "":
            self.메뉴4_button.text = f"드립 {dic_coffee_cup["드립"]}"
        elif self.메뉴5_button.text == "":
            self.메뉴5_button.text = f"드립 {dic_coffee_cup["드립"]}"
        elif self.메뉴6_button.text == "":
            self.메뉴6_button.text = f"드립 {dic_coffee_cup["드립"]}"
        elif self.메뉴7_button.text == "":
            self.메뉴7_button.text = f"드립 {dic_coffee_cup["드립"]}"
        count = 1
        self.popup.dismiss()
        self.cup.text = "1"
        print(f"{dic_coffee_sum["드립"]} {dic_coffee_cup["드립"]}")
        
    def go_to_더치(self,instance):
        global count,dic_coffee_cup,dic_coffee_sum
        dic_coffee_sum["더치"] += (3500 * count)
        dic_coffee_cup["더치"] += count
        if self.메뉴1_button.text == "":
            self.메뉴1_button.text = f"더치 {dic_coffee_cup["더치"]}"
        elif self.메뉴2_button.text == "":
            self.메뉴2_button.text = f"더치 {dic_coffee_cup["더치"]}"
        elif self.메뉴3_button.text == "":
            self.메뉴3_button.text = f"더치 {dic_coffee_cup["더치"]}"
        elif self.메뉴4_button.text == "":
            self.메뉴4_button.text = f"더치 {dic_coffee_cup["더치"]}"
        elif self.메뉴5_button.text == "":
            self.메뉴5_button.text = f"더치 {dic_coffee_cup["더치"]}"
        elif self.메뉴6_button.text == "":
            self.메뉴6_button.text = f"더치 {dic_coffee_cup["더치"]}"
        elif self.메뉴7_button.text == "":
            self.메뉴7_button.text = f"더치 {dic_coffee_cup["더치"]}"
        count = 1
        self.popup.dismiss()
        self.cup.text = "1"
        print(f"{dic_coffee_sum["더치"]} {dic_coffee_cup["더치"]}")
        
    def go_to_라떼(self,instance):
        global count,dic_coffee_cup,dic_coffee_sum
        dic_coffee_sum["라떼"] += (3000 * count)
        dic_coffee_cup["라떼"] += count
        if self.메뉴1_button.text == "":
            self.메뉴1_button.text = f"라떼 {dic_coffee_cup["라떼"]}"
        elif self.메뉴2_button.text == "":
            self.메뉴2_button.text = f"라떼 {dic_coffee_cup["라떼"]}"
        elif self.메뉴3_button.text == "":
            self.메뉴3_button.text = f"라떼 {dic_coffee_cup["라떼"]}"
        elif self.메뉴4_button.text == "":
            self.메뉴4_button.text = f"라떼 {dic_coffee_cup["라떼"]}"
        elif self.메뉴5_button.text == "":
            self.메뉴5_button.text = f"라떼 {dic_coffee_cup["라떼"]}"
        elif self.메뉴6_button.text == "":
            self.메뉴6_button.text = f"라떼 {dic_coffee_cup["라떼"]}"
        elif self.메뉴7_button.text == "":
            self.메뉴7_button.text = f"라떼 {dic_coffee_cup["라떼"]}"
        count = 1
        self.popup.dismiss()
        self.cup.text = "1"
        print(f"{dic_coffee_sum["라떼"]} {dic_coffee_cup["라떼"]}")
        
    def go_to_더치라떼(self,instance):
        global count,dic_coffee_sum,dic_coffee_cup
        dic_coffee_sum["더치라떼"] += (4000 * count)
        dic_coffee_cup["더치라떼"] += count
        if self.메뉴1_button.text == "":
            self.메뉴1_button.text = f"더치라떼 {dic_coffee_cup["더치라떼"]}"
        elif self.메뉴2_button.text == "":
            self.메뉴2_button.text = f"더치라떼 {dic_coffee_cup["더치라떼"]}"
        elif self.메뉴3_button.text == "":
            self.메뉴3_button.text = f"더치라떼 {dic_coffee_cup["더치라떼"]}"
        elif self.메뉴4_button.text == "":
            self.메뉴4_button.text = f"더치라떼 {dic_coffee_cup["더치라떼"]}"
        elif self.메뉴5_button.text == "":
            self.메뉴5_button.text = f"더치라떼 {dic_coffee_cup["더치라떼"]}"
        elif self.메뉴6_button.text == "":
            self.메뉴6_button.text = f"더치라떼 {dic_coffee_cup["더치라떼"]}"
        elif self.메뉴7_button.text == "":
            self.메뉴7_button.text = f"더치라떼 {dic_coffee_cup["더치라떼"]}"
        count = 1
        self.popup.dismiss()
        self.cup.text = "1"
        print(f"{dic_coffee_sum["더치라떼"]} {dic_coffee_cup["더치라떼"]}")
        
    def go_to_바닐라라떼(self,instance):
        global count,dic_coffee_sum,dic_coffee_cup
        dic_coffee_sum["바닐라라떼"] += (3500 * count)
        dic_coffee_cup["바닐라라떼"] += count
        if self.메뉴1_button.text == "":
            self.메뉴1_button.text = f"바닐라라떼 {dic_coffee_cup["바닐라라떼"]}"
        elif self.메뉴2_button.text == "":
            self.메뉴2_button.text = f"바닐라라떼 {dic_coffee_cup["바닐라라떼"]}"
        elif self.메뉴3_button.text == "":
            self.메뉴3_button.text = f"바닐라라떼 {dic_coffee_cup["바닐라라떼"]}"
        elif self.메뉴4_button.text == "":
            self.메뉴4_button.text = f"바닐라라떼 {dic_coffee_cup["바닐라라떼"]}"
        elif self.메뉴5_button.text == "":
            self.메뉴5_button.text = f"바닐라라떼 {dic_coffee_cup["바닐라라떼"]}"
        elif self.메뉴6_button.text == "":
            self.메뉴6_button.text = f"바닐라라떼 {dic_coffee_cup["바닐라라떼"]}"
        elif self.메뉴7_button.text == "":
            self.메뉴7_button.text = f"바닐라라떼 {dic_coffee_cup["바닐라라떼"]}"
        count = 1
        self.popup.dismiss()
        self.cup.text = "1"
        print(f"{dic_coffee_sum["바닐라라떼"]} {dic_coffee_cup["바닐라라떼"]}")
        
    def go_to_민트라떼종류(self,instance):
        global count,dic_coffee_sum,dic_coffee_cup
        dic_coffee_sum["민트라떼"] += (4000 * count)
        dic_coffee_cup["민트라떼"] += count
        if self.메뉴1_button.text == "":
            self.메뉴1_button.text = f"민트라떼 {dic_coffee_cup["민트라떼"]}"
        elif self.메뉴2_button.text == "":
            self.메뉴2_button.text = f"민트라떼 {dic_coffee_cup["민트라떼"]}"
        elif self.메뉴3_button.text == "":
            self.메뉴3_button.text = f"민트라떼 {dic_coffee_cup["민트라떼"]}"
        elif self.메뉴4_button.text == "":
            self.메뉴4_button.text = f"민트라떼 {dic_coffee_cup["민트라떼"]}"
        elif self.메뉴5_button.text == "":
            self.메뉴5_button.text = f"민트라떼 {dic_coffee_cup["민트라떼"]}"
        elif self.메뉴6_button.text == "":
            self.메뉴6_button.text = f"민트라떼 {dic_coffee_cup["민트라떼"]}"
        elif self.메뉴7_button.text == "":
            self.메뉴7_button.text = f"민트라떼 {dic_coffee_cup["민트라떼"]}"
        count = 1
        self.popup.dismiss()
        self.cup.text = "1"
        print(f"{dic_coffee_sum["민트라떼"]} {dic_coffee_cup["민트라떼"]}")
        
    def go_to_카푸치노(self,instance):
        global count,dic_coffee_cup,dic_coffee_sum
        dic_coffee_sum["카푸치노"] += (3000 * count)
        dic_coffee_cup["카푸치노"] += count
        if self.메뉴1_button.text == "":
            self.메뉴1_button.text = f"카푸치노 {dic_coffee_cup["카푸치노"]}"
        elif self.메뉴2_button.text == "":
            self.메뉴2_button.text = f"카푸치노 {dic_coffee_cup["카푸치노"]}"
        elif self.메뉴3_button.text == "":
            self.메뉴3_button.text = f"카푸치노 {dic_coffee_cup["카푸치노"]}"
        elif self.메뉴4_button.text == "":
            self.메뉴4_button.text = f"카푸치노 {dic_coffee_cup["카푸치노"]}"
        elif self.메뉴5_button.text == "":
            self.메뉴5_button.text = f"카푸치노 {dic_coffee_cup["카푸치노"]}"
        elif self.메뉴6_button.text == "":
            self.메뉴6_button.text = f"카푸치노 {dic_coffee_cup["카푸치노"]}"
        elif self.메뉴7_button.text == "":
            self.메뉴7_button.text = f"카푸치노 {dic_coffee_cup["카푸치노"]}"
        count = 1
        self.popup.dismiss()
        self.cup.text = "1"
        print(f"{dic_coffee_sum["카푸치노"]} {dic_coffee_cup["카푸치노"]}")
        
    def go_to_콜드브루(self,instance):
        global count,dic_coffee_cup,dic_coffee_sum
        dic_coffee_sum["콜드브루"] += (3000 * count)
        dic_coffee_cup["콜드브루"] += count
        if self.메뉴1_button.text == "":
            self.메뉴1_button.text = f"콜드브루 {dic_coffee_cup["콜드브루"]}"
        elif self.메뉴2_button.text == "":
            self.메뉴2_button.text = f"콜드브루 {dic_coffee_cup["콜드브루"]}"
        elif self.메뉴3_button.text == "":
            self.메뉴3_button.text = f"콜드브루 {dic_coffee_cup["콜드브루"]}"
        elif self.메뉴4_button.text == "":
            self.메뉴4_button.text = f"콜드브루 {dic_coffee_cup["콜드브루"]}"
        elif self.메뉴5_button.text == "":
            self.메뉴5_button.text = f"콜드브루 {dic_coffee_cup["콜드브루"]}"
        elif self.메뉴6_button.text == "":
            self.메뉴6_button.text = f"콜드브루 {dic_coffee_cup["콜드브루"]}"
        elif self.메뉴7_button.text == "":
            self.메뉴7_button.text = f"콜드브루 {dic_coffee_cup["콜드브루"]}"
        count = 1
        self.popup.dismiss()
        self.cup.text = "1"
        print(f"{dic_coffee_sum["콜드브루"]} {dic_coffee_cup["콜드브루"]}")
    
    def go_to_카페모카(self,instance):
        global count,dic_coffee_cup,dic_coffee_sum
        dic_coffee_sum["카페모카"] += (3500 * count)
        dic_coffee_cup["카페모카"] += count
        if self.메뉴1_button.text == "":
            self.메뉴1_button.text = f"카페모카 {dic_coffee_cup["카페모카"]}"
        elif self.메뉴2_button.text == "":
            self.메뉴2_button.text = f"카페모카 {dic_coffee_cup["카페모카"]}"
        elif self.메뉴3_button.text == "":
            self.메뉴3_button.text = f"카페모카 {dic_coffee_cup["카페모카"]}"
        elif self.메뉴4_button.text == "":
            self.메뉴4_button.text = f"카페모카 {dic_coffee_cup["카페모카"]}"
        elif self.메뉴5_button.text == "":
            self.메뉴5_button.text = f"카페모카 {dic_coffee_cup["카페모카"]}"
        elif self.메뉴6_button.text == "":
            self.메뉴6_button.text = f"카페모카 {dic_coffee_cup["카페모카"]}"
        elif self.메뉴7_button.text == "":
            self.메뉴7_button.text = f"카페모카 {dic_coffee_cup["카페모카"]}"
        count = 1
        self.popup.dismiss()
        self.cup.text = "1"
        print(f"{dic_coffee_sum["카페모카"]} {dic_coffee_cup["카페모카"]}")
        
    def go_to_보리커피(self,instance):
        global count,dic_coffee_cup,dic_coffee_sum
        dic_coffee_sum["보리커피"] += (2500 * count)
        dic_coffee_cup["보리커피"] += count
        if self.메뉴1_button.text == "":
            self.메뉴1_button.text = f"보리커피 {dic_coffee_cup["보리커피"]}"
        elif self.메뉴2_button.text == "":
            self.메뉴2_button.text = f"보리커피 {dic_coffee_cup["보리커피"]}"
        elif self.메뉴3_button.text == "":
            self.메뉴3_button.text = f"보리커피 {dic_coffee_cup["보리커피"]}"
        elif self.메뉴4_button.text == "":
            self.메뉴4_button.text = f"보리커피 {dic_coffee_cup["보리커피"]}"
        elif self.메뉴5_button.text == "":
            self.메뉴5_button.text = f"보리커피 {dic_coffee_cup["보리커피"]}"
        elif self.메뉴6_button.text == "":
            self.메뉴6_button.text = f"보리커피 {dic_coffee_cup["보리커피"]}"
        elif self.메뉴7_button.text == "":
            self.메뉴7_button.text = f"보리커피 {dic_coffee_cup["보리커피"]}"
        count = 1
        self.popup.dismiss()
        self.cup.text = "1"
        print(f"{dic_coffee_sum["보리커피"]} {dic_coffee_cup["보리커피"]}")
        
    def go_to_플렛화이트(self,instance):
        global count,dic_coffee_cup,dic_coffee_sum
        dic_coffee_sum["플렛화이트"] += (3000 * count)
        dic_coffee_cup["플렛화이트"] += count
        if self.메뉴1_button.text == "":
            self.메뉴1_button.text = f"플렛화이트 {dic_coffee_cup["플렛화이트"]}"
        elif self.메뉴2_button.text == "":
            self.메뉴2_button.text = f"플렛화이트 {dic_coffee_cup["플렛화이트"]}"
        elif self.메뉴3_button.text == "":
            self.메뉴3_button.text = f"플렛화이트 {dic_coffee_cup["플렛화이트"]}"
        elif self.메뉴4_button.text == "":
            self.메뉴4_button.text = f"플렛화이트 {dic_coffee_cup["플렛화이트"]}"
        elif self.메뉴5_button.text == "":
            self.메뉴5_button.text = f"플렛화이트 {dic_coffee_cup["플렛화이트"]}"
        elif self.메뉴6_button.text == "":
            self.메뉴6_button.text = f"플렛화이트 {dic_coffee_cup["플렛화이트"]}"
        elif self.메뉴7_button.text == "":
            self.메뉴7_button.text = f"플렛화이트 {dic_coffee_cup["플렛화이트"]}"
        count = 1
        self.popup.dismiss()
        self.cup.text = "1"
        print(f"{dic_coffee_sum["플렛화이트"]} {dic_coffee_cup["플렛화이트"]}")

    def go_to_꼼빠냐(self,instance):
        global count,dic_coffee_cup,dic_coffee_sum
        dic_coffee_sum["꼼빠냐"] += (3500 * count)
        dic_coffee_cup["꼼빠냐"] += count
        if self.메뉴1_button.text == "":
            self.메뉴1_button.text = f"꼼빠냐 {dic_coffee_cup["꼼빠냐"]}"
        elif self.메뉴2_button.text == "":
            self.메뉴2_button.text = f"꼼빠냐 {dic_coffee_cup["꼼빠냐"]}"
        elif self.메뉴3_button.text == "":
            self.메뉴3_button.text = f"꼼빠냐 {dic_coffee_cup["꼼빠냐"]}"
        elif self.메뉴4_button.text == "":
            self.메뉴4_button.text = f"꼼빠냐 {dic_coffee_cup["꼼빠냐"]}"
        elif self.메뉴5_button.text == "":
            self.메뉴5_button.text = f"꼼빠냐 {dic_coffee_cup["꼼빠냐"]}"
        elif self.메뉴6_button.text == "":
            self.메뉴6_button.text = f"꼼빠냐 {dic_coffee_cup["꼼빠냐"]}"
        elif self.메뉴7_button.text == "":
            self.메뉴7_button.text = f"꼼빠냐 {dic_coffee_cup["꼼빠냐"]}"
        count = 1
        self.popup.dismiss()
        self.cup.text = "1"
        print(f"{dic_coffee_sum["꼼빠냐"]} {dic_coffee_cup["꼼빠냐"]}")
        
    def go_to_아인슈페너(self,instance):
        global count,dic_coffee_cup,dic_coffee_sum
        dic_coffee_sum["아인슈페너"] += (4000 * count)
        dic_coffee_cup["아인슈페너"] += count
        if self.메뉴1_button.text == "":
            self.메뉴1_button.text = f"아인슈페너 {dic_coffee_cup["아인슈페너"]}"
        elif self.메뉴2_button.text == "":
            self.메뉴2_button.text = f"아인슈페너 {dic_coffee_cup["아인슈페너"]}"
        elif self.메뉴3_button.text == "":
            self.메뉴3_button.text = f"아인슈페너 {dic_coffee_cup["아인슈페너"]}"
        elif self.메뉴4_button.text == "":
            self.메뉴4_button.text = f"아인슈페너 {dic_coffee_cup["아인슈페너"]}"
        elif self.메뉴5_button.text == "":
            self.메뉴5_button.text = f"아인슈페너 {dic_coffee_cup["아인슈페너"]}"
        elif self.메뉴6_button.text == "":
            self.메뉴6_button.text = f"아인슈페너 {dic_coffee_cup["아인슈페너"]}"
        elif self.메뉴7_button.text == "":
            self.메뉴7_button.text = f"아인슈페너 {dic_coffee_cup["아인슈페너"]}"
        count = 1
        self.popup.dismiss()
        self.cup.text = "1"
        print(f"{dic_coffee_sum["아인슈페너"]} {dic_coffee_cup["아인슈페너"]}")
        
    def go_to_베리고(self,instance):
        global count,베리고,베리고_잔수
        베리고 += (2500 * count)
        베리고_잔수 += count
        if self.메뉴1_button.text == "":
            self.메뉴1_button.text = f"베리고 {베리고_잔수}"
        elif self.메뉴2_button.text == "":
            self.메뉴2_button.text = f"베리고 {베리고_잔수}"
        elif self.메뉴3_button.text == "":
            self.메뉴3_button.text = f"베리고 {베리고_잔수}"
        elif self.메뉴4_button.text == "":
            self.메뉴4_button.text = f"베리고 {베리고_잔수}"
        elif self.메뉴5_button.text == "":
            self.메뉴5_button.text = f"베리고 {베리고_잔수}"
        elif self.메뉴6_button.text == "":
            self.메뉴6_button.text = f"베리고 {베리고_잔수}"
        elif self.메뉴7_button.text == "":
            self.메뉴7_button.text = f"베리고 {베리고_잔수}"
        count = 1
        self.popup.dismiss()
        self.cup.text = "1"
        print(f"{베리고} {베리고_잔수}")
        
    def go_to_망고스무디(self,instance):
        global count,망고스무디,망고스무디_잔수
        망고스무디 += (2500 * count)
        망고스무디_잔수 += count
        if self.메뉴1_button.text == "":
            self.메뉴1_button.text = f"망고스무디 {망고스무디_잔수}"
        elif self.메뉴2_button.text == "":
            self.메뉴2_button.text = f"망고스무디 {망고스무디_잔수}"
        elif self.메뉴3_button.text == "":
            self.메뉴3_button.text = f"망고스무디 {망고스무디_잔수}"
        elif self.메뉴4_button.text == "":
            self.메뉴4_button.text = f"망고스무디 {망고스무디_잔수}"
        elif self.메뉴5_button.text == "":
            self.메뉴5_button.text = f"망고스무디 {망고스무디_잔수}"
        elif self.메뉴6_button.text == "":
            self.메뉴6_button.text = f"망고스무디 {망고스무디_잔수}"
        elif self.메뉴7_button.text == "":
            self.메뉴7_button.text = f"망고스무디 {망고스무디_잔수}"
        count = 1
        self.popup.dismiss()
        self.cup.text = "1"
        print(f"{망고스무디} {망고스무디_잔수}")
        
    def go_to_아보카도바나나(self,instance):
        global count,아보카도바나나,아보카도바나나_잔수
        아보카도바나나 += (2500 * count)
        아보카도바나나_잔수 += count
        if self.메뉴1_button.text == "":
            self.메뉴1_button.text = f"아보카도바나나 {아보카도바나나_잔수}"
        elif self.메뉴2_button.text == "":
            self.메뉴2_button.text = f"아보카도바나나 {아보카도바나나_잔수}"
        elif self.메뉴3_button.text == "":
            self.메뉴3_button.text = f"아보카도바나나 {아보카도바나나_잔수}"
        elif self.메뉴4_button.text == "":
            self.메뉴4_button.text = f"아보카도바나나 {아보카도바나나_잔수}"
        elif self.메뉴5_button.text == "":
            self.메뉴5_button.text = f"아보카도바나나 {아보카도바나나_잔수}"
        elif self.메뉴6_button.text == "":
            self.메뉴6_button.text = f"아보카도바나나 {아보카도바나나_잔수}"
        elif self.메뉴7_button.text == "":
            self.메뉴7_button.text = f"아보카도바나나 {아보카도바나나_잔수}"
        count = 1
        self.popup.dismiss()
        self.cup.text = "1"
        print(f"{아보카도바나나} {아보카도바나나_잔수}")
        
    def go_to_망고바나나(self,instance):
        global count,망고바나나,망고바나나_잔수
        망고바나나 += (2500 * count)
        망고바나나_잔수 += count
        if self.메뉴1_button.text == "":
            self.메뉴1_button.text = f"망고바나나 {망고바나나_잔수}"
        elif self.메뉴2_button.text == "":
            self.메뉴2_button.text = f"망고바나나 {망고바나나_잔수}"
        elif self.메뉴3_button.text == "":
            self.메뉴3_button.text = f"망고바나나 {망고바나나_잔수}"
        elif self.메뉴4_button.text == "":
            self.메뉴4_button.text = f"망고바나나 {망고바나나_잔수}"
        elif self.메뉴5_button.text == "":
            self.메뉴5_button.text = f"망고바나나 {망고바나나_잔수}"
        elif self.메뉴6_button.text == "":
            self.메뉴6_button.text = f"망고바나나 {망고바나나_잔수}"
        elif self.메뉴7_button.text == "":
            self.메뉴7_button.text = f"망고바나나 {망고바나나_잔수}"
        count = 1
        self.popup.dismiss()
        self.cup.text = "1"
        print(f"{망고바나나} {망고바나나_잔수}")
        
    def go_to_패션후르츠(self,instance):
        global count,패션후르츠,패션후르츠_잔수
        패션후르츠 += (2500 * count)
        패션후르츠_잔수 += count
        if self.메뉴1_button.text == "":
            self.메뉴1_button.text = f"패션후르츠 {패션후르츠_잔수}"
        elif self.메뉴2_button.text == "":
            self.메뉴2_button.text = f"패션후르츠 {패션후르츠_잔수}"
        elif self.메뉴3_button.text == "":
            self.메뉴3_button.text = f"패션후르츠 {패션후르츠_잔수}"
        elif self.메뉴4_button.text == "":
            self.메뉴4_button.text = f"패션후르츠 {패션후르츠_잔수}"
        elif self.메뉴5_button.text == "":
            self.메뉴5_button.text = f"패션후르츠 {패션후르츠_잔수}"
        elif self.메뉴6_button.text == "":
            self.메뉴6_button.text = f"패션후르츠 {패션후르츠_잔수}"
        elif self.메뉴7_button.text == "":
            self.메뉴7_button.text = f"패션후르츠 {패션후르츠_잔수}"
        count = 1
        self.popup.dismiss()
        self.cup.text = "1"
        print(f"{패션후르츠} {패션후르츠_잔수}")
        
    def go_to_레몬에이드(self,instance):
        global count,레몬에이드,레몬에이드_잔수
        레몬에이드 += (2500 * count)
        레몬에이드_잔수 += count
        if self.메뉴1_button.text == "":
            self.메뉴1_button.text = f"레몬에이드 {레몬에이드_잔수}"
        elif self.메뉴2_button.text == "":
            self.메뉴2_button.text = f"레몬에이드 {레몬에이드_잔수}"
        elif self.메뉴3_button.text == "":
            self.메뉴3_button.text = f"레몬에이드 {레몬에이드_잔수}"
        elif self.메뉴4_button.text == "":
            self.메뉴4_button.text = f"레몬에이드 {레몬에이드_잔수}"
        elif self.메뉴5_button.text == "":
            self.메뉴5_button.text = f"레몬에이드 {레몬에이드_잔수}"
        elif self.메뉴6_button.text == "":
            self.메뉴6_button.text = f"레몬에이드 {레몬에이드_잔수}"
        elif self.메뉴7_button.text == "":
            self.메뉴7_button.text = f"레몬에이드 {레몬에이드_잔수}"
        count = 1
        self.popup.dismiss()
        self.cup.text = "1"
        print(f"{레몬에이드} {레몬에이드_잔수}")
        
    def go_to_복숭아바질(self,instance):
        global count,복숭아바질,복숭아바질_잔수
        복숭아바질 += (2500 * count)
        복숭아바질_잔수 += count
        if self.메뉴1_button.text == "":
            self.메뉴1_button.text = f"복숭아바질 {복숭아바질_잔수}"
        elif self.메뉴2_button.text == "":
            self.메뉴2_button.text = f"복숭아바질 {복숭아바질_잔수}"
        elif self.메뉴3_button.text == "":
            self.메뉴3_button.text = f"복숭아바질 {복숭아바질_잔수}"
        elif self.메뉴4_button.text == "":
            self.메뉴4_button.text = f"복숭아바질 {복숭아바질_잔수}"
        elif self.메뉴5_button.text == "":
            self.메뉴5_button.text = f"복숭아바질 {복숭아바질_잔수}"
        elif self.메뉴6_button.text == "":
            self.메뉴6_button.text = f"복숭아바질 {복숭아바질_잔수}"
        elif self.메뉴7_button.text == "":
            self.메뉴7_button.text = f"복숭아바질 {복숭아바질_잔수}"
        count = 1
        self.popup.dismiss()
        self.cup.text = "1"
        print(f"{복숭아바질} {복숭아바질_잔수}")
        
    def go_to_초코라떼(self,instance):
        instance.background_color = (0, 1, 0, 1)
        global 주문금액
        주문금액 += 4000
        Clock.schedule_once(lambda dt: self.reset_color(instance), 0.2)
        
    def go_to_핫초코(self,instance):
        instance.background_color = (0, 1, 0, 1)
        global 주문금액
        주문금액 += 4000
        Clock.schedule_once(lambda dt: self.reset_color(instance), 0.2)
        
    def go_to_자두에이드(self,instance):
        instance.background_color = (0, 1, 0, 1)
        global 주문금액
        주문금액 += 4000
        Clock.schedule_once(lambda dt: self.reset_color(instance), 0.2)
        
    def go_to_유자민트티(self,instance):
        instance.background_color = (0, 1, 0, 1)
        global 주문금액
        주문금액 += 3500
        Clock.schedule_once(lambda dt: self.reset_color(instance), 0.2)

    def go_to_미숫가루(self,instance):
        instance.background_color = (0, 1, 0, 1)
        global 주문금액
        주문금액 += 3500
        Clock.schedule_once(lambda dt: self.reset_color(instance), 0.2)
        
    def go_to_밀크티(self,instance):
        instance.background_color = (0, 1, 0, 1)
        global 주문금액
        주문금액 += 3500
        Clock.schedule_once(lambda dt: self.reset_color(instance), 0.2)
        
    def go_to_딸기라떼(self,instance):
        instance.background_color = (0, 1, 0, 1)
        global 주문금액
        주문금액 += 3500
        Clock.schedule_once(lambda dt: self.reset_color(instance), 0.2)
        
    def go_to_애플민트스무디(self,instance):
        instance.background_color = (0, 1, 0, 1)
        global 주문금액
        주문금액 += 3500
        Clock.schedule_once(lambda dt: self.reset_color(instance), 0.2)
    
    def go_to_제주누보(self,instance):
        instance.background_color = (0, 1, 0, 1)
        global 주문금액
        주문금액 += 4000
        Clock.schedule_once(lambda dt: self.reset_color(instance), 0.2)
        
    def go_to_레몬사와(self,instance):
        instance.background_color = (0, 1, 0, 1)
        global 주문금액
        주문금액 += 3100
        Clock.schedule_once(lambda dt: self.reset_color(instance), 0.2)

    def go_to_유자사와(self,instance):
        instance.background_color = (0, 1, 0, 1)
        global 주문금액
        주문금액 += 3500
        Clock.schedule_once(lambda dt: self.reset_color(instance), 0.2)
        
    def go_to_아사히(self,instance):
        instance.background_color = (0, 1, 0, 1)
        global 주문금액
        주문금액 += 3100
        Clock.schedule_once(lambda dt: self.reset_color(instance), 0.2)
    
    def go_to_탄산수(self,instance):
        instance.background_color = (0, 1, 0, 1)
        global 주문금액
        주문금액 += 3100
        Clock.schedule_once(lambda dt: self.reset_color(instance), 0.2)
        
    def go_to_쌍화탕(self,instance):
        instance.background_color = (0, 1, 0, 1)
        global 주문금액
        주문금액 += 3100
        Clock.schedule_once(lambda dt: self.reset_color(instance), 0.2)
        
    def go_to_포춘쿠키(self,instance):
        instance.background_color = (0, 1, 0, 1)
        global 주문금액
        주문금액 += 3100
        Clock.schedule_once(lambda dt: self.reset_color(instance), 0.2)
        
    def go_to_튀일쿠키(self,instance):
        instance.background_color = (0, 1, 0, 1)
        global 주문금액
        주문금액 += 1700
        Clock.schedule_once(lambda dt: self.reset_color(instance), 0.2)
        
    def go_to_브륄레(self,instance):
        instance.background_color = (0, 1, 0, 1)
        global 주문금액
        주문금액 += 3100
        Clock.schedule_once(lambda dt: self.reset_color(instance), 0.2)

    def go_to_캐모마일(self,instance):
        instance.background_color = (0, 1, 0, 1)
        global 주문금액
        주문금액 += 3100
        Clock.schedule_once(lambda dt: self.reset_color(instance), 0.2)
        
    def go_to_캐모마일(self,instance):
        instance.background_color = (0, 1, 0, 1)
        global 주문금액
        주문금액 += 2700
        Clock.schedule_once(lambda dt: self.reset_color(instance), 0.2)
        
    def go_to_루이보스(self,instance):
        instance.background_color = (0, 1, 0, 1)
        global 주문금액
        주문금액 += 2700
        Clock.schedule_once(lambda dt: self.reset_color(instance), 0.2)
        
    def go_to_보이차(self,instance):
        instance.background_color = (0, 1, 0, 1)
        global 주문금액
        주문금액 += 2700
        Clock.schedule_once(lambda dt: self.reset_color(instance), 0.2)
    
    def go_to_페퍼민트차(self,instance):
        instance.background_color = (0, 1, 0, 1)
        global 주문금액
        주문금액 += 2700
        Clock.schedule_once(lambda dt: self.reset_color(instance), 0.2)
        
    def go_to_레몬그라스(self,instance):
        instance.background_color = (0, 1, 0, 1)
        global 주문금액
        주문금액 += 2700
        Clock.schedule_once(lambda dt: self.reset_color(instance), 0.2)
        
    def go_to_라벤더(self,instance):
        instance.background_color = (0, 1, 0, 1)
        global 주문금액
        주문금액 += 2700
        Clock.schedule_once(lambda dt: self.reset_color(instance), 0.2)
        
        #self.메뉴1_button.bind(on_press =lambda instance, name="[장바구니]" + self.메뉴1_button.text.split(" ")[0]: self.메뉴1_open_popup(name,instance))
        
    def go_to_주문(self,instance):
        m1 = self.메뉴1_button.text.split(" ")[0]
        print(m1, dic_coffee_sum[m1], dic_coffee_cup[m1])
        m2 = self.메뉴2_button.text.split(" ")[0]
        print(m2, dic_coffee_sum[m2], dic_coffee_cup[m2])
        m3 = self.메뉴3_button.text.split(" ")[0]
        print(m3, dic_coffee_sum[m3], dic_coffee_cup[m3])
        m4 = self.메뉴4_button.text.split(" ")[0]
        print(m4, dic_coffee_sum[m4], dic_coffee_cup[m4])
        
            
    
    def go_to_뒤로(self,instance):
        # global 모든 전역변수 초기화 0으로
        self.메뉴1_button.text = ''
        self.메뉴2_button.text = ''
        self.메뉴3_button.text = ''
        self.메뉴4_button.text = ''
        self.메뉴5_button.text = ''
        self.메뉴6_button.text = ''
        self.메뉴7_button.text = ''
        for i in dic_coffee_sum.keys():
            dic_coffee_sum[i] = 0
            dic_coffee_cup[i] = 0
        for n in dic_beverage_sum.keys():
            dic_beverage_sum[n] = 0
            dic_beverage_cup[n] = 0
        self.manager.current = 'name_choose'
        self.scroll_view.scroll_y = 1
        

        
        
        
        
        

class GiftScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        welcome_label = Label(
            text="환영합니다! 선물 화면입니다.",
            font_name="NanumGothic",
            font_size=24
        )
        layout.add_widget(welcome_label)
        
        뒤로_button = Button(
            text="뒤로",
            font_name="NanumGothic",
            size_hint=(0.12, 0.08),
            pos_hint={"center_x": 0.5, "center_y": 0.06}
        )
        뒤로_button.bind(on_press = self.go_to_뒤로)
        layout.add_widget(뒤로_button)
        
        self.add_widget(layout)
        
    def go_to_뒤로(self,instance):
        self.manager.current = 'home'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(NamechooseScreen(name='name_choose'))
        sm.add_widget(OrderScreen(name='order'))
        sm.add_widget(GiftScreen(name='gift'))
        
        return sm
    
if __name__ == '__main__':
    app = MyApp()
    app.run()