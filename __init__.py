from mycroft import MycroftSkill, intent_file_handler


class Grocy(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('grocy.intent')
    def handle_grocy(self, message):
        self.speak_dialog('grocy')


def create_skill():
    return Grocy()

