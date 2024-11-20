'''class To_Do_App():
    # def init(self):
    #     self.tasks = []
        
     
    def task(self):
        tasks = []
        print("_____Welcome_____")
        total_task = int(input("Enter how many task you want to add: "))
        
        for i in range(1,total_task+1):
            task_name = input(f"Enter a Task {i}: ")
            tasks.append(task_name)
            print(f"Tasks are {tasks}") 
        
        while True:
            operations = input("Enter\n1-ADD\n2-UPDATE\n3-DELETE\n4-VIEW\n5-EXTIT/STOP\n")
            
            if operations=='1':#ADD TASK
                add = input("Add your Task Here : ")
                tasks.append(add)
                print(f"Task '{add}' has been Added successfully.\nNow You have tasks :{tasks}")
                
            elif operations=='2':#update task
                print(f"Here are your Tasks List :{tasks}")
                updated_val = input("Enter a task you want to update : ")
                if updated_val in tasks:
                    updated_task = input("Enter New task : ")
                    ind = tasks.index(updated_val)
                    tasks[ind]=updated_task
                    print(f"Task '{updated_task}' updated successefully.\nNow You have tasks :{tasks}")
                    
            elif operations=='3':
                print(f"Here are your Tasks List :{tasks}")
                del_val = input("Enter a task you want to delete : ")
                if del_val in tasks:
                    ind = tasks.index(del_val)
                    del tasks[ind]
                    print(f"sucessfully deleted {del_val}\nNow You have tasks :{tasks} ")
                    
            elif operations == '4':
                print(f"Here are your tasks : {tasks}")
                
            elif operations=='5':
                print("closing the programm")
                break    
                
            else :
                print("Invalid option, Please choose a valid option")
           
                
todo = To_Do_App()
todo.task()  '''                  
                    
         