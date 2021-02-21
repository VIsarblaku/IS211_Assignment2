# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import argparse
import logging
import datetime
import argparse

def downloadData ():
    pass
    import urllib.request
    with urllib.request.urlopen('https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv') as response:
        file_content = response.read().decode('utf-8')
    return file_content

def processData (file_content):
    logger = logging.getLogger("assignment2")
    data_list = file_content.split('\n')

    personData = {}
    lineum = 0

    for line in data_list:
        lineum = lineum +1
        info = line.split(',')
        if len(info) <3:
            continue
        try:
            id = info[0]
            name = [1]
            birthday = datetime.datetime.strptime(info[2], "%d/%m/%y")
            data_tuple = (name, birthday)
            personData[id] = data_tuple

        except:
            loging.error("Error processing line #" + str(linenum) + "for ID #" +str(id))
        returnpersonData

def displayPerson(id, personData):
    id = str(id)
    if id in personData. keys():
        data_tuple = personData[id]
        name = data_tuple[0]
        birthdate = datetime.datetime.strftime(data_tuple[1], "%y/%m/%d")
        print ('Person # {} is {} with a birthday of {}'.format(id, name, birthday))
    else:
        print("No user found with that id")

    def main(url):
        print(f"Running main with URL = {url}...")
        try:
            file_content = downloadData(url)
            personData = processData(file_content)
            while true:
                val = int(input("Enter ID to lookup: "))
                if val <1:
                    break
                displayPerson(val, personData)
        except Exception as e:
            print (str(e))

        if__name__ == "__main__"

        parser = argparse.ArgumentParser()
        parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
        args = parser.parse_args()
        logger = loging.getLogger("assignmet")
        logging.basicConfig(filename='errors.log', level=logging.ERROR)
        main(args.url)