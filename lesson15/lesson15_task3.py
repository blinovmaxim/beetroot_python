class TVController:
    def __init__(self):
        self.channels=["BBC", "Discovery","TV1000","RTR","CNN","STB"]
        self.index_current_channel=0
        

    
    def first_channel(self):
        return self.channels[0]

    def last_channel(self):
        for i in range(0,len(self.channels)):
            if i == (len(self.channels)-1):
                return self.channels[i]

    def turn_channel(self,x):
        self.index_current_channel=x-1
        # a=self.index_current_channel
        turn_on_channel=self.channels[x-1]
        Number_Channels=x
        return print(f"Turn on Channel Numder {Number_Channels} :",turn_on_channel)
    
               
    def next_channel(self):
        if self.index_current_channel==(len(self.channels)-1):
            return self.channels[0]   
        else:
            return self.channels[self.index_current_channel+1]
    
    def previous_channel(self):
        if self.index_current_channel==0:
            return self.channels[(len(self.channels)-1)]   
        else:
            return self.channels[self.index_current_channel-1]

    def current_channel(self):
        return  self.channels[self.index_current_channel]

        
    def is_exist(self,name,N):
        for s in self.channels:
            if name in self.channels:
                print(f"This is channel '{name}' exist: YES" )
                break
            else: 
                print(f"This is Channel '{name}' don't exist: NO")
                break
            
        if N <= (len(self.channels)):
            return print(f"This is Channel {N} exist: YES")              
        else:
            return print(f"This is Channel {N} don't exist: NO")
         

controller=TVController()
print("Channels:",controller.channels)
print("First channel: " ,controller.first_channel())
print("Last channel: ",controller.last_channel())
controller.turn_channel(6)
print("Next channel: ",controller.next_channel())
print("Previous channel: ", controller.previous_channel())
print("Currrennt channel: ", controller.current_channel())
controller.is_exist("CNN",5)














    