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
import re
from kivy.uix.widget import Widget


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

주문_이름 = ""
mul = "\u00D7"

m1 = ''
m1_sum = 0
m2 = ''
m2_sum = 0
m3 = ''
m3_sum = 0
m4 = ''
m4_sum = 0
m5 = ''
m5_sum = 0
m6 = ''
m6_sum = 0
m7 = ''
m7_sum = 0

count = 1
check = 0

dic_coffee_sum = {"아메리카노" : 0, '에스프레소' : 0, '드립' : 0, '더치' : 0, '라떼' : 0, '더치라떼' : 0, '바닐라라떼' : 0, '민트라떼' : 0, '카푸치노' : 0,
           '콜드브루' : 0, '카페모카' : 0, '보리커피' : 0, '플렛화이트' : 0, '꼼빠냐' : 0, '아인슈페너' : 0, '아아A' : 0, '아아B' : 0, '뜨아A' : 0, '뜨아B' : 0,
           '(아샷추\u00D71)아아A' : 0,'(아샷추\u00D71)아아B' : 0, '(아샷추\u00D71)뜨아A' : 0, '(아샷추\u00D71)뜨아B' : 0, '(아샷추\u00D72)아아A' : 0,'(아샷추\u00D72)아아B' : 0, '(아샷추\u00D72)뜨아A' : 0, '(아샷추\u00D72)뜨아B' : 0,
           '(샷\u00D71)아아A' : 0,'(샷\u00D71)아아B' : 0, '(샷\u00D71)뜨아A' : 0, '(샷\u00D71)뜨아B' : 0, '(샷\u00D72)아아A' : 0,'(샷\u00D72)아아B' : 0, '(샷\u00D72)뜨아A' : 0, '(샷\u00D72)뜨아B' : 0,
           '(Ice)드립' : 0, '(Hot)드립' : 0, '(Ice)더치' : 0, '(Hot)더치' : 0, '(Ice)에스프레소' : 0, '(Hot)에스프레소' : 0,'(Ice)라떼' : 0, '(Hot)라떼' : 0, '(Ice)더치라떼' : 0, '(Hot)더치라떼' : 0, '(Ice)바닐라라떼' : 0, '(Hot)바닐라라떼' : 0,
           '(Ice)콜드브루' : 0, '(Hot)콜드브루' : 0,'(Ice)카페모카' : 0, '(Hot)카페모카' : 0,'(Ice)보리커피' : 0, '(Hot)보리커피' : 0,'(Ice)플렛화이트' : 0, '(Hot)플렛화이트' : 0, '(Ice)아인슈페너' : 0, '(Hot)아인슈페너' : 0}

dic_coffee_cup = {"아메리카노" : 0, '에스프레소' : 0, '드립' : 0, '더치' : 0, '라떼' : 0, '더치라떼' : 0, '바닐라라떼' : 0, '민트라떼' : 0, '카푸치노' : 0,
           '콜드브루' : 0, '카페모카' : 0, '보리커피' : 0, '플렛화이트' : 0, '꼼빠냐' : 0, '아인슈페너' : 0, '아아A' : 0, '아아B' : 0, '뜨아A' : 0, '뜨아B' : 0,
           '(아샷추\u00D71)아아A' : 0,'(아샷추\u00D71)아아B' : 0, '(아샷추\u00D71)뜨아A' : 0, '(아샷추\u00D71)뜨아B' : 0, '(아샷추\u00D72)아아A' : 0,'(아샷추\u00D72)아아B' : 0, '(아샷추\u00D72)뜨아A' : 0, '(아샷추\u00D72)뜨아B' : 0,
           '(샷\u00D71)아아A' : 0,'(샷\u00D71)아아B' : 0, '(샷\u00D71)뜨아A' : 0, '(샷\u00D71)뜨아B' : 0, '(샷\u00D72)아아A' : 0,'(샷\u00D72)아아B' : 0, '(샷\u00D72)뜨아A' : 0, '(샷\u00D72)뜨아B' : 0, '(Ice)드립' : 0, '(Hot)드립' : 0,
           '(Ice)더치' : 0, '(Hot)더치' : 0, '(Ice)에스프레소' : 0, '(Hot)에스프레소' : 0, '(Ice)라떼' : 0, '(Hot)라떼' : 0, '(Ice)더치라떼' : 0, '(Hot)더치라떼' : 0, '(Ice)바닐라라떼' : 0, '(Hot)바닐라라떼' : 0,
           '(Ice)콜드브루' : 0, '(Hot)콜드브루' : 0,'(Ice)카페모카' : 0, '(Hot)카페모카' : 0,'(Ice)보리커피' : 0, '(Hot)보리커피' : 0,'(Ice)플렛화이트' : 0, '(Hot)플렛화이트' : 0, '(Ice)아인슈페너' : 0, '(Hot)아인슈페너' : 0}

dic_beverage_sum = {'베리고' : 0, '망고스무디' : 0, '아보카도바나나' : 0, '망고바나나' : 0, '패션후르츠' : 0, '레몬에이드' : 0, '복숭아바질' : 0, '초코라떼' : 0,
                    'Hot초코' : 0, '자두에이드' : 0, '유자민트티' : 0, '미숫가루' : 0, '밀크티' : 0, '딸기라떼' : 0, '애플민트스무디' : 0,
                    '(Ice)초코라떼' : 0, '(Hot)초코라떼' : 0, '(Ice)밀크티' : 0, '(Hot)밀크티' : 0, '(Ice)미숫가루' : 0, '(Hot)미숫가루' : 0}

dic_beverage_cup = {'베리고' : 0, '망고스무디' : 0, '아보카도바나나' : 0, '망고바나나' : 0, '패션후르츠' : 0, '레몬에이드' : 0, '복숭아바질' : 0, '초코라떼' : 0,
                    'Hot초코' : 0, '자두에이드' : 0, '유자민트티' : 0, '미숫가루' : 0, '밀크티' : 0, '딸기라떼' : 0, '애플민트스무디' : 0,
                    '(Ice)초코라떼' : 0, '(Hot)초코라떼' : 0, '(Ice)밀크티' : 0, '(Hot)밀크티' : 0, '(Ice)미숫가루' : 0, '(Hot)미숫가루' : 0}

dic_etc_sum = {'제주누보' : 0, '레몬사와' : 0, '유자사와' : 0, '아사히' : 0, '탄산수' : 0, '쌍화탕' : 0, '포춘쿠키' : 0, '튀일쿠키' : 0, '브륄레' : 0,
               '캐모마일' : 0, '루이보스' : 0, '보이차' : 0, '페퍼민트' : 0, '레몬그라스' : 0, '라벤더' : 0}

dic_etc_cup = {'제주누보' : 0, '레몬사와' : 0, '유자사와' : 0, '아사히' : 0, '탄산수' : 0, '쌍화탕' : 0, '포춘쿠키' : 0, '튀일쿠키' : 0, '브륄레' : 0,
               '캐모마일' : 0, '루이보스' : 0, '보이차' : 0, '페퍼민트' : 0, '레몬그라스' : 0, '라벤더' : 0}

dic_menu_price = {"아메리카노" : 2500, '에스프레소' : 2500, '드립' : 4000, '더치' : 3500, '라떼' : 3000, '더치라떼' : 4000, '바닐라라떼' : 3500, '민트라떼' : 4000, '카푸치노' : 3000,
           '콜드브루' : 3000, '카페모카' : 3500, '보리커피' : 2500, '플렛화이트' : 3000, '꼼빠냐' : 3500, '아인슈페너' : 4000, '베리고' : 4000, '망고스무디' : 4000, '아보카도바나나' : 3500,
           '망고바나나' : 4000, '패션후르츠' : 3500, '레몬에이드' : 3500, '복숭아바질' : 3500, '초코라떼' : 3500,
                    'Hot초코' : 3500, '자두에이드' : 3500, '유자민트티' : 4000, '미숫가루' : 3500, '밀크티' : 3000, '딸기라떼' : 3500, '애플민트스무디' : 3500,
                    '제주누보' : 3000, '레몬사와' : 3000, '유자사와' : 3000, '아사히' : 3000, '탄산수' : 500, '쌍화탕' : 1700, '포춘쿠키' : 1000, '튀일쿠키' : 2000, '브륄레' : 3000,
               '캐모마일' : 2500, '루이보스' : 2500, '보이차' : 2500, '페퍼민트' : 2500, '레몬그라스' : 2500, '라벤더' : 2500, '아아A' : 2500, '아아B' : 2500, '뜨아A' : 2500, '뜨아B' : 2500,
           '(아샷추\u00D71)아아A' : 3000,'(아샷추\u00D71)아아B' : 3000, '(아샷추\u00D71)뜨아A' : 3000, '(아샷추\u00D71)뜨아B' : 3000, '(아샷추\u00D72)아아A' : 3500,'(아샷추\u00D72)아아B' : 3500, '(아샷추\u00D72)뜨아A' : 3500, '(아샷추\u00D72)뜨아B' : 3500,
           '(샷\u00D71)아아A' : 3000,'(샷\u00D71)아아B' : 3000, '(샷\u00D71)뜨아A' : 3000, '(샷\u00D71)뜨아B' : 3000, '(샷\u00D72)아아A' : 3500,'(샷\u00D72)아아B' : 3500, '(샷\u00D72)뜨아A' : 3500, '(샷\u00D72)뜨아B' : 3500,
           '(Ice)드립' : 4000, '(Hot)드립' : 4000, '(Ice)더치' : 3500, '(Hot)더치' : 3500,'(Ice)에스프레소' : 2500, '(Hot)에스프레소' : 2500, '(Ice)라떼' : 3000, '(Hot)라떼' : 3000, '(Ice)더치라떼' : 4000, '(Hot)더치라떼' : 4000, '(Ice)바닐라라떼' : 3500, '(Hot)바닐라라떼' : 3500,
           '(Ice)콜드브루' : 3000, '(Hot)콜드브루' : 3000,'(Ice)카페모카' : 3500, '(Hot)카페모카' : 3500,'(Ice)보리커피' : 2500, '(Hot)보리커피' : 2500,'(Ice)플렛화이트' : 3000, '(Hot)플렛화이트' : 3000, '(Ice)아인슈페너' : 4000, '(Hot)아인슈페너' : 4000,
           '(Ice)초코라떼' : 3500, '(Hot)초코라떼' : 3500, '(Ice)밀크티' : 3000, '(Hot)밀크티' : 3000, '(Ice)미숫가루' : 3500, '(Hot)미숫가루' : 3500}


def fetch_data(a):
    print(주문_이름)
    url = "http://134.185.107.112:5000/finall"

    data = {
            "name" : a
        }

    response = requests.post(url, json=data,timeout=2)    
    response_data = response.json()
    gift_value = response_data.get("gift")
    return gift_value


def fetch_pay_data():
    url = "http://134.185.107.112:5000/pay"
    response = requests.post(url)    
    response_data = response.json()
    pay = response_data.get("pay")
    return pay

def fetch_log_data():
    url = "http://134.185.107.112:5000/log"
    response = requests.post(url)    
    response_data = response.json()
    log = response_data.get("log")
    return log
    
def pay_to_db(pay):
    url = "http://134.185.107.112:5000/pay_to_db"
    data = {"pay" : pay}
    response = requests.post(url, json=data,timeout=2)    
    response_data = response.json()
    pay = response_data.get("pay")
    return pay

def gift_to_db(gift,name):
    url = "http://134.185.107.112:5000/gift_to_db"
    data = {"gift" : gift,
            "name" : name}
    response = requests.post(url, json=data,timeout=2)    
    response_data = response.json()
    pay = response_data.get("name")
    return pay

def most_to_db(name, most):
    url = "http://134.185.107.112:5000/most_to_db"
    data = {"most" : most,
            "name" : name}  
    response = requests.post(url, json=data,timeout=2)    
    response_data = response.json()
    pay = response_data.get("name")
    return pay
    
def jumoon_log_to_db(log):
    url = "http://134.185.107.112:5000/log_to_db"
    data = {
        "log" : log
    }
    response = requests.post(url, json=data,timeout=2)    
    response_data = response.json()
    pay = response_data.get("name")
    return pay
    
    
    



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
        
        url = "http://134.185.107.112:5000/login_button_click"

        data = {
            "password": password
        }
        try : 
            
            response = requests.post(url, json=data,timeout=2)
            
        
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
            size_hint = (0.37,0.2),
            pos_hint={"x": 0.1, "y": 0.45}
        )
        
        주문_button.bind(on_press = self.go_to_주문화면)
        layout.add_widget(주문_button)

        기록_button = Button(
            text="주문기록",
            font_name="NanumGothic",
            size_hint = (0.37,0.2),
            pos_hint={"x": 0.5, "y": 0.45}
        )
        
        기록_button.bind(on_press = self.go_to_기록화면)
        layout.add_widget(기록_button)
        
        self.add_widget(layout)
        
        
    
    def go_to_주문화면(self, instance):
        self.manager.current = 'jumoon'
    
    def go_to_기록화면(self, instance):
        self.manager.current = 'log'
        
        
class Jumoon_choose(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
           
        실시간주문_button = Button(
            text="실시간_주문",
            font_name="NanumGothic",
            size_hint = (0.37,0.2),
            pos_hint={"x": 0.1, "y": 0.45}
        )
        
        실시간주문_button.bind(on_press = self.go_to_실시간주문화면)
        layout.add_widget(실시간주문_button)

        기록용주문_button = Button(
            text="기록용_주문",
            font_name="NanumGothic",
            size_hint = (0.37,0.2),
            pos_hint={"x": 0.5, "y": 0.45}
        )
        
        기록용주문_button.bind(on_press = self.go_to_기록용주문화면)
        layout.add_widget(기록용주문_button)
        
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
            width=200
        )
        뒤로_button.bind(on_press=self.go_to_뒤로)
        back_layout.add_widget(뒤로_button)
        
        layout.add_widget(back_layout)
        
        self.add_widget(layout)
        
        
    def go_to_뒤로(self, instance):
        self.manager.current = 'home'
        
    def go_to_실시간주문화면(self, instance):
        self.manager.current = 'live_name_choose'
    
    def go_to_기록용주문화면(self, instance):
        self.manager.current = 'name_choose'
        
class NamechooseScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.items = ["오주현", "오세현", "김향", "박세범", "윤자", "송송이", "정태오","바태","고유진","김서인","서윤구","고유빈"]
        self.filtered_items = self.items

        # BoxLayout의 padding을 늘려서 화면에 여유 공간을 추가합니다.
        root_layout = BoxLayout(orientation="vertical", padding=[0, 0, 0, 20], spacing=20)  # 위쪽 padding을 50으로 추가
        
        back_layout = BoxLayout(
            size_hint=(1, 0.15),  # 가로 전체, 세로 10%
            pos_hint={"left": 0.5, "top": 1},  # 화면 상단
            orientation="horizontal",
            padding=(5, 0, 5, 10),
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
        
        root_layout.add_widget(back_layout)
        root_layout.add_widget(Widget(size_hint=(1, 0.15)))

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

    def go_to_뒤로(self, instance):
        self.manager.current = 'jumoon'
        
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
        selected_name = instance.text
        global 주문_이름
        주문_이름 = selected_name
        self.search_input.text = ''
        self.manager.current = 'order'
        
        
class Live_NamechooseScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.items = ["오주현", "오세현", "김향", "박세범", "윤자", "송송이", "정태오","바태","고유진","김서인","서윤구","고유빈"]
        self.filtered_items = self.items

        # BoxLayout의 padding을 늘려서 화면에 여유 공간을 추가합니다.
        root_layout = BoxLayout(orientation="vertical", padding=[0, 0, 0, 20], spacing=20)  # 위쪽 padding을 50으로 추가
        
        back_layout = BoxLayout(
            size_hint=(1, 0.15),  # 가로 전체, 세로 10%
            pos_hint={"left": 0.5, "top": 1},  # 화면 상단
            orientation="horizontal",
            padding=(5, 0, 5, 10),
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
        
        root_layout.add_widget(back_layout)
        root_layout.add_widget(Widget(size_hint=(1, 0.15)))

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

    def go_to_뒤로(self, instance):
        self.manager.current = 'jumoon'
        
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
        selected_name = instance.text
        global 주문_이름
        주문_이름 = selected_name
        self.search_input.text = ''
        self.manager.current = 'live_order'
    
        

class OrderScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.last_selected = None
        self.last_selected2 = None
        
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
        에스프레소_button.bind(on_press =lambda instance, name='에스프레소': self.에스_open_popup(name,instance))
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
        드립_button.bind(on_press =lambda instance, name='드립': self.드립_open_popup(name,instance))
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
        더치_button.bind(on_press =lambda instance, name='더치': self.더치_open_popup(name,instance))
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
        라떼_button.bind(on_press =lambda instance, name='라떼': self.라떼_open_popup(name,instance))
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
        더치라떼_button.bind(on_press =lambda instance, name='더치라떼': self.더치라떼_open_popup(name,instance))
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
        바닐라라떼_button.bind(on_press =lambda instance, name='바닐라라떼': self.바닐라라떼_open_popup(name,instance))
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
        민트라떼종류_button.bind(on_press =lambda instance, name='민트라떼': self.민트라떼종류_open_popup(name,instance))
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
        카푸치노_button.bind(on_press =lambda instance, name='카푸치노': self.카푸치노_open_popup(name,instance))
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
        콜드브루_button.bind(on_press =lambda instance, name='콜드브루': self.콜드브루_open_popup(name,instance))
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
        카페모카_button.bind(on_press =lambda instance, name='카페모카': self.카페모카_open_popup(name,instance))
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
        보리커피_button.bind(on_press =lambda instance, name='보리커피': self.보리커피_open_popup(name,instance))
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
        플렛화이트_button.bind(on_press =lambda instance, name='플렛화이트': self.플렛화이트_open_popup(name,instance))
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
        꼼빠냐_button.bind(on_press =lambda instance, name='꼼빠냐': self.꼼빠냐_open_popup(name,instance))
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
        아인슈페너_button.bind(on_press =lambda instance, name='아인슈페너': self.아인슈페너_open_popup(name,instance))
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
        베리고_button.bind(on_press =lambda instance, name='베리고': self.베리고_open_popup(name,instance))
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
        망고스무디_button.bind(on_press =lambda instance, name='망고스무디': self.망고스무디_open_popup(name,instance))
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
        아보카도바나나_button.bind(on_press =lambda instance, name='아보카도바나나': self.아보카도바나나_open_popup(name,instance))
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
        망고바나나_button.bind(on_press =lambda instance, name='망고바나나': self.망고바나나_open_popup(name,instance))
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
        패션후르츠에이드_button.bind(on_press =lambda instance, name='패션후르츠': self.패션후르츠_open_popup(name,instance))
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
        레몬에이드_button.bind(on_press =lambda instance, name='레몬에이드': self.레몬에이드_open_popup(name,instance))
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
        복숭아바질에이드_button.bind(on_press =lambda instance, name='복숭아바질': self.복숭아바질_open_popup(name,instance))
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
        초코라떼_button.bind(on_press =lambda instance, name='초코라떼': self.초코라떼_open_popup(name,instance))
        menu_layout.add_widget(초코라떼_button)
        
        Hot초코_button = Button(
            text="Hot초코\n\n\u20A93,500",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        Hot초코_button.bind(on_press =lambda instance, name='Hot초코': self.Hot초코_open_popup(name,instance))
        menu_layout.add_widget(Hot초코_button)
        
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
        자두에이드_button.bind(on_press =lambda instance, name='자두에이드': self.자두에이드_open_popup(name,instance))
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
        유자민트티_button.bind(on_press =lambda instance, name='유자민트티': self.유자민트티_open_popup(name,instance))
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
        미숫가루_button.bind(on_press =lambda instance, name='미숫가루': self.미숫가루_open_popup(name,instance))
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
        밀크티_button.bind(on_press =lambda instance, name='밀크티': self.밀크티_open_popup(name,instance))
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
        딸기라떼_button.bind(on_press =lambda instance, name='딸기라떼': self.딸기라떼_open_popup(name,instance))
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
        애플민트스무디_button.bind(on_press =lambda instance, name='애플민트스무디': self.애플민트스무디_open_popup(name,instance))
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
        제주누보_button.bind(on_press =lambda instance, name='제주누보': self.제주누보_open_popup(name,instance))
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
        레몬사와_button.bind(on_press =lambda instance, name='레몬사와': self.레몬사와_open_popup(name,instance))
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
        유자사와_button.bind(on_press =lambda instance, name='유자사와': self.유자사와_open_popup(name,instance))
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
        아사히_button.bind(on_press =lambda instance, name='아사히': self.아사히_open_popup(name,instance))
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
        탄산수_button.bind(on_press =lambda instance, name='탄산수': self.탄산수_open_popup(name,instance))
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
        쌍화탕_button.bind(on_press =lambda instance, name='쌍화탕': self.쌍화탕_open_popup(name,instance))
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
        포춘쿠키_button.bind(on_press =lambda instance, name='포춘쿠키': self.포춘쿠키_open_popup(name,instance))
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
        튀일쿠키_button.bind(on_press =lambda instance, name='튀일쿠키': self.튀일쿠키_open_popup(name,instance))
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
        브륄레_button.bind(on_press =lambda instance, name='브륄레': self.브륄레_open_popup(name,instance))
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
        캐모마일_button.bind(on_press =lambda instance, name='캐모마일': self.캐모마일_open_popup(name,instance))
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
        루이보스_button.bind(on_press =lambda instance, name='루이보스': self.루이보스_open_popup(name,instance))
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
        보이차_button.bind(on_press =lambda instance, name='보이차': self.보이차_open_popup(name,instance))
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
        페퍼민트차_button.bind(on_press =lambda instance, name='페퍼민트': self.페퍼민트_open_popup(name,instance))
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
        레몬그라스_button.bind(on_press =lambda instance, name='레몬그라스': self.레몬그라스_open_popup(name,instance))
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
        라벤더_button.bind(on_press =lambda instance, name='라벤더': self.라벤더_open_popup(name,instance))
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
        
        self.알림창 = Label(
            text="",
            font_name="NanumGothic",
            size_hint=(1, 0.2),
            font_size=sp(16),
            color=(1, 0, 0, 1),  # 빨간색 텍스트
            pos_hint={"center_x": 0.5, "y": 0.5}
        )
        back_layout.add_widget(self.알림창)
        
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
            text="Hot!",
            font_name="NanumGothic",
            size_hint=(0.2, 0.07),  # 버튼 크기
            pos_hint={'x': 0.3, 'y': 0.6},  # y 값을 조정하여 버튼 위치 설정
            group='온도'
        )
        self.아아_button = ToggleButton(
            text="Ice!",
            font_name="NanumGothic",
            size_hint=(0.2, 0.07),
            pos_hint={'x': 0.6, 'y': 0.6},
            group='온도'
        )
        
        self.따아_button.bind(on_press=lambda instance: self.record_selection(instance))
        self.아아_button.bind(on_press=lambda instance: self.record_selection(instance))
        
        content.add_widget(self.따아_button)
        content.add_widget(self.아아_button)
        
        self.A_button = ToggleButton(
            text="A",
            font_name="NanumGothic",
            size_hint=(0.2, 0.07),  # 버튼 크기
            pos_hint={'x': 0.3, 'y': 0.5},  # y 값을 조정하여 버튼 위치 설정
            group='온도'
        )
        self.B_button = ToggleButton(
            text="B",
            font_name="NanumGothic",
            size_hint=(0.2, 0.07),
            pos_hint={'x': 0.6, 'y': 0.5},
            group='온도'
        )
        
        self.A_button.bind(on_press=lambda instance: self.record_selection(instance))
        self.B_button.bind(on_press=lambda instance: self.record_selection(instance))
        
        content.add_widget(self.A_button)
        content.add_widget(self.B_button)

        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.15, 0.15),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.15, 0.15), pos_hint={'x': 0.85, 'y': 0}, on_press=lambda _ : self.go_to_아메리카노(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.9, 0.7),
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
        
    def 초코라떼_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_초코라떼(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def Hot초코_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_Hot초코(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def 자두에이드_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_자두에이드(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def 유자민트티_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_유자민트티(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def 미숫가루_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_미숫가루(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def 밀크티_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_밀크티(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def 딸기라떼_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_딸기라떼(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def 애플민트스무디_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_애플민트스무디(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()

    def 제주누보_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_제주누보(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()

    def 레몬사와_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_레몬사와(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def 유자사와_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_유자사와(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def 아사히_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_아사히(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def 탄산수_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_탄산수(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()

    def 쌍화탕_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_쌍화탕(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()

    def 포춘쿠키_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_포춘쿠키(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def 튀일쿠키_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_튀일쿠키(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def 브륄레_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_브륄레(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()

    def 캐모마일_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_캐모마일(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def 루이보스_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_루이보스(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def 보이차_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_보이차(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def 페퍼민트_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_페퍼민트차(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def 레몬그라스_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_레몬그라스(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def 라벤더_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_라벤더(instance)))
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
        if menu_name == "[장바구니] ":
            pass
        else :
            content = FloatLayout()
            content.add_widget(Label(font_name="NanumGothic",font_size=sp(26), pos_hint={'center_x': 0.5, 'y': 0.45}, text=menu_name))
            수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.5},text="[수량]")
            content.add_widget(수량)
        
        
            self.a = instance.text.split(" ")[0]
            self.b = 0
            if self.a in dic_coffee_sum.keys():
                self.b = dic_coffee_cup[self.a]
            elif self.a in dic_beverage_sum.keys():
                self.b = dic_beverage_cup[self.a]
            elif self.a in dic_etc_sum.keys():
                self.b = dic_etc_cup[self.a]
            
            self.cup = Label(
                font_name="NanumGothic",
                font_size=sp(18),
                size_hint=(None, None), 
                size=(100, 50),  
                pos_hint={'center_x': 0.5, 'y': 0.32},  # y를 조정하여 버튼 아래로 위치
                text=str(self.b)
                )
            content.add_widget(self.cup)

            content.add_widget(Button(text="정정", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_정정(instance)))
            content.add_widget(Button(text="삭제", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_삭제(instance)))
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
        elif self.a in dic_etc_cup.keys():
            dic_etc_cup[self.a] += 1
            self.cup.text = str(dic_etc_cup[self.a])
            
    def minus_2(self, instance):
        global dic_beverage_cup,dic_coffee_cup
        if int(self.cup.text) > 1:
            if self.a in dic_beverage_cup.keys():
                dic_beverage_cup[self.a] -= 1
                self.cup.text = str(dic_beverage_cup[self.a])
            elif self.a in dic_coffee_cup.keys():
                dic_coffee_cup[self.a] -= 1
                self.cup.text = str(dic_coffee_cup[self.a])
            elif self.a in dic_etc_cup.keys():
                dic_etc_cup[self.a] -= 1
                self.cup.text = str(dic_etc_cup[self.a])
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
        elif self.a in dic_etc_cup.keys():
            dic_etc_cup[self.a] = 0
            dic_etc_sum[self.a] = 0

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
            
        elif self.a in dic_etc_cup.keys():
            instance.text = instance.text.split(" ")[0] + " " + str(dic_etc_cup[self.a])
            dic_etc_sum[self.a] = dic_menu_price[self.a] * dic_etc_cup[self.a]
            self.popup.dismiss()
    
    def go_to_아메리카노(self,instance):
        global count,dic_coffee_sum,dic_coffee_cup
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if "아메리카노" in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_coffee_sum["아메리카노"] += (2500 * count)
            dic_coffee_cup["아메리카노"] += count
            #self.메뉴1_button.text = f"아메리카노 {아메리카노_잔수}"
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"아메리카노 {dic_coffee_cup['아메리카노']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"아메리카노 {dic_coffee_cup['아메리카노']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"아메리카노 {dic_coffee_cup['아메리카노']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"아메리카노 {dic_coffee_cup['아메리카노']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"아메리카노 {dic_coffee_cup['아메리카노']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"아메리카노 {dic_coffee_cup['아메리카노']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"아메리카노 {dic_coffee_cup['아메리카노']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
            print(f"{dic_coffee_sum['아메리카노']} {dic_coffee_cup['아메리카노']}")
        
    def go_to_에스프레소(self,instance):
        global count,dic_coffee_sum,dic_coffee_cup
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '에스프레소' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_coffee_sum['에스프레소'] += (2500 * count)
            dic_coffee_cup['에스프레소'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"에스프레소 {dic_coffee_cup['에스프레소']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"에스프레소 {dic_coffee_cup['에스프레소']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"에스프레소 {dic_coffee_cup['에스프레소']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"에스프레소 {dic_coffee_cup['에스프레소']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"에스프레소 {dic_coffee_cup['에스프레소']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"에스프레소 {dic_coffee_cup['에스프레소']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"에스프레소 {dic_coffee_cup['에스프레소']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
            print(f"{dic_coffee_sum['에스프레소']} {dic_coffee_cup['에스프레소']}")
            
    
    def go_to_드립(self,instance):
        global count,dic_coffee_cup,dic_coffee_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '드립' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_coffee_sum['드립'] += (4000 * count)
            dic_coffee_cup['드립']+= count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"드립 {dic_coffee_cup['드립']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"드립 {dic_coffee_cup['드립']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"드립 {dic_coffee_cup['드립']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"드립 {dic_coffee_cup['드립']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"드립 {dic_coffee_cup['드립']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"드립 {dic_coffee_cup['드립']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"드립 {dic_coffee_cup['드립']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
            print(f"{dic_coffee_sum['드립']} {dic_coffee_cup['드립']}")
        
    def go_to_더치(self,instance):
        global count,dic_coffee_cup,dic_coffee_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '더치' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_coffee_sum['더치'] += (3500 * count)
            dic_coffee_cup['더치'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"더치 {dic_coffee_cup['더치']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"더치 {dic_coffee_cup['더치']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"더치 {dic_coffee_cup['더치']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"더치 {dic_coffee_cup['더치']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"더치 {dic_coffee_cup['더치']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"더치 {dic_coffee_cup['더치']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"더치 {dic_coffee_cup['더치']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
            print(f"{dic_coffee_sum['더치']} {dic_coffee_cup['더치']}")
        
    def go_to_라떼(self,instance):
        global count,dic_coffee_cup,dic_coffee_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '라떼' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_coffee_sum['라떼'] += (3000 * count)
            dic_coffee_cup['라떼'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"라떼 {dic_coffee_cup['라떼']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"라떼 {dic_coffee_cup['라떼']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"라떼 {dic_coffee_cup['라떼']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"라떼 {dic_coffee_cup['라떼']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"라떼 {dic_coffee_cup['라떼']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"라떼 {dic_coffee_cup['라떼']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"라떼 {dic_coffee_cup['라떼']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
            print(f"{dic_coffee_sum['라떼']} {dic_coffee_cup['라떼']}")
        
    def go_to_더치라떼(self,instance):
        global count,dic_coffee_sum,dic_coffee_cup
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '더치라떼' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_coffee_sum['더치라떼'] += (4000 * count)
            dic_coffee_cup['더치라떼'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"더치라떼 {dic_coffee_cup['더치라떼']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"더치라떼 {dic_coffee_cup['더치라떼']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"더치라떼 {dic_coffee_cup['더치라떼']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"더치라떼 {dic_coffee_cup['더치라떼']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"더치라떼 {dic_coffee_cup['더치라떼']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"더치라떼 {dic_coffee_cup['더치라떼']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"더치라떼 {dic_coffee_cup['더치라떼']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
            print(f"{dic_coffee_sum['더치라떼']} {dic_coffee_cup['더치라떼']}")
        
    def go_to_바닐라라떼(self,instance):
        global count,dic_coffee_sum,dic_coffee_cup
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '바닐라라떼' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_coffee_sum['바닐라라떼'] += (3500 * count)
            dic_coffee_cup['바닐라라떼'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"바닐라라떼 {dic_coffee_cup['바닐라라떼']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"바닐라라떼 {dic_coffee_cup['바닐라라떼']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"바닐라라떼 {dic_coffee_cup['바닐라라떼']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"바닐라라떼 {dic_coffee_cup['바닐라라떼']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"바닐라라떼 {dic_coffee_cup['바닐라라떼']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"바닐라라떼 {dic_coffee_cup['바닐라라떼']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"바닐라라떼 {dic_coffee_cup['바닐라라떼']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
            print(f"{dic_coffee_sum['바닐라라떼']} {dic_coffee_cup['바닐라라떼']}")
        
    def go_to_민트라떼종류(self,instance):
        global count,dic_coffee_sum,dic_coffee_cup
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '민트라떼' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_coffee_sum['민트라떼'] += (4000 * count)
            dic_coffee_cup['민트라떼'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"민트라떼 {dic_coffee_cup['민트라떼']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"민트라떼 {dic_coffee_cup['민트라떼']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"민트라떼 {dic_coffee_cup['민트라떼']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"민트라떼 {dic_coffee_cup['민트라떼']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"민트라떼 {dic_coffee_cup['민트라떼']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"민트라떼 {dic_coffee_cup['민트라떼']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"민트라떼 {dic_coffee_cup['민트라떼']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
            print(f"{dic_coffee_sum['민트라떼']} {dic_coffee_cup['민트라떼']}")
            
    def go_to_카푸치노(self,instance):
        global count,dic_coffee_cup,dic_coffee_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '카푸치노' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_coffee_sum['카푸치노'] += (3000 * count)
            dic_coffee_cup['카푸치노'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"카푸치노 {dic_coffee_cup['카푸치노']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"카푸치노 {dic_coffee_cup['카푸치노']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"카푸치노 {dic_coffee_cup['카푸치노']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"카푸치노 {dic_coffee_cup['카푸치노']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"카푸치노 {dic_coffee_cup['카푸치노']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"카푸치노 {dic_coffee_cup['카푸치노']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"카푸치노 {dic_coffee_cup['카푸치노']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
            print(f"{dic_coffee_sum['카푸치노']} {dic_coffee_cup['카푸치노']}")
        
    def go_to_콜드브루(self,instance):
        global count,dic_coffee_cup,dic_coffee_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '콜드브루' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_coffee_sum['콜드브루'] += (3000 * count)
            dic_coffee_cup['콜드브루'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"콜드브루 {dic_coffee_cup['콜드브루']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"콜드브루 {dic_coffee_cup['콜드브루']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"콜드브루 {dic_coffee_cup['콜드브루']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"콜드브루 {dic_coffee_cup['콜드브루']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"콜드브루 {dic_coffee_cup['콜드브루']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"콜드브루 {dic_coffee_cup['콜드브루']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"콜드브루 {dic_coffee_cup['콜드브루']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
            print(f"{dic_coffee_sum['콜드브루']} {dic_coffee_cup['콜드브루']}")
    
    def go_to_카페모카(self,instance):
        global count,dic_coffee_cup,dic_coffee_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '카페모카' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_coffee_sum['카페모카'] += (3500 * count)
            dic_coffee_cup['카페모카'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"카페모카 {dic_coffee_cup['카페모카']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"카페모카 {dic_coffee_cup['카페모카']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"카페모카 {dic_coffee_cup['카페모카']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"카페모카 {dic_coffee_cup['카페모카']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"카페모카 {dic_coffee_cup['카페모카']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"카페모카 {dic_coffee_cup['카페모카']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"카페모카 {dic_coffee_cup['카페모카']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
            print(f"{dic_coffee_sum['카페모카']} {dic_coffee_cup['카페모카']}")
        
    def go_to_보리커피(self,instance):
        global count,dic_coffee_cup,dic_coffee_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '보리커피' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_coffee_sum['보리커피'] += (2500 * count)
            dic_coffee_cup['보리커피'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"보리커피 {dic_coffee_cup['보리커피']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"보리커피 {dic_coffee_cup['보리커피']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"보리커피 {dic_coffee_cup['보리커피']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"보리커피 {dic_coffee_cup['보리커피']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"보리커피 {dic_coffee_cup['보리커피']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"보리커피 {dic_coffee_cup['보리커피']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"보리커피 {dic_coffee_cup['보리커피']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
            print(f"{dic_coffee_sum['보리커피']} {dic_coffee_cup['보리커피']}")
        
    def go_to_플렛화이트(self,instance):
        global count,dic_coffee_cup,dic_coffee_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '플렛화이트' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_coffee_sum['플렛화이트'] += (3000 * count)
            dic_coffee_cup['플렛화이트'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"플렛화이트 {dic_coffee_cup['플렛화이트']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"플렛화이트 {dic_coffee_cup['플렛화이트']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"플렛화이트 {dic_coffee_cup['플렛화이트']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"플렛화이트 {dic_coffee_cup['플렛화이트']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"플렛화이트 {dic_coffee_cup['플렛화이트']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"플렛화이트 {dic_coffee_cup['플렛화이트']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"플렛화이트 {dic_coffee_cup['플렛화이트']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
            print(f"{dic_coffee_sum['플렛화이트']} {dic_coffee_cup['플렛화이트']}")

    def go_to_꼼빠냐(self,instance):
        global count,dic_coffee_cup,dic_coffee_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '꼼빠냐' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_coffee_sum['꼼빠냐'] += (3500 * count)
            dic_coffee_cup['꼼빠냐'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"꼼빠냐 {dic_coffee_cup['꼼빠냐']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"꼼빠냐 {dic_coffee_cup['꼼빠냐']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"꼼빠냐 {dic_coffee_cup['꼼빠냐']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"꼼빠냐 {dic_coffee_cup['꼼빠냐']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"꼼빠냐 {dic_coffee_cup['꼼빠냐']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"꼼빠냐 {dic_coffee_cup['꼼빠냐']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"꼼빠냐 {dic_coffee_cup['꼼빠냐']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
            print(f"{dic_coffee_sum['꼼빠냐']} {dic_coffee_cup['꼼빠냐']}")
        
    def go_to_아인슈페너(self,instance):
        global count,dic_coffee_cup,dic_coffee_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '아인슈페너' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_coffee_sum['아인슈페너'] += (4000 * count)
            dic_coffee_cup['아인슈페너'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"아인슈페너 {dic_coffee_cup['아인슈페너']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"아인슈페너 {dic_coffee_cup['아인슈페너']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"아인슈페너 {dic_coffee_cup['아인슈페너']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"아인슈페너 {dic_coffee_cup['아인슈페너']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"아인슈페너 {dic_coffee_cup['아인슈페너']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"아인슈페너 {dic_coffee_cup['아인슈페너']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"아인슈페너 {dic_coffee_cup['아인슈페너']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
            print(f"{dic_coffee_sum['아인슈페너']} {dic_coffee_cup['아인슈페너']}")
        
    def go_to_베리고(self,instance):
        global count,dic_beverage_cup,dic_beverage_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '베리고' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_beverage_sum['베리고'] += (4000 * count)
            dic_beverage_cup['베리고'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"베리고 {dic_beverage_cup['베리고']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"베리고 {dic_beverage_cup['베리고']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"베리고 {dic_beverage_cup['베리고']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"베리고 {dic_beverage_cup['베리고']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"베리고 {dic_beverage_cup['베리고']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"베리고 {dic_beverage_cup['베리고']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"베리고 {dic_beverage_cup['베리고']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_망고스무디(self,instance):
        global count,dic_beverage_cup,dic_beverage_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '망고스무디' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_beverage_sum['망고스무디'] += (4000 * count)
            dic_beverage_cup['망고스무디'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"망고스무디 {dic_beverage_cup['망고스무디']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"망고스무디 {dic_beverage_cup['망고스무디']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"망고스무디 {dic_beverage_cup['망고스무디']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"망고스무디 {dic_beverage_cup['망고스무디']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"망고스무디 {dic_beverage_cup['망고스무디']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"망고스무디 {dic_beverage_cup['망고스무디']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"망고스무디 {dic_beverage_cup['망고스무디']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_아보카도바나나(self,instance):
        global count,dic_beverage_cup,dic_beverage_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '아보카도바나나' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_beverage_sum['아보카도바나나'] += (3500 * count)
            dic_beverage_cup['아보카도바나나'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"아보카도바나나 {dic_beverage_cup['아보카도바나나']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"아보카도바나나 {dic_beverage_cup['아보카도바나나']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"아보카도바나나 {dic_beverage_cup['아보카도바나나']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"아보카도바나나 {dic_beverage_cup['아보카도바나나']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"아보카도바나나 {dic_beverage_cup['아보카도바나나']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"아보카도바나나 {dic_beverage_cup['아보카도바나나']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"아보카도바나나 {dic_beverage_cup['아보카도바나나']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_망고바나나(self,instance):
        global count,dic_beverage_cup,dic_beverage_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '망고바나나' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_beverage_sum['망고바나나'] += (4000 * count)
            dic_beverage_cup['망고바나나'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"망고바나나 {dic_beverage_cup['망고바나나']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"망고바나나 {dic_beverage_cup['망고바나나']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"망고바나나 {dic_beverage_cup['망고바나나']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"망고바나나 {dic_beverage_cup['망고바나나']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"망고바나나 {dic_beverage_cup['망고바나나']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"망고바나나 {dic_beverage_cup['망고바나나']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"망고바나나 {dic_beverage_cup['망고바나나']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_패션후르츠(self,instance):
        global count,dic_beverage_cup,dic_beverage_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '패션후르츠' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_beverage_sum['패션후르츠'] += (3500 * count)
            dic_beverage_cup['패션후르츠'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"패션후르츠 {dic_beverage_cup['패션후르츠']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"패션후르츠 {dic_beverage_cup['패션후르츠']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"패션후르츠 {dic_beverage_cup['패션후르츠']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"패션후르츠 {dic_beverage_cup['패션후르츠']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"패션후르츠 {dic_beverage_cup['패션후르츠']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"패션후르츠 {dic_beverage_cup['패션후르츠']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"패션후르츠 {dic_beverage_cup['패션후르츠']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_레몬에이드(self,instance):
        global count,dic_beverage_cup,dic_beverage_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '레몬에이드' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_beverage_sum['레몬에이드'] += (3500 * count)
            dic_beverage_cup['레몬에이드'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"레몬에이드 {dic_beverage_cup['레몬에이드']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"레몬에이드 {dic_beverage_cup['레몬에이드']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"레몬에이드 {dic_beverage_cup['레몬에이드']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"레몬에이드 {dic_beverage_cup['레몬에이드']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"레몬에이드 {dic_beverage_cup['레몬에이드']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"레몬에이드 {dic_beverage_cup['레몬에이드']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"레몬에이드 {dic_beverage_cup['레몬에이드']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_복숭아바질(self,instance):
        global count,dic_beverage_cup,dic_beverage_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '복숭아바질' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_beverage_sum['복숭아바질'] += (3500 * count)
            dic_beverage_cup['복숭아바질'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"복숭아바질 {dic_beverage_cup['복숭아바질']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"복숭아바질 {dic_beverage_cup['복숭아바질']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"복숭아바질 {dic_beverage_cup['복숭아바질']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"복숭아바질 {dic_beverage_cup['복숭아바질']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"복숭아바질 {dic_beverage_cup['복숭아바질']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"복숭아바질 {dic_beverage_cup['복숭아바질']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"복숭아바질 {dic_beverage_cup['복숭아바질']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_초코라떼(self,instance):
        global count,dic_beverage_cup,dic_beverage_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '초코라떼' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_beverage_sum['초코라떼'] += (3500 * count)
            dic_beverage_cup['초코라떼'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"초코라떼 {dic_beverage_cup['초코라떼']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"초코라떼 {dic_beverage_cup['초코라떼']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"초코라떼 {dic_beverage_cup['초코라떼']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"초코라떼 {dic_beverage_cup['초코라떼']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"초코라떼 {dic_beverage_cup['초코라떼']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"초코라떼 {dic_beverage_cup['초코라떼']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"초코라떼 {dic_beverage_cup['초코라떼']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_Hot초코(self,instance):
        global count,dic_beverage_cup,dic_beverage_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if 'Hot초코' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_beverage_sum['Hot초코'] += (3500 * count)
            dic_beverage_cup['Hot초코'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"Hot초코 {dic_beverage_cup['Hot초코']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"Hot초코 {dic_beverage_cup['Hot초코']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"Hot초코 {dic_beverage_cup['Hot초코']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"Hot초코 {dic_beverage_cup['Hot초코']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"Hot초코 {dic_beverage_cup['Hot초코']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"Hot초코 {dic_beverage_cup['Hot초코']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"Hot초코 {dic_beverage_cup['Hot초코']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_자두에이드(self,instance):
        global count,dic_beverage_cup,dic_beverage_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '자두에이드' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_beverage_sum['자두에이드'] += (3500 * count)
            dic_beverage_cup['자두에이드'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"자두에이드 {dic_beverage_cup['자두에이드']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"자두에이드 {dic_beverage_cup['자두에이드']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"자두에이드 {dic_beverage_cup['자두에이드']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"자두에이드 {dic_beverage_cup['자두에이드']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"자두에이드 {dic_beverage_cup['자두에이드']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"자두에이드 {dic_beverage_cup['자두에이드']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"자두에이드 {dic_beverage_cup['자두에이드']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_유자민트티(self,instance):
        global count,dic_beverage_cup,dic_beverage_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '유자민트티' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_beverage_sum['유자민트티'] += (3000 * count)
            dic_beverage_cup['유자민트티'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"유자민트티 {dic_beverage_cup['유자민트티']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"유자민트티 {dic_beverage_cup['유자민트티']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"유자민트티 {dic_beverage_cup['유자민트티']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"유자민트티 {dic_beverage_cup['유자민트티']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"유자민트티 {dic_beverage_cup['유자민트티']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"유자민트티 {dic_beverage_cup['유자민트티']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"유자민트티 {dic_beverage_cup['유자민트티']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"

    def go_to_미숫가루(self,instance):
        global count,dic_beverage_cup,dic_beverage_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '미숫가루' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_beverage_sum['미숫가루'] += (3500 * count)
            dic_beverage_cup['미숫가루'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"미숫가루 {dic_beverage_cup['미숫가루']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"미숫가루 {dic_beverage_cup['미숫가루']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"미숫가루 {dic_beverage_cup['미숫가루']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"미숫가루 {dic_beverage_cup['미숫가루']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"미숫가루 {dic_beverage_cup['미숫가루']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"미숫가루 {dic_beverage_cup['미숫가루']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"미숫가루 {dic_beverage_cup['미숫가루']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_밀크티(self,instance):
        global count,dic_beverage_cup,dic_beverage_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '밀크티' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_beverage_sum['밀크티'] += (3000 * count)
            dic_beverage_cup['밀크티'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"밀크티 {dic_beverage_cup['밀크티']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"밀크티 {dic_beverage_cup['밀크티']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"밀크티 {dic_beverage_cup['밀크티']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"밀크티 {dic_beverage_cup['밀크티']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"밀크티 {dic_beverage_cup['밀크티']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"밀크티 {dic_beverage_cup['밀크티']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"밀크티 {dic_beverage_cup['밀크티']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_딸기라떼(self,instance):
        global count,dic_beverage_cup,dic_beverage_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '딸기라떼' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_beverage_sum['딸기라떼'] += (3500 * count)
            dic_beverage_cup['딸기라떼'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"딸기라떼 {dic_beverage_cup['딸기라떼']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"딸기라떼 {dic_beverage_cup['딸기라떼']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"딸기라떼 {dic_beverage_cup['딸기라떼']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"딸기라떼 {dic_beverage_cup['딸기라떼']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"딸기라떼 {dic_beverage_cup['딸기라떼']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"딸기라떼 {dic_beverage_cup['딸기라떼']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"딸기라떼 {dic_beverage_cup['딸기라떼']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_애플민트스무디(self,instance):
        global count,dic_beverage_cup,dic_beverage_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '애플민트스무디' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_beverage_sum['애플민트스무디'] += (3500 * count)
            dic_beverage_cup['애플민트스무디'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"애플민트스무디 {dic_beverage_cup['애플민트스무디']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"애플민트스무디 {dic_beverage_cup['애플민트스무디']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"애플민트스무디 {dic_beverage_cup['애플민트스무디']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"애플민트스무디 {dic_beverage_cup['애플민트스무디']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"애플민트스무디 {dic_beverage_cup['애플민트스무디']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"애플민트스무디 {dic_beverage_cup['애플민트스무디']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"애플민트스무디 {dic_beverage_cup['애플민트스무디']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
    
    def go_to_제주누보(self,instance):
        global count,dic_etc_cup,dic_etc_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '제주누보' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_etc_sum['제주누보'] += (3000 * count)
            dic_etc_cup['제주누보'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"제주누보 {dic_etc_cup['제주누보']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"제주누보 {dic_etc_cup['제주누보']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"제주누보 {dic_etc_cup['제주누보']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"제주누보 {dic_etc_cup['제주누보']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"제주누보 {dic_etc_cup['제주누보']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"제주누보 {dic_etc_cup['제주누보']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"제주누보 {dic_etc_cup['제주누보']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_레몬사와(self,instance):
        global count,dic_etc_cup,dic_etc_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '레몬사와' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_etc_sum['레몬사와'] += (3000 * count)
            dic_etc_cup['레몬사와'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"레몬사와 {dic_etc_cup['레몬사와']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"레몬사와 {dic_etc_cup['레몬사와']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"레몬사와 {dic_etc_cup['레몬사와']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"레몬사와 {dic_etc_cup['레몬사와']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"레몬사와 {dic_etc_cup['레몬사와']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"레몬사와 {dic_etc_cup['레몬사와']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"레몬사와 {dic_etc_cup['레몬사와']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"

    def go_to_유자사와(self,instance):
        global count,dic_etc_cup,dic_etc_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '유자사와' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_etc_sum['유자사와'] += (3000 * count)
            dic_etc_cup['유자사와'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"유자사와 {dic_etc_cup['유자사와']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"유자사와 {dic_etc_cup['유자사와']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"유자사와 {dic_etc_cup['유자사와']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"유자사와 {dic_etc_cup['유자사와']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"유자사와 {dic_etc_cup['유자사와']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"유자사와 {dic_etc_cup['유자사와']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"유자사와 {dic_etc_cup['유자사와']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_아사히(self,instance):
        global count,dic_etc_cup,dic_etc_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '아사히' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_etc_sum['아사히'] += (3000 * count)
            dic_etc_cup['아사히'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"아사히 {dic_etc_cup['아사히']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"아사히 {dic_etc_cup['아사히']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"아사히 {dic_etc_cup['아사히']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"아사히 {dic_etc_cup['아사히']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"아사히 {dic_etc_cup['아사히']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"아사히 {dic_etc_cup['아사히']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"아사히 {dic_etc_cup['아사히']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
    
    def go_to_탄산수(self,instance):
        global count,dic_etc_cup,dic_etc_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '탄산수' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_etc_sum['탄산수'] += (500 * count)
            dic_etc_cup['탄산수'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"탄산수 {dic_etc_cup['탄산수']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"탄산수 {dic_etc_cup['탄산수']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"탄산수 {dic_etc_cup['탄산수']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"탄산수 {dic_etc_cup['탄산수']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"탄산수 {dic_etc_cup['탄산수']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"탄산수 {dic_etc_cup['탄산수']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"탄산수 {dic_etc_cup['탄산수']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_쌍화탕(self,instance):
        global count,dic_etc_cup,dic_etc_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '쌍화탕' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_etc_sum['쌍화탕'] += (1700 * count)
            dic_etc_cup['쌍화탕'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"쌍화탕 {dic_etc_cup['쌍화탕']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"쌍화탕 {dic_etc_cup['쌍화탕']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"쌍화탕 {dic_etc_cup['쌍화탕']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"쌍화탕 {dic_etc_cup['쌍화탕']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"쌍화탕 {dic_etc_cup['쌍화탕']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"쌍화탕 {dic_etc_cup['쌍화탕']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"쌍화탕 {dic_etc_cup['쌍화탕']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_포춘쿠키(self,instance):
        global count,dic_etc_cup,dic_etc_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '포춘쿠키' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_etc_sum['포춘쿠키'] += (1000 * count)
            dic_etc_cup['포춘쿠키'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"포춘쿠키 {dic_etc_cup['포춘쿠키']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"포춘쿠키 {dic_etc_cup['포춘쿠키']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"포춘쿠키 {dic_etc_cup['포춘쿠키']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"포춘쿠키 {dic_etc_cup['포춘쿠키']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"포춘쿠키 {dic_etc_cup['포춘쿠키']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"포춘쿠키 {dic_etc_cup['포춘쿠키']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"포춘쿠키 {dic_etc_cup['포춘쿠키']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_튀일쿠키(self,instance):
        global count,dic_etc_cup,dic_etc_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '튀일쿠키' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_etc_sum['튀일쿠키'] += (2000 * count)
            dic_etc_cup['튀일쿠키'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"튀일쿠키 {dic_etc_cup['튀일쿠키']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"튀일쿠키 {dic_etc_cup['튀일쿠키']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"튀일쿠키 {dic_etc_cup['튀일쿠키']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"튀일쿠키 {dic_etc_cup['튀일쿠키']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"튀일쿠키 {dic_etc_cup['튀일쿠키']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"튀일쿠키 {dic_etc_cup['튀일쿠키']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"튀일쿠키 {dic_etc_cup['튀일쿠키']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_브륄레(self,instance):
        global count,dic_etc_cup,dic_etc_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '브륄레' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_etc_sum['브륄레'] += (3000 * count)
            dic_etc_cup['브륄레'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"브륄레 {dic_etc_cup['브륄레']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"브륄레 {dic_etc_cup['브륄레']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"브륄레 {dic_etc_cup['브륄레']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"브륄레 {dic_etc_cup['브륄레']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"브륄레 {dic_etc_cup['브륄레']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"브륄레 {dic_etc_cup['브륄레']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"브륄레 {dic_etc_cup['브륄레']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"

    def go_to_캐모마일(self,instance):
        global count,dic_etc_cup,dic_etc_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '캐모마일' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_etc_sum['캐모마일'] += (2500 * count)
            dic_etc_cup['캐모마일'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"캐모마일 {dic_etc_cup['캐모마일']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"캐모마일 {dic_etc_cup['캐모마일']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"캐모마일 {dic_etc_cup['캐모마일']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"캐모마일 {dic_etc_cup['캐모마일']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"캐모마일 {dic_etc_cup['캐모마일']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"캐모마일 {dic_etc_cup['캐모마일']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"캐모마일 {dic_etc_cup['캐모마일']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_루이보스(self,instance):
        global count,dic_etc_cup,dic_etc_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '루이보스' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_etc_sum['루이보스'] += (2500 * count)
            dic_etc_cup['루이보스'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"루이보스 {dic_etc_cup['루이보스']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"루이보스 {dic_etc_cup['루이보스']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"루이보스 {dic_etc_cup['루이보스']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"루이보스 {dic_etc_cup['루이보스']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"루이보스 {dic_etc_cup['루이보스']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"루이보스 {dic_etc_cup['루이보스']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"루이보스 {dic_etc_cup['루이보스']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_보이차(self,instance):
        global count,dic_etc_cup,dic_etc_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '보이차' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_etc_sum['보이차'] += (2500 * count)
            dic_etc_cup['보이차'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"보이차 {dic_etc_cup['보이차']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"보이차 {dic_etc_cup['보이차']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"보이차 {dic_etc_cup['보이차']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"보이차 {dic_etc_cup['보이차']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"보이차 {dic_etc_cup['보이차']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"보이차 {dic_etc_cup['보이차']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"보이차 {dic_etc_cup['보이차']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
    
    def go_to_페퍼민트차(self,instance):
        global count,dic_etc_cup,dic_etc_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '페퍼민트' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_etc_sum['페퍼민트'] += (2500 * count)
            dic_etc_cup['페퍼민트'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"페퍼민트 {dic_etc_cup['페퍼민트']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"페퍼민트 {dic_etc_cup['페퍼민트']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"페퍼민트 {dic_etc_cup['페퍼민트']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"페퍼민트 {dic_etc_cup['페퍼민트']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"페퍼민트 {dic_etc_cup['페퍼민트']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"페퍼민트 {dic_etc_cup['페퍼민트']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"페퍼민트 {dic_etc_cup['페퍼민트']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_레몬그라스(self,instance):
        global count,dic_etc_cup,dic_etc_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '레몬그라스' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_etc_sum['레몬그라스'] += (2500 * count)
            dic_etc_cup['레몬그라스'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"레몬그라스 {dic_etc_cup['레몬그라스']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"레몬그라스 {dic_etc_cup['레몬그라스']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"레몬그라스 {dic_etc_cup['레몬그라스']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"레몬그라스 {dic_etc_cup['레몬그라스']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"레몬그라스 {dic_etc_cup['레몬그라스']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"레몬그라스 {dic_etc_cup['레몬그라스']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"레몬그라스 {dic_etc_cup['레몬그라스']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_라벤더(self,instance):
        global count,dic_etc_cup,dic_etc_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '라벤더' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_etc_sum['라벤더'] += (2500 * count)
            dic_etc_cup['라벤더'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"라벤더 {dic_etc_cup['라벤더']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"라벤더 {dic_etc_cup['라벤더']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"라벤더 {dic_etc_cup['라벤더']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"라벤더 {dic_etc_cup['라벤더']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"라벤더 {dic_etc_cup['라벤더']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"라벤더 {dic_etc_cup['라벤더']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"라벤더 {dic_etc_cup['라벤더']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
        #self.메뉴1_button.bind(on_press =lambda instance, name="[장바구니]" + self.메뉴1_button.text.split(" ")[0]: self.메뉴1_open_popup(name,instance))
    
    def clear_message(self,instance):
        self.알림창.text = ""
    
    
    def go_to_주문(self,instance):
        global m1,m1_sum,m2,m2_sum,m3,m3_sum,m4,m4_sum,m5,m5_sum,m6,m6_sum,m7,m7_sum
        for _ in range(7):
            if _ == 0:
                if self.메뉴1_button.text == '':
                    pass
                elif self.메뉴1_button.text.split(" ")[0] in dic_coffee_sum.keys():
                    m1 = self.메뉴1_button.text.split(" ")[0]
                    m1_sum = dic_coffee_sum[m1]
                elif self.메뉴1_button.text.split(" ")[0] in dic_beverage_sum.keys():
                    m1 = self.메뉴1_button.text.split(" ")[0]
                    m1_sum = dic_beverage_sum[m1]
                elif self.메뉴1_button.text.split(" ")[0] in dic_etc_sum.keys():
                    m1 = self.메뉴1_button.text.split(" ")[0]
                    m1_sum = dic_etc_sum[m1]
                    
            elif _ == 1:
                if self.메뉴2_button.text == '':
                    pass
                elif self.메뉴2_button.text.split(" ")[0] in dic_coffee_sum.keys():
                    m2 = self.메뉴2_button.text.split(" ")[0]
                    m2_sum = dic_coffee_sum[m2]
                elif self.메뉴2_button.text.split(" ")[0] in dic_beverage_sum.keys():
                    m2 = self.메뉴2_button.text.split(" ")[0]
                    m2_sum = dic_beverage_sum[m2]
                elif self.메뉴2_button.text.split(" ")[0] in dic_etc_sum.keys():
                    m2 = self.메뉴2_button.text.split(" ")[0]
                    m2_sum = dic_etc_sum[m2]
                    
            elif _ == 2:
                if self.메뉴3_button.text == '':
                    pass
                elif self.메뉴3_button.text.split(" ")[0] in dic_coffee_sum.keys():
                    m3 = self.메뉴3_button.text.split(" ")[0]
                    m3_sum = dic_coffee_sum[m3]
                elif self.메뉴3_button.text.split(" ")[0] in dic_beverage_sum.keys():
                    m3 = self.메뉴3_button.text.split(" ")[0]
                    m3_sum = dic_beverage_sum[m3]
                elif self.메뉴3_button.text.split(" ")[0] in dic_etc_sum.keys():
                    m3 = self.메뉴3_button.text.split(" ")[0]
                    m3_sum = dic_etc_sum[m3]
                    
            elif _ == 3:
                if self.메뉴4_button.text == '':
                    pass
                elif self.메뉴4_button.text.split(" ")[0] in dic_coffee_sum.keys():
                    m4 = self.메뉴4_button.text.split(" ")[0]
                    m4_sum = dic_coffee_sum[m4]
                elif self.메뉴4_button.text.split(" ")[0] in dic_beverage_sum.keys():
                    m4 = self.메뉴4_button.text.split(" ")[0]
                    m4_sum = dic_beverage_sum[m4]
                elif self.메뉴4_button.text.split(" ")[0] in dic_etc_sum.keys():
                    m4 = self.메뉴4_button.text.split(" ")[0]
                    m4_sum = dic_etc_sum[m4]
                    
                    
            elif _ == 4:
                if self.메뉴5_button.text == '':
                    pass
                elif self.메뉴5_button.text.split(" ")[0] in dic_coffee_sum.keys():
                    m5 = self.메뉴5_button.text.split(" ")[0]
                    m5_sum = dic_coffee_sum[m5]
                elif self.메뉴5_button.text.split(" ")[0] in dic_beverage_sum.keys():
                    m5 = self.메뉴5_button.text.split(" ")[0]
                    m5_sum = dic_beverage_sum[m5]
                elif self.메뉴5_button.text.split(" ")[0] in dic_etc_sum.keys():
                    m5 = self.메뉴5_button.text.split(" ")[0]
                    m5_sum = dic_etc_sum[m5]
                    
            elif _ == 5:
                if self.메뉴6_button.text == '':
                    pass
                elif self.메뉴6_button.text.split(" ")[0] in dic_coffee_sum.keys():
                    m6 = self.메뉴6_button.text.split(" ")[0]
                    m6_sum = dic_coffee_sum[m6]
                elif self.메뉴6_button.text.split(" ")[0] in dic_beverage_sum.keys():
                    m6 = self.메뉴6_button.text.split(" ")[0]
                    m6_sum = dic_beverage_sum[m6]
                elif self.메뉴6_button.text.split(" ")[0] in dic_etc_sum.keys():
                    m6 = self.메뉴6_button.text.split(" ")[0]
                    m6_sum = dic_etc_sum[m6]
                    
            elif _ == 6:
                if self.메뉴7_button.text == '':
                    pass
                elif self.메뉴7_button.text.split(" ")[0] in dic_coffee_sum.keys():
                    m7 = self.메뉴7_button.text.split(" ")[0]
                    m7_sum = dic_coffee_sum[m7]
                elif self.메뉴7_button.text.split(" ")[0] in dic_beverage_sum.keys():
                    m7 = self.메뉴7_button.text.split(" ")[0]
                    m7_sum = dic_beverage_sum[m7]
                elif self.메뉴7_button.text.split(" ")[0] in dic_etc_sum.keys():
                    m7 = self.메뉴7_button.text.split(" ")[0]
                    m7_sum = dic_etc_sum[m7]

        self.manager.current = 'cash'
        self.scroll_view.scroll_y = 1
        
        return self.scroll_view
        
                    
        
            
    
    def go_to_뒤로(self,instance):
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
        for m in dic_etc_sum.keys():
            dic_etc_sum[m] = 0
            dic_etc_cup[m] = 0
        self.manager.current = 'name_choose'
        self.scroll_view.scroll_y = 1
        
        return self.scroll_view
        
        
        
        
        
class Live_OrderScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.last_selected = None
        self.last_selected2 = None
        
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
        
        샷_추가1_아메리카노_button = Button(
            text="샷\u00D71 아메리카노\n\n\u20A93,000",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        샷_추가1_아메리카노_button.bind(on_press =lambda instance, name="(샷\u00D71)아메리카노": self.아메샷1_open_popup(name,instance))
        menu_layout.add_widget(샷_추가1_아메리카노_button)
        
        샷_추가2_아메리카노_button = Button(
            text="샷\u00D72 아메리카노\n\n\u20A93,500",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        샷_추가2_아메리카노_button.bind(on_press =lambda instance, name="(샷\u00D72)아메리카노": self.아메샷2_open_popup(name,instance))
        menu_layout.add_widget(샷_추가2_아메리카노_button)
        
        샷_추가3_아메리카노_button = Button(
            text="아샷추\u00D71 아메리카노\n\n\u20A93,000",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        샷_추가3_아메리카노_button.bind(on_press =lambda instance, name="(아샷추\u00D71)아메리카노": self.아메샷3_open_popup(name,instance))
        menu_layout.add_widget(샷_추가3_아메리카노_button)
        
        샷_추가4_아메리카노_button = Button(
            text="아샷추\u00D72 아메리카노\n\n\u20A93,500",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        샷_추가4_아메리카노_button.bind(on_press =lambda instance, name="(아샷추\u00D72)아메리카노": self.아메샷4_open_popup(name,instance))
        menu_layout.add_widget(샷_추가4_아메리카노_button)
        
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
        에스프레소_button.bind(on_press =lambda instance, name='에스프레소': self.에스_open_popup(name,instance))
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
        드립_button.bind(on_press =lambda instance, name='드립': self.드립_open_popup(name,instance))
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
        더치_button.bind(on_press =lambda instance, name='더치': self.더치_open_popup(name,instance))
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
        라떼_button.bind(on_press =lambda instance, name='라떼': self.라떼_open_popup(name,instance))
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
        더치라떼_button.bind(on_press =lambda instance, name='더치라떼': self.더치라떼_open_popup(name,instance))
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
        바닐라라떼_button.bind(on_press =lambda instance, name='바닐라라떼': self.바닐라라떼_open_popup(name,instance))
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
        민트라떼종류_button.bind(on_press =lambda instance, name='민트라떼': self.민트라떼종류_open_popup(name,instance))
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
        카푸치노_button.bind(on_press =lambda instance, name='카푸치노': self.카푸치노_open_popup(name,instance))
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
        콜드브루_button.bind(on_press =lambda instance, name='콜드브루': self.콜드브루_open_popup(name,instance))
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
        카페모카_button.bind(on_press =lambda instance, name='카페모카': self.카페모카_open_popup(name,instance))
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
        보리커피_button.bind(on_press =lambda instance, name='보리커피': self.보리커피_open_popup(name,instance))
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
        플렛화이트_button.bind(on_press =lambda instance, name='플렛화이트': self.플렛화이트_open_popup(name,instance))
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
        꼼빠냐_button.bind(on_press =lambda instance, name='꼼빠냐': self.꼼빠냐_open_popup(name,instance))
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
        아인슈페너_button.bind(on_press =lambda instance, name='아인슈페너': self.아인슈페너_open_popup(name,instance))
        menu_layout.add_widget(아인슈페너_button)
        
        #menu_layout.add_widget(Label(size_hint=(None, None), width=310, height=270))
        menu_layout.add_widget(Label(size_hint=(None, None), width=310, height=270))
        menu_layout.add_widget(Label(size_hint=(None, None), width=310, height=270))
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
        베리고_button.bind(on_press =lambda instance, name='베리고': self.베리고_open_popup(name,instance))
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
        망고스무디_button.bind(on_press =lambda instance, name='망고스무디': self.망고스무디_open_popup(name,instance))
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
        아보카도바나나_button.bind(on_press =lambda instance, name='아보카도바나나': self.아보카도바나나_open_popup(name,instance))
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
        망고바나나_button.bind(on_press =lambda instance, name='망고바나나': self.망고바나나_open_popup(name,instance))
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
        패션후르츠에이드_button.bind(on_press =lambda instance, name='패션후르츠': self.패션후르츠_open_popup(name,instance))
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
        레몬에이드_button.bind(on_press =lambda instance, name='레몬에이드': self.레몬에이드_open_popup(name,instance))
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
        복숭아바질에이드_button.bind(on_press =lambda instance, name='복숭아바질': self.복숭아바질_open_popup(name,instance))
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
        초코라떼_button.bind(on_press =lambda instance, name='초코라떼': self.초코라떼_open_popup(name,instance))
        menu_layout.add_widget(초코라떼_button)
        
        Hot초코_button = Button(
            text="Hot초코\n\n\u20A93,500",
            font_name="NanumGothic",
            size_hint=(None, None),
            text_size=(270, None),
            font_size = font_size,
            halign="center",
            valign="middle",
            height=270,
            width=310
        )
        Hot초코_button.bind(on_press =lambda instance, name='Hot초코': self.Hot초코_open_popup(name,instance))
        menu_layout.add_widget(Hot초코_button)
        
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
        자두에이드_button.bind(on_press =lambda instance, name='자두에이드': self.자두에이드_open_popup(name,instance))
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
        유자민트티_button.bind(on_press =lambda instance, name='유자민트티': self.유자민트티_open_popup(name,instance))
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
        미숫가루_button.bind(on_press =lambda instance, name='미숫가루': self.미숫가루_open_popup(name,instance))
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
        밀크티_button.bind(on_press =lambda instance, name='밀크티': self.밀크티_open_popup(name,instance))
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
        딸기라떼_button.bind(on_press =lambda instance, name='딸기라떼': self.딸기라떼_open_popup(name,instance))
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
        애플민트스무디_button.bind(on_press =lambda instance, name='애플민트스무디': self.애플민트스무디_open_popup(name,instance))
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
        제주누보_button.bind(on_press =lambda instance, name='제주누보': self.제주누보_open_popup(name,instance))
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
        레몬사와_button.bind(on_press =lambda instance, name='레몬사와': self.레몬사와_open_popup(name,instance))
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
        유자사와_button.bind(on_press =lambda instance, name='유자사와': self.유자사와_open_popup(name,instance))
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
        아사히_button.bind(on_press =lambda instance, name='아사히': self.아사히_open_popup(name,instance))
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
        탄산수_button.bind(on_press =lambda instance, name='탄산수': self.탄산수_open_popup(name,instance))
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
        쌍화탕_button.bind(on_press =lambda instance, name='쌍화탕': self.쌍화탕_open_popup(name,instance))
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
        포춘쿠키_button.bind(on_press =lambda instance, name='포춘쿠키': self.포춘쿠키_open_popup(name,instance))
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
        튀일쿠키_button.bind(on_press =lambda instance, name='튀일쿠키': self.튀일쿠키_open_popup(name,instance))
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
        브륄레_button.bind(on_press =lambda instance, name='브륄레': self.브륄레_open_popup(name,instance))
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
        캐모마일_button.bind(on_press =lambda instance, name='캐모마일': self.캐모마일_open_popup(name,instance))
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
        루이보스_button.bind(on_press =lambda instance, name='루이보스': self.루이보스_open_popup(name,instance))
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
        보이차_button.bind(on_press =lambda instance, name='보이차': self.보이차_open_popup(name,instance))
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
        페퍼민트차_button.bind(on_press =lambda instance, name='페퍼민트': self.페퍼민트_open_popup(name,instance))
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
        레몬그라스_button.bind(on_press =lambda instance, name='레몬그라스': self.레몬그라스_open_popup(name,instance))
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
        라벤더_button.bind(on_press =lambda instance, name='라벤더': self.라벤더_open_popup(name,instance))
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
        
        self.알림창 = Label(
            text="",
            font_name="NanumGothic",
            size_hint=(1, 0.2),
            font_size=sp(16),
            color=(1, 0, 0, 1),  # 빨간색 텍스트
            pos_hint={"center_x": 0.5, "y": 0.5}
        )
        back_layout.add_widget(self.알림창)
        
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
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.43},text="[수량]")
        content.add_widget(수량)
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None),  # 크기를 고정
            size=(100, 50),  # 고정 크기 설정
            pos_hint={'center_x': 0.5, 'y': 0.282},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)

        self.따아_button = ToggleButton(
            text="Hot",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),  # 버튼 크기
            pos_hint={'x': 0.31, 'y': 0.7},  # y 값을 조정하여 버튼 위치 설정
            group='온도'
        )
        self.아아_button = ToggleButton(
            text="Ice",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),
            pos_hint={'x': 0.51, 'y': 0.7},
            group='온도'
        )
        
        self.따아_button.bind(on_press=lambda instance: self.record_selection(instance))
        self.아아_button.bind(on_press=lambda instance: self.record_selection(instance))
        
        content.add_widget(self.따아_button)
        content.add_widget(self.아아_button)
        
        self.A_button = ToggleButton(
            text="A",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),  # 버튼 크기
            pos_hint={'x': 0.31, 'y': 0.55},  # y 값을 조정하여 버튼 위치 설정
            group='맛'
        )
        self.B_button = ToggleButton(
            text="B",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),
            pos_hint={'x': 0.51, 'y': 0.55},
            group='맛'
        )
        
        
        self.A_button.bind(on_press=lambda instance: self.record_selection2(instance))
        self.B_button.bind(on_press=lambda instance: self.record_selection2(instance))
        
        content.add_widget(self.A_button)
        content.add_widget(self.B_button)


        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_아메리카노(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.552, 'y': 0.26}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.348, 'y': 0.26}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
        
    def 아메샷1_open_popup(self, menu_name, instance):
        # 팝업 내용 정의
        content = FloatLayout()
        content.add_widget(Label(font_name="NanumGothic",font_size=sp(26), pos_hint={'center_x': 0.5, 'y': 0.45}, text=menu_name))
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.43},text="[수량]")
        content.add_widget(수량)
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None),  # 크기를 고정
            size=(100, 50),  # 고정 크기 설정
            pos_hint={'center_x': 0.5, 'y': 0.282},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)

        self.따아_button = ToggleButton(
            text="Hot",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),  # 버튼 크기
            pos_hint={'x': 0.31, 'y': 0.7},  # y 값을 조정하여 버튼 위치 설정
            group='온도'
        )
        self.아아_button = ToggleButton(
            text="Ice",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),
            pos_hint={'x': 0.51, 'y': 0.7},
            group='온도'
        )
        
        self.따아_button.bind(on_press=lambda instance: self.record_selection(instance))
        self.아아_button.bind(on_press=lambda instance: self.record_selection(instance))
        
        content.add_widget(self.따아_button)
        content.add_widget(self.아아_button)
        
        self.A_button = ToggleButton(
            text="A",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),  # 버튼 크기
            pos_hint={'x': 0.31, 'y': 0.55},  # y 값을 조정하여 버튼 위치 설정
            group='맛'
        )
        self.B_button = ToggleButton(
            text="B",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),
            pos_hint={'x': 0.51, 'y': 0.55},
            group='맛'
        )
        
        
        self.A_button.bind(on_press=lambda instance: self.record_selection2(instance))
        self.B_button.bind(on_press=lambda instance: self.record_selection2(instance))
        
        content.add_widget(self.A_button)
        content.add_widget(self.B_button)


        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_아메리카노샷1(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.552, 'y': 0.26}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.348, 'y': 0.26}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
        
    def 아메샷2_open_popup(self, menu_name, instance):
        # 팝업 내용 정의
        content = FloatLayout()
        content.add_widget(Label(font_name="NanumGothic",font_size=sp(26), pos_hint={'center_x': 0.5, 'y': 0.45}, text=menu_name))
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.43},text="[수량]")
        content.add_widget(수량)
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None),  # 크기를 고정
            size=(100, 50),  # 고정 크기 설정
            pos_hint={'center_x': 0.5, 'y': 0.282},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)

        self.따아_button = ToggleButton(
            text="Hot",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),  # 버튼 크기
            pos_hint={'x': 0.31, 'y': 0.7},  # y 값을 조정하여 버튼 위치 설정
            group='온도'
        )
        self.아아_button = ToggleButton(
            text="Ice",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),
            pos_hint={'x': 0.51, 'y': 0.7},
            group='온도'
        )
        
        self.따아_button.bind(on_press=lambda instance: self.record_selection(instance))
        self.아아_button.bind(on_press=lambda instance: self.record_selection(instance))
        
        content.add_widget(self.따아_button)
        content.add_widget(self.아아_button)
        
        self.A_button = ToggleButton(
            text="A",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),  # 버튼 크기
            pos_hint={'x': 0.31, 'y': 0.55},  # y 값을 조정하여 버튼 위치 설정
            group='맛'
        )
        self.B_button = ToggleButton(
            text="B",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),
            pos_hint={'x': 0.51, 'y': 0.55},
            group='맛'
        )
        
        
        self.A_button.bind(on_press=lambda instance: self.record_selection2(instance))
        self.B_button.bind(on_press=lambda instance: self.record_selection2(instance))
        
        content.add_widget(self.A_button)
        content.add_widget(self.B_button)


        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_아메리카노샷2(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.552, 'y': 0.26}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.348, 'y': 0.26}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
        
    def 아메샷3_open_popup(self, menu_name, instance):
        # 팝업 내용 정의
        content = FloatLayout()
        content.add_widget(Label(font_name="NanumGothic",font_size=sp(26), pos_hint={'center_x': 0.5, 'y': 0.45}, text=menu_name))
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.43},text="[수량]")
        content.add_widget(수량)
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None),  # 크기를 고정
            size=(100, 50),  # 고정 크기 설정
            pos_hint={'center_x': 0.5, 'y': 0.282},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)

        self.따아_button = ToggleButton(
            text="Hot",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),  # 버튼 크기
            pos_hint={'x': 0.31, 'y': 0.7},  # y 값을 조정하여 버튼 위치 설정
            group='온도'
        )
        self.아아_button = ToggleButton(
            text="Ice",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),
            pos_hint={'x': 0.51, 'y': 0.7},
            group='온도'
        )
        
        self.따아_button.bind(on_press=lambda instance: self.record_selection(instance))
        self.아아_button.bind(on_press=lambda instance: self.record_selection(instance))
        
        content.add_widget(self.따아_button)
        content.add_widget(self.아아_button)
        
        self.A_button = ToggleButton(
            text="A",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),  # 버튼 크기
            pos_hint={'x': 0.31, 'y': 0.55},  # y 값을 조정하여 버튼 위치 설정
            group='맛'
        )
        self.B_button = ToggleButton(
            text="B",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),
            pos_hint={'x': 0.51, 'y': 0.55},
            group='맛'
        )
        
        
        self.A_button.bind(on_press=lambda instance: self.record_selection2(instance))
        self.B_button.bind(on_press=lambda instance: self.record_selection2(instance))
        
        content.add_widget(self.A_button)
        content.add_widget(self.B_button)


        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_아메리카노샷3(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.552, 'y': 0.26}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.348, 'y': 0.26}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        

    def 아메샷4_open_popup(self, menu_name, instance):
        # 팝업 내용 정의
        content = FloatLayout()
        content.add_widget(Label(font_name="NanumGothic",font_size=sp(26), pos_hint={'center_x': 0.5, 'y': 0.45}, text=menu_name))
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.43},text="[수량]")
        content.add_widget(수량)
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None),  # 크기를 고정
            size=(100, 50),  # 고정 크기 설정
            pos_hint={'center_x': 0.5, 'y': 0.282},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)

        self.따아_button = ToggleButton(
            text="Hot",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),  # 버튼 크기
            pos_hint={'x': 0.31, 'y': 0.7},  # y 값을 조정하여 버튼 위치 설정
            group='온도'
        )
        self.아아_button = ToggleButton(
            text="Ice",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),
            pos_hint={'x': 0.51, 'y': 0.7},
            group='온도'
        )
        
        self.따아_button.bind(on_press=lambda instance: self.record_selection(instance))
        self.아아_button.bind(on_press=lambda instance: self.record_selection(instance))
        
        content.add_widget(self.따아_button)
        content.add_widget(self.아아_button)
        
        self.A_button = ToggleButton(
            text="A",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),  # 버튼 크기
            pos_hint={'x': 0.31, 'y': 0.55},  # y 값을 조정하여 버튼 위치 설정
            group='맛'
        )
        self.B_button = ToggleButton(
            text="B",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),
            pos_hint={'x': 0.51, 'y': 0.55},
            group='맛'
        )
        
        
        self.A_button.bind(on_press=lambda instance: self.record_selection2(instance))
        self.B_button.bind(on_press=lambda instance: self.record_selection2(instance))
        
        content.add_widget(self.A_button)
        content.add_widget(self.B_button)


        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_아메리카노샷4(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.552, 'y': 0.26}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.348, 'y': 0.26}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
        
    def 에스_open_popup(self, menu_name, instance):
        # 팝업 내용 정의
        content = FloatLayout()
        content.add_widget(Label(font_name="NanumGothic",font_size=sp(26), pos_hint={'center_x': 0.5, 'y': 0.45}, text=menu_name))
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.43},text="[수량]")
        content.add_widget(수량)
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None), 
            size=(100, 50),  
            pos_hint={'center_x': 0.5, 'y': 0.322},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)
        
        self.따에스_button = ToggleButton(
            text="Hot",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),  # 버튼 크기
            pos_hint={'x': 0.31, 'y': 0.6},  # y 값을 조정하여 버튼 위치 설정
            group='온도'
        )
        self.아에스_button = ToggleButton(
            text="Ice",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),
            pos_hint={'x': 0.51, 'y': 0.6},
            group='온도'
        )
        
        self.따에스_button.bind(on_press=lambda instance: self.record_selection(instance))
        self.아에스_button.bind(on_press=lambda instance: self.record_selection(instance))
        
        content.add_widget(self.따에스_button)
        content.add_widget(self.아에스_button)

        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_에스프레소(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.552, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.348, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
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
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.43},text="[수량]")
        content.add_widget(수량)
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None), 
            size=(100, 50),  
            pos_hint={'center_x': 0.5, 'y': 0.322},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)
        
        self.따드_button = ToggleButton(
            text="Hot",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),  # 버튼 크기
            pos_hint={'x': 0.31, 'y': 0.6},  # y 값을 조정하여 버튼 위치 설정
            group='온도'
        )
        self.아드_button = ToggleButton(
            text="Ice",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),
            pos_hint={'x': 0.51, 'y': 0.6},
            group='온도'
        )
        
        self.따드_button.bind(on_press=lambda instance: self.record_selection(instance))
        self.아드_button.bind(on_press=lambda instance: self.record_selection(instance))
        
        content.add_widget(self.따드_button)
        content.add_widget(self.아드_button)

        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_드립(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.552, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.348, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
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
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y':  0.43},text="[수량]")
        content.add_widget(수량)
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None), 
            size=(100, 50),  
            pos_hint={'center_x': 0.5, 'y': 0.322},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)
        
        self.따더_button = ToggleButton(
            text="Hot",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),  # 버튼 크기
            pos_hint={'x': 0.31, 'y': 0.6},  # y 값을 조정하여 버튼 위치 설정
            group='온도'
        )
        self.아더_button = ToggleButton(
            text="Ice",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),
            pos_hint={'x': 0.51, 'y': 0.6},
            group='온도'
        )
        
        self.따더_button.bind(on_press=lambda instance: self.record_selection(instance))
        self.아더_button.bind(on_press=lambda instance: self.record_selection(instance))
        
        content.add_widget(self.따더_button)
        content.add_widget(self.아더_button)

        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_더치(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.552, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.348, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
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
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.43},text="[수량]")
        content.add_widget(수량)
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None), 
            size=(100, 50),  
            pos_hint={'center_x': 0.5, 'y': 0.322},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)
        
        self.따라_button = ToggleButton(
            text="Hot",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),  # 버튼 크기
            pos_hint={'x': 0.31, 'y': 0.6},  # y 값을 조정하여 버튼 위치 설정
            group='온도'
        )
        self.아라_button = ToggleButton(
            text="Ice",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),
            pos_hint={'x': 0.51, 'y': 0.6},
            group='온도'
        )
        
        self.따라_button.bind(on_press=lambda instance: self.record_selection(instance))
        self.아라_button.bind(on_press=lambda instance: self.record_selection(instance))
        
        content.add_widget(self.따라_button)
        content.add_widget(self.아라_button)

        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_라떼(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.552, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.348, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
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
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.43},text="[수량]")
        content.add_widget(수량)
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None), 
            size=(100, 50),  
            pos_hint={'center_x': 0.5, 'y': 0.322},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)
        
        self.따더라_button = ToggleButton(
            text="Hot",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),  # 버튼 크기
            pos_hint={'x': 0.31, 'y': 0.6},  # y 값을 조정하여 버튼 위치 설정
            group='온도'
        )
        self.아더라_button = ToggleButton(
            text="Ice",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),
            pos_hint={'x': 0.51, 'y': 0.6},
            group='온도'
        )
        
        self.따더라_button.bind(on_press=lambda instance: self.record_selection(instance))
        self.아더라_button.bind(on_press=lambda instance: self.record_selection(instance))
        
        content.add_widget(self.따더라_button)
        content.add_widget(self.아더라_button)

        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_더치라떼(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.552, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.348, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
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
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.43},text="[수량]")
        content.add_widget(수량)
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None), 
            size=(100, 50),  
            pos_hint={'center_x': 0.5, 'y': 0.322},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)
        
        self.따바라_button = ToggleButton(
            text="Hot",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),  # 버튼 크기
            pos_hint={'x': 0.31, 'y': 0.6},  # y 값을 조정하여 버튼 위치 설정
            group='온도'
        )
        self.아바라_button = ToggleButton(
            text="Ice",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),
            pos_hint={'x': 0.51, 'y': 0.6},
            group='온도'
        )
        
        self.따바라_button.bind(on_press=lambda instance: self.record_selection(instance))
        self.아바라_button.bind(on_press=lambda instance: self.record_selection(instance))
        
        content.add_widget(self.따바라_button)
        content.add_widget(self.아바라_button)

        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_바닐라라떼(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.552, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.348, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
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
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.43},text="[수량]")
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
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.43},text="[수량]")
        content.add_widget(수량)
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None), 
            size=(100, 50),  
            pos_hint={'center_x': 0.5, 'y': 0.322},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)
        
        self.따콜드_button = ToggleButton(
            text="Hot",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),  # 버튼 크기
            pos_hint={'x': 0.31, 'y': 0.6},  # y 값을 조정하여 버튼 위치 설정
            group='온도'
        )
        self.아콜드_button = ToggleButton(
            text="Ice",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),
            pos_hint={'x': 0.51, 'y': 0.6},
            group='온도'
        )
        
        self.따콜드_button.bind(on_press=lambda instance: self.record_selection(instance))
        self.아콜드_button.bind(on_press=lambda instance: self.record_selection(instance))
        
        content.add_widget(self.따콜드_button)
        content.add_widget(self.아콜드_button)

        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_콜드브루(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.552, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.348, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
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
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.43},text="[수량]")
        content.add_widget(수량)
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None), 
            size=(100, 50),  
            pos_hint={'center_x': 0.5, 'y': 0.322},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)
        
        self.따카페_button = ToggleButton(
            text="Hot",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),  # 버튼 크기
            pos_hint={'x': 0.31, 'y': 0.6},  # y 값을 조정하여 버튼 위치 설정
            group='온도'
        )
        self.아카페_button = ToggleButton(
            text="Ice",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),
            pos_hint={'x': 0.51, 'y': 0.6},
            group='온도'
        )
        
        self.따카페_button.bind(on_press=lambda instance: self.record_selection(instance))
        self.아카페_button.bind(on_press=lambda instance: self.record_selection(instance))
        
        content.add_widget(self.따카페_button)
        content.add_widget(self.아카페_button)

        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_카페모카(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.552, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.348, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
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
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.43},text="[수량]")
        content.add_widget(수량)
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None), 
            size=(100, 50),  
            pos_hint={'center_x': 0.5, 'y': 0.322},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)
        
        self.따보리_button = ToggleButton(
            text="Hot",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),  # 버튼 크기
            pos_hint={'x': 0.31, 'y': 0.6},  # y 값을 조정하여 버튼 위치 설정
            group='온도'
        )
        self.아보리_button = ToggleButton(
            text="Ice",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),
            pos_hint={'x': 0.51, 'y': 0.6},
            group='온도'
        )
        
        self.따보리_button.bind(on_press=lambda instance: self.record_selection(instance))
        self.아보리_button.bind(on_press=lambda instance: self.record_selection(instance))
        
        content.add_widget(self.따보리_button)
        content.add_widget(self.아보리_button)

        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_보리커피(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.552, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.348, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
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
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.43},text="[수량]")
        content.add_widget(수량)
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None), 
            size=(100, 50),  
            pos_hint={'center_x': 0.5, 'y': 0.322},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)
        
        self.따플렛_button = ToggleButton(
            text="Hot",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),  # 버튼 크기
            pos_hint={'x': 0.31, 'y': 0.6},  # y 값을 조정하여 버튼 위치 설정
            group='온도'
        )
        self.아플렛_button = ToggleButton(
            text="Ice",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),
            pos_hint={'x': 0.51, 'y': 0.6},
            group='온도'
        )
        
        self.따플렛_button.bind(on_press=lambda instance: self.record_selection(instance))
        self.아플렛_button.bind(on_press=lambda instance: self.record_selection(instance))
        
        content.add_widget(self.따플렛_button)
        content.add_widget(self.아플렛_button)

        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_플렛화이트(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.552, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.348, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
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
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.43},text="[수량]")
        content.add_widget(수량)
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None), 
            size=(100, 50),  
            pos_hint={'center_x': 0.5, 'y': 0.322},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)
        
        self.따아인_button = ToggleButton(
            text="Hot",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),  # 버튼 크기
            pos_hint={'x': 0.31, 'y': 0.6},  # y 값을 조정하여 버튼 위치 설정
            group='온도'
        )
        self.아아인_button = ToggleButton(
            text="Ice",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),
            pos_hint={'x': 0.51, 'y': 0.6},
            group='온도'
        )
        
        self.따아인_button.bind(on_press=lambda instance: self.record_selection(instance))
        self.아아인_button.bind(on_press=lambda instance: self.record_selection(instance))
        
        content.add_widget(self.따아인_button)
        content.add_widget(self.아아인_button)

        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_아인슈페너(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.552, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.348, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
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
        
    def 초코라떼_open_popup(self, menu_name, instance):
        # 팝업 내용 정의
        content = FloatLayout()
        content.add_widget(Label(font_name="NanumGothic",font_size=sp(26), pos_hint={'center_x': 0.5, 'y': 0.45}, text=menu_name))
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.43},text="[수량]")
        content.add_widget(수량)
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None), 
            size=(100, 50),  
            pos_hint={'center_x': 0.5, 'y': 0.322},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)
        
        self.따초코_button = ToggleButton(
            text="Hot",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),  # 버튼 크기
            pos_hint={'x': 0.31, 'y': 0.6},  # y 값을 조정하여 버튼 위치 설정
            group='온도'
        )
        self.아초코_button = ToggleButton(
            text="Ice",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),
            pos_hint={'x': 0.51, 'y': 0.6},
            group='온도'
        )
        
        self.따초코_button.bind(on_press=lambda instance: self.record_selection(instance))
        self.아초코_button.bind(on_press=lambda instance: self.record_selection(instance))
        
        content.add_widget(self.따초코_button)
        content.add_widget(self.아초코_button)

        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_초코라떼(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.552, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.348, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def Hot초코_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_Hot초코(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def 자두에이드_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_자두에이드(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def 유자민트티_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_유자민트티(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def 미숫가루_open_popup(self, menu_name, instance):
        # 팝업 내용 정의
        content = FloatLayout()
        content.add_widget(Label(font_name="NanumGothic",font_size=sp(26), pos_hint={'center_x': 0.5, 'y': 0.45}, text=menu_name))
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.43},text="[수량]")
        content.add_widget(수량)
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None), 
            size=(100, 50),  
            pos_hint={'center_x': 0.5, 'y': 0.322},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)
        
        self.따미숫_button = ToggleButton(
            text="Hot",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),  # 버튼 크기
            pos_hint={'x': 0.31, 'y': 0.6},  # y 값을 조정하여 버튼 위치 설정
            group='온도'
        )
        self.아미숫_button = ToggleButton(
            text="Ice",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),
            pos_hint={'x': 0.51, 'y': 0.6},
            group='온도'
        )
        
        self.따미숫_button.bind(on_press=lambda instance: self.record_selection(instance))
        self.아미숫_button.bind(on_press=lambda instance: self.record_selection(instance))
        
        content.add_widget(self.따미숫_button)
        content.add_widget(self.아미숫_button)

        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_미숫가루(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.552, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.348, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def 밀크티_open_popup(self, menu_name, instance):
        # 팝업 내용 정의
        content = FloatLayout()
        content.add_widget(Label(font_name="NanumGothic",font_size=sp(26), pos_hint={'center_x': 0.5, 'y': 0.45}, text=menu_name))
        수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.43},text="[수량]")
        content.add_widget(수량)
        self.cup = Label(
            font_name="NanumGothic",
            font_size=sp(18),
            size_hint=(None, None), 
            size=(100, 50),  
            pos_hint={'center_x': 0.5, 'y': 0.322},  # y를 조정하여 버튼 아래로 위치
            text="1"
            )
        content.add_widget(self.cup)
        
        self.따밀크_button = ToggleButton(
            text="Hot",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),  # 버튼 크기
            pos_hint={'x': 0.31, 'y': 0.6},  # y 값을 조정하여 버튼 위치 설정
            group='온도'
        )
        self.아밀크_button = ToggleButton(
            text="Ice",
            font_name="NanumGothic",
            size_hint=(0.18, 0.1),
            pos_hint={'x': 0.51, 'y': 0.6},
            group='온도'
        )
        
        self.따밀크_button.bind(on_press=lambda instance: self.record_selection(instance))
        self.아밀크_button.bind(on_press=lambda instance: self.record_selection(instance))
        
        content.add_widget(self.따밀크_button)
        content.add_widget(self.아밀크_button)

        content.add_widget(Button(text="닫기", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_닫기(instance)))
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_밀크티(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.552, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.348, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def 딸기라떼_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_딸기라떼(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def 애플민트스무디_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_애플민트스무디(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()

    def 제주누보_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_제주누보(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()

    def 레몬사와_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_레몬사와(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def 유자사와_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_유자사와(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def 아사히_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_아사히(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def 탄산수_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_탄산수(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()

    def 쌍화탕_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_쌍화탕(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()

    def 포춘쿠키_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_포춘쿠키(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def 튀일쿠키_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_튀일쿠키(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def 브륄레_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_브륄레(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()

    def 캐모마일_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_캐모마일(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def 루이보스_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_루이보스(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def 보이차_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_보이차(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def 페퍼민트_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_페퍼민트차(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def 레몬그라스_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_레몬그라스(instance)))
        content.add_widget(Button(text="+", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.3}, on_press=lambda _ : self.plus(instance)))
        content.add_widget(Button(text="-", font_name="NanumGothic",size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.3}, on_press=lambda _ : self.minus(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    def 라벤더_open_popup(self, menu_name, instance):
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
        content.add_widget(Button(text="담기", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_라벤더(instance)))
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
        if menu_name == "[장바구니] ":
            pass
        else :
            content = FloatLayout()
            content.add_widget(Label(font_name="NanumGothic",font_size=sp(26), pos_hint={'center_x': 0.5, 'y': 0.45}, text=menu_name))
            수량 = Label(font_name="NanumGothic",font_size=sp(20),size_hint=(None, None),size=(100, 50),pos_hint={'center_x': 0.5, 'y': 0.5},text="[수량]")
            content.add_widget(수량)
        
        
            self.a = instance.text.split(" ")[0]
            self.b = 0
            if self.a in dic_coffee_sum.keys():
                self.b = dic_coffee_cup[self.a]
            elif self.a in dic_beverage_sum.keys():
                self.b = dic_beverage_cup[self.a]
            elif self.a in dic_etc_sum.keys():
                self.b = dic_etc_cup[self.a]
            
            self.cup = Label(
                font_name="NanumGothic",
                font_size=sp(18),
                size_hint=(None, None), 
                size=(100, 50),  
                pos_hint={'center_x': 0.5, 'y': 0.32},  # y를 조정하여 버튼 아래로 위치
                text=str(self.b)
                )
            content.add_widget(self.cup)

            content.add_widget(Button(text="정정", font_name="NanumGothic",size_hint=(0.2, 0.2),pos_hint={'x': 0.8, 'y': 0}, on_press=lambda _ : self.go_to_정정(instance)))
            content.add_widget(Button(text="삭제", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'x': 0, 'y': 0}, on_press=lambda _ : self.go_to_삭제(instance)))
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
            
    def record_selection2(self,instance):
        if instance.state == 'down':
            self.last_selected2 = instance.text
        else : 
            self.last_selected2 = None
            
    
    def plus_2(self, instance):
        global dic_beverage_cup,dic_coffee_cup
        if self.a in dic_beverage_cup.keys():
            dic_beverage_cup[self.a] += 1
            self.cup.text = str(dic_beverage_cup[self.a])
        elif self.a in dic_coffee_cup.keys():
            dic_coffee_cup[self.a] += 1
            self.cup.text = str(dic_coffee_cup[self.a])
        elif self.a in dic_etc_cup.keys():
            dic_etc_cup[self.a] += 1
            self.cup.text = str(dic_etc_cup[self.a])
            
    def minus_2(self, instance):
        global dic_beverage_cup,dic_coffee_cup
        if int(self.cup.text) > 1:
            if self.a in dic_beverage_cup.keys():
                dic_beverage_cup[self.a] -= 1
                self.cup.text = str(dic_beverage_cup[self.a])
            elif self.a in dic_coffee_cup.keys():
                dic_coffee_cup[self.a] -= 1
                self.cup.text = str(dic_coffee_cup[self.a])
            elif self.a in dic_etc_cup.keys():
                dic_etc_cup[self.a] -= 1
                self.cup.text = str(dic_etc_cup[self.a])
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
        elif self.a in dic_etc_cup.keys():
            dic_etc_cup[self.a] = 0
            dic_etc_sum[self.a] = 0

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
            
        elif self.a in dic_etc_cup.keys():
            instance.text = instance.text.split(" ")[0] + " " + str(dic_etc_cup[self.a])
            dic_etc_sum[self.a] = dic_menu_price[self.a] * dic_etc_cup[self.a]
            self.popup.dismiss()

    def go_to_아메리카노(self,instance):
        global count,dic_coffee_sum,dic_coffee_cup
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if ((self.last_selected == "Ice" and self.last_selected2 == "A") and "아아A" in lst) or ((self.last_selected == "Ice" and self.last_selected2 == "B") and "아아B" in lst) or ((self.last_selected == "Hot" and self.last_selected2 == "A") and "뜨아A" in lst) or ((self.last_selected == "Hot" and self.last_selected2 == "B") and "뜨아B" in lst) :
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            if (self.last_selected == "Ice") and (self.last_selected2 == "A"):
                dic_coffee_sum["아아A"] += (2500 * count)
                dic_coffee_cup["아아A"] += count
                #self.메뉴1_button.text = f"아메리카노 {아메리카노_잔수}"
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"아아A {dic_coffee_cup[f'아아A']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"아아A {dic_coffee_cup[f'아아A']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"아아A {dic_coffee_cup[f'아아A']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"아아A {dic_coffee_cup[f'아아A']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"아아A {dic_coffee_cup[f'아아A']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"아아A {dic_coffee_cup[f'아아A']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"아아A {dic_coffee_cup[f'아아A']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"

            elif (self.last_selected == "Ice") and (self.last_selected2 == "B"):
                dic_coffee_sum["아아B"] += (2500 * count)
                dic_coffee_cup["아아B"] += count
                #self.메뉴1_button.text = f"아메리카노 {아메리카노_잔수}"
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"아아B {dic_coffee_cup[f'아아B']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"아아B {dic_coffee_cup[f'아아B']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"아아B {dic_coffee_cup[f'아아B']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"아아B {dic_coffee_cup[f'아아B']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"아아B {dic_coffee_cup[f'아아B']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"아아B {dic_coffee_cup[f'아아B']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"아아B {dic_coffee_cup[f'아아B']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"
        
            elif (self.last_selected == "Hot") and (self.last_selected2 == "A"):
                dic_coffee_sum["뜨아A"] += (2500 * count)
                dic_coffee_cup["뜨아A"] += count
                #self.메뉴1_button.text = f"아메리카노 {아메리카노_잔수}"
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"뜨아A {dic_coffee_cup[f'뜨아A']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"뜨아A {dic_coffee_cup[f'뜨아A']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"뜨아A {dic_coffee_cup[f'뜨아A']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"뜨아A {dic_coffee_cup[f'뜨아A']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"뜨아A {dic_coffee_cup[f'뜨아A']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"뜨아A {dic_coffee_cup[f'뜨아A']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"뜨아A {dic_coffee_cup[f'뜨아A']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"
                
            elif (self.last_selected == "Hot") and (self.last_selected2 == "B"):
                dic_coffee_sum["뜨아B"] += (2500 * count)
                dic_coffee_cup["뜨아B"] += count
                #self.메뉴1_button.text = f"아메리카노 {아메리카노_잔수}"
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"뜨아B {dic_coffee_cup[f'뜨아B']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"뜨아B {dic_coffee_cup[f'뜨아B']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"뜨아B {dic_coffee_cup[f'뜨아B']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"뜨아B {dic_coffee_cup[f'뜨아B']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"뜨아B {dic_coffee_cup[f'뜨아B']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"뜨아B {dic_coffee_cup[f'뜨아B']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"뜨아B {dic_coffee_cup[f'뜨아B']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"


    def go_to_아메리카노샷1(self,instance):
        global count,dic_coffee_sum,dic_coffee_cup
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if ((self.last_selected == "Ice" and self.last_selected2 == "A") and "(샷\u00D71)아아A" in lst) or ((self.last_selected == "Ice" and self.last_selected2 == "B") and "(샷\u00D71)아아B" in lst) or ((self.last_selected == "Hot" and self.last_selected2 == "A") and "(샷\u00D71)뜨아A" in lst) or ((self.last_selected == "Hot" and self.last_selected2 == "B") and "(샷\u00D71)뜨아B" in lst) :
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            if (self.last_selected == "Ice") and (self.last_selected2 == "A"):
                dic_coffee_sum["(샷\u00D71)아아A"] += (3000 * count)
                dic_coffee_cup["(샷\u00D71)아아A"] += count
                #self.메뉴1_button.text = f"아메리카노 {아메리카노_잔수}"
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(샷{mul}1)아아A {dic_coffee_cup[f'(샷{mul}1)아아A']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(샷{mul}1)아아A {dic_coffee_cup[f'(샷{mul}1)아아A']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(샷{mul}1)아아A {dic_coffee_cup[f'(샷{mul}1)아아A']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(샷{mul}1)아아A {dic_coffee_cup[f'(샷{mul}1)아아A']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(샷{mul}1)아아A {dic_coffee_cup[f'(샷{mul}1)아아A']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(샷{mul}1)아아A {dic_coffee_cup[f'(샷{mul}1)아아A']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(샷{mul}1)아아A {dic_coffee_cup[f'(샷{mul}1)아아A']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"

            elif (self.last_selected == "Ice") and (self.last_selected2 == "B"):
                dic_coffee_sum["(샷\u00D71)아아B"] += (3000 * count)
                dic_coffee_cup["(샷\u00D71)아아B"] += count
                #self.메뉴1_button.text = f"아메리카노 {아메리카노_잔수}"
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(샷{mul}1)아아B {dic_coffee_cup[f'(샷{mul}1)아아B']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(샷{mul}1)아아B {dic_coffee_cup[f'(샷{mul}1)아아B']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(샷{mul}1)아아B {dic_coffee_cup[f'(샷{mul}1)아아B']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(샷{mul}1)아아B {dic_coffee_cup[f'(샷{mul}1)아아B']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(샷{mul}1)아아B {dic_coffee_cup[f'(샷{mul}1)아아B']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(샷{mul}1)아아B {dic_coffee_cup[f'(샷{mul}1)아아B']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(샷{mul}1)아아B {dic_coffee_cup[f'(샷{mul}1)아아B']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"
        
            elif (self.last_selected == "Hot") and (self.last_selected2 == "A"):
                dic_coffee_sum["(샷\u00D71)뜨아A"] += (3000 * count)
                dic_coffee_cup["(샷\u00D71)뜨아A"] += count
                #self.메뉴1_button.text = f"아메리카노 {아메리카노_잔수}"
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(샷{mul}1)뜨아A {dic_coffee_cup[f'(샷{mul}1)뜨아A']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(샷{mul}1)뜨아A {dic_coffee_cup[f'(샷{mul}1)뜨아A']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(샷{mul}1)뜨아A {dic_coffee_cup[f'(샷{mul}1)뜨아A']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(샷{mul}1)뜨아A {dic_coffee_cup[f'(샷{mul}1)뜨아A']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(샷{mul}1)뜨아A {dic_coffee_cup[f'(샷{mul}1)뜨아A']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(샷{mul}1)뜨아A {dic_coffee_cup[f'(샷{mul}1)뜨아A']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(샷{mul}1)뜨아A {dic_coffee_cup[f'(샷{mul}1)뜨아A']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"
                
            elif (self.last_selected == "Hot") and (self.last_selected2 == "B"):
                dic_coffee_sum["(샷\u00D71)뜨아B"] += (3000 * count)
                dic_coffee_cup["(샷\u00D71)뜨아B"] += count
                #self.메뉴1_button.text = f"아메리카노 {아메리카노_잔수}"
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(샷{mul}1)뜨아B {dic_coffee_cup[f'(샷{mul}1)뜨아B']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(샷{mul}1)뜨아B {dic_coffee_cup[f'(샷{mul}1)뜨아B']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(샷{mul}1)뜨아B {dic_coffee_cup[f'(샷{mul}1)뜨아B']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(샷{mul}1)뜨아B {dic_coffee_cup[f'(샷{mul}1)뜨아B']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(샷{mul}1)뜨아B {dic_coffee_cup[f'(샷{mul}1)뜨아B']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(샷{mul}1)뜨아B {dic_coffee_cup[f'(샷{mul}1)뜨아B']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(샷{mul}1)뜨아B {dic_coffee_cup[f'(샷{mul}1)뜨아B']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"
                
    def go_to_아메리카노샷2(self,instance):
        global count,dic_coffee_sum,dic_coffee_cup
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if ((self.last_selected == "Ice" and self.last_selected2 == "A") and "(샷\u00D72)아아A" in lst) or ((self.last_selected == "Ice" and self.last_selected2 == "B") and "(샷\u00D72)아아B" in lst) or ((self.last_selected == "Hot" and self.last_selected2 == "A") and "(샷\u00D72)뜨아A" in lst) or ((self.last_selected == "Hot" and self.last_selected2 == "B") and "(샷\u00D72)뜨아B" in lst) :
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            if (self.last_selected == "Ice") and (self.last_selected2 == "A"):
                dic_coffee_sum["(샷\u00D72)아아A"] += (3500 * count)
                dic_coffee_cup["(샷\u00D72)아아A"] += count
                #self.메뉴1_button.text = f"아메리카노 {아메리카노_잔수}"
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(샷{mul}2)아아A {dic_coffee_cup[f'(샷{mul}2)아아A']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(샷{mul}2)아아A {dic_coffee_cup[f'(샷{mul}2)아아A']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(샷{mul}2)아아A {dic_coffee_cup[f'(샷{mul}2)아아A']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(샷{mul}2)아아A {dic_coffee_cup[f'(샷{mul}2)아아A']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(샷{mul}2)아아A {dic_coffee_cup[f'(샷{mul}2)아아A']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(샷{mul}2)아아A {dic_coffee_cup[f'(샷{mul}2)아아A']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(샷{mul}2)아아A {dic_coffee_cup[f'(샷{mul}2)아아A']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"

            elif (self.last_selected == "Ice") and (self.last_selected2 == "B"):
                dic_coffee_sum["(샷\u00D72)아아B"] += (3500 * count)
                dic_coffee_cup["(샷\u00D72)아아B"] += count
                #self.메뉴1_button.text = f"아메리카노 {아메리카노_잔수}"
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(샷{mul}2)아아B {dic_coffee_cup[f'(샷{mul}2)아아B']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(샷{mul}2)아아B {dic_coffee_cup[f'(샷{mul}2)아아B']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(샷{mul}2)아아B {dic_coffee_cup[f'(샷{mul}2)아아B']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(샷{mul}2)아아B {dic_coffee_cup[f'(샷{mul}2)아아B']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(샷{mul}2)아아B {dic_coffee_cup[f'(샷{mul}2)아아B']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(샷{mul}2)아아B {dic_coffee_cup[f'(샷{mul}2)아아B']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(샷{mul}2)아아B {dic_coffee_cup[f'(샷{mul}2)아아B']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"
        
            elif (self.last_selected == "Hot") and (self.last_selected2 == "A"):
                dic_coffee_sum["(샷\u00D72)뜨아A"] += (3500 * count)
                dic_coffee_cup["(샷\u00D72)뜨아A"] += count
                #self.메뉴1_button.text = f"아메리카노 {아메리카노_잔수}"
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(샷{mul}2)뜨아A {dic_coffee_cup[f'(샷{mul}2)뜨아A']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(샷{mul}2)뜨아A {dic_coffee_cup[f'(샷{mul}2)뜨아A']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(샷{mul}2)뜨아A {dic_coffee_cup[f'(샷{mul}2)뜨아A']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(샷{mul}2)뜨아A {dic_coffee_cup[f'(샷{mul}2)뜨아A']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(샷{mul}2)뜨아A {dic_coffee_cup[f'(샷{mul}2)뜨아A']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(샷{mul}2)뜨아A {dic_coffee_cup[f'(샷{mul}2)뜨아A']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(샷{mul}2)뜨아A {dic_coffee_cup[f'(샷{mul}2)뜨아A']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"
                
            elif (self.last_selected == "Hot") and (self.last_selected2 == "B"):
                dic_coffee_sum["(샷\u00D72)뜨아B"] += (3500 * count)
                dic_coffee_cup["(샷\u00D72)뜨아B"] += count
                #self.메뉴1_button.text = f"아메리카노 {아메리카노_잔수}"
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(샷{mul}2)뜨아B {dic_coffee_cup[f'(샷{mul}2)뜨아B']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(샷{mul}2)뜨아B {dic_coffee_cup[f'(샷{mul}2)뜨아B']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(샷{mul}2)뜨아B {dic_coffee_cup[f'(샷{mul}2)뜨아B']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(샷{mul}2)뜨아B {dic_coffee_cup[f'(샷{mul}2)뜨아B']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(샷{mul}2)뜨아B {dic_coffee_cup[f'(샷{mul}2)뜨아B']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(샷{mul}2)뜨아B {dic_coffee_cup[f'(샷{mul}2)뜨아B']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(샷{mul}2)뜨아B {dic_coffee_cup[f'(샷{mul}2)뜨아B']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"
                
    def go_to_아메리카노샷3(self,instance):
        global count,dic_coffee_sum,dic_coffee_cup
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if ((self.last_selected == "Ice" and self.last_selected2 == "A") and "(아샷추\u00D71)아아A" in lst) or ((self.last_selected == "Ice" and self.last_selected2 == "B") and "(아샷추\u00D71)아아B" in lst) or ((self.last_selected == "Hot" and self.last_selected2 == "A") and "(아샷추\u00D71)뜨아A" in lst) or ((self.last_selected == "Hot" and self.last_selected2 == "B") and "(아샷추\u00D71)뜨아B" in lst) :
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            if (self.last_selected == "Ice") and (self.last_selected2 == "A"):
                dic_coffee_sum["(아샷추\u00D71)아아A"] += (3000 * count)
                dic_coffee_cup["(아샷추\u00D71)아아A"] += count
                #self.메뉴1_button.text = f"아메리카노 {아메리카노_잔수}"
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(아샷추{mul}1)아아A {dic_coffee_cup[f'(아샷추{mul}1)아아A']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(아샷추{mul}1)아아A {dic_coffee_cup[f'(아샷추{mul}1)아아A']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(아샷추{mul}1)아아A {dic_coffee_cup[f'(아샷추{mul}1)아아A']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(아샷추{mul}1)아아A {dic_coffee_cup[f'(아샷추{mul}1)아아A']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(아샷추{mul}1)아아A {dic_coffee_cup[f'(아샷추{mul}1)아아A']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(아샷추{mul}1)아아A {dic_coffee_cup[f'(아샷추{mul}1)아아A']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(아샷추{mul}1)아아A {dic_coffee_cup[f'(아샷추{mul}1)아아A']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"

            elif (self.last_selected == "Ice") and (self.last_selected2 == "B"):
                dic_coffee_sum["(아샷추\u00D71)아아B"] += (3000 * count)
                dic_coffee_cup["(아샷추\u00D71)아아B"] += count
                #self.메뉴1_button.text = f"아메리카노 {아메리카노_잔수}"
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(아샷추{mul}1)아아B {dic_coffee_cup[f'(아샷추{mul}1)아아B']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(아샷추{mul}1)아아B {dic_coffee_cup[f'(아샷추{mul}1)아아B']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(아샷추{mul}1)아아B {dic_coffee_cup[f'(아샷추{mul}1)아아B']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(아샷추{mul}1)아아B {dic_coffee_cup[f'(아샷추{mul}1)아아B']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(아샷추{mul}1)아아B {dic_coffee_cup[f'(아샷추{mul}1)아아B']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(아샷추{mul}1)아아B {dic_coffee_cup[f'(아샷추{mul}1)아아B']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(아샷추{mul}1)아아B {dic_coffee_cup[f'(아샷추{mul}1)아아B']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"
        
            elif (self.last_selected == "Hot") and (self.last_selected2 == "A"):
                dic_coffee_sum["(아샷추\u00D71)뜨아A"] += (3000 * count)
                dic_coffee_cup["(아샷추\u00D71)뜨아A"] += count
                #self.메뉴1_button.text = f"아메리카노 {아메리카노_잔수}"
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(아샷추{mul}1)뜨아A {dic_coffee_cup[f'(아샷추{mul}1)뜨아A']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(아샷추{mul}1)뜨아A {dic_coffee_cup[f'(아샷추{mul}1)뜨아A']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(아샷추{mul}1)뜨아A {dic_coffee_cup[f'(아샷추{mul}1)뜨아A']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(아샷추{mul}1)뜨아A {dic_coffee_cup[f'(아샷추{mul}1)뜨아A']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(아샷추{mul}1)뜨아A {dic_coffee_cup[f'(아샷추{mul}1)뜨아A']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(아샷추{mul}1)뜨아A {dic_coffee_cup[f'(아샷추{mul}1)뜨아A']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(아샷추{mul}1)뜨아A {dic_coffee_cup[f'(아샷추{mul}1)뜨아A']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"
                
            elif (self.last_selected == "Hot") and (self.last_selected2 == "B"):
                dic_coffee_sum["(아샷추\u00D71)뜨아B"] += (3000 * count)
                dic_coffee_cup["(아샷추\u00D71)뜨아B"] += count
                #self.메뉴1_button.text = f"아메리카노 {아메리카노_잔수}"
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(아샷추{mul}1)뜨아B {dic_coffee_cup[f'(아샷추{mul}1)뜨아B']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(아샷추{mul}1)뜨아B {dic_coffee_cup[f'(아샷추{mul}1)뜨아B']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(아샷추{mul}1)뜨아B {dic_coffee_cup[f'(아샷추{mul}1)뜨아B']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(아샷추{mul}1)뜨아B {dic_coffee_cup[f'(아샷추{mul}1)뜨아B']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(아샷추{mul}1)뜨아B {dic_coffee_cup[f'(아샷추{mul}1)뜨아B']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(아샷추{mul}1)뜨아B {dic_coffee_cup[f'(아샷추{mul}1)뜨아B']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(아샷추{mul}1)뜨아B {dic_coffee_cup[f'(아샷추{mul}1)뜨아B']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"
                
    def go_to_아메리카노샷4(self,instance):
        global count,dic_coffee_sum,dic_coffee_cup
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if ((self.last_selected == "Ice" and self.last_selected2 == "A") and "(아샷추\u00D72)아아A" in lst) or ((self.last_selected == "Ice" and self.last_selected2 == "B") and "(아샷추\u00D72)아아B" in lst) or ((self.last_selected == "Hot" and self.last_selected2 == "A") and "(아샷추\u00D72)뜨아A" in lst) or ((self.last_selected == "Hot" and self.last_selected2 == "B") and "(아샷추\u00D72)뜨아B" in lst) :
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            if (self.last_selected == "Ice") and (self.last_selected2 == "A"):
                dic_coffee_sum["(아샷추\u00D72)아아A"] += (3500 * count)
                dic_coffee_cup["(아샷추\u00D72)아아A"] += count
                #self.메뉴1_button.text = f"아메리카노 {아메리카노_잔수}"
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(아샷추{mul}2)아아A {dic_coffee_cup[f'(아샷추{mul}2)아아A']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(아샷추{mul}2)아아A {dic_coffee_cup[f'(아샷추{mul}2)아아A']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(아샷추{mul}2)아아A {dic_coffee_cup[f'(아샷추{mul}2)아아A']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(아샷추{mul}2)아아A {dic_coffee_cup[f'(아샷추{mul}2)아아A']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(아샷추{mul}2)아아A {dic_coffee_cup[f'(아샷추{mul}2)아아A']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(아샷추{mul}2)아아A {dic_coffee_cup[f'(아샷추{mul}2)아아A']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(아샷추{mul}2)아아A {dic_coffee_cup[f'(아샷추{mul}2)아아A']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"

            elif (self.last_selected == "Ice") and (self.last_selected2 == "B"):
                dic_coffee_sum["(아샷추\u00D72)아아B"] += (3500 * count)
                dic_coffee_cup["(아샷추\u00D72)아아B"] += count
                #self.메뉴1_button.text = f"아메리카노 {아메리카노_잔수}"
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(아샷추{mul}2)아아B {dic_coffee_cup[f'(아샷추{mul}2)아아B']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(아샷추{mul}2)아아B {dic_coffee_cup[f'(아샷추{mul}2)아아B']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(아샷추{mul}2)아아B {dic_coffee_cup[f'(아샷추{mul}2)아아B']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(아샷추{mul}2)아아B {dic_coffee_cup[f'(아샷추{mul}2)아아B']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(아샷추{mul}2)아아B {dic_coffee_cup[f'(아샷추{mul}2)아아B']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(아샷추{mul}2)아아B {dic_coffee_cup[f'(아샷추{mul}2)아아B']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(아샷추{mul}2)아아B {dic_coffee_cup[f'(아샷추{mul}2)아아B']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"
        
            elif (self.last_selected == "Hot") and (self.last_selected2 == "A"):
                dic_coffee_sum["(아샷추\u00D72)뜨아A"] += (3500 * count)
                dic_coffee_cup["(아샷추\u00D72)뜨아A"] += count
                #self.메뉴1_button.text = f"아메리카노 {아메리카노_잔수}"
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(아샷추{mul}2)뜨아A {dic_coffee_cup[f'(아샷추{mul}2)뜨아A']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(아샷추{mul}2)뜨아A {dic_coffee_cup[f'(아샷추{mul}2)뜨아A']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(아샷추{mul}2)뜨아A {dic_coffee_cup[f'(아샷추{mul}2)뜨아A']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(아샷추{mul}2)뜨아A {dic_coffee_cup[f'(아샷추{mul}2)뜨아A']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(아샷추{mul}2)뜨아A {dic_coffee_cup[f'(아샷추{mul}2)뜨아A']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(아샷추{mul}2)뜨아A {dic_coffee_cup[f'(아샷추{mul}2)뜨아A']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(아샷추{mul}2)뜨아A {dic_coffee_cup[f'(아샷추{mul}2)뜨아A']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"
                
            elif (self.last_selected == "Hot") and (self.last_selected2 == "B"):
                dic_coffee_sum["(아샷추\u00D72)뜨아B"] += (3500 * count)
                dic_coffee_cup["(아샷추\u00D72)뜨아B"] += count
                #self.메뉴1_button.text = f"아메리카노 {아메리카노_잔수}"
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(아샷추{mul}2)뜨아B {dic_coffee_cup[f'(아샷추{mul}2)뜨아B']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(아샷추{mul}2)뜨아B {dic_coffee_cup[f'(아샷추{mul}2)뜨아B']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(아샷추{mul}2)뜨아B {dic_coffee_cup[f'(아샷추{mul}2)뜨아B']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(아샷추{mul}2)뜨아B {dic_coffee_cup[f'(아샷추{mul}2)뜨아B']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(아샷추{mul}2)뜨아B {dic_coffee_cup[f'(아샷추{mul}2)뜨아B']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(아샷추{mul}2)뜨아B {dic_coffee_cup[f'(아샷추{mul}2)뜨아B']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(아샷추{mul}2)뜨아B {dic_coffee_cup[f'(아샷추{mul}2)뜨아B']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"
                
                
    def go_to_에스프레소(self,instance):
        global count,dic_coffee_sum,dic_coffee_cup
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if (self.last_selected == "Hot" and '(Hot)에스프레소' in lst) or (self.last_selected == "Ice" and '(Ice)에스프레소' in lst):
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            if self.last_selected == "Hot":
                dic_coffee_sum['(Hot)에스프레소'] += (2500 * count)
                dic_coffee_cup['(Hot)에스프레소'] += count
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(Hot)에스프레소 {dic_coffee_cup['(Hot)에스프레소']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(Hot)에스프레소 {dic_coffee_cup['(Hot)에스프레소']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(Hot)에스프레소 {dic_coffee_cup['(Hot)에스프레소']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(Hot)에스프레소 {dic_coffee_cup['(Hot)에스프레소']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(Hot)에스프레소 {dic_coffee_cup['(Hot)에스프레소']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(Hot)에스프레소 {dic_coffee_cup['(Hot)에스프레소']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(Hot)에스프레소 {dic_coffee_cup['(Hot)에스프레소']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"
                
            elif self.last_selected == "Ice":
                dic_coffee_sum['(Ice)에스프레소'] += (2500 * count)
                dic_coffee_cup['(Ice)에스프레소'] += count
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(Ice)에스프레소 {dic_coffee_cup['(Ice)에스프레소']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(Ice)에스프레소 {dic_coffee_cup['(Ice)에스프레소']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(Ice)에스프레소 {dic_coffee_cup['(Ice)에스프레소']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(Ice)에스프레소 {dic_coffee_cup['(Ice)에스프레소']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(Ice)에스프레소 {dic_coffee_cup['(Ice)에스프레소']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(Ice)에스프레소 {dic_coffee_cup['(Ice)에스프레소']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(Ice)에스프레소 {dic_coffee_cup['(Ice)에스프레소']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"
            
    
    def go_to_드립(self,instance):
        global count,dic_coffee_cup,dic_coffee_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if (self.last_selected == "Ice" and '(Ice)드립' in lst) or (self.last_selected == "Hot" and '(Hot)드립' in lst):
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            if self.last_selected == "Ice":
                dic_coffee_sum['(Ice)드립'] += (4000 * count)
                dic_coffee_cup['(Ice)드립']+= count
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(Ice)드립 {dic_coffee_cup['(Ice)드립']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(Ice)드립 {dic_coffee_cup['(Ice)드립']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(Ice)드립 {dic_coffee_cup['(Ice)드립']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(Ice)드립 {dic_coffee_cup['(Ice)드립']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(Ice)드립 {dic_coffee_cup['(Ice)드립']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(Ice)드립 {dic_coffee_cup['(Ice)드립']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(Ice)드립 {dic_coffee_cup['(Ice)드립']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"
                
            elif self.last_selected == "Hot":
                dic_coffee_sum['(Hot)드립'] += (4000 * count)
                dic_coffee_cup['(Hot)드립']+= count
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(Hot)드립 {dic_coffee_cup['(Hot)드립']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(Hot)드립 {dic_coffee_cup['(Hot)드립']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(Hot)드립 {dic_coffee_cup['(Hot)드립']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(Hot)드립 {dic_coffee_cup['(Hot)드립']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(Hot)드립 {dic_coffee_cup['(Hot)드립']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(Hot)드립 {dic_coffee_cup['(Hot)드립']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(Hot)드립 {dic_coffee_cup['(Hot)드립']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"
        
    def go_to_더치(self,instance):
        global count,dic_coffee_cup,dic_coffee_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if (self.last_selected == "Ice" and '(Ice)더치' in lst) or (self.last_selected == "Hot" and '(Hot)더치' in lst):
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            if (self.last_selected == "Ice"):
                dic_coffee_sum['(Ice)더치'] += (3500 * count)
                dic_coffee_cup['(Ice)더치'] += count
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(Ice)더치 {dic_coffee_cup['(Ice)더치']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(Ice)더치 {dic_coffee_cup['(Ice)더치']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(Ice)더치 {dic_coffee_cup['(Ice)더치']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(Ice)더치 {dic_coffee_cup['(Ice)더치']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(Ice)더치 {dic_coffee_cup['(Ice)더치']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(Ice)더치 {dic_coffee_cup['(Ice)더치']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(Ice)더치 {dic_coffee_cup['(Ice)더치']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"
                
            elif (self.last_selected == "Hot"):
                dic_coffee_sum['(Hot)더치'] += (3500 * count)
                dic_coffee_cup['(Hot)더치'] += count
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(Hot)더치 {dic_coffee_cup['(Hot)더치']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(Hot)더치 {dic_coffee_cup['(Hot)더치']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(Hot)더치 {dic_coffee_cup['(Hot)더치']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(Hot)더치 {dic_coffee_cup['(Hot)더치']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(Hot)더치 {dic_coffee_cup['(Hot)더치']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(Hot)더치 {dic_coffee_cup['(Hot)더치']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(Hot)더치 {dic_coffee_cup['(Hot)더치']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"
        
    def go_to_라떼(self,instance):
        global count,dic_coffee_cup,dic_coffee_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if (self.last_selected == "Ice" and '(Ice)라떼' in lst) or (self.last_selected == "Hot" and '(Hot)라떼' in lst):
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            if self.last_selected == "Ice":
                dic_coffee_sum['(Ice)라떼'] += (3000 * count)
                dic_coffee_cup['(Ice)라떼'] += count
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(Ice)라떼 {dic_coffee_cup['(Ice)라떼']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(Ice)라떼 {dic_coffee_cup['(Ice)라떼']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(Ice)라떼 {dic_coffee_cup['(Ice)라떼']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(Ice)라떼 {dic_coffee_cup['(Ice)라떼']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(Ice)라떼 {dic_coffee_cup['(Ice)라떼']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(Ice)라떼 {dic_coffee_cup['(Ice)라떼']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(Ice)라떼 {dic_coffee_cup['(Ice)라떼']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"
                
            elif self.last_selected == "Hot":
                dic_coffee_sum['(Hot)라떼'] += (3000 * count)
                dic_coffee_cup['(Hot)라떼'] += count
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(Hot)라떼 {dic_coffee_cup['(Hot)라떼']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(Hot)라떼 {dic_coffee_cup['(Hot)라떼']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(Hot)라떼 {dic_coffee_cup['(Hot)라떼']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(Hot)라떼 {dic_coffee_cup['(Hot)라떼']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(Hot)라떼 {dic_coffee_cup['(Hot)라떼']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(Hot)라떼 {dic_coffee_cup['(Hot)라떼']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(Hot)라떼 {dic_coffee_cup['(Hot)라떼']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"
        
    def go_to_더치라떼(self,instance):
        global count,dic_coffee_sum,dic_coffee_cup
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if (self.last_selected == 'Ice' and '(Ice)더치라떼' in lst) or (self.last_selected == 'Hot' and '(Hot)더치라떼' in lst):
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            if self.last_selected == 'Ice':
                dic_coffee_sum['(Ice)더치라떼'] += (4000 * count)
                dic_coffee_cup['(Ice)더치라떼'] += count
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(Ice)더치라떼 {dic_coffee_cup['(Ice)더치라떼']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(Ice)더치라떼 {dic_coffee_cup['(Ice)더치라떼']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(Ice)더치라떼 {dic_coffee_cup['(Ice)더치라떼']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(Ice)더치라떼 {dic_coffee_cup['(Ice)더치라떼']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(Ice)더치라떼 {dic_coffee_cup['(Ice)더치라떼']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(Ice)더치라떼 {dic_coffee_cup['(Ice)더치라떼']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(Ice)더치라떼 {dic_coffee_cup['(Ice)더치라떼']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"
                
            elif self.last_selected == 'Hot':
                dic_coffee_sum['(Hot)더치라떼'] += (4000 * count)
                dic_coffee_cup['(Hot)더치라떼'] += count
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(Hot)더치라떼 {dic_coffee_cup['(Hot)더치라떼']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(Hot)더치라떼 {dic_coffee_cup['(Hot)더치라떼']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(Hot)더치라떼 {dic_coffee_cup['(Hot)더치라떼']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(Hot)더치라떼 {dic_coffee_cup['(Hot)더치라떼']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(Hot)더치라떼 {dic_coffee_cup['(Hot)더치라떼']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(Hot)더치라떼 {dic_coffee_cup['(Hot)더치라떼']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(Hot)더치라떼 {dic_coffee_cup['(Hot)더치라떼']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"
        
    def go_to_바닐라라떼(self,instance):
        global count,dic_coffee_sum,dic_coffee_cup
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if (self.last_selected == "Ice" and '(Ice)바닐라라떼' in lst) or (self.last_selected == "Hot" and '(Hot)바닐라라떼' in lst):
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            if self.last_selected == "Ice":
                dic_coffee_sum['(Ice)바닐라라떼'] += (3500 * count)
                dic_coffee_cup['(Ice)바닐라라떼'] += count
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(Ice)바닐라라떼 {dic_coffee_cup['(Ice)바닐라라떼']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(Ice)바닐라라떼 {dic_coffee_cup['(Ice)바닐라라떼']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(Ice)바닐라라떼 {dic_coffee_cup['(Ice)바닐라라떼']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(Ice)바닐라라떼 {dic_coffee_cup['(Ice)바닐라라떼']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(Ice)바닐라라떼 {dic_coffee_cup['(Ice)바닐라라떼']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(Ice)바닐라라떼 {dic_coffee_cup['(Ice)바닐라라떼']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(Ice)바닐라라떼 {dic_coffee_cup['(Ice)바닐라라떼']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"
        
            if self.last_selected == "Hot":
                dic_coffee_sum['(Hot)바닐라라떼'] += (3500 * count)
                dic_coffee_cup['(Hot)바닐라라떼'] += count
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(Hot)바닐라라떼 {dic_coffee_cup['(Hot)바닐라라떼']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(Hot)바닐라라떼 {dic_coffee_cup['(Hot)바닐라라떼']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(Hot)바닐라라떼 {dic_coffee_cup['(Hot)바닐라라떼']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(Hot)바닐라라떼 {dic_coffee_cup['(Hot)바닐라라떼']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(Hot)바닐라라떼 {dic_coffee_cup['(Hot)바닐라라떼']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(Hot)바닐라라떼 {dic_coffee_cup['(Hot)바닐라라떼']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(Hot)바닐라라떼 {dic_coffee_cup['(Hot)바닐라라떼']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"
                
                
    def go_to_민트라떼종류(self,instance):
        global count,dic_coffee_sum,dic_coffee_cup
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '민트라떼' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_coffee_sum['민트라떼'] += (4000 * count)
            dic_coffee_cup['민트라떼'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"민트라떼 {dic_coffee_cup['민트라떼']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"민트라떼 {dic_coffee_cup['민트라떼']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"민트라떼 {dic_coffee_cup['민트라떼']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"민트라떼 {dic_coffee_cup['민트라떼']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"민트라떼 {dic_coffee_cup['민트라떼']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"민트라떼 {dic_coffee_cup['민트라떼']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"민트라떼 {dic_coffee_cup['민트라떼']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
            print(f"{dic_coffee_sum['민트라떼']} {dic_coffee_cup['민트라떼']}")
            
    def go_to_카푸치노(self,instance):
        global count,dic_coffee_cup,dic_coffee_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '카푸치노' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_coffee_sum['카푸치노'] += (3000 * count)
            dic_coffee_cup['카푸치노'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"카푸치노 {dic_coffee_cup['카푸치노']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"카푸치노 {dic_coffee_cup['카푸치노']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"카푸치노 {dic_coffee_cup['카푸치노']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"카푸치노 {dic_coffee_cup['카푸치노']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"카푸치노 {dic_coffee_cup['카푸치노']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"카푸치노 {dic_coffee_cup['카푸치노']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"카푸치노 {dic_coffee_cup['카푸치노']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
            print(f"{dic_coffee_sum['카푸치노']} {dic_coffee_cup['카푸치노']}")
        
    def go_to_콜드브루(self,instance):
        global count,dic_coffee_cup,dic_coffee_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if (self.last_selected == "Ice" and '(Ice)콜드브루' in lst) or (self.last_selected == "Hot" and '(Hot)콜드브루' in lst):
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            if self.last_selected == "Ice":
                dic_coffee_sum['(Ice)콜드브루'] += (3000 * count)
                dic_coffee_cup['(Ice)콜드브루'] += count
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(Ice)콜드브루 {dic_coffee_cup['(Ice)콜드브루']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(Ice)콜드브루 {dic_coffee_cup['(Ice)콜드브루']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(Ice)콜드브루 {dic_coffee_cup['(Ice)콜드브루']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(Ice)콜드브루 {dic_coffee_cup['(Ice)콜드브루']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(Ice)콜드브루 {dic_coffee_cup['(Ice)콜드브루']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(Ice)콜드브루 {dic_coffee_cup['(Ice)콜드브루']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(Ice)콜드브루 {dic_coffee_cup['(Ice)콜드브루']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"

            elif self.last_selected == "Hot":
                dic_coffee_sum['(Hot)콜드브루'] += (3000 * count)
                dic_coffee_cup['(Hot)콜드브루'] += count
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(Hot)콜드브루 {dic_coffee_cup['(Hot)콜드브루']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(Hot)콜드브루 {dic_coffee_cup['(Hot)콜드브루']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(Hot)콜드브루 {dic_coffee_cup['(Hot)콜드브루']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(Hot)콜드브루 {dic_coffee_cup['(Hot)콜드브루']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(Hot)콜드브루 {dic_coffee_cup['(Hot)콜드브루']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(Hot)콜드브루 {dic_coffee_cup['(Hot)콜드브루']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(Hot)콜드브루 {dic_coffee_cup['(Hot)콜드브루']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"
                
    def go_to_카페모카(self,instance):
        global count,dic_coffee_cup,dic_coffee_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if (self.last_selected == 'Ice' and '(Ice)카페모카' in lst) and (self.last_selected == 'Hot' and '(Hot)카페모카' in lst):
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            if self.last_selected == 'Ice':
                dic_coffee_sum['(Ice)카페모카'] += (3500 * count)
                dic_coffee_cup['(Ice)카페모카'] += count
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(Ice)카페모카 {dic_coffee_cup['(Ice)카페모카']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(Ice)카페모카 {dic_coffee_cup['(Ice)카페모카']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(Ice)카페모카 {dic_coffee_cup['(Ice)카페모카']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(Ice)카페모카 {dic_coffee_cup['(Ice)카페모카']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(Ice)카페모카 {dic_coffee_cup['(Ice)카페모카']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(Ice)카페모카 {dic_coffee_cup['(Ice)카페모카']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(Ice)카페모카 {dic_coffee_cup['(Ice)카페모카']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"
                
            elif self.last_selected == 'Hot':
                dic_coffee_sum['(Hot)카페모카'] += (3500 * count)
                dic_coffee_cup['(Hot)카페모카'] += count
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(Hot)카페모카 {dic_coffee_cup['(Hot)카페모카']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(Hot)카페모카 {dic_coffee_cup['(Hot)카페모카']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(Hot)카페모카 {dic_coffee_cup['(Hot)카페모카']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(Hot)카페모카 {dic_coffee_cup['(Hot)카페모카']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(Hot)카페모카 {dic_coffee_cup['(Hot)카페모카']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(Hot)카페모카 {dic_coffee_cup['(Hot)카페모카']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(Hot)카페모카 {dic_coffee_cup['(Hot)카페모카']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"
        
    def go_to_보리커피(self,instance):
        global count,dic_coffee_cup,dic_coffee_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if (self.last_selected == 'Ice' and '(Ice)보리커피' in lst) or (self.last_selected == 'Hot' and '(Hot)보리커피' in lst):
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            if self.last_selected == 'Ice':
                dic_coffee_sum['(Ice)보리커피'] += (2500 * count)
                dic_coffee_cup['(Ice)보리커피'] += count
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(Ice)보리커피 {dic_coffee_cup['(Ice)보리커피']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(Ice)보리커피 {dic_coffee_cup['(Ice)보리커피']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(Ice)보리커피 {dic_coffee_cup['(Ice)보리커피']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(Ice)보리커피 {dic_coffee_cup['(Ice)보리커피']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(Ice)보리커피 {dic_coffee_cup['(Ice)보리커피']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(Ice)보리커피 {dic_coffee_cup['(Ice)보리커피']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(Ice)보리커피 {dic_coffee_cup['(Ice)보리커피']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"
                
            elif self.last_selected == 'Hot':
                dic_coffee_sum['(Hot)보리커피'] += (2500 * count)
                dic_coffee_cup['(Hot)보리커피'] += count
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(Hot)보리커피 {dic_coffee_cup['(Hot)보리커피']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(Hot)보리커피 {dic_coffee_cup['(Hot)보리커피']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(Hot)보리커피 {dic_coffee_cup['(Hot)보리커피']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(Hot)보리커피 {dic_coffee_cup['(Hot)보리커피']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(Hot)보리커피 {dic_coffee_cup['(Hot)보리커피']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(Hot)보리커피 {dic_coffee_cup['(Hot)보리커피']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(Hot)보리커피 {dic_coffee_cup['(Hot)보리커피']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"
        
    def go_to_플렛화이트(self,instance):
        global count,dic_coffee_cup,dic_coffee_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if (self.last_selected == 'Ice' and '(Ice)플렛화이트' in lst) or (self.last_selected == 'Hot' and '(Hot)플렛화이트' in lst):
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            if self.last_selected == 'Ice':
                dic_coffee_sum['(Ice)플렛화이트'] += (3000 * count)
                dic_coffee_cup['(Ice)플렛화이트'] += count
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(Ice)플렛화이트 {dic_coffee_cup['(Ice)플렛화이트']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(Ice)플렛화이트 {dic_coffee_cup['(Ice)플렛화이트']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(Ice)플렛화이트 {dic_coffee_cup['(Ice)플렛화이트']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(Ice)플렛화이트 {dic_coffee_cup['(Ice)플렛화이트']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(Ice)플렛화이트 {dic_coffee_cup['(Ice)플렛화이트']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(Ice)플렛화이트 {dic_coffee_cup['(Ice)플렛화이트']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(Ice)플렛화이트 {dic_coffee_cup['(Ice)플렛화이트']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"
                
            if self.last_selected == 'Hot':
                dic_coffee_sum['(Hot)플렛화이트'] += (3000 * count)
                dic_coffee_cup['(Hot)플렛화이트'] += count
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(Hot)플렛화이트 {dic_coffee_cup['(Hot)플렛화이트']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(Hot)플렛화이트 {dic_coffee_cup['(Hot)플렛화이트']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(Hot)플렛화이트 {dic_coffee_cup['(Hot)플렛화이트']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(Hot)플렛화이트 {dic_coffee_cup['(Hot)플렛화이트']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(Hot)플렛화이트 {dic_coffee_cup['(Hot)플렛화이트']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(Hot)플렛화이트 {dic_coffee_cup['(Hot)플렛화이트']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(Hot)플렛화이트 {dic_coffee_cup['(Hot)플렛화이트']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"

    def go_to_꼼빠냐(self,instance):
        global count,dic_coffee_cup,dic_coffee_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '꼼빠냐' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_coffee_sum['꼼빠냐'] += (3500 * count)
            dic_coffee_cup['꼼빠냐'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"꼼빠냐 {dic_coffee_cup['꼼빠냐']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"꼼빠냐 {dic_coffee_cup['꼼빠냐']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"꼼빠냐 {dic_coffee_cup['꼼빠냐']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"꼼빠냐 {dic_coffee_cup['꼼빠냐']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"꼼빠냐 {dic_coffee_cup['꼼빠냐']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"꼼빠냐 {dic_coffee_cup['꼼빠냐']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"꼼빠냐 {dic_coffee_cup['꼼빠냐']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
            print(f"{dic_coffee_sum['꼼빠냐']} {dic_coffee_cup['꼼빠냐']}")
        
    def go_to_아인슈페너(self,instance):
        global count,dic_coffee_cup,dic_coffee_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if (self.last_selected == 'Ice' and '(Ice)아인슈페너' in lst) or (self.last_selected == 'Hot' and '(Hot)아인슈페너' in lst):
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            if self.last_selected == 'Ice':
                dic_coffee_sum['(Ice)아인슈페너'] += (4000 * count)
                dic_coffee_cup['(Ice)아인슈페너'] += count
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(Ice)아인슈페너 {dic_coffee_cup['(Ice)아인슈페너']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(Ice)아인슈페너 {dic_coffee_cup['(Ice)아인슈페너']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(Ice)아인슈페너 {dic_coffee_cup['(Ice)아인슈페너']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(Ice)아인슈페너 {dic_coffee_cup['(Ice)아인슈페너']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(Ice)아인슈페너 {dic_coffee_cup['(Ice)아인슈페너']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(Ice)아인슈페너 {dic_coffee_cup['(Ice)아인슈페너']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(Ice)아인슈페너 {dic_coffee_cup['(Ice)아인슈페너']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"
                
            elif self.last_selected == 'Hot':
                dic_coffee_sum['(Hot)아인슈페너'] += (4000 * count)
                dic_coffee_cup['(Hot)아인슈페너'] += count
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(Hot)아인슈페너 {dic_coffee_cup['(Hot)아인슈페너']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(Hot)아인슈페너 {dic_coffee_cup['(Hot)아인슈페너']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(Hot)아인슈페너 {dic_coffee_cup['(Hot)아인슈페너']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(Hot)아인슈페너 {dic_coffee_cup['(Hot)아인슈페너']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(Hot)아인슈페너 {dic_coffee_cup['(Hot)아인슈페너']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(Hot)아인슈페너 {dic_coffee_cup['(Hot)아인슈페너']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(Hot)아인슈페너 {dic_coffee_cup['(Hot)아인슈페너']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"
        
    def go_to_베리고(self,instance):
        global count,dic_beverage_cup,dic_beverage_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '베리고' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_beverage_sum['베리고'] += (4000 * count)
            dic_beverage_cup['베리고'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"베리고 {dic_beverage_cup['베리고']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"베리고 {dic_beverage_cup['베리고']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"베리고 {dic_beverage_cup['베리고']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"베리고 {dic_beverage_cup['베리고']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"베리고 {dic_beverage_cup['베리고']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"베리고 {dic_beverage_cup['베리고']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"베리고 {dic_beverage_cup['베리고']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_망고스무디(self,instance):
        global count,dic_beverage_cup,dic_beverage_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '망고스무디' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_beverage_sum['망고스무디'] += (4000 * count)
            dic_beverage_cup['망고스무디'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"망고스무디 {dic_beverage_cup['망고스무디']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"망고스무디 {dic_beverage_cup['망고스무디']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"망고스무디 {dic_beverage_cup['망고스무디']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"망고스무디 {dic_beverage_cup['망고스무디']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"망고스무디 {dic_beverage_cup['망고스무디']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"망고스무디 {dic_beverage_cup['망고스무디']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"망고스무디 {dic_beverage_cup['망고스무디']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_아보카도바나나(self,instance):
        global count,dic_beverage_cup,dic_beverage_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '아보카도바나나' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_beverage_sum['아보카도바나나'] += (3500 * count)
            dic_beverage_cup['아보카도바나나'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"아보카도바나나 {dic_beverage_cup['아보카도바나나']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"아보카도바나나 {dic_beverage_cup['아보카도바나나']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"아보카도바나나 {dic_beverage_cup['아보카도바나나']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"아보카도바나나 {dic_beverage_cup['아보카도바나나']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"아보카도바나나 {dic_beverage_cup['아보카도바나나']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"아보카도바나나 {dic_beverage_cup['아보카도바나나']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"아보카도바나나 {dic_beverage_cup['아보카도바나나']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_망고바나나(self,instance):
        global count,dic_beverage_cup,dic_beverage_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '망고바나나' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_beverage_sum['망고바나나'] += (4000 * count)
            dic_beverage_cup['망고바나나'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"망고바나나 {dic_beverage_cup['망고바나나']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"망고바나나 {dic_beverage_cup['망고바나나']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"망고바나나 {dic_beverage_cup['망고바나나']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"망고바나나 {dic_beverage_cup['망고바나나']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"망고바나나 {dic_beverage_cup['망고바나나']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"망고바나나 {dic_beverage_cup['망고바나나']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"망고바나나 {dic_beverage_cup['망고바나나']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_패션후르츠(self,instance):
        global count,dic_beverage_cup,dic_beverage_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '패션후르츠' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_beverage_sum['패션후르츠'] += (3500 * count)
            dic_beverage_cup['패션후르츠'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"패션후르츠 {dic_beverage_cup['패션후르츠']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"패션후르츠 {dic_beverage_cup['패션후르츠']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"패션후르츠 {dic_beverage_cup['패션후르츠']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"패션후르츠 {dic_beverage_cup['패션후르츠']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"패션후르츠 {dic_beverage_cup['패션후르츠']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"패션후르츠 {dic_beverage_cup['패션후르츠']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"패션후르츠 {dic_beverage_cup['패션후르츠']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_레몬에이드(self,instance):
        global count,dic_beverage_cup,dic_beverage_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '레몬에이드' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_beverage_sum['레몬에이드'] += (3500 * count)
            dic_beverage_cup['레몬에이드'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"레몬에이드 {dic_beverage_cup['레몬에이드']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"레몬에이드 {dic_beverage_cup['레몬에이드']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"레몬에이드 {dic_beverage_cup['레몬에이드']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"레몬에이드 {dic_beverage_cup['레몬에이드']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"레몬에이드 {dic_beverage_cup['레몬에이드']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"레몬에이드 {dic_beverage_cup['레몬에이드']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"레몬에이드 {dic_beverage_cup['레몬에이드']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_복숭아바질(self,instance):
        global count,dic_beverage_cup,dic_beverage_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '복숭아바질' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_beverage_sum['복숭아바질'] += (3500 * count)
            dic_beverage_cup['복숭아바질'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"복숭아바질 {dic_beverage_cup['복숭아바질']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"복숭아바질 {dic_beverage_cup['복숭아바질']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"복숭아바질 {dic_beverage_cup['복숭아바질']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"복숭아바질 {dic_beverage_cup['복숭아바질']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"복숭아바질 {dic_beverage_cup['복숭아바질']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"복숭아바질 {dic_beverage_cup['복숭아바질']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"복숭아바질 {dic_beverage_cup['복숭아바질']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_초코라떼(self,instance):
        global count,dic_beverage_cup,dic_beverage_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if (self.last_selected == 'Ice' and '(Ice)초코라떼' in lst) or (self.last_selected == 'Hot' and '(Hot)초코라떼' in lst):
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            if self.last_selected == 'Ice':
                dic_beverage_sum['(Ice)초코라떼'] += (3500 * count)
                dic_beverage_cup['(Ice)초코라떼'] += count
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(Ice)초코라떼 {dic_beverage_cup['(Ice)초코라떼']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(Ice)초코라떼 {dic_beverage_cup['(Ice)초코라떼']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(Ice)초코라떼 {dic_beverage_cup['(Ice)초코라떼']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(Ice)초코라떼 {dic_beverage_cup['(Ice)초코라떼']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(Ice)초코라떼 {dic_beverage_cup['(Ice)초코라떼']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(Ice)초코라떼 {dic_beverage_cup['(Ice)초코라떼']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(Ice)초코라떼 {dic_beverage_cup['(Ice)초코라떼']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"
                
            elif self.last_selected == 'Hot':
                dic_beverage_sum['(Hot)초코라떼'] += (3500 * count)
                dic_beverage_cup['(Hot)초코라떼'] += count
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(Hot)초코라떼 {dic_beverage_cup['(Hot)초코라떼']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(Hot)초코라떼 {dic_beverage_cup['(Hot)초코라떼']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(Hot)초코라떼 {dic_beverage_cup['(Hot)초코라떼']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(Hot)초코라떼 {dic_beverage_cup['(Hot)초코라떼']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(Hot)초코라떼 {dic_beverage_cup['(Hot)초코라떼']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(Hot)초코라떼 {dic_beverage_cup['(Hot)초코라떼']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(Hot)초코라떼 {dic_beverage_cup['(Hot)초코라떼']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"
        
    def go_to_Hot초코(self,instance):
        global count,dic_beverage_cup,dic_beverage_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if 'Hot초코' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_beverage_sum['Hot초코'] += (3500 * count)
            dic_beverage_cup['Hot초코'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"Hot초코 {dic_beverage_cup['Hot초코']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"Hot초코 {dic_beverage_cup['Hot초코']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"Hot초코 {dic_beverage_cup['Hot초코']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"Hot초코 {dic_beverage_cup['Hot초코']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"Hot초코 {dic_beverage_cup['Hot초코']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"Hot초코 {dic_beverage_cup['Hot초코']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"Hot초코 {dic_beverage_cup['Hot초코']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_자두에이드(self,instance):
        global count,dic_beverage_cup,dic_beverage_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '자두에이드' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_beverage_sum['자두에이드'] += (3500 * count)
            dic_beverage_cup['자두에이드'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"자두에이드 {dic_beverage_cup['자두에이드']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"자두에이드 {dic_beverage_cup['자두에이드']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"자두에이드 {dic_beverage_cup['자두에이드']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"자두에이드 {dic_beverage_cup['자두에이드']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"자두에이드 {dic_beverage_cup['자두에이드']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"자두에이드 {dic_beverage_cup['자두에이드']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"자두에이드 {dic_beverage_cup['자두에이드']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_유자민트티(self,instance):
        global count,dic_beverage_cup,dic_beverage_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '유자민트티' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_beverage_sum['유자민트티'] += (3000 * count)
            dic_beverage_cup['유자민트티'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"유자민트티 {dic_beverage_cup['유자민트티']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"유자민트티 {dic_beverage_cup['유자민트티']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"유자민트티 {dic_beverage_cup['유자민트티']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"유자민트티 {dic_beverage_cup['유자민트티']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"유자민트티 {dic_beverage_cup['유자민트티']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"유자민트티 {dic_beverage_cup['유자민트티']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"유자민트티 {dic_beverage_cup['유자민트티']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"

    def go_to_미숫가루(self,instance):
        global count,dic_beverage_cup,dic_beverage_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if (self.last_selected == 'Ice' and '(Ice)미숫가루' in lst) or (self.last_selected == 'Hot' and '(Hot)미숫가루' in lst):
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            if self.last_selected == 'Ice':
                dic_beverage_sum['(Ice)미숫가루'] += (3500 * count)
                dic_beverage_cup['(Ice)미숫가루'] += count
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(Ice)미숫가루 {dic_beverage_cup['(Ice)미숫가루']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(Ice)미숫가루 {dic_beverage_cup['(Ice)미숫가루']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(Ice)미숫가루 {dic_beverage_cup['(Ice)미숫가루']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(Ice)미숫가루 {dic_beverage_cup['(Ice)미숫가루']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(Ice)미숫가루 {dic_beverage_cup['(Ice)미숫가루']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(Ice)미숫가루 {dic_beverage_cup['(Ice)미숫가루']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(Ice)미숫가루 {dic_beverage_cup['(Ice)미숫가루']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"
                
            elif self.last_selected == 'Hot':
                dic_beverage_sum['(Hot)미숫가루'] += (3500 * count)
                dic_beverage_cup['(Hot)미숫가루'] += count
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(Hot)미숫가루 {dic_beverage_cup['(Hot)미숫가루']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(Hot)미숫가루 {dic_beverage_cup['(Hot)미숫가루']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(Hot)미숫가루 {dic_beverage_cup['(Hot)미숫가루']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(Hot)미숫가루 {dic_beverage_cup['(Hot)미숫가루']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(Hot)미숫가루 {dic_beverage_cup['(Hot)미숫가루']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(Hot)미숫가루 {dic_beverage_cup['(Hot)미숫가루']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(Hot)미숫가루 {dic_beverage_cup['(Hot)미숫가루']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"
        
    def go_to_밀크티(self,instance):
        global count,dic_beverage_cup,dic_beverage_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if (self.last_selected == 'Ice' and  '(Ice)밀크티' in lst) or (self.last_selected == 'Hot' and  '(Hot)밀크티' in lst):
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            if self.last_selected == 'Ice':
                dic_beverage_sum['(Ice)밀크티'] += (3000 * count)
                dic_beverage_cup['(Ice)밀크티'] += count
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(Ice)밀크티 {dic_beverage_cup['(Ice)밀크티']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(Ice)밀크티 {dic_beverage_cup['(Ice)밀크티']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(Ice)밀크티 {dic_beverage_cup['(Ice)밀크티']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(Ice)밀크티 {dic_beverage_cup['(Ice)밀크티']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(Ice)밀크티 {dic_beverage_cup['(Ice)밀크티']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(Ice)밀크티 {dic_beverage_cup['(Ice)밀크티']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(Ice)밀크티 {dic_beverage_cup['(Ice)밀크티']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"
                
            elif self.last_selected == 'Hot':
                dic_beverage_sum['(Hot)밀크티'] += (3000 * count)
                dic_beverage_cup['(Hot)밀크티'] += count
                if self.메뉴1_button.text == "":
                    self.메뉴1_button.text = f"(Hot)밀크티 {dic_beverage_cup['(Hot)밀크티']}"
                elif self.메뉴2_button.text == "":
                    self.메뉴2_button.text = f"(Hot)밀크티 {dic_beverage_cup['(Hot)밀크티']}"
                elif self.메뉴3_button.text == "":
                    self.메뉴3_button.text = f"(Hot)밀크티 {dic_beverage_cup['(Hot)밀크티']}"
                elif self.메뉴4_button.text == "":
                    self.메뉴4_button.text = f"(Hot)밀크티 {dic_beverage_cup['(Hot)밀크티']}"
                elif self.메뉴5_button.text == "":
                    self.메뉴5_button.text = f"(Hot)밀크티 {dic_beverage_cup['(Hot)밀크티']}"
                elif self.메뉴6_button.text == "":
                    self.메뉴6_button.text = f"(Hot)밀크티 {dic_beverage_cup['(Hot)밀크티']}"
                elif self.메뉴7_button.text == "":
                    self.메뉴7_button.text = f"(Hot)밀크티 {dic_beverage_cup['(Hot)밀크티']}"
                count = 1
                self.popup.dismiss()
                self.cup.text = "1"
        
    def go_to_딸기라떼(self,instance):
        global count,dic_beverage_cup,dic_beverage_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '딸기라떼' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_beverage_sum['딸기라떼'] += (3500 * count)
            dic_beverage_cup['딸기라떼'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"딸기라떼 {dic_beverage_cup['딸기라떼']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"딸기라떼 {dic_beverage_cup['딸기라떼']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"딸기라떼 {dic_beverage_cup['딸기라떼']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"딸기라떼 {dic_beverage_cup['딸기라떼']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"딸기라떼 {dic_beverage_cup['딸기라떼']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"딸기라떼 {dic_beverage_cup['딸기라떼']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"딸기라떼 {dic_beverage_cup['딸기라떼']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_애플민트스무디(self,instance):
        global count,dic_beverage_cup,dic_beverage_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '애플민트스무디' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_beverage_sum['애플민트스무디'] += (3500 * count)
            dic_beverage_cup['애플민트스무디'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"애플민트스무디 {dic_beverage_cup['애플민트스무디']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"애플민트스무디 {dic_beverage_cup['애플민트스무디']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"애플민트스무디 {dic_beverage_cup['애플민트스무디']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"애플민트스무디 {dic_beverage_cup['애플민트스무디']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"애플민트스무디 {dic_beverage_cup['애플민트스무디']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"애플민트스무디 {dic_beverage_cup['애플민트스무디']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"애플민트스무디 {dic_beverage_cup['애플민트스무디']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
    
    def go_to_제주누보(self,instance):
        global count,dic_etc_cup,dic_etc_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '제주누보' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_etc_sum['제주누보'] += (3000 * count)
            dic_etc_cup['제주누보'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"제주누보 {dic_etc_cup['제주누보']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"제주누보 {dic_etc_cup['제주누보']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"제주누보 {dic_etc_cup['제주누보']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"제주누보 {dic_etc_cup['제주누보']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"제주누보 {dic_etc_cup['제주누보']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"제주누보 {dic_etc_cup['제주누보']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"제주누보 {dic_etc_cup['제주누보']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_레몬사와(self,instance):
        global count,dic_etc_cup,dic_etc_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '레몬사와' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_etc_sum['레몬사와'] += (3000 * count)
            dic_etc_cup['레몬사와'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"레몬사와 {dic_etc_cup['레몬사와']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"레몬사와 {dic_etc_cup['레몬사와']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"레몬사와 {dic_etc_cup['레몬사와']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"레몬사와 {dic_etc_cup['레몬사와']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"레몬사와 {dic_etc_cup['레몬사와']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"레몬사와 {dic_etc_cup['레몬사와']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"레몬사와 {dic_etc_cup['레몬사와']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"

    def go_to_유자사와(self,instance):
        global count,dic_etc_cup,dic_etc_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '유자사와' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_etc_sum['유자사와'] += (3000 * count)
            dic_etc_cup['유자사와'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"유자사와 {dic_etc_cup['유자사와']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"유자사와 {dic_etc_cup['유자사와']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"유자사와 {dic_etc_cup['유자사와']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"유자사와 {dic_etc_cup['유자사와']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"유자사와 {dic_etc_cup['유자사와']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"유자사와 {dic_etc_cup['유자사와']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"유자사와 {dic_etc_cup['유자사와']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_아사히(self,instance):
        global count,dic_etc_cup,dic_etc_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '아사히' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_etc_sum['아사히'] += (3000 * count)
            dic_etc_cup['아사히'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"아사히 {dic_etc_cup['아사히']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"아사히 {dic_etc_cup['아사히']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"아사히 {dic_etc_cup['아사히']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"아사히 {dic_etc_cup['아사히']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"아사히 {dic_etc_cup['아사히']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"아사히 {dic_etc_cup['아사히']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"아사히 {dic_etc_cup['아사히']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
    
    def go_to_탄산수(self,instance):
        global count,dic_etc_cup,dic_etc_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '탄산수' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_etc_sum['탄산수'] += (500 * count)
            dic_etc_cup['탄산수'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"탄산수 {dic_etc_cup['탄산수']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"탄산수 {dic_etc_cup['탄산수']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"탄산수 {dic_etc_cup['탄산수']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"탄산수 {dic_etc_cup['탄산수']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"탄산수 {dic_etc_cup['탄산수']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"탄산수 {dic_etc_cup['탄산수']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"탄산수 {dic_etc_cup['탄산수']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_쌍화탕(self,instance):
        global count,dic_etc_cup,dic_etc_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '쌍화탕' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_etc_sum['쌍화탕'] += (1700 * count)
            dic_etc_cup['쌍화탕'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"쌍화탕 {dic_etc_cup['쌍화탕']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"쌍화탕 {dic_etc_cup['쌍화탕']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"쌍화탕 {dic_etc_cup['쌍화탕']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"쌍화탕 {dic_etc_cup['쌍화탕']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"쌍화탕 {dic_etc_cup['쌍화탕']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"쌍화탕 {dic_etc_cup['쌍화탕']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"쌍화탕 {dic_etc_cup['쌍화탕']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_포춘쿠키(self,instance):
        global count,dic_etc_cup,dic_etc_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '포춘쿠키' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_etc_sum['포춘쿠키'] += (1000 * count)
            dic_etc_cup['포춘쿠키'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"포춘쿠키 {dic_etc_cup['포춘쿠키']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"포춘쿠키 {dic_etc_cup['포춘쿠키']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"포춘쿠키 {dic_etc_cup['포춘쿠키']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"포춘쿠키 {dic_etc_cup['포춘쿠키']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"포춘쿠키 {dic_etc_cup['포춘쿠키']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"포춘쿠키 {dic_etc_cup['포춘쿠키']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"포춘쿠키 {dic_etc_cup['포춘쿠키']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_튀일쿠키(self,instance):
        global count,dic_etc_cup,dic_etc_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '튀일쿠키' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_etc_sum['튀일쿠키'] += (2000 * count)
            dic_etc_cup['튀일쿠키'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"튀일쿠키 {dic_etc_cup['튀일쿠키']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"튀일쿠키 {dic_etc_cup['튀일쿠키']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"튀일쿠키 {dic_etc_cup['튀일쿠키']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"튀일쿠키 {dic_etc_cup['튀일쿠키']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"튀일쿠키 {dic_etc_cup['튀일쿠키']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"튀일쿠키 {dic_etc_cup['튀일쿠키']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"튀일쿠키 {dic_etc_cup['튀일쿠키']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_브륄레(self,instance):
        global count,dic_etc_cup,dic_etc_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '브륄레' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_etc_sum['브륄레'] += (3000 * count)
            dic_etc_cup['브륄레'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"브륄레 {dic_etc_cup['브륄레']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"브륄레 {dic_etc_cup['브륄레']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"브륄레 {dic_etc_cup['브륄레']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"브륄레 {dic_etc_cup['브륄레']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"브륄레 {dic_etc_cup['브륄레']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"브륄레 {dic_etc_cup['브륄레']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"브륄레 {dic_etc_cup['브륄레']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"

    def go_to_캐모마일(self,instance):
        global count,dic_etc_cup,dic_etc_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '캐모마일' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_etc_sum['캐모마일'] += (2500 * count)
            dic_etc_cup['캐모마일'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"캐모마일 {dic_etc_cup['캐모마일']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"캐모마일 {dic_etc_cup['캐모마일']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"캐모마일 {dic_etc_cup['캐모마일']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"캐모마일 {dic_etc_cup['캐모마일']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"캐모마일 {dic_etc_cup['캐모마일']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"캐모마일 {dic_etc_cup['캐모마일']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"캐모마일 {dic_etc_cup['캐모마일']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_루이보스(self,instance):
        global count,dic_etc_cup,dic_etc_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '루이보스' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_etc_sum['루이보스'] += (2500 * count)
            dic_etc_cup['루이보스'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"루이보스 {dic_etc_cup['루이보스']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"루이보스 {dic_etc_cup['루이보스']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"루이보스 {dic_etc_cup['루이보스']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"루이보스 {dic_etc_cup['루이보스']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"루이보스 {dic_etc_cup['루이보스']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"루이보스 {dic_etc_cup['루이보스']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"루이보스 {dic_etc_cup['루이보스']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_보이차(self,instance):
        global count,dic_etc_cup,dic_etc_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '보이차' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_etc_sum['보이차'] += (2500 * count)
            dic_etc_cup['보이차'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"보이차 {dic_etc_cup['보이차']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"보이차 {dic_etc_cup['보이차']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"보이차 {dic_etc_cup['보이차']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"보이차 {dic_etc_cup['보이차']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"보이차 {dic_etc_cup['보이차']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"보이차 {dic_etc_cup['보이차']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"보이차 {dic_etc_cup['보이차']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
    
    def go_to_페퍼민트차(self,instance):
        global count,dic_etc_cup,dic_etc_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '페퍼민트' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_etc_sum['페퍼민트'] += (2500 * count)
            dic_etc_cup['페퍼민트'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"페퍼민트 {dic_etc_cup['페퍼민트']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"페퍼민트 {dic_etc_cup['페퍼민트']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"페퍼민트 {dic_etc_cup['페퍼민트']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"페퍼민트 {dic_etc_cup['페퍼민트']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"페퍼민트 {dic_etc_cup['페퍼민트']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"페퍼민트 {dic_etc_cup['페퍼민트']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"페퍼민트 {dic_etc_cup['페퍼민트']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_레몬그라스(self,instance):
        global count,dic_etc_cup,dic_etc_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '레몬그라스' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_etc_sum['레몬그라스'] += (2500 * count)
            dic_etc_cup['레몬그라스'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"레몬그라스 {dic_etc_cup['레몬그라스']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"레몬그라스 {dic_etc_cup['레몬그라스']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"레몬그라스 {dic_etc_cup['레몬그라스']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"레몬그라스 {dic_etc_cup['레몬그라스']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"레몬그라스 {dic_etc_cup['레몬그라스']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"레몬그라스 {dic_etc_cup['레몬그라스']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"레몬그라스 {dic_etc_cup['레몬그라스']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
    def go_to_라벤더(self,instance):
        global count,dic_etc_cup,dic_etc_sum
        pattern = r"(\S+)\s\d+"
        lst = re.findall(pattern,self.메뉴1_button.text) + re.findall(pattern,self.메뉴2_button.text) + re.findall(pattern,self.메뉴3_button.text) + re.findall(pattern,self.메뉴4_button.text) + re.findall(pattern,self.메뉴5_button.text) + re.findall(pattern,self.메뉴6_button.text) + re.findall(pattern,self.메뉴7_button.text)
        if '라벤더' in lst:
            self.popup.dismiss()
            self.알림창.text = "해당메뉴가 이미 장바구니에 있습니다!"
            Clock.schedule_once(self.clear_message, 4)
        else:
            dic_etc_sum['라벤더'] += (2500 * count)
            dic_etc_cup['라벤더'] += count
            if self.메뉴1_button.text == "":
                self.메뉴1_button.text = f"라벤더 {dic_etc_cup['라벤더']}"
            elif self.메뉴2_button.text == "":
                self.메뉴2_button.text = f"라벤더 {dic_etc_cup['라벤더']}"
            elif self.메뉴3_button.text == "":
                self.메뉴3_button.text = f"라벤더 {dic_etc_cup['라벤더']}"
            elif self.메뉴4_button.text == "":
                self.메뉴4_button.text = f"라벤더 {dic_etc_cup['라벤더']}"
            elif self.메뉴5_button.text == "":
                self.메뉴5_button.text = f"라벤더 {dic_etc_cup['라벤더']}"
            elif self.메뉴6_button.text == "":
                self.메뉴6_button.text = f"라벤더 {dic_etc_cup['라벤더']}"
            elif self.메뉴7_button.text == "":
                self.메뉴7_button.text = f"라벤더 {dic_etc_cup['라벤더']}"
            count = 1
            self.popup.dismiss()
            self.cup.text = "1"
        
        #self.메뉴1_button.bind(on_press =lambda instance, name="[장바구니]" + self.메뉴1_button.text.split(" ")[0]: self.메뉴1_open_popup(name,instance))
    
    def clear_message(self,instance):
        self.알림창.text = ""
    
    
    def go_to_주문(self,instance):
        global m1,m1_sum,m2,m2_sum,m3,m3_sum,m4,m4_sum,m5,m5_sum,m6,m6_sum,m7,m7_sum
        for _ in range(7):
            if _ == 0:
                if self.메뉴1_button.text == '':
                    pass
                elif self.메뉴1_button.text.split(" ")[0] in dic_coffee_sum.keys():
                    m1 = self.메뉴1_button.text.split(" ")[0]
                    m1_sum = dic_coffee_sum[m1]
                elif self.메뉴1_button.text.split(" ")[0] in dic_beverage_sum.keys():
                    m1 = self.메뉴1_button.text.split(" ")[0]
                    m1_sum = dic_beverage_sum[m1]
                elif self.메뉴1_button.text.split(" ")[0] in dic_etc_sum.keys():
                    m1 = self.메뉴1_button.text.split(" ")[0]
                    m1_sum = dic_etc_sum[m1]
                    
            elif _ == 1:
                if self.메뉴2_button.text == '':
                    pass
                elif self.메뉴2_button.text.split(" ")[0] in dic_coffee_sum.keys():
                    m2 = self.메뉴2_button.text.split(" ")[0]
                    m2_sum = dic_coffee_sum[m2]
                elif self.메뉴2_button.text.split(" ")[0] in dic_beverage_sum.keys():
                    m2 = self.메뉴2_button.text.split(" ")[0]
                    m2_sum = dic_beverage_sum[m2]
                elif self.메뉴2_button.text.split(" ")[0] in dic_etc_sum.keys():
                    m2 = self.메뉴2_button.text.split(" ")[0]
                    m2_sum = dic_etc_sum[m2]
                    
            elif _ == 2:
                if self.메뉴3_button.text == '':
                    pass
                elif self.메뉴3_button.text.split(" ")[0] in dic_coffee_sum.keys():
                    m3 = self.메뉴3_button.text.split(" ")[0]
                    m3_sum = dic_coffee_sum[m3]
                elif self.메뉴3_button.text.split(" ")[0] in dic_beverage_sum.keys():
                    m3 = self.메뉴3_button.text.split(" ")[0]
                    m3_sum = dic_beverage_sum[m3]
                elif self.메뉴3_button.text.split(" ")[0] in dic_etc_sum.keys():
                    m3 = self.메뉴3_button.text.split(" ")[0]
                    m3_sum = dic_etc_sum[m3]
                    
            elif _ == 3:
                if self.메뉴4_button.text == '':
                    pass
                elif self.메뉴4_button.text.split(" ")[0] in dic_coffee_sum.keys():
                    m4 = self.메뉴4_button.text.split(" ")[0]
                    m4_sum = dic_coffee_sum[m4]
                elif self.메뉴4_button.text.split(" ")[0] in dic_beverage_sum.keys():
                    m4 = self.메뉴4_button.text.split(" ")[0]
                    m4_sum = dic_beverage_sum[m4]
                elif self.메뉴4_button.text.split(" ")[0] in dic_etc_sum.keys():
                    m4 = self.메뉴4_button.text.split(" ")[0]
                    m4_sum = dic_etc_sum[m4]
                    
                    
            elif _ == 4:
                if self.메뉴5_button.text == '':
                    pass
                elif self.메뉴5_button.text.split(" ")[0] in dic_coffee_sum.keys():
                    m5 = self.메뉴5_button.text.split(" ")[0]
                    m5_sum = dic_coffee_sum[m5]
                elif self.메뉴5_button.text.split(" ")[0] in dic_beverage_sum.keys():
                    m5 = self.메뉴5_button.text.split(" ")[0]
                    m5_sum = dic_beverage_sum[m5]
                elif self.메뉴5_button.text.split(" ")[0] in dic_etc_sum.keys():
                    m5 = self.메뉴5_button.text.split(" ")[0]
                    m5_sum = dic_etc_sum[m5]
                    
            elif _ == 5:
                if self.메뉴6_button.text == '':
                    pass
                elif self.메뉴6_button.text.split(" ")[0] in dic_coffee_sum.keys():
                    m6 = self.메뉴6_button.text.split(" ")[0]
                    m6_sum = dic_coffee_sum[m6]
                elif self.메뉴6_button.text.split(" ")[0] in dic_beverage_sum.keys():
                    m6 = self.메뉴6_button.text.split(" ")[0]
                    m6_sum = dic_beverage_sum[m6]
                elif self.메뉴6_button.text.split(" ")[0] in dic_etc_sum.keys():
                    m6 = self.메뉴6_button.text.split(" ")[0]
                    m6_sum = dic_etc_sum[m6]
                    
            elif _ == 6:
                if self.메뉴7_button.text == '':
                    pass
                elif self.메뉴7_button.text.split(" ")[0] in dic_coffee_sum.keys():
                    m7 = self.메뉴7_button.text.split(" ")[0]
                    m7_sum = dic_coffee_sum[m7]
                elif self.메뉴7_button.text.split(" ")[0] in dic_beverage_sum.keys():
                    m7 = self.메뉴7_button.text.split(" ")[0]
                    m7_sum = dic_beverage_sum[m7]
                elif self.메뉴7_button.text.split(" ")[0] in dic_etc_sum.keys():
                    m7 = self.메뉴7_button.text.split(" ")[0]
                    m7_sum = dic_etc_sum[m7]

        self.manager.current = 'add_text'
        self.scroll_view.scroll_y = 1
        
        return self.scroll_view
        
                    
        
            
    
    def go_to_뒤로(self,instance):
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
        for m in dic_etc_sum.keys():
            dic_etc_sum[m] = 0
            dic_etc_cup[m] = 0
        self.manager.current = 'live_name_choose'
        self.scroll_view.scroll_y = 1
        
        return self.scroll_view
        
        

class AddTextScreen(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        root_layout = BoxLayout(orientation="vertical", padding=[0, 0, 0, 0], spacing=20)  # 위쪽 padding을 50으로 추가
        
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
        root_layout.add_widget(back_layout)


        self.scroll_view = ScrollView(size_hint=(1, 1))
        
        self.result_layout = GridLayout(
            cols=1,
            size_hint_y=None,  # 높이를 동적으로 설정
        )
        self.result_layout.bind(minimum_height=self.result_layout.setter("height"))
        
        self.scroll_view.add_widget(self.result_layout)
        
        root_layout.add_widget(self.scroll_view)
        
        next_layout = BoxLayout(
            size_hint=(1, 0.1),  # 가로 전체, 세로 10%
            orientation="horizontal",
            padding=(5, 0, 5, 0),
            spacing=3,
        )
        
        
        empty_space = Widget(size_hint=(1, 1))
        next_layout.add_widget(empty_space)

        
        다음_button = Button(
            text="다음",
            font_name="NanumGothic",
            size_hint=(None, 1),
            width=200,
        )
        다음_button.bind(on_press=self.go_to_다음)
        next_layout.add_widget(다음_button)
        root_layout.add_widget(next_layout)
        
        self.add_widget(root_layout)
        
    def on_enter(self):
        self.object = self.manager.get_screen('live_order')
        self.update_search_results()

    def update_search_results(self):
        
        self.result_layout.clear_widgets()
        c = []
        count = 0
        for i in [self.object.메뉴1_button.text,self.object.메뉴2_button.text,self.object.메뉴3_button.text,self.object.메뉴4_button.text,self.object.메뉴5_button.text,self.object.메뉴6_button.text,self.object.메뉴7_button.text]:
            if i == '':
                pass
            else:
                c.append(i)
        for item in c:
            count += 1
            button = Button(
                text=item,
                font_name="NanumGothic",
                font_size = (font_size-3),
                size_hint_y=None,
                height=200,
                text_size=(self.result_layout.width - 30, None),  # 텍스트 영역 너비를 버튼 너비로 설정 (여백 고려)
                halign="left",  # 텍스트 수평 왼쪽 정렬
                valign="top",
                padding=(25, 0)
            )
            button.bind(
            size=lambda instance, value: setattr(
                instance, "text_size", (instance.width - 30, None)
                )
            )  # 버튼 크기에 맞춰 텍스트 크기 조정
            if count == 1:
                button.bind(on_press =lambda instance, name=item: self.메뉴1_popup(name,instance))
                self.result_layout.add_widget(button)
            elif count == 2:
                button.bind(on_press =lambda instance, name=item: self.메뉴2_popup(name,instance))
                self.result_layout.add_widget(button)
            elif count == 3:
                button.bind(on_press =lambda instance, name=item: self.메뉴3_popup(name,instance))
                self.result_layout.add_widget(button)
            elif count == 4:
                button.bind(on_press =lambda instance, name=item: self.메뉴4_popup(name,instance))
                self.result_layout.add_widget(button)
            elif count == 5:
                button.bind(on_press =lambda instance, name=item: self.메뉴5_popup(name,instance))
                self.result_layout.add_widget(button)
            elif count == 6:
                button.bind(on_press =lambda instance, name=item: self.메뉴6_popup(name,instance))
                self.result_layout.add_widget(button)
            elif count == 7:
                button.bind(on_press =lambda instance, name=item: self.메뉴7_popup(name,instance))
                self.result_layout.add_widget(button)





    def 메뉴1_popup(self, menu_name, instance):
        content = FloatLayout()
        content.add_widget(Label(font_name="NanumGothic",font_size=sp(26), pos_hint={'center_x': 0.5, 'y': 0.45}, text=menu_name))
        
        self.textbox1 = TextInput(
            hint_text="공감지기에게 전달할 추가사항",
            font_name="NanumGothic",
            password=False,
            multiline=False,
            size_hint=(0.6, 0.2),
            font_size=(font_size),
            pos_hint={"center_x": 0.5, "center_y": 0.7}
        )
        
        content.add_widget(self.textbox1)
        

        content.add_widget(Button(text="확인", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'center_x': 0.5, 'y': 0}, on_press=lambda _ : self.메뉴1(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
        
    
    def 메뉴2_popup(self, menu_name, instance):
        content = FloatLayout()
        content.add_widget(Label(font_name="NanumGothic",font_size=sp(26), pos_hint={'center_x': 0.5, 'y': 0.45}, text=menu_name))
        
        self.textbox2 = TextInput(
            hint_text="공감지기에게 전달할 추가사항",
            font_name="NanumGothic",
            password=False,
            multiline=False,
            size_hint=(0.6, 0.2),
            font_size=(font_size),
            pos_hint={"center_x": 0.5, "center_y": 0.7}
        )
        
        content.add_widget(self.textbox2)
        

        content.add_widget(Button(text="확인", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'center_x': 0.5, 'y': 0}, on_press=lambda _ : self.메뉴2(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
    
    def 메뉴3_popup(self, menu_name, instance):
        content = FloatLayout()
        content.add_widget(Label(font_name="NanumGothic",font_size=sp(26), pos_hint={'center_x': 0.5, 'y': 0.45}, text=menu_name))
        
        self.textbox3 = TextInput(
            hint_text="공감지기에게 전달할 추가사항",
            font_name="NanumGothic",
            password=False,
            multiline=False,
            size_hint=(0.6, 0.2),
            font_size=(font_size),
            pos_hint={"center_x": 0.5, "center_y": 0.7}
        )
        
        content.add_widget(self.textbox3)
        

        content.add_widget(Button(text="확인", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'center_x': 0.5, 'y': 0}, on_press=lambda _ : self.메뉴3(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
    
    def 메뉴4_popup(self, menu_name, instance):
        content = FloatLayout()
        content.add_widget(Label(font_name="NanumGothic",font_size=sp(26), pos_hint={'center_x': 0.5, 'y': 0.45}, text=menu_name))
        
        self.textbox4 = TextInput(
            hint_text="공감지기에게 전달할 추가사항",
            font_name="NanumGothic",
            password=False,
            multiline=False,
            size_hint=(0.6, 0.2),
            font_size=(font_size),
            pos_hint={"center_x": 0.5, "center_y": 0.7}
        )
        
        content.add_widget(self.textbox4)
        

        content.add_widget(Button(text="확인", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'center_x': 0.5, 'y': 0}, on_press=lambda _ : self.메뉴4(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
    
    def 메뉴5_popup(self, menu_name, instance):
        content = FloatLayout()
        content.add_widget(Label(font_name="NanumGothic",font_size=sp(26), pos_hint={'center_x': 0.5, 'y': 0.45}, text=menu_name))
        
        self.textbox5 = TextInput(
            hint_text="공감지기에게 전달할 추가사항",
            font_name="NanumGothic",
            password=False,
            multiline=False,
            size_hint=(0.6, 0.2),
            font_size=(font_size),
            pos_hint={"center_x": 0.5, "center_y": 0.7}
        )
        
        content.add_widget(self.textbox5)
        

        content.add_widget(Button(text="확인", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'center_x': 0.5, 'y': 0}, on_press=lambda _ : self.메뉴5(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
    
    def 메뉴6_popup(self, menu_name, instance):
        content = FloatLayout()
        content.add_widget(Label(font_name="NanumGothic",font_size=sp(26), pos_hint={'center_x': 0.5, 'y': 0.45}, text=menu_name))
        
        self.textbox6 = TextInput(
            hint_text="공감지기에게 전달할 추가사항",
            font_name="NanumGothic",
            password=False,
            multiline=False,
            size_hint=(0.6, 0.2),
            font_size=(font_size),
            pos_hint={"center_x": 0.5, "center_y": 0.7}
        )
        
        content.add_widget(self.textbox6)
        

        content.add_widget(Button(text="확인", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'center_x': 0.5, 'y': 0}, on_press=lambda _ : self.메뉴6(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()
    
    def 메뉴7_popup(self, menu_name, instance):
        content = FloatLayout()
        content.add_widget(Label(font_name="NanumGothic",font_size=sp(26), pos_hint={'center_x': 0.5, 'y': 0.45}, text=menu_name))
        
        self.textbox7 = TextInput(
            hint_text="공감지기에게 전달할 추가사항",
            font_name="NanumGothic",
            password=False,
            multiline=False,
            size_hint=(0.6, 0.2),
            font_size=(font_size),
            pos_hint={"center_x": 0.5, "center_y": 0.7}
        )
        
        content.add_widget(self.textbox7)
        

        content.add_widget(Button(text="확인", font_name="NanumGothic",size_hint=(0.2, 0.2), pos_hint={'center_x': 0.5, 'y': 0}, on_press=lambda _ : self.메뉴7(instance)))
        self.popup = Popup(title="",
                           content=content,
                           size_hint=(0.7,None),
                           height = dp(400),
                           auto_dismiss=False)
        self.popup.open()


    def 메뉴1(self,instance):
        self.popup.dismiss()
        
        
    def 메뉴2(self,instance):
        self.popup.dismiss()
        
        
    def 메뉴3(self,instance):
        self.popup.dismiss()
        
        
    def 메뉴4(self,instance):
        self.popup.dismiss()
        
        
    def 메뉴5(self,instance):
        self.popup.dismiss()
        
        
    def 메뉴6(self,instance):
        self.popup.dismiss()
        
        
    def 메뉴7(self,instance):
        self.popup.dismiss()
            
        
    def go_to_뒤로(self,instance):
        self.manager.current = "live_order"
        
    def go_to_다음(self,instance):
        self.manager.current = "live_cash"
        
        
        
        
        
        


class CashScreen(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.layout = FloatLayout()
        self.label_1 = Label(text="Loading data...",
                             font_name="NanumGothic",
                             font_size="22sp",
                             pos_hint = {'center_x' : 0.5, 'center_y' : 0.85}
                             )
        
        self.label_2 = Label(
            text="Loading data...",
            font_name="NanumGothic",
            font_size="22sp",
            halign="center",
            valign="middle",
            pos_hint={'center_x': 0.5, 'center_y': 0.75},
            size_hint=(0.8, None), 
            height=300,  
            text_size=(0.8 * Window.width, None)  
        )
        self.label_2.bind(size=self.label_2.setter('text_size'))

        self.label_3 = Label(text="Loading data...",
                             font_name="NanumGothic",
                             font_size="22sp",
                             pos_hint = {'center_x' : 0.5, 'center_y' : 0.65}
                             )
        
        self.label_4 = Label(text="Loading data...",
                             font_name="NanumGothic",
                             font_size="22sp",
                             markup = True,
                             pos_hint = {'center_x' : 0.5, 'center_y' : 0.55}
                             )
        
        self.label_45 = Label(text="Loading data...",
                             font_name="NanumGothic",
                             font_size="22sp",
                             markup = True,
                             pos_hint = {'center_x' : 0.5, 'center_y' : 0.47}
                             )
        
        self.label_5 = Label(text="Loading data...",
                             font_name="NanumGothic",
                             font_size="22sp",
                             markup = True,
                             pos_hint = {'center_x' : 0.5, 'center_y' : 0.38}
                             )
        
        self.label_55 = Label(text="Loading data...",
                             font_name="NanumGothic",
                             font_size="22sp",
                             markup = True,
                             pos_hint = {'center_x' : 0.5, 'center_y' : 0.3}
                             )
        

        self.label_7 = Label(text="Loading data...",
                             font_name="NanumGothic",
                             font_size="22sp",
                             color=(1, 0, 0, 1),
                             pos_hint = {'center_x' : 0.5, 'center_y' : 0.22}
                             )
        self.layout.add_widget(self.label_1)
        self.layout.add_widget(self.label_2)
        self.layout.add_widget(self.label_3)
        self.layout.add_widget(self.label_4)
        self.layout.add_widget(self.label_45)
        self.layout.add_widget(self.label_5)
        self.layout.add_widget(self.label_55)
        self.layout.add_widget(self.label_7)
        
        ok_button = Button(
            text = "완료",
            font_name="NanumGothic",
            size_hint = (0.35,0.1),
            pos_hint = {'center_x' : 0.5, 'center_y' : 0.1}
            
        )
        ok_button.bind(on_press=self.go_ok)
        self.layout.add_widget(ok_button)
        
        back_layout = BoxLayout(
            size_hint=(1, 0.1),  # 가로 전체, 세로 10%
            pos_hint={"left": 0.5, "top": 1},  # 화면 상단
            orientation="horizontal",
            padding=(5, 0, 5, 0),
            spacing=3,
        )
        
        back_button = Button(
            text="뒤로",
            font_name="NanumGothic",
            size_hint=(None, 1),
            width=200,
        )
        back_button.bind(on_press=self.go_back)
        back_layout.add_widget(back_button)
        self.layout.add_widget(back_layout)
        self.add_widget(self.layout)
        


    def on_enter(self):
        global check
        self.data = fetch_data(주문_이름)
        self.label_1.text = f"주문자 : {주문_이름}"
        self.label_5.text = f"[남은 선물금액]"
        self.label_55.text = f"{self.data:,}원"
        self.pay = fetch_pay_data()
        self.label_4.text = f"[남은 페이금액]"
        self.label_45.text = f"{self.pay:,}원"
        object = self.manager.get_screen('order')
        self.text = ''
        for i in [object.메뉴1_button.text,object.메뉴2_button.text,object.메뉴3_button.text,object.메뉴4_button.text,object.메뉴5_button.text,object.메뉴6_button.text,object.메뉴7_button.text]:
            if i == '':
                pass
            else:
                self.text = self.text + i + ", "
        self.text = self.text[:-2]
        self.label_2.text = f"고른 메뉴 : {self.text}"
        jumun_sum = m1_sum + m2_sum + m3_sum + m4_sum + m5_sum + m6_sum + m7_sum
        self.label_3.text = f"주문 금액 : {jumun_sum:,}원"
        self.total = 0
        if self.pay >= jumun_sum : 
            check = 1 ######
            self.label_45.text = f"{self.pay:,}원 - [color=ff0000]{jumun_sum:,}원[/color] = [color=0000ff]{self.pay-jumun_sum:,}원[/color]"
            self.label_7.text = f"청구될될 금액 : {self.total:,}원"
            self.pay = self.pay - jumun_sum
            #pay_to_db(pay)
        
        elif self.pay > 0:
            self.label_45.text = f"{self.pay:,}원 - [color=ff0000]{self.pay:,}원[/color] = [color=0000ff]{self.pay-self.pay:,}원[/color]"
            self.total = jumun_sum - self.pay
            if self.data >= self.total:
                check = 2 ######
                #pay_to_db(0)
                self.label_55.text = f"{self.data:,}원 - [color=ff0000]{self.total:,}원[/color] = [color=0000ff]{self.data-self.total:,}원[/color]"
                self.data = self.data - self.total
                self.total = 0
                self.label_7.text = f"청구될 금액 : {self.total:,}원"
                #gift_to_db(data,주문_이름)
            elif self.data > 0:
                check = 3 ######
                #pay_to_db(0)
                self.label_55.text = f"{self.data:,}원 - [color=ff0000]{self.data:,}원[/color] = [color=0000ff]{self.data-self.data:,}원[/color]"
                self.total = self.total - self.data
                #gift_to_db(0,주문_이름)
                self.label_7.text = f"청구될 금액 : {self.total:,}원"
                #most_to_db(total,주문_이름)
            else :
                check = 4 ######
                #pay_to_db(0)
                self.label_7.text = f"청구될 금액 : {self.total:,}원"
                #most_to_db(total,주문_이름)
                
        
        else :
            if self.data >= jumun_sum:
                check = 5 ######
                self.total = jumun_sum
                self.label_55.text = f"{self.data:,}원 - [color=ff0000]{self.total:,}원[/color] = [color=0000ff]{self.data-self.total:,}원[/color]"
                self.total = 0
                self.label_7.text = f"청구될 금액 : {self.total:,}원"
                self.data = self.data - jumun_sum
                #gift_to_db(data,주문_이름)
                self.total = 0
            elif self.data > 0:
                check = 6 ######
                self.total = jumun_sum - self.data
                self.label_55.text = f"{self.data:,}원 - [color=ff0000]{self.data:,}원[/color] = [color=0000ff]{self.data-self.data:,}원[/color]"
                #gift_to_db(0,주문_이름)
                self.label_7.text = f"청구될 금액 : {self.total:,}원"
                #most_to_db(total,주문_이름)
            else :
                check = 7 ######
                self.total = jumun_sum
                self.label_7.text = f"청구될 금액 : {self.total:,}원"
                #most_to_db(total,주문_이름)
                
            
                
    def go_ok(self, instance):
        global check,m1,m1_sum,m2,m2_sum,m3,m3_sum,m4,m4_sum,m5,m5_sum,m6,m6_sum,m7,m7_sum
        object = self.manager.get_screen('order')
        if check == 1:
            pay_to_db(self.pay)
        elif check == 2:
            pay_to_db(0)
            gift_to_db(self.data, 주문_이름)
        elif check == 3:
            pay_to_db(0)
            gift_to_db(0,주문_이름)
            most_to_db(주문_이름,self.total)
        elif check == 4:
            pay_to_db(0)
            most_to_db(주문_이름,self.total)
        elif check == 5:
            gift_to_db(self.data,주문_이름)
        elif check == 6:
            gift_to_db(0,주문_이름)
            most_to_db(주문_이름,self.total)
        elif check == 7:
            most_to_db(주문_이름,self.total)
        
        check = 0
        
        jumoon_log_to_db(주문_이름+" - "+self.text)

        m1 = ''
        m1_sum = 0
        m2 = ''
        m2_sum = 0
        m3 = ''
        m3_sum = 0
        m4 = ''
        m4_sum = 0
        m5 = ''
        m5_sum = 0
        m6 = ''
        m6_sum = 0
        m7 = ''
        m7_sum = 0
        object.메뉴1_button.text = ''
        object.메뉴2_button.text = ''
        object.메뉴3_button.text = ''
        object.메뉴4_button.text = ''
        object.메뉴5_button.text = ''
        object.메뉴6_button.text = ''
        object.메뉴7_button.text = ''
        for i in dic_coffee_sum.keys():
            dic_coffee_sum[i] = 0
            dic_coffee_cup[i] = 0
            
        for k in dic_beverage_sum.keys():
            dic_beverage_sum[k] = 0
            dic_beverage_cup[k] = 0
        
        for m in dic_etc_sum.keys():
            dic_etc_sum[m] = 0
            dic_etc_cup[m] = 0
        self.manager.current = 'name_choose'
            
            
            
            
        
                
        
        
                
        
        
    def go_back(self, instance):
        global m1,m1_sum,m2,m2_sum,m3,m3_sum,m4,m4_sum,m5,m5_sum,m6,m6_sum,m7,m7_sum
        m1 = ''
        m1_sum = 0
        m2 = ''
        m2_sum = 0
        m3 = ''
        m3_sum = 0
        m4 = ''
        m4_sum = 0
        m5 = ''
        m5_sum = 0
        m6 = ''
        m6_sum = 0
        m7 = ''
        m7_sum = 0
        
        self.manager.current = "order"
        
        
        










class live_CashScreen(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.layout = FloatLayout()
        self.label_1 = Label(text="Loading data...",
                             font_name="NanumGothic",
                             font_size="22sp",
                             pos_hint = {'center_x' : 0.5, 'center_y' : 0.85}
                             )
        
        self.label_2 = Label(
            text="Loading data...",
            font_name="NanumGothic",
            font_size="22sp",
            halign="center",
            valign="middle",
            pos_hint={'center_x': 0.5, 'center_y': 0.75},
            size_hint=(0.8, None), 
            height=300,  
            text_size=(0.8 * Window.width, None)  
        )
        self.label_2.bind(size=self.label_2.setter('text_size'))

        self.label_3 = Label(text="Loading data...",
                             font_name="NanumGothic",
                             font_size="22sp",
                             pos_hint = {'center_x' : 0.5, 'center_y' : 0.65}
                             )
        
        self.label_4 = Label(text="Loading data...",
                             font_name="NanumGothic",
                             font_size="22sp",
                             markup = True,
                             pos_hint = {'center_x' : 0.5, 'center_y' : 0.55}
                             )
        
        self.label_45 = Label(text="Loading data...",
                             font_name="NanumGothic",
                             font_size="22sp",
                             markup = True,
                             pos_hint = {'center_x' : 0.5, 'center_y' : 0.47}
                             )
        
        self.label_5 = Label(text="Loading data...",
                             font_name="NanumGothic",
                             font_size="22sp",
                             markup = True,
                             pos_hint = {'center_x' : 0.5, 'center_y' : 0.38}
                             )
        
        self.label_55 = Label(text="Loading data...",
                             font_name="NanumGothic",
                             font_size="22sp",
                             markup = True,
                             pos_hint = {'center_x' : 0.5, 'center_y' : 0.3}
                             )
        

        self.label_7 = Label(text="Loading data...",
                             font_name="NanumGothic",
                             font_size="22sp",
                             color=(1, 0, 0, 1),
                             pos_hint = {'center_x' : 0.5, 'center_y' : 0.22}
                             )
        self.layout.add_widget(self.label_1)
        self.layout.add_widget(self.label_2)
        self.layout.add_widget(self.label_3)
        self.layout.add_widget(self.label_4)
        self.layout.add_widget(self.label_45)
        self.layout.add_widget(self.label_5)
        self.layout.add_widget(self.label_55)
        self.layout.add_widget(self.label_7)
        
        ok_button = Button(
            text = "완료",
            font_name="NanumGothic",
            size_hint = (0.35,0.1),
            pos_hint = {'center_x' : 0.5, 'center_y' : 0.1}
            
        )
        ok_button.bind(on_press=self.go_ok)
        self.layout.add_widget(ok_button)
        
        back_layout = BoxLayout(
            size_hint=(1, 0.1),  # 가로 전체, 세로 10%
            pos_hint={"left": 0.5, "top": 1},  # 화면 상단
            orientation="horizontal",
            padding=(5, 0, 5, 0),
            spacing=3,
        )
        
        back_button = Button(
            text="뒤로",
            font_name="NanumGothic",
            size_hint=(None, 1),
            width=200,
        )
        back_button.bind(on_press=self.go_back)
        back_layout.add_widget(back_button)
        self.layout.add_widget(back_layout)
        self.add_widget(self.layout)
        


    def on_enter(self):
        global check
        self.data = fetch_data(주문_이름)
        self.label_1.text = f"주문자 : {주문_이름}"
        self.label_5.text = f"[남은 선물금액]"
        self.label_55.text = f"{self.data:,}원"
        self.pay = fetch_pay_data()
        self.label_4.text = f"[남은 페이금액]"
        self.label_45.text = f"{self.pay:,}원"
        object = self.manager.get_screen('live_order')
        self.text = ''
        for i in [object.메뉴1_button.text,object.메뉴2_button.text,object.메뉴3_button.text,object.메뉴4_button.text,object.메뉴5_button.text,object.메뉴6_button.text,object.메뉴7_button.text]:
            if i == '':
                pass
            else:
                self.text = self.text + i + ", "
        self.text = self.text[:-2]
        self.label_2.text = f"고른 메뉴 : {self.text}"
        jumun_sum = m1_sum + m2_sum + m3_sum + m4_sum + m5_sum + m6_sum + m7_sum
        self.label_3.text = f"주문 금액 : {jumun_sum:,}원"
        self.total = 0
        if self.pay >= jumun_sum : 
            check = 1 ######
            self.label_45.text = f"{self.pay:,}원 - [color=ff0000]{jumun_sum:,}원[/color] = [color=0000ff]{self.pay-jumun_sum:,}원[/color]"
            self.label_7.text = f"청구될될 금액 : {self.total:,}원"
            self.pay = self.pay - jumun_sum
            #pay_to_db(pay)
        
        elif self.pay > 0:
            self.label_45.text = f"{self.pay:,}원 - [color=ff0000]{self.pay:,}원[/color] = [color=0000ff]{self.pay-self.pay:,}원[/color]"
            self.total = jumun_sum - self.pay
            if self.data >= self.total:
                check = 2 ######
                #pay_to_db(0)
                self.label_55.text = f"{self.data:,}원 - [color=ff0000]{self.total:,}원[/color] = [color=0000ff]{self.data-self.total:,}원[/color]"
                self.data = self.data - self.total
                self.total = 0
                self.label_7.text = f"청구될 금액 : {self.total:,}원"
                #gift_to_db(data,주문_이름)
            elif self.data > 0:
                check = 3 ######
                #pay_to_db(0)
                self.label_55.text = f"{self.data:,}원 - [color=ff0000]{self.data:,}원[/color] = [color=0000ff]{self.data-self.data:,}원[/color]"
                self.total = self.total - self.data
                #gift_to_db(0,주문_이름)
                self.label_7.text = f"청구될 금액 : {self.total:,}원"
                #most_to_db(total,주문_이름)
            else :
                check = 4 ######
                #pay_to_db(0)
                self.label_7.text = f"청구될 금액 : {self.total:,}원"
                #most_to_db(total,주문_이름)
                
        
        else :
            if self.data >= jumun_sum:
                check = 5 ######
                self.total = jumun_sum
                self.label_55.text = f"{self.data:,}원 - [color=ff0000]{self.total:,}원[/color] = [color=0000ff]{self.data-self.total:,}원[/color]"
                self.total = 0
                self.label_7.text = f"청구될 금액 : {self.total:,}원"
                self.data = self.data - jumun_sum
                #gift_to_db(data,주문_이름)
                self.total = 0
            elif self.data > 0:
                check = 6 ######
                self.total = jumun_sum - self.data
                self.label_55.text = f"{self.data:,}원 - [color=ff0000]{self.data:,}원[/color] = [color=0000ff]{self.data-self.data:,}원[/color]"
                #gift_to_db(0,주문_이름)
                self.label_7.text = f"청구될 금액 : {self.total:,}원"
                #most_to_db(total,주문_이름)
            else :
                check = 7 ######
                self.total = jumun_sum
                self.label_7.text = f"청구될 금액 : {self.total:,}원"
                #most_to_db(total,주문_이름)
                
            
                
    def go_ok(self, instance):
        global check,m1,m1_sum,m2,m2_sum,m3,m3_sum,m4,m4_sum,m5,m5_sum,m6,m6_sum,m7,m7_sum
        object = self.manager.get_screen('live_order')
        if check == 1:
            pay_to_db(self.pay)
        elif check == 2:
            pay_to_db(0)
            gift_to_db(self.data, 주문_이름)
        elif check == 3:
            pay_to_db(0)
            gift_to_db(0,주문_이름)
            most_to_db(주문_이름,self.total)
        elif check == 4:
            pay_to_db(0)
            most_to_db(주문_이름,self.total)
        elif check == 5:
            gift_to_db(self.data,주문_이름)
        elif check == 6:
            gift_to_db(0,주문_이름)
            most_to_db(주문_이름,self.total)
        elif check == 7:
            most_to_db(주문_이름,self.total)
        
        check = 0
        
        jumoon_log_to_db(주문_이름+" - "+self.text)

        m1 = ''
        m1_sum = 0
        m2 = ''
        m2_sum = 0
        m3 = ''
        m3_sum = 0
        m4 = ''
        m4_sum = 0
        m5 = ''
        m5_sum = 0
        m6 = ''
        m6_sum = 0
        m7 = ''
        m7_sum = 0
        object.메뉴1_button.text = ''
        object.메뉴2_button.text = ''
        object.메뉴3_button.text = ''
        object.메뉴4_button.text = ''
        object.메뉴5_button.text = ''
        object.메뉴6_button.text = ''
        object.메뉴7_button.text = ''
        for i in dic_coffee_sum.keys():
            dic_coffee_sum[i] = 0
            dic_coffee_cup[i] = 0
            
        for k in dic_beverage_sum.keys():
            dic_beverage_sum[k] = 0
            dic_beverage_cup[k] = 0
        
        for m in dic_etc_sum.keys():
            dic_etc_sum[m] = 0
            dic_etc_cup[m] = 0
        self.manager.current = 'live_name_choose'
            
            
            
            
        
                
        
        
                
        
        
    def go_back(self, instance):
        global m1,m1_sum,m2,m2_sum,m3,m3_sum,m4,m4_sum,m5,m5_sum,m6,m6_sum,m7,m7_sum
        m1 = ''
        m1_sum = 0
        m2 = ''
        m2_sum = 0
        m3 = ''
        m3_sum = 0
        m4 = ''
        m4_sum = 0
        m5 = ''
        m5_sum = 0
        m6 = ''
        m6_sum = 0
        m7 = ''
        m7_sum = 0
        
        self.manager.current = "add_text"
        
        
        
        
        
        
        
        
        
        

class LogScreen(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        root_layout = BoxLayout(orientation="vertical", padding=[0, 0, 0, 20], spacing=20)  # 위쪽 padding을 50으로 추가
        
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
        root_layout.add_widget(back_layout)
        
        self.scroll_view = ScrollView(size_hint=(1, 1))
        
        self.result_layout = GridLayout(
            cols=1,
            size_hint_y=None,  # 높이를 동적으로 설정
        )
        self.result_layout.bind(minimum_height=self.result_layout.setter("height"))
        
        self.scroll_view.add_widget(self.result_layout)
        
        root_layout.add_widget(self.scroll_view)
        
        self.add_widget(root_layout)
        
    def on_enter(self):
        self.update_search_results()

    def update_search_results(self):
        
        self.result_layout.clear_widgets()
        list = fetch_log_data()
        for item in list[::-1]:
            button = Button(
                text=item,
                font_name="NanumGothic",
                font_size = (font_size-3),
                size_hint_y=None,
                height=200,
                text_size=(self.result_layout.width - 30, None),  # 텍스트 영역 너비를 버튼 너비로 설정 (여백 고려)
                halign="left",  # 텍스트 수평 왼쪽 정렬
                valign="top",
                padding=(25, 0)
            )
            button.bind(
            size=lambda instance, value: setattr(
                instance, "text_size", (instance.width - 30, None)
                )
            )  # 버튼 크기에 맞춰 텍스트 크기 조정
            button.bind(on_press=self.on_item_select)
            self.result_layout.add_widget(button)






    def on_item_select(self, instance):
        pass


            
        
    def go_to_뒤로(self,instance):
        self.manager.current = "home"





    




class MyApp(App):
    def build(self):
        sm = ScreenManager()
        
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(Jumoon_choose(name='jumoon'))
        sm.add_widget(NamechooseScreen(name='name_choose'))
        sm.add_widget(OrderScreen(name='order'))
        sm.add_widget(LogScreen(name='log'))
        sm.add_widget(CashScreen(name='cash'))
        sm.add_widget(live_CashScreen(name='live_cash'))
        sm.add_widget(Live_OrderScreen(name='live_order'))
        sm.add_widget(AddTextScreen(name='add_text'))
        sm.add_widget(Live_NamechooseScreen(name='live_name_choose'))
        return sm
    
if __name__ == '__main__':
    app = MyApp()
    app.run()