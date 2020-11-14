import os
while True:
	os.system("clear")
	os.system("tput setaf 4")
	print("\t\t\t\tWelcome to LVM Automation Program")
	os.system("tput setaf 2")
	print("\t\t-------------------------------------------------------------")
	os.system("tput setaf 6")	
	print("\t\t\tpress 1 : To see all disk attached to the OS");
	print("\t\t\tpress 2 : To display the disk usage of the file system");
	print("\t\t\tpress 3 : To create a Physical Volume");
	print("\t\t\tpress 4 : To display the Physical Volume created");
	print("\t\t\tpress 5 : To create the Volume Group");
	print("\t\t\tpress 6 : To display the Volume Group created");
	print("\t\t\tpress 7 : To create the Logical Volume");
	print("\t\t\tpress 8 : To display the Logical Volume created");
	print("\t\t\tpress 9 : To format the Logical Volume");
	print("\t\t\tpress 10: To mount the Logical Volume");
	print("\t\t\tpress 11: To exit");
	os.system("tput setaf 0")
	ch=int(input("\t\t\tEnter your choice :- "))
	if ch==1:
		os.system("fdisk -l")
	elif ch==2:
		os.system("df -h")	
	elif ch==3:
		n=int(input("Enter the number of disks inserted"))
		for i in range(n):
			x=input("Enter the disk name:- ");
			os.system("pvcreate {}".format(x))
			

	elif ch==4:
		pvname=input("Enter physical volume(PV): ")
		os.system("pvdisplay {}".format(pvname))
	
	elif ch==5:
		vgname=input("Enter the name for VG:- ")
		if(n==2):
			y=input("Enter the 1st PV name:- ")
			z=input("Enter the 2nd PV name:- ")
			os.system("vgcreate {} {} {}".format(vgname,y,z))
		elif(n==1):
			yn=input("Enter the PV name:- ")
			os.system("vgcreate {} {}".format(vgname,yn))

	elif ch==6:
		vgname=input("Enter name of volume group(VG): ")
		os.system("vgdisplay {}".format(vgname))	


	elif ch==7:
		size=input("Enter the size for the LV:- ")
		lvname=input("Enter name for the LV:- ")
		vgname=input("Enter name of the VG:- ")
		os.system("lvcreate --size {} --name {} {}".format(size,lvname,vgname))
		
	 
	elif ch==8:
		lv=input("Enter name of the LV:- ")
		os.system("lvdisplay {}".format(lv))		 
	elif ch==9:
		lv=input("Enter the LV name:- ")
		os.system("mkfs.ext4 {}".format(lv))
	elif ch==10:
		folder=input("Enter name for folder:- ")
		lv=input("Enter the LV name:- ")
		os.system("mkdir /{}".format(folder))
		os.system("mount {} /{}".format(lv,folder))	 
	elif ch==11:
		exit()
	else:
		print("\t\t\tPlease enter the correct choice")
	input("\t\t\tPlease enter to continue.....")
