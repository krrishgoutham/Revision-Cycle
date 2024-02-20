import Reminder_System

class Learning_Session:
    def __init__(self, name, start_date):
        self.name = name
        self.no_of_revisions = 0
        self.intervals = []
        self.confidence_scores = []
        self.factor_value = 2.5
        self.session_start_date = start_date
    
    def get_user_confidence_score(self, confi_score):
        self.confidence_scores.append(confi_score)
    
    def next_interval(self):
        if self.no_of_revisions == 0:
            self.intervals.append(1)
            self.no_of_revisions += 1
            return self.intervals[self.no_of_revisions - 1]
        if self.confidence_scores[self.no_of_revisions - 1] >= 3:
            self.factor_value = get_net_factor(self.confidence_scores[self.no_of_revisions - 1], self.factor_value)
            #print(f'Factor Value: {self.factor_value}')
            self.intervals.append(round(self.intervals[self.no_of_revisions - 1] * self.factor_value))
            self.no_of_revisions += 1
            return self.intervals[self.no_of_revisions - 1]
        elif self.confidence_scores[self.no_of_revisions - 1] == 1:
            self.intervals.append(1)
            self.factor_value = get_net_factor(self.confidence_scores[self.no_of_revisions - 1], self.factor_value)
            #print(f'Factor Value: {self.factor_value}')
            self.no_of_revisions += 1
            return self.intervals[self.no_of_revisions - 1]        
        elif self.confidence_scores[self.no_of_revisions - 1] == 2:
            self.intervals.append(2) 
            self.factor_value = get_net_factor(self.confidence_scores[self.no_of_revisions - 1], self.factor_value)
            #print(f'Factor Value: {self.factor_value}')
            self.no_of_revisions += 1
            return self.intervals[self.no_of_revisions - 1]
    
    def get_session_info(self):
        return self.session_start_date, self.no_of_revisions, self.intervals, self.confidence_scores
    
    def set_next_interval_reminder(self):
        Reminder_System.set_reminder(self.name, self.next_interval())
        return self.intervals[self.no_of_revisions - 1]
    
def get_confidence_offset(confidence_score):
    if confidence_score == 1:
        return -0.7
    elif confidence_score == 2:
        return -0.5
    elif confidence_score == 3:
        return -0.3
    elif confidence_score == 4:
        return 0
    else:
        return 0.1

def get_net_factor(confidence_score, factor):
    #print(f'In Function Factor Value: {factor}')
    factor = factor + get_confidence_offset(confidence_score)
    if factor <= 1.3:
        factor = 1.3
    return round(factor, 1)
