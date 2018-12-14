from mycroft import MycroftSkill, intent_file_handler


class MyPcStatus(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('status.pc.my.intent')
    def handle_status_pc_my(self, message):
        available_mem_mb = ''
        bb_time = ''
        free_disk = ''
        free_mem_mb = ''
        total_disk = ''
        total_mem_mb = ''
        used_disk = ''

        self.speak_dialog('status.pc.my', data={
            'free_disk': free_disk,
            'total_mem_mb': total_mem_mb,
            'bb_time': bb_time,
            'available_mem_mb': available_mem_mb,
            'free_mem_mb': free_mem_mb,
            'total_disk': total_disk,
            'used_disk': used_disk
        })


def create_skill():
    return MyPcStatus()

