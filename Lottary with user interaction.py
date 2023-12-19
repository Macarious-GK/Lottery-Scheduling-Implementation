import random
class task:
    def __init__(self, P_Name='None', Persentage=0, Tic_list=[]):
        self.P_Name = P_Name
        self.Persentage = Persentage
        self.Tic_list = Tic_list

class Lotery_scheduler:
    def __init__(self):
        self.Process_name=[]
        self.P_List = []
        self.Persentage = []
        self.Total = []
        self.dicts = []
        self.Total_number = 0
        

    def Adding_Process(self,Process):
        self.Process_name.append(Process.P_Name)
        self.P_List.append(Process.Tic_list)
        self.Persentage.append(Process.Persentage)
        self.Total_number += Process.Persentage


    def Ticket_disruption(self):
        for i in range(self.Total_number):
            self.Total.append(i)
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
                        

S = Lotery_scheduler()         # Total tickets number
Number_or_Process = eval(input('Please enter the number of process: '))
process_List = []
for i in range(Number_or_Process):
    Name = input('enter the name of process: ')
    process_List.append(Name)
    tickets = eval(input(f'enter the number of tackets for process {Name}: '))
    create = task(Name,tickets,[])
    S.Adding_Process(create)

S.Ticket_disruption()
                




L = []
for i in range(1000):
    L.append(S.Run_scheduler())
print(L)
for i in range(len(process_List)):

    print(f"{process_List[i]}: {round((L.count(process_List[i])/1000)*100,2)}%") # Testing the persentage

