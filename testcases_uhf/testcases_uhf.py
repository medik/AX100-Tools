import sys

def gen_custom_msg(int_arr, delay):
    # int_arr is an array of integers from 0 to 256
    
    toSend = ""

    for i in int_arr:
        toSend += str(i) + " "

    return str(delay) + " 0 0 obckth tc " + toSend

def gen_ping(delay, size):
    return str(delay) + " 0 0 ping 1 1 " + str(size)

def main():
    #print("Generating testcases")
    
    n = int(sys.argv[1])
    interval = int(sys.argv[2])
    size = int(sys.argv[3])
    
    for i in range(n):
        print(gen_ping(interval, size))

if __name__ == "__main__":
    main()