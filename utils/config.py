class config(object):
    def __init__(self):
        self.data_path='questions.txt'
        self.dict_path='dict.pkl'
        self.use_data_path='input.txt'
        
        self.dict_size=50000
        self.vocab_size=self.dict_size+3
        
        self.forward_save_path='./model/forward'
        self.backward_save_path='./model/backward'
        self.forward_log_path='./log/forward_log.txt'
        self.backward_log_path='./log/backward_log.txt'
        self.shuffle=False
        self.use_log_path='./log/use_log.txt'
        
        self.batch_size=32
        self.num_steps=50
        self.hidden_size=300
        self.keep_prob=1
        
        self.GPU='0'
        self.mode='forward'                               
        
        self.search_size=100
        self.use_output_path='./output/output.txt'