class config(object):
    def __init__(self):
        self.data_path='/content/chatbot-text-gen/data/questions.txt'
        self.dict_path='/content/chatbot-text-gen/data/dict.pkl'
        self.use_data_path='/content/chatbot-text-gen/data/input.txt'
        
        self.dict_size=30000
        self.vocab_size=self.dict_size+4
        
        self.forward_save_path='gs://winningarc-bucket-1/forward'
        self.backward_save_path='gs://winningarc-bucket-1/backward'
        
        self.forward_log_path='gs://winningarc-bucket-1/log/forward_log.txt'
        self.backward_log_path='gs://winningarc-bucket-1/log/backward_log.txt'

        self.use_log_path='gs://winningarc-bucket-1/log/use_log.txt'

        self.shuffle=False
        
        self.max_epoch=100
        self.batch_size=32
        self.num_steps=50
        self.hidden_size=300
        self.keep_prob=1
        self.num_layers=2
        
        self.max_grad_norm=5
        
        self.GPU='0'
        self.mode='forward'                               
        self.sample_time=500
        self.record_time=[100,200,300]
        self.sample_sentence_number=119
        
        self.search_size=100
        self.use_output_path='/content/output.txt'
      
        #self.sample_prior=[1,1,1,1]
        self.action_prob=[0.3,0.3,0.3,0.1]                                         #the prior of 4 actions
        #self.threshold=0.1
        self.sim=None                                                                       #matching model
        #self.sim_word=True
        self.double_LM=False                                                            
        self.keyword_pos=False
        self.keyboard_input=False
        self.sim_hardness=5
        self.rare_since=30000
        self.just_acc_rate=0.0
        self.key_num=4    
        self.max_length=10                  