'''
Kang Zheng
Li Xu
September 3 2023
Assignment #1 Plotting Data Scientists and Community Data
'''

#import libraries
import numpy as np
import matplotlib.pyplot as plt
from IPython.core.display import Image 


plt.style.use('classic')
plt.style.use('seaborn-whitegrid')
#Mike's input
#In case that you have warning output on the use of the previous style statement
#plt.style.use('seaborn-v0_8-whitegrid')

#Problem 1: Plotting the Club Members
'''For this problem, you need to write the function plotData1 to plot the data scientists in the data-science 
club so that we can conveniently visualize their tenured years, salaries, and paid accounts or not. 
Your plot should be similar to the figure that can be displayed below by running the code cell.
'''
def plotData1(data):
    """
    data: a list of data scientist tuples
    The function plots the the data scientists as required in the problem
    this founction will return a figure.
    """
    #create varaiables
    tenuredata1 = [d[0] for d in data if d[2]==1]#these lines sort the data as I want them to be
    tenuredata0 = [d[0] for d in data if d[2]==0]
    salarydata1 = [d[1] for d in data if d[2]==1]
    salarydata0 = [d[1] for d in data if d[2]==0]
    plt.plot(tenuredata1, salarydata1,'ro', tenuredata0, salarydata0,'b+')
    plt.title("Data-Science Club Menbers")#plot modification
    plt.xlabel("Years as Data Scientist")
    plt.ylabel("Salary")
    plt.grid(True)
    plt.legend(["Unpaid", "Paid"], loc = "upper left")
    plt.savefig("p1.png")#save the image
    Image(filename='p1.png')
    plt.show()
    
#Problem 2
'''For this problem, you need to write a function plotData2 to create a histogram plot. 
The histogram plot allows us discover the underlying frequency distribution of tenure data associated 
with the data scientists including paid and unpaid members in the club. Your plot should be similar to the
figure that can be displayed below by running the code cell.
'''
def plotData2(data):
    '''
    data: a list of data (tuple) used to plot
    this function will take the sorted tenure data to show unpaid and paid probabilities
    this founction will return a figure.
    '''
    #create varaiables
    tenuredata = [d[0] for d in data]
    tenuredata1 = [d[0] for d in data if d[2]==1]
    tenuredata0 = [d[0] for d in data if d[2]==0]
    plt.figure(figsize=(12,6))
    plt.grid(True)
    colors = ["red", "blue"]
    #edit our plot
    plt.hist([tenuredata1, tenuredata0], bins = len(tenuredata),stacked= True,color=colors, density = True)
    plt.title("Histogram of Tenure")
    plt.xlabel("Tenure Data")
    plt.ylabel("Probability Density")
    plt.legend(["Paid", "Unpaid"], loc = "upper right")
    plt.savefig("p2.png")
    Image(filename = "p2.png")
    plt.show()



#Problem 3
'''
For this problem, you need to write a function plotData3 to make a figure with two subplots. 
One is a bar plot, and the other is a histogram plot. The bar plot can conveniently support users to 
visualize how many accounts are paid and how many are unpaid. The histogram plot allows us discover the 
underlying frequency distribution of salary data associated with the two types of data scientists (paid and unpaid). 
Your plot should be similar to the figure that can be displayed below by running the code cell.
'''

def plotData3(data):
    '''
    This function takes one prameter of data, which is a list of tuple
    It will plot a shared x-axis plot with two different graphics on the screen
    using subplots. this founction will return a figure.
    '''
    #create varaiables
    tenuredata = [d[0] for d in data]
    tenuredata1 = [d[0] for d in data if d[2]==1]
    tenuredata0 = [d[0] for d in data if d[2]==0]
    numPaid = len(tenuredata1)
    numUnpaid = len(tenuredata0)
    salarydata1 = [d[1] for d in data if d[2]==1]
    salarydata0 = [d[1] for d in data if d[2]==0]
    names = ["Paid", "Unpaid"]
    values = [numPaid, numUnpaid]
    colors = ["blue", "darkgreen"]
    fig,(ax1,ax2) = plt.subplots(2)
    #fig 1
    ax1.bar(names, values, color = ['r', 'b'])
    ax1.set_ylabel("Number of members")
    ax1.set_title("Unpaid vs. Paid Accounts")
    #fig2
    ax2.hist([salarydata0, salarydata1], color = colors, bins = len(tenuredata), histtype="bar")
    ax2.set_ylabel("Number of members")
    ax2.set_xlabel("Salary")
    ax2.set_title("Histogram of Salary")
    fig.set_figwidth(15)
    fig.set_figheight(10)
    ax2.legend(["Paid", "Unpaid"], loc = "upper right")
    plt.savefig("p3.png")
    Image(filename = "p3.png")
    plt.show()


#Problem 4 Community Data
'''
For this problem, you need to write a function barCommunityData make a bar plot that shows numbers of 
counties in states. Your plot should be similar to the figure that can be displayed below by running the 
code cell that has the Image object. To approach this problem, you need to parse the data from the provided 
file named "county.csv". For the result plot, you need to plot the numbers of counties in Arizona, California, and Texas.
'''
def barCommunityData(fName, aList):
    '''
    This function takes two prameters, fName is the file name that the user need to out in
    aList is the list that are processed by this function, and will be used to plot the histgram.
    this function will return a dictionary contains county names that they user would like to see.
    '''
    inFile = open (fName,'r')#file in
    stateDict = {}
    county = []
    #loop trhrough the line and put them to a new list county
    for line in inFile:
        line = line.strip().split(',')
        county.append(line)
    #check each list in list county to get what we need 
    for each in county:
        #print(each)
        state_key = each[1]#key in the dictionary
        if each[0] != "FIPS" and each[2] != '':#check if we want it
            countyname = each[2] 
            if state_key not in stateDict:
                stateDict[state_key]=[]
                if countyname not in stateDict[state_key]:
                    stateDict[state_key].append(countyname)
                else:
                    continue
            else:
                if countyname not in stateDict[state_key]:
                    stateDict[state_key].append(countyname)
                else:
                    continue
        else: #print no county if there is no county name recorded
            print ("No county found\n")
            continue   
    return stateDict

def plotData4(state,data):
    '''
    this founction will take two prameters, one is the state name that user put in, 
    one is the list we processed. this founction will return a figure.
    '''
    plt.figure(figsize=(15,10))
    plt.bar(state, data, color = 'r')
    plt.title("Number of Counties in States")
    plt.savefig("p4.png")
    Image(filename = "p4.png")
    plt.show()
     

def main():
    '''
    This main function runs the functions we created and also take the user input to get what they are interested.
    Then this function will get the file name and processing informatioon from user.
    '''
    #data for question 1 -3
    data = [(0.7,48000,1),(1.9,48000,0),(2.5,60000,1),(4.2,63000,0),(6,76000,0),(6.5,69000,0),(7.5,76000,0),(8.1,88000,0),(8.7,83000,1),(10,83000,1),(0.8,43000,0),(1.8,60000,0),(10,79000,1),(6.1,76000,0),(1.4,50000,0),(9.1,92000,0),(5.8,75000,0),(5.2,69000,0),(1,56000,0),(6,67000,0),(4.9,74000,0),(6.4,63000,1),(6.2,82000,0),(3.3,58000,0),(9.3,90000,1),(5.5,57000,1),(9.1,102000,0),(2.4,54000,0),(8.2,65000,1),(5.3,82000,0),(9.8,107000,0),(1.8,64000,0),(0.6,46000,1),(0.8,48000,0),(8.6,84000,1),(0.6,45000,0),(0.5,30000,1),(7.3,89000,0),(2.5,48000,1),(5.6,76000,0),(7.4,77000,0),(2.7,56000,0),(0.7,48000,0),(1.2,42000,0),(0.2,32000,1),(4.7,56000,1),(2.8,44000,1),(7.6,78000,0),(1.1,63000,0),(8,79000,1),(2.7,56000,0),(6,52000,1),(4.6,56000,0),(2.5,51000,0),(5.7,71000,0),(2.9,65000,0),(1.1,33000,1),(3,62000,0),(4,71000,0),(2.4,61000,0),(7.5,75000,0),(9.7,81000,1),(3.2,62000,0),(7.9,88000,0),(4.7,44000,1),(2.5,55000,0),(1.6,41000,0),(6.7,64000,1),(6.9,66000,1),(7.9,78000,1),(8.1,102000,0),(5.3,48000,1),(8.5,66000,1),(0.2,56000,0),(6,69000,0),(7.5,77000,0),(8,86000,0),(4.4,68000,0),(4.9,75000,0),(1.5,60000,0),(2.2,50000,0),(3.4,49000,1),(4.2,70000,0),(7.7,98000,0),(8.2,85000,0),(5.4,88000,0),(0.1,46000,0),(1.5,37000,0),(6.3,86000,0),(3.7,57000,0),(8.4,85000,0),(2,42000,0),(5.8,69000,1),(2.7,64000,0),(3.1,63000,0),(1.9,48000,0),(10,72000,1),(0.2,45000,0),(8.6,95000,0),(1.5,64000,0),(9.8,95000,0),(5.3,65000,0),(7.5,80000,0),(9.9,91000,0),(9.7,50000,1),(2.8,68000,0),(3.6,58000,0),(3.9,74000,0),(4.4,76000,0),(2.5,49000,0),(7.2,81000,0),(5.2,60000,1),(2.4,62000,0),(8.9,94000,0),(2.4,63000,0),(6.8,69000,1),(6.5,77000,0),(7,86000,0),(9.4,94000,0),(7.8,72000,1),(0.2,53000,0),(10,97000,0),(5.5,65000,0),(7.7,71000,1),(8.1,66000,1),(9.8,91000,0),(8,84000,0),(2.7,55000,0),(2.8,62000,0),(9.4,79000,0),(2.5,57000,0),(7.4,70000,1),(2.1,47000,0),(5.3,62000,1),(6.3,79000,0),(6.8,58000,1),(5.7,80000,0),(2.2,61000,0),(4.8,62000,0),(3.7,64000,0),(4.1,85000,0),(2.3,51000,0),(3.5,58000,0),(0.9,43000,0),(0.9,54000,0),(4.5,74000,0),(6.5,55000,1),(4.1,41000,1),(7.1,73000,0),(1.1,66000,0),(9.1,81000,1),(8,69000,1),(7.3,72000,1),(3.3,50000,0),(3.9,58000,0),(2.6,49000,0),(1.6,78000,0),(0.7,56000,0),(2.1,36000,1),(7.5,90000,0),(4.8,59000,1),(8.9,95000,0),(6.2,72000,0),(6.3,63000,0),(9.1,100000,0),(7.3,61000,1),(5.6,74000,0),(0.5,66000,0),(1.1,59000,0),(5.1,61000,0),(6.2,70000,0),(6.6,56000,1),(6.3,76000,0),(6.5,78000,0),(5.1,59000,0),(9.5,74000,1),(4.5,64000,0),(2,54000,0),(1,52000,0),(4,69000,0),(6.5,76000,0),(3,60000,0),(4.5,63000,0),(7.8,70000,0),(3.9,60000,1),(0.8,51000,0),(4.2,78000,0),(1.1,54000,0),(6.2,60000,0),(2.9,59000,0),(2.1,52000,0),(8.2,87000,0),(4.8,73000,0),(2.2,42000,1),(9.1,98000,0),(6.5,84000,0),(6.9,73000,0),(5.1,72000,0),(9.1,69000,1),(9.8,79000,1),]
    plotData1(data)
    plotData2(data)
    plotData3(data) 
    fileName = input("Enter your file name: \n")
    n = int(input("Enter the number of states you want to check:\n"))
    i = 0
    stateName = []
    while i < n:
        state = input("Enter the names of states: \n")
        stateName.append(state.capitalize())
        i += 1
    print("You have enter the sates name as below: \n\n",stateName,"\n")
    countydict = barCommunityData(fileName, stateName)
    result= []
    for each in stateName:
        if each in countydict:
            result.append(len(countydict[each]))
    print("\n\n Data found for your states: ",result,"\n")
    plotData4(stateName,result)

if __name__ == '__main__':
    
    main()
