#!/usr/bin/python3

def main():
    mylist = []

    mylist.append("192.168.102.55")
    
    mylist.append("10.10.0.1")
    print(mylist)

    myotherlist = []
    
    myotherlist.extend("abcdefg")
    print(myotherlist)

    mylastlist = ["192.168.0.1", "8.8.8.8"]

    mylastlist.extend(["9.9.9.9", "4.4.4.4"])

    print(mylastlist)

if __name__ == "__main__":
    main()


