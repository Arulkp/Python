
import pandas as pd
import csv
import numpy as np
class first:
  
    def write_data(self):
        s_id=input("Enter uset id: ")
        s_name=raw_input("Enter user name: ")
        s_age=input("Enter user Age: ")
        s_cat=raw_input("Enter user category: ")
        user_details= {
                             'user_id':[s_id],
                             'username':[s_name],
                             'age':[s_age],
                             'gender':[s_cat]  
                          }
        print(type(user_details))
        df = pd.DataFrame(user_details,columns = ['user_id','username','age','gender'])
        df.index = np.arange(1, len(df)+1)
        df.to_csv('csvfile.csv');


    def append_data(self):
         df=pd.read_csv('csvfile.csv',index_col=0);
         df.index = np.arange(1, len(df)+1)
         print(df);
         s_id=input("Enter uset id: ")
         s_name=raw_input("Enter user name: ")
         s_age=input("Enter user Age: ")
         s_cat=raw_input("Enter user category: ")
         user_details= {
                             'user_id':[s_id],
                             'username':[s_name],
                             'age':[s_age],
                             'gender':[s_cat]  
                          }
         data=pd.DataFrame(user_details,columns=['user_id','username','age','gender']);
         _temp=df.append(data);
         _temp.index=np.arange(1, len(_temp)+1);
         date1=_temp.to_csv('csvfile.csv');
    
 
    def remove_data(self):
        df=pd.read_csv('csvfile.csv',index_col=0)
        df.index = np.arange(1, len(df)+1)
        print(df);
        removed_username=raw_input('Enter the name wants to removed you........: ')
        remove=df[df.username != removed_username];
        data_row=pd.DataFrame(remove,columns=['user_id','username','age','gender']);
        data_row.index=np.arange(1, len(data_row)+1);
        remove_row=data_row.to_csv('csvfile.csv');
        print("Name is Removed in table.......")

    def update_data(Self):
        df=pd.read_csv('csvfile.csv',index_col=0)
        df.index = np.arange(1, len(df)+1)
        print(df);
        print("Options for Updation.......")
        print("1.update id")
        print("2.update username")
        print("3.update gender age");
        user_request=input("Enter Your options..");
        if user_request == 1:
             your_name=raw_input("Enter your name: ");
             update_id=raw_input("Enter Yout updated id: ");
             df=pd.read_csv('csvfile.csv',index_col=0)
             df.index = np.arange(1, len(df)+1)
             df.loc[df.username == your_name,'user_id'] =  update_id
             data_row=pd.DataFrame(df,columns=['user_id','username','age','gender']);
             df1=data_row.to_csv('csvfile.csv')
             print("Updated Your Id Successfully......")
             print(df1)
        
        elif user_request == 2:
             your_name=raw_input("Enter your name: ");
             update_name=raw_input("Enter Yout updated name: ");
             df=pd.read_csv('csvfile.csv',index_col=0)
             print(df);
             df.index = np.arange(1, len(df)+1)
             df.loc[df.username == your_name,'username'] = update_name
             data_row=pd.DataFrame(df,columns=['user_id','username','age','gender']);
             data_row.to_csv('csvfile.csv')
             print("Updated Your Name Successfully......")
             print(df)
            
        else:
             your_name=raw_input("Enter your name: ");
             update_age=raw_input("Enter Your update: ");
             df=pd.read_csv('csvfile.csv',index_col=0)
             df.index = np.arange(1, len(df)+1)
             df.loc[df.username == your_name,'age'] = update_age
             print(df)
             data_row=pd.DataFrame(df,columns=['user_id','username','age','gender']);
             data_row.to_csv('csvfile.csv')
             print("Updated Your Age Successfully......")
             print(df)

    def process(self):
        print("Your opeation");
        print("1.Register");
        print("2.Deregister");
        print("3.Update details");
        print("4.exit");
        R=input("Enter your request");

        if R == 1:
            self.append_data();
        elif R == 2:
            self.remove_data();
        elif R == 3:
            self.update_data();
        else:
            self.exit()


    def exit(self):
        quit(); 


Pandas_csv=first()
while True:
    Pandas_csv.process()