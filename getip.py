
# 获取IP地址，只输出10.91开头的那个
import socket
def GetLocalIPByPrefix(prefix):
    """ 多网卡情况下，根据前缀获取IP（Windows 下适用） """
    localIP = ''
    for ip in socket.gethostbyname_ex(socket.gethostname())[2]:
        if ip.startswith(prefix):
            localIP = ip

    return localIP

print("                            ")
print(GetLocalIPByPrefix('10.91'))
print("                            ")
print("按回车键关闭")
input()
