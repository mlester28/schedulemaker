import textwrap
import os
import csv

classes = []
classheader = {
    "class": "Class",
    "professor": "Professor",
    "days": "Days",
    "time" : "Time",
    "department": "Department",
    "credits": "Credits"
    }
field_order = ["class", "professor", "days", "time", "department", "credits"]


def delete_class(classes, which):
    if not which.isdigit():
        print ("'" + which + 
            "' needs to be the number of a class!")
        return {}
    which = int(which)
    if which < 1 or which > len(classes):
        print ("'" + str(which) + 
            "' needs to be the number of a class!")
        return {}
    class1 = classes[which-1]
    del classes[which-1]
    print( "Deleted class #" + str(which))
    return class1

def find_sort_field():
    """ Find out which field to sort by """
    print("Which column do you want to sort by?")
    print("   class) Class")
    print("   prof) Professor")
    print("   day) Days")
    print("   dept) Department")
    action = input("> ")    
    if action.lower() in ['class','prof','day','dept']:
        action = action.lower()
        if action == 'class':
            return "class"
        elif action == 'prof':
            return "professor"
        elif action == 'day':
            return "days"
        else:
            return "department"
    else:
        print(action +"?")
        print("That's not an field that I know about")
        return None

 
def sort_classes_by(which):
    global classes
    classes.sort(key=lambda e: e[which].lower())  
    
def sort_classes():
    global classes
    temp=[]
    # I want to sort by class. So I'm building a list temp of little lists 
    # where each little list has title first and the rest of the item next
    for item in classes:
        temp.append((item["class"].lower(),item))
    class1 = []
    # sorted sorts by the key, but only the values are appended to class2.
    # Recall that the second item of the little list.
    for key, value in sorted(temp):
        class1.append(value)
    classes = class1

    
def edit_class(classes, which):
    if not which.isdigit():
        print ("'" + which + 
            "' needs to be the number of a class!")
        return {}
    which = int(which)
    if which < 1 or which > len(classes):
        print ("'" + str(which) + 
            "' needs to be the number of a class!")
        return {}
        
    class1 = classes[which-1]
    print("Enter the data for a new class. Press <enter> to leave unchanged.")
    
    print(class1["class"])
    newclass = input("Enter Class name to change or press return: ")
    if newclass == "":
        newclass = class1["class"]
        
    print(class1["professor"])
    newprof = input("Enter professor's name to change or press return: ")
    if newprof == "":
        newprof = class1["professor"]

    print(class1["days"])
    newdays = input("Enter days to change or press return: ")
    if newdays == "":
        newdays = class1["days"]
        
    print(class1["time"])
    newtime = input("Enter time to change or press return: ")
    if newtime == "":
        newtime = class1["time"]
    
    print(class1["department"])
    newdept = input("Enter department (hum, sbs, or nsm) to change or press return: ")
    if newdept == "":
        newdept = class1["department"]

    print(class1["credits"])
    newcredits = input("Enter number of credits to change or press return: ")
    if newcredits == "":
        newcredits = class1["credits"]  

    class1 = {
    "class": newclass,
    "professor": newprof,
    "days": newdays,
    "time" : newtime,
    "department": newdept,
    "credits": newcredits,
    }
    classes[which-1] = class1
    sort_classes()
    return class1


def save_class_list():
    global classes
    global field_order
    
    f = open("myclasses.csv", 'w', newline='')
    csv_writer = csv.DictWriter(f,fieldnames=field_order,extrasaction='ignore')
    csv_writer.writerows(classes)
    f.close()
  
  
def load_class_list():
    global classes
    global field_order
    # can't be opened if not there
    if os.access("myclasses.csv",os.F_OK):
        with open("myclasses.csv", newline='') as csv_file:
            #restval = blank columns = - /// restkey = extra columns +
            reader = csv.DictReader(csv_file, fieldnames=field_order, restkey='+', 
                                    restval='-', delimiter=',', quotechar='"')
    
            try:
                for row in reader:
                    classes.append(row)
            except csv.Error as e:
                print('file {}, line {}: {}'.format(csv_file, reader.line_num, e))

def show_classes():
    show_class(classheader)

    for index, class1 in enumerate(classes):
        show_class(class1, index)
        if (index+1) % 10 == 0:
            input("Hit return to continue ...")
    print()


def show_class(class1, index=None):
    wrapped_class = textwrap.wrap(class1['class'], 22)
    wrapped_professor = textwrap.wrap(class1['professor'], 16)
    wrapped_days = textwrap.wrap(class1['days'],10)
    wrapped_time = textwrap.wrap(class1['time'], 16)
    wrapped_department = textwrap.wrap(class1['department'], 10)
    wrapped_credits = textwrap.wrap(class1['credits'], 10)
    
    if index == None:
        output = " "*6
    else:
        output = str(index+1).rjust(4) + "  "
        
    output += wrapped_class[0].ljust(22) + "  "
    output += wrapped_professor[0].ljust(16) + "  "
    output += wrapped_days[0].ljust(10)+ "  "
    output += wrapped_time[0].ljust(16)+ "  "
    output += wrapped_department[0].ljust(10)+ "  "
    output += wrapped_credits[0].ljust(10)
    output += "\n"
    
    max_len = max(len(wrapped_class), 
                  len(wrapped_professor),
                  len(wrapped_days),
                  len(wrapped_time),
                  len(wrapped_department),
                  len(wrapped_credits))
    for next_line in range(1, max_len):
        output += " " * 4 + "  "
        if next_line < len(wrapped_class):
            output += wrapped_class[next_line].ljust(22) + "  "
        else:
            output += " " * 22 + "  "
        if next_line < len(wrapped_professor):
            output += wrapped_professor[next_line].ljust(16) + "  "
        else:
            output += " " * 16 + "  "
        if next_line < len(wrapped_days):
            output += wrapped_days[next_line].ljust(10) + "  "
        else:
            output += " " * 16 + "  "
        if next_line < len(wrapped_time):
            output += wrapped_time[next_line].ljust(16) + "  "
        else:
            output += " " * 16 + "  "
        if next_line < len(wrapped_department):
            output += wrapped_department[next_line].ljust(10) + "  "
        else:
            output += " " * 24 + "  "
        if next_line < len(wrapped_credits):
            output += wrapped_credits[next_line].ljust(10) + "  "
        output += "\n"
        
    print(output)
    

def create_class(classes):
    print("Enter the data for a new class:")
    newclass = input("Enter Class name: ")
    newprof = input("Enter professor's name: ")
    newdays = input("Enter days: ")
    newtime = input("Enter class time: ")
    #if class day&time conflicts, then do not enter class
    for item in classes:
        if item["days"] == newdays and item["time"] == newtime:
            input("Conflicting class, you cannot add this to your schedule.")
            return {}

    newdept = input("Enter department (nsm, sbs, or hum): " )
    newcredits = input("Enter number of class credits: ")
    class1 = {
    "class": newclass,
    "professor": newprof,
    "days" : newdays,
    "time" : newtime,
    "department": newdept,
    "credits": newcredits
    }
    classes.append(class1)
    sort_classes()
    return class1
  
  
def get_action():
    """ Find out what the player wants to do next. """
    print("Choose from among the following option?")
    print("   n) new")
    print("   d) delete")
    print("   l) look at current one")
    print("   s) show")
    print("   r) re-sort by another field")
    print("   c) total semester credits")
    print("   g) general education requirement")
    print("   e) edit")
    print("   q) quit")
    action = input("> ")    
    if action.lower() in ['n','d','l', 'r', 's', 'c', 'e', 'q', 'g']:
        return action.lower()
    else:
        print(action +"?")
        print("That's not an option that I know about")
        return None


def main_loop():
    class1={}
    load_class_list()
    while 1:
        action = get_action()
        if action == None:
            continue
        action = action.lower()
        if "q" in action:
            print( "Exiting...")
            break
        elif action == 'n':
            class1 = create_class(classes)
        elif action == 'd':
            which = input("Which class do you want to delete? ")
            print("which is ", which)
            class1 = delete_class(classes,which)
        elif action == 'l':
             if class1 != {}:
                 show_class(classheader)
                 show_class(class1)
             else:
                 print("No current class record chosen.")
        elif action == 's':
             show_classes()
        elif action == 'r':
            print("sort by")
            which = find_sort_field()
            if which == None:
                continue
            print("which is ", which)
            sort_classes_by(which)
        elif action == 'c':
            total = 0
            for item in classes:
                total = total + float(item["credits"])
            print("You are taking",total,"total credits this semester.")
        elif action == 'g':
            totalnsm = 0
            totalsbs = 0
            totalhum = 0
            for item in classes:
                if item["department"] == "nsm":
                    totalnsm = totalnsm + float(item["credits"])
                elif item["department"] == "hum":
                    totalhum = totalhum + float(item["credits"])
                else:
                    totalsbs = totalsbs + float(item["credits"])
            print("You are taking", totalnsm,"nsm credit(s) this semester. \n")
            print("You are taking", totalsbs,"sbs credit(s) this semester. \n")
            print("You are taking", totalhum,"hum credit(s) this semester. \n")
        
        elif action == 'e':
            which = input("Which class do you want to edit? ")
            print("which is ", which)
            class1 = edit_class(classes,which)
        else:
            print("I don't know that command.")
    save_class_list()

# The following makes this program start running at main_loop() 
# when executed as a stand-alone program.    
if __name__ == '__main__':
    main_loop()
