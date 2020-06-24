# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 22:20:30 2020

@author: Dana
"""
import glob
import numpy as np
import matplotlib.pyplot as plt

def extractData(f):

    # Create initial dictionary
    D = {}
    majorbreakdown = []
    busrace = []
    engrace = []
    edurace = []
    racebreakdown = []
    genderbreakdown = []
    
    majorslist = ['education','engineering','law','bio/life\nsciences','math','physical\nsciences','dentistry','medicine','business/\nadmin']
    racelist = ['American Indian/\nAlaska Native','Asian/\nNative Hawaiian/\nPacific Islander','Black/African\nAmerican','Hispanic','White']
    for frame in glob.glob(f):
        f = open(frame)
        matrix = []
        
        for line in f:
            s = line.split(',')    
            
            frame_list1 = ['Data_2018.csv','Data_2016.csv','Data_2014.csv','Data_2012.csv','Data_2010.csv']
            frame_list2 = ['Data_2006.csv','Data_2004.csv','Data_2002.csv']
            
            if frame in frame_list1:
                # Don't read the first line, which has the labels
                if s[0] == 'UNITID': continue
            
                else:
                    modifiedline = []
                    
                    # These are the columns that I wish to extract 
                    # data from; all the other columns are useless 
                    # and unneccesary so I'll leave them out
                    listofcolumns = [0,2,7,9,11,13,25,31,43]
                  
                    # These are all strings by default; convert to 
                    # numbers so the statistics can be worked with
                    s[4] = int(s[4])
                    s[19] = int(s[19])
                    s[37] = int(s[37])
                    for num in listofcolumns:
                        if num == 2:
                            s[num] = float(s[num])
                        else:
                            s[num] = int(s[num])
                            
                        # Reduce the needed lines down to 
                        # only the needed columns    
                        if s[4] == 3:
                            modifiedline.append(s[num])
                            
                    # This format does not combine Asian and 
                    # Pacific Islanders, so do it manually
                    modifiedline.append(s[19]+s[37])

                    # Form a matrix that contains only the 
                    # desired rows and columns
                    if s[4] == 3:
                        matrix.append(modifiedline)
     
                
            if frame == 'Data_2008.csv':
                if s[0].upper() == 'UNITID': continue
                else:
                    listofcolumns = [0,2,7,9,11,13,25,31,37,19]
                    for num in listofcolumns:
                        if num == 2:
                            s[num] = float(s[num])
                        else:
                            s[num] = int(s[num])
                    s[4] = int(s[4])
                    
                    modifiedline = []
                    for num in listofcolumns:
                        if s[4] == 3:
                            modifiedline.append(s[num])
    
                    if s[4] == 3:
                        matrix.append(modifiedline)   

                
            if frame in frame_list2:
                if s[0].upper() == 'UNITID': continue
                else:
                    listofcolumns = [0,2,53,35,37,43,41,47,49,45]
                    for num in listofcolumns:
                        if num == 2:
                            s[num] = float(s[num])
                        else:
                            s[num] = int(s[num])
                    s[4] = int(s[4])
                    
                    modifiedline = []
                    for num in listofcolumns:
                        if s[4] == 3:
                            modifiedline.append(s[num])
    
                    if s[4] == 3:
                        matrix.append(modifiedline)
                        
        # Create a dictionary of all the matrixes (one for each year)
        D[frame] = matrix
        
#    np.savetxt('dictionary.csv',D['2018.csv'])
        
    
        # Define variables for 'Calculate yearly stats of majors'
        total = 0
        t_edu = 0
        t_ege = 0
        t_law = 0
        t_bio = 0
        t_mth = 0
        t_phy = 0
        t_dty = 0
        t_med = 0
        t_bus = 0
        
        # Define variables for 'Calculate breakdown of race per year'
        bus_amind = 0
        bus_aa = 0
        bus_his = 0
        bus_white = 0
        bus_ashawpi = 0
        bus_male = 0
        bus_female = 0
        
        eng_amind = 0
        eng_aa = 0
        eng_his = 0
        eng_white = 0    
        eng_ashawpi = 0
        
        edu_amind = 0
        edu_aa = 0
        edu_his = 0
        edu_white = 0
        edu_ashawpi = 0
        
        amind = 0
        aa = 0
        his = 0
        white = 0
        ashawpi = 0
        
        female = 0
        male = 0
        
        for j, k in enumerate(D[frame]):
            
            '''
            How to use the dictionary!

            D[frame/year ie: '2018.csv'][go through all of these, these are all the lines in the excel doc][one of the following:]
            0 = school ID
            1 = CIP code for major field
            	13=Education
                14=Engineering
                22.0101=Law
                26=Biological Sciences/Life Sciences
                27=Math
                40=Physical Sciences
                51.0401=Dentistry
                51.1201=Medicine
                52=Business Management/Admin Service
            2 = total students studying it
            3 = total men
            4 = total women
            5 = total American Indian/Alaska Native
            6 = total black/african american
            7 = total Hispanic
            8 = total white
            9 = total Asian/Native Hawaiian/Pacific Islander
            
            '''
            # Calculate yearly stats of majors
            total += D[frame][j][2]
            mc = D[frame][j][1]
            st = D[frame][j][2]
            if mc == 13: t_edu += st
            if mc == 14: t_ege += st
            if mc == 22.0101: t_law += st
            if mc == 26: t_bio += st          
            if mc == 27: t_mth += st
            if mc == 40: t_phy += st
            if mc == 51.0401: t_dty += st                  
            if mc == 51.1201: t_med += st
            if mc == 52: t_bus += st
            
            # Calculate breakdown of race among business majors per year
            if D[frame][j][1] == 52:
                bus_amind += D[frame][j][5]
                bus_aa += D[frame][j][6]
                bus_his += D[frame][j][7]
                bus_white += D[frame][j][8]
                bus_ashawpi += D[frame][j][9]
                bus_male += D[frame][j][3]
                bus_female += D[frame][j][4]
                
            # Calculate breakdown of race among engineering majors per year
            if D[frame][j][1] == 14:
                eng_amind += D[frame][j][5]
                eng_aa += D[frame][j][6]
                eng_his += D[frame][j][7]
                eng_white += D[frame][j][8]
                eng_ashawpi += D[frame][j][9]
                
            # Calculate breakdown of race among education majors per year                
            if D[frame][j][1] == 13:
                edu_amind += D[frame][j][5]
                edu_aa += D[frame][j][6]
                edu_his += D[frame][j][7]
                edu_white += D[frame][j][8]
                edu_ashawpi += D[frame][j][9]
                
            amind += D[frame][j][5]
            aa += D[frame][j][6]
            his += D[frame][j][7]
            white += D[frame][j][8]
            ashawpi += D[frame][j][9]
            
            male += D[frame][j][3]
            female += D[frame][j][4]

        # Create list for 'Calculate yearly stats of majors'   
        majorbreakdown.append([t_edu,t_ege,t_law,t_bio,t_mth,t_phy,t_dty,t_med,t_bus])
         
        busrace.append([bus_amind,bus_ashawpi,bus_aa,bus_his,bus_white])
        engrace.append([eng_amind,eng_ashawpi,eng_aa,eng_his,eng_white])
        edurace.append([edu_amind,edu_ashawpi,edu_aa,edu_his,edu_white])
        racebreakdown.append([amind,ashawpi,aa,his,white])
        genderbreakdown.append([male,female])

        f.close()
        
#        print(D[frame]) 
   
    # Plot graph of major breakdown per year
    fig1 = plt.figure(dpi=200)
    x = np.linspace(1,9,9)
    w = 1/11
    plt.bar(x-(4*w),majorbreakdown[0],width=w,label='2002')
    plt.bar(x-(3*w),majorbreakdown[1],width=w,label='2004')
    plt.bar(x-(2*w),majorbreakdown[2],width=w,label='2006')
    plt.bar(x-w,majorbreakdown[3],width=w,label='2008')
    plt.bar(x,majorbreakdown[4],width=w,label='2010')
    plt.bar(x+(w),majorbreakdown[5],width=w,label='2012')
    plt.bar(x+(2*w),majorbreakdown[6],width=w,label='2014')
    plt.bar(x+(3*w),majorbreakdown[7],width=w,label='2016')
    plt.bar(x+(4*w),majorbreakdown[8],width=w,label='2018')
    plt.subplots_adjust(top=0.925,bottom=0.23,left=0.1,right=0.97)
    plt.xlim([0.5,9.5])
    plt.legend(ncol=2)
    plt.title('Graph 1: Breakdown of Majors by Year in US')
    plt.xlabel('Major')
    plt.ylabel('Students (millions)')
    plt.xticks(range(1,10),majorslist,rotation=45,va='top',horizontalalignment='center')
    plt.yticks(range(0,11000000,1000000),range(0,11))
    
#    # Plot graph of gender breakdown per year
#    fig1 = plt.figure(dpi=200)
#    x = np.linspace(1,2,2)
#    plt.bar(x-(5*w),genderbreakdown[0],width=w,label='1998')
#    plt.bar(x-(4*w),genderbreakdown[1],width=w,label='2000')
#    plt.bar(x-(3*w),genderbreakdown[2],width=w,label='2002')
#    plt.bar(x-(2*w),genderbreakdown[3],width=w,label='2004')
#    plt.bar(x-w,genderbreakdown[4],width=w,label='2006')
#    plt.bar(x,genderbreakdown[5],width=w,label='2008')
#    plt.bar(x+w,genderbreakdown[6],width=w,label='2010')
#    plt.bar(x+(2*w),genderbreakdown[7],width=w,label='2012')
#    plt.bar(x+(3*w),genderbreakdown[8],width=w,label='2014')
#    plt.bar(x+(4*w),genderbreakdown[9],width=w,label='2016')
#    plt.bar(x+(5*w),genderbreakdown[10],width=w,label='2018')
#    plt.subplots_adjust(top=0.925,bottom=0.23,left=0.1,right=0.97)
#    plt.xlim([0.5,2.5])
#    plt.legend(ncol=2)
#    plt.title('Breakdown of Gender by Year in US')
#    plt.xlabel('Gender')
#    plt.ylabel('Students (millions)')
#    plt.xticks(range(1,3),genderlist,rotation=45,va='top',horizontalalignment='center')
##    plt.yticks(range(0,11000000,1000000),range(0,11))
#    
#    
##    def createBarGraph(desiredlist,left,title,rangemax,rangeinc,newrange):
##        fig = plt.figure(dpi=200)
##        y = np.linspace(1,5,5)
##        w = 1/13
##        plt.bar(y-(5*w),desiredlist[0],width=w,label='1998')
##        plt.bar(y-(4*w),desiredlist[1],width=w,label='2000')
##        plt.bar(y-(3*w),desiredlist[2],width=w,label='2002')
##        plt.bar(y-(2*w),desiredlist[3],width=w,label='2004')
##        plt.bar(y-(w),desiredlist[4],width=w,label='2006')
##        plt.bar(y,desiredlist[5],width=w,label='2008')
##        plt.bar(y+w,desiredlist[6],width=w,label='2010')
##        plt.bar(y+(2*w),desiredlist[7],width=w,label='2012')
##        plt.bar(y+(3*w),desiredlist[8],width=w,label='2014')
##        plt.bar(y+(4*w),desiredlist[9],width=w,label='2016')
##        plt.bar(y+(5*w),desiredlist[10],width=w,label='2018')
##        plt.subplots_adjust(top=0.925,bottom=0.305,left=left,right=0.97)
##        plt.xlim([0.5,5.5])
##        plt.legend()
##        plt.title(title)
##        plt.xlabel('Race')
##        plt.ylabel('Students (millions)')
##        plt.xticks(range(1,6),racelist,rotation=45,va='top',horizontalalignment='center')
##        plt.yticks(range(0,rangemax,rangeinc),newrange)
##        plt.show()
##    return 
#
##    createBarGraph(busrace,0.08,'Breakdown of Races within Business Majors by Year in US',6000000,1000000,range(0,6))
#    
    # Plot graph of business majors and race
    fig2 = plt.figure(dpi=200)
    y = np.linspace(1,5,5)
    plt.bar(y-(4*w),busrace[0],width=w,label='2002')
    plt.bar(y-(3*w),busrace[1],width=w,label='2004')
    plt.bar(y-(2*w),busrace[2],width=w,label='2006')
    plt.bar(y-w,busrace[3],width=w,label='2008')
    plt.bar(y,busrace[4],width=w,label='2010')
    plt.bar(y+(w),busrace[5],width=w,label='2012')
    plt.bar(y+(2*w),busrace[6],width=w,label='2014')
    plt.bar(y+(3*w),busrace[7],width=w,label='2016')
    plt.bar(y+(4*w),busrace[8],width=w,label='2018')
    plt.subplots_adjust(top=0.925,bottom=0.305,left=0.08,right=0.97)
    plt.xlim([0.5,5.5])
    plt.legend(ncol=2)
    plt.title('Breakdown of Races within Business Majors by Year in US')
    plt.xlabel('Race')
    plt.ylabel('Students (millions)')
    plt.xticks(range(1,6),racelist,rotation=45,va='top',horizontalalignment='center')
    plt.yticks(range(0,6000000,1000000),range(0,6))

    # Plot graph of engineering majors and race
    fig3 = plt.figure(dpi=200)
    plt.bar(y-(4*w),engrace[0],width=w,label='2002')
    plt.bar(y-(3*w),engrace[1],width=w,label='2004')
    plt.bar(y-(2*w),engrace[2],width=w,label='2006')
    plt.bar(y-w,engrace[3],width=w,label='2008')
    plt.bar(y,engrace[4],width=w,label='2010')
    plt.bar(y+(w),engrace[5],width=w,label='2012')
    plt.bar(y+(2*w),engrace[6],width=w,label='2014')
    plt.bar(y+(3*w),engrace[7],width=w,label='2016')
    plt.bar(y+(4*w),engrace[8],width=w,label='2018')
    plt.subplots_adjust(top=0.925,bottom=0.305,left=0.12,right=0.97)
    plt.xlim([0.5,5.5])
    plt.legend(ncol=2)
    plt.title('Breakdown of Races within Engineering Majors by Year in US')
    plt.xlabel('Race')
    plt.ylabel('Students (millions)')
    plt.xticks(range(1,6),racelist,rotation=45,va='top',horizontalalignment='center')
    plt.yticks(range(0,2000000,250000),np.linspace(0,2,9))
        
    # Plot graph of education majors and race
    fig4 = plt.figure(dpi=200)
    plt.bar(y-(4*w),edurace[0],width=w,label='2002')
    plt.bar(y-(3*w),edurace[1],width=w,label='2004')
    plt.bar(y-(2*w),edurace[2],width=w,label='2006')
    plt.bar(y-w,edurace[3],width=w,label='2008')
    plt.bar(y,edurace[4],width=w,label='2010')
    plt.bar(y+(w),edurace[5],width=w,label='2012')
    plt.bar(y+(2*w),edurace[6],width=w,label='2014')
    plt.bar(y+(3*w),edurace[7],width=w,label='2016')
    plt.bar(y+(4*w),edurace[8],width=w,label='2018')
    plt.subplots_adjust(top=0.925,bottom=0.305,left=0.12,right=0.97)
    plt.xlim([0.5,5.5])
    plt.legend(ncol=2)
    plt.title('Breakdown of Races within Education Majors by Year in US')
    plt.xlabel('Race')
    plt.ylabel('Students (millions)')
    plt.xticks(range(1,6),racelist,rotation=45,va='top',horizontalalignment='center')
    plt.yticks(range(0,3000000,250000),np.linspace(0,3,13))

    # Plot graph of education majors and race
    fig5 = plt.figure(dpi=200)
    plt.bar(y-(4*w),racebreakdown[0],width=w,label='2002')
    plt.bar(y-(3*w),racebreakdown[1],width=w,label='2004')
    plt.bar(y-(2*w),racebreakdown[2],width=w,label='2006')
    plt.bar(y-w,racebreakdown[3],width=w,label='2008')
    plt.bar(y,racebreakdown[4],width=w,label='2010')
    plt.bar(y+(w),racebreakdown[5],width=w,label='2012')
    plt.bar(y+(2*w),racebreakdown[6],width=w,label='2014')
    plt.bar(y+(3*w),racebreakdown[7],width=w,label='2016')
    plt.bar(y+(4*w),racebreakdown[8],width=w,label='2018')
    plt.subplots_adjust(top=0.925,bottom=0.305,left=0.095,right=0.97)
    plt.xlim([0.5,5.5])
    plt.legend(ncol=2)
    plt.title('Graph 3: Breakdown of Race by Year in US')
    plt.xlabel('Race')
    plt.ylabel('Students (millions)')
    plt.xticks(range(1,6),racelist,rotation=45,va='top',horizontalalignment='center')
    plt.yticks(range(0,12000000,1000000),range(0,12))
    
        
    # Create pie plot of race in 2018
    # Account for unspecified race/ multiple race students
    totalbyrace = 0
    for r in racebreakdown[8]:
        totalbyrace += r
    racebreakdown[8].append((total-totalbyrace))
    racelist.append('other')
    #
    fig6 = plt.figure(dpi=200)
    plt.axis('equal')
    plt.pie(racebreakdown[8],labels=racelist,autopct='%1.1f%%',textprops={'fontsize':7},wedgeprops={'linewidth':0.1,'edgecolor':"black"})
    plt.title('Graph 2: Race Breakdown of US Students in 2018')

    plt.show()
    
    return 

print(extractData('Data_****.csv'))



