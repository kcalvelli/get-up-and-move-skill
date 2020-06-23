from mycroft import MycroftSkill, intent_file_handler


class GetUpAndMove(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('move.and.up.get.intent')
    def handle_move_and_up_get(self, message):
        self.speak_dialog('move.and.up.get')


def create_skill():
    return GetUpAndMove()

