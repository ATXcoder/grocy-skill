from mycroft import MycroftSkill, intent_file_handler
from pygrocy import Grocy
from pygrocy.data_models.generic import EntityType

class GrocySkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.grocy_api_key = self.settings.get('grocy_api_key')
        self.grocy_url = self.settings.get('grocy_url')
        self.grocy_port = self.settings.get('grocy_port')
        self.grocy = Grocy(self.grocy_url, self.grocy_api_key, port=self.grocy_port)


    @intent_file_handler('grocy.intent')
    def handle_grocy(self, message):
        self.speak_dialog('grocy')

    @intent_file_handler('add.item.intent')
    def add_item(self, message):
        product_name = message.data.get('product')
        items = self.grocy.all_products()
        for item in items:
            if item.name == product_name:
                self.grocy.add_product_to_shopping_list(item.id)
                self.speak_dialog('add.item', {'product': item.name})


def create_skill():
    return GrocySkill()

