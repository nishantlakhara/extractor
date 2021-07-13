from selenium import webdriver
import time

driver = webdriver.Chrome("chromedriver")

driver.get("https://web.whatsapp.com")


def reps():
    print("Do you want to send more msg to anyone")
    askUser = input("Press y for Yes and n for No : ")
    if (askUser == 'Y' or askUser == 'y'):
        msg()
    elif (askUser == 'N' or askUser == 'n'):
        print("Thank you see you soon")
    else:
        print("Please Enter Valid option :\n")
        reps()


def msg():
    name = input('\nEnter Group/User Name: ')
    message = input("Enter your message to group/user: ")

    # Find Whom to message
    try:
        Count = int(input("Enter the message count:"))

        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        user.click()
    except:
        msg()


    #time.sleep(3)
    text_box = driver.find_element_by_class_name('_2A8P4')

    # Send Button
    for i in range(Count):
        try:
            send_message(message, text_box)
        except:
            #Retry once
            send_message(message, text_box)
    reps()


def send_message(message, text_box):
    time.sleep(3)
    text_box.send_keys(message)
    time.sleep(3)
    button = driver.find_element_by_xpath("//span[@data-icon='send']")
    button.click()


msg()