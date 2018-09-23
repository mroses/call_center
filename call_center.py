from datetime import datetime

class Call(object):
    def __init__(self, call_id, name, caller_number, call_reason):
        self.call_id = call_id
        self.name = name
        self.caller_number = caller_number
        self.call_time = datetime.now()
        self.call_reason = call_reason

    def disp(self):
        print "Call id: {}".format(self.call_id)
        print "Caller Name: {}".format(self.name)
        print "Caller Number: {}".format(self.caller_number)
        print "Call Time: {}".format(self.call_time)
        print "Call Reason: {}".format(self.call_reason)
        return self
    
class CallCenter(Call):
    def __init__(self):
        self.calls = []
        self.queue_size = len(self.calls)

    def add_call(self, call):
        self.calls.append(call)
        self.queue_size = len(self.calls)
        return self

    def remove_call(self, call):
        self.calls.pop(0)
        self.queue_size = len(self.calls)
        return self

    def call_info(self):
        for call in self.calls:
            print "Caller Name: {}, Caller Phone: {}".format(call.name, call.caller_number)

        print self.queue_size
        return self

call1 = Call(1, "Dave", "2062221111", "order pizza")
call2 = Call(2, "Ray", "2061081081", "Help me!")

callcenter1 = CallCenter().add_call(call1).call_info()
