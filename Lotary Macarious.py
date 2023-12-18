import random
class task:
    def __init__(self, P_Name='None', Persentage=0, Tic_list=[]):
        self.P_Name = P_Name
        self.Persentage = Persentage
        self.Tic_list = Tic_list

class Lotery_scheduler:
    def __init__(self,Total_number=0):
        self.Process_name=[]
        self.P_List = []
        self.Persentage = []
        self.Total = []
        self.dicts = []
        self.Total_number = Total_number+1
        for i in range(self.Total_number):
            self.Total.append(i)

    def Adding_Process(self,Process):
        self.Process_name.append(Process.P_Name)
        self.P_List.append(Process.Tic_list)
        self.Persentage.append(Process.Persentage)

    def Ticket_disruption(self):
        for i in range(len(self.P_List)):
                for j in range(self.Persentage[i]):
                    self.P_List[i].append(self.Total.pop())

        for i in range(len(self.P_List)):
            temp_dict = {self.Process_name[i]: self.P_List[i]}
            self.dicts.append(temp_dict)

    def Run_scheduler(self):
        if self.Process_name==[]:
            print('No Process in scheduler')
            return
        else:
            wininng_ticket = random.randint(1,self.Total_number-1)
            found_in_dict = None
            found_key = None
            for d in self.dicts:
                values_list = list(d.values())[0]
                if wininng_ticket in values_list:
                    found_in_dict = d
                    found_key = list(d.keys())[0]
                    break

            if found_in_dict:
                print(f"The Ticket {wininng_ticket} Owend by {found_key}")
                return found_key
            else:
                print(f"The number {wininng_ticket} was not found in any dictionary.")
                        
            
                


P_1 =task('Coping Process',5,[]) # 50% of Total tickets number 
P_2 =task('Gamming',2,[])        # 20% of Total tickets number
P_3 =task('Downloading',3,[])    # 30% of Total tickets number

S = Lotery_scheduler(10)         # Total tickets number
S.Adding_Process(P_1)
S.Adding_Process(P_2)
S.Adding_Process(P_3)
S.Ticket_disruption()

L = []
for i in range(100):
    L.append(S.Run_scheduler())

print(f"Coping Process: {round((L.count('Coping Process')/100)*100,2)}%, Gamming: {round((L.count('Gamming')/100)*100,2)}% Downloading: {round((L.count('Downloading')/100)*100,2)}%") # Testing the persentage

