class WiFiDevice:

    def wifi(self):
        print("WiFi Connected")


class VoiceAssistant:

    def voice(self):
        print("Voice Control Activated")


class SmartSpeaker(WiFiDevice, VoiceAssistant):

    def display(self):
        print("Smart Speaker is Ready")


s1 = SmartSpeaker()

s1.wifi()
s1.voice()
s1.display()
