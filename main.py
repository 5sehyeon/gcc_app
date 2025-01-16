from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import requests
import socketio
import kivy
from kivy.clock import Clock,mainthread
from datetime import datetime
import os
kivy.require('2.1.0')

# 폰트 파일 경로 설정
FONT_NAME = "C:/Users/djdjd/OneDrive/바탕 화면/Python/NanumGothic.ttf"


# 로그인 화면 클래스
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # 아이디 입력 필드
        self.username_input = TextInput(
            hint_text="아이디를 입력하세요",
            font_name=FONT_NAME,
            multiline=False,
            size_hint=(1, 0.2)
        )
        layout.add_widget(self.username_input)

        # 비밀번호 입력 필드
        self.password_input = TextInput(
            hint_text="비밀번호를 입력하세요",
            font_name=FONT_NAME,
            password=True,
            multiline=False,
            size_hint=(1, 0.2)
        )
        layout.add_widget(self.password_input)

        # 로그인 버튼
        login_button = Button(
            text="로그인",
            font_name=FONT_NAME,
            size_hint=(1, 0.2)
        )
        login_button.bind(on_press=self.verify_login)
        layout.add_widget(login_button)

        # 상태 메시지 출력용 레이블
        self.message_label = Label(
            text="",
            font_name=FONT_NAME,
            size_hint=(1, 0.2),
            color=(1, 0, 0, 1)  # 빨간색 텍스트
        )
        layout.add_widget(self.message_label)

        self.add_widget(layout)

    def verify_login(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        
        url = "http://15.165.161.106:5000/button_click"
        data = {
            "username": username,
            "password": password
        }
        response = requests.post(url, json=data)
        print(response.json())
        
        # 간단한 검증 (예제용)
        if username == "admin" and password == "1234":
            self.message_label.text = "로그인 성공!"
            self.manager.current = "home"  # 홈 화면으로 이동
        else:
            self.message_label.text = "아이디 또는 비밀번호가 틀렸습니다."


# 홈 화면 클래스
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        welcome_label = Label(
            text="환영합니다! 홈 화면입니다.",
            font_name=FONT_NAME,
            font_size=24
        )
        layout.add_widget(welcome_label)
        self.add_widget(layout)
        
        
# 알람 창을 띄우는 클래스
class AlarmScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = Label(text="알람 대기 중...", font_size=30)
        self.button = Button(text="닫기", on_press=self.stop_app, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        
        # SocketIO 클라이언트 연결
        self.sio = socketio.Client()
        self.sio.connect('http://15.165.161.106:5000')  # Flask 서버 주소에 연결
        self.sio.on('alarm', self.on_alarm)  # 'alarm' 이벤트 수신
        self.add_widget(self.label)
        self.add_widget(self.button)
        self.alarm_time = None
        
    @mainthread
    def on_alarm(self, data):
        """알람을 받으면 창을 띄운다."""
        self.alarm_time = data.get('time')  # 수신된 알람 시간
        self.show_alarm_window()
        
    def show_alarm_window(self):
        """알람 창을 띄운다."""
        self.manager.current = "alarm_end"

    def stop_app(self, instance):
        """앱을 종료한다."""
        self.stop()
        
        
class alarmscreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # 알람이 울렸을 때 표시될 메시지와 닫기 버튼
        self.label = Label(text="알람이 울렸습니다!", font_size=30)
        self.button = Button(
            text="알약 내보내기", 
            size_hint=(0.5, 0.5), 
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            font_name="NanumGothic.ttf"
        )
        self.button.bind(on_press=self.go_to_home)
        
        # 위젯 추가
        self.add_widget(self.label)
        self.add_widget(self.button)

        
    def go_to_home(self, instance):
        alarm_screen = self.manager.get_screen('alarm')
        alarm_time = alarm_screen.alarm_time # 알람 시간!
        print(alarm_time)
        
        url = "http://15.165.161.106:5000/data_process" # 어떤 함수로 보낼지, url 마지막에 명시 해둬야 한다.
        data = {"alarm_time" : alarm_time}
        response = requests.post(url, json=data)
        print(response.json())
        self.manager.current = "home"


# 메인 앱 클래스
class MyApp(App):
    def build(self):
        sm = ScreenManager()

        # 로그인 화면, 홈 화면, 알람 화면 추가
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(AlarmScreen(name='alarm'))
        sm.add_widget(alarmscreen(name="alarm_end"))
        return sm

if __name__ == '__main__':
    app = MyApp()
    app.run() # 앱을 계속 켜두고, 사용자의 요청에 대기 상태를 만들어 놓음