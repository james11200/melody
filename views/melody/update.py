import os
import json
class Members():
    def __init__(self):
        self.members_file = open('member/member.json', 'r')
        self.data = json.load(self.members_file)
        # with open('member/member.json', 'r') as members:
        #     data = json.load(members)    
        self.members()
        main()

    def __del__(self):
        self.members_file.close()


    def members(self):
        print("Add member press a, remove member press r, show all the member press s, go back to previous page press pp")
        job=input(':')
        if  job.lower()=='a':
            self.add_member()
        elif job.lower() == 'r':
            self.remove_member()
        elif job.lower() == 's':
            self.see_member()
        elif job.lower() == 'pp':
            main()
        else:
            print(job," is an invalid value, please type again.")
            self.members()

    def see_member(self):
        for i in (self.data):
            print(i)

    def add_member(self): 
        x=input('Name: ') 
        y=input('Year: ') 
        print(x,y)
        new_member = {
            "name": x,
            "year": y
        }
        # Add the new object to the list
        self.data.append(new_member)
        for i in (self.data):
            print(i)

        with open('member/member.json', 'w') as f:
            json.dump(self.data, f)

    def remove_member(self):  
        x=input('remove name: ') 
        check=False
        for i in range(len(self.data)):
            #  print(data[i])
            if x ==self.data[i]['name']:
                del self.data[i]
                check=True
                break
        if check:
            print('Member ',x,"removed")
            for i in (self.data):
                print(i)
        else:
            print("Member ",x," not found")    
            for i in (self.data):
                print(i)  



class Publications():
    def __init__(self):
        self.publications_file = open('publication/publication.json', 'r')
        self.data = json.load(self.publications_file)
        self.publications()        
        main()

    def __del__(self):
        self.publications_file.close()

    def publications(self):
        print("add publication press a, remove publication press r, show all the member press s, go back to previous page press pp")
        job=input(':')
        if  job.lower()=='a':
            self.add_publication()

        elif job.lower() == 'r':
            self.remove_publication()
        
        elif job.lower() == 's':
            self.show_publication()

        elif job.lower() == 'pp':
            main()
        else:
            print(job," is an invalid value, please type again.")
            self.publications()
    
    def show_publication(self):
        for i in (self.data):
            print(i)


    def add_publication(self): 
        a=input("Order: ")
        b=input("image_link: ")
        c=input("Subject: ")
        d=input("Authors: ")
        e=input("Cite: ")

        x=input('name: ') 
        y=input('year: ') 
        print(x,y)
        new_publication = {
            "name": x,
            "year": y
        }
        # Add the new object to the list
        self.data.append(new_publication)
        for i in (self.data):
            print(i)

        with open('publication/publication.json', 'w') as f:
            json.dump(self.data, f)

    def remove_publication(self):  
        x=input('remove publication: ') 
        check=False
        for i in range(len(self.data)):
            #  print(data[i])
            if x ==self.data[i]['name']:
                del self.data[i]
                check=True
                break
        if check:
            print('Publication ',x,"removed")
            for i in (self.data):
                print(i)
        else:
            print("Publication ",x," not found")      
            for i in (self.data):
                print(i)




def main():
    print("Edit publications press p, member press m")
    job=input(':')
    if 'p' == job.lower():
        Publications()
    elif job.lower() == 'm':
        Members()
    else:
        print(job," is an invalid value, please type again.")
        main()


if __name__ == '__main__':
    main()