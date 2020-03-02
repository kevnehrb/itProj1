import socket as mysoc







try:
    cs=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
    print("[C]: Client socket created")
except mysoc.error as err:
    print('{} \n'.format("socket open error ", err))
