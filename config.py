class config(object):
    def __init__(self):
        self.data_path='/content/chatbot-text-gen/data/questions.txt'
        self.dict_path='/content/chatbot-text-gen/data/dict.pkl'
        self.use_data_path='input.txt'
        self.max_epoch=10
        
        self.dict_size=50000
        self.vocab_size=self.dict_size+3
        
        self.forward_save_path='/content/chatbot-text-gen/model/forward'
        self.backward_save_path='/content/chatbot-text-gen/model/backward'
        self.forward_log_path='/content/chatbot-text-gen/log/forward_log.txt'
        self.backward_log_path='/content/chatbot-text-gen/log/backward_log.txt'
        self.shuffle=False
        self.use_log_path='/content/chatbot-text-gen/log/use_log.txt'
        
        self.batch_size=32
        self.num_steps=50
        self.hidden_size=300
        self.keep_prob=1
        
        self.GPU='0'
        self.mode='forward'                               
        
        self.search_size=100
        self.use_output_path='/content/chatbot-text-gen/output/output.txt'