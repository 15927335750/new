# Demo file for Spyder Tutorial

#FFFFFFFFFFFFFFFE0008FFFFFFF70006E00000000000C,long:32
#fffffffffffffffe0008fffffff70006e00000000000c

#收到的信息：fffffffffffffffe0008fffffff70044c0000007fff000c,从192.168.1.199,5000

#GetDlgItem(IDC_EDIT6)->GetWindowText(strShow);

#收到的信息：fffffffffffffffe0008fffffff70006e00000000000c,从192.168.1.199,5000

#FFFFFFFFFFFFFFFE000AFFFFFFF50044C000000FFFF00FFFF000E,long:36

#void CXMTServerPDlg::ChangIntToTwoChar(int tmpInt,unsigned char TmpChar[2])//将整形数据转化为4个Char类型的数据
import os
import sys
import threading
import time
import ctypes
from ctypes import *

FilePath = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(FilePath)

def sleep(mytime):
        time.sleep(mytime)
        print("SleepUseTime=%.3f"%mytime)
# Hans Fangohr, University of Southampton, UK
def hello():
    """Print "Hello World" and return None"""
    print("Hello World XMTDemonum-ymd%d"%20180920)
    
def SendVolt(ChannelDataInput,SendDataInput):#发送电压数据函数 通道 0 对应1路 1对应二路 2对应三路 
    comm_B3=0#开环 0 闭环 1
    comm_B4=0
    ChannelData = ChannelDataInput#0表示1路 1表示2路 2表示3路
    sendData=SendDataInput
    dll.XMT_COMMAND_SinglePoint.argtypes=[c_int,ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_double]  #定义传参类型
   # sendData = 5.7#发送数据值
    dll.XMT_COMMAND_SinglePoint.restype = ctypes.c_int
    dll.XMT_COMMAND_SinglePoint(ctypes.c_int(0),ctypes.c_int(1),ctypes.c_int(comm_B3),ctypes.c_int(comm_B4),ctypes.c_int(ChannelData),ctypes.c_double(sendData))#发送10v电压                                                 
   # print("第%d次:SendData=%f"%(i,sendData))  
   
def SendMove(ChannelDataInput,SendDataInput):#发送闭环数据函数 通道 0 对应1路 1对应二路 2对应三路 
    comm_B3=1#开环 0 闭环 1
    comm_B4=0
    ChannelData = ChannelDataInput#0表示1路 1表示2路 2表示3路
    sendData=SendDataInput
    dll.XMT_COMMAND_SinglePoint.argtypes=[c_int,ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_double]  #定义传参类型
   # sendData = 5.7#发送数据值
    dll.XMT_COMMAND_SinglePoint.restype = ctypes.c_int
    dll.XMT_COMMAND_SinglePoint(ctypes.c_int(0),ctypes.c_int(1),ctypes.c_int(comm_B3),ctypes.c_int(comm_B4),ctypes.c_int(ChannelData),ctypes.c_double(sendData))#发送10v电压                                                 
   # print("第%d次:SendData=%f"%(i,sendData))      
def ReadChannelVoltData(ChannelDataInput):#读取通道对应的开环数据
    #读取电压或位移数据值 需要加适当延时
    #XMT_COMMAND_ReadData(int usbDeviceNum,
    #	                unsigned char address,
    #					unsigned char Command_B3,
    #					unsigned char Command_B4,
    #					unsigned char Channel_Num
    #					);
    comm_B3=5#开环 5 闭环 6
    comm_B4=0
    ChannelData = ChannelDataInput#表示1路 1表示2路 2表示3路
    ReadData = -10.0
  #  print("初始值：ReadData=%d"%ReadData)
    dll.XMT_COMMAND_ReadData.restype = ctypes.c_double#转化为返回值浮点数
    ReadData = dll.XMT_COMMAND_ReadData(0,1,comm_B3,comm_B4,ChannelData)#发送10v电压
    return ReadData
   # print("发送数据值:%.4fV,读取的数据值:ReadData=%.4fV"%(sendData,ReadData))
   
def ReadChannelMoveData(ChannelDataInput):#读取通道对应的开环数据
    #读取电压或位移数据值 需要加适当延时
    #XMT_COMMAND_ReadData(int usbDeviceNum,
    #	                unsigned char address,
    #					unsigned char Command_B3,
    #					unsigned char Command_B4,
    #					unsigned char Channel_Num
    #					);
    comm_B3=6#开环 5 闭环 6
    comm_B4=0
    ChannelData = ChannelDataInput#表示1路 1表示2路 2表示3路
    ReadData = -10.0
  #  print("初始值：ReadData=%d"%ReadData)
    dll.XMT_COMMAND_ReadData.restype = ctypes.c_double#转化为返回值浮点数
    ReadData = dll.XMT_COMMAND_ReadData(0,1,comm_B3,comm_B4,ChannelData)#发送10v电压
    return ReadData
   # print("发送数据值:%.4fV,读取的数据值:ReadData=%.4fV"%(sendData,ReadData))
    
      
def SendVoltDataAndReadData(i):#发送电压数据同时读取电压数据 
    sendData = i;
    print("循环次数:%d"%i)
    comm_B3=0#开环 0 闭环 1
    comm_B4=0
    ChannelData = 0#0表示1路 1表示2路 2表示3路
    #发送数据为浮点数 声明下浮点数输出
    dll.XMT_COMMAND_SinglePoint.argtypes=[c_int,ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_double]  #定义传参类型
   # sendData = 5.7#发送数据值
    dll.XMT_COMMAND_SinglePoint.restype = ctypes.c_int
    dll.XMT_COMMAND_SinglePoint(c_int(0),ctypes.c_int(1),ctypes.c_int(comm_B3),ctypes.c_int(comm_B4),ctypes.c_int(ChannelData),ctypes.c_double(sendData))#发送10v电压                                                 
    print("第%d次:SendData=%f"%(i,sendData))
    
    print("call sleep")
    distime = 0.25
    sleep(distime)#sleep 5s
    print("sleep end distim=%f秒"%distime)
    comm_B3=5#开环 5 闭环 6
    comm_B4=0
    ChannelData = 0#表示1路 1表示2路 2表示3路
    ReadData = -10.0#发送数据值
    print("初始值：ReadData=%d"%ReadData)
    dll.XMT_COMMAND_ReadData.restype = ctypes.c_double#转化为返回值浮点数
    ReadData = dll.XMT_COMMAND_ReadData(0,1,comm_B3,comm_B4,ChannelData)#发送10v电压
    print("第:%d次,发送数据值:%.4fV,读取的数据值:ReadData=%.4fV"%(i,sendData,ReadData))
    
def SendDataMoveAndReadData(i):#发送位移数据同时读取位移数据 
    sendData = i;
    print("循环次数:%d"%i)
    comm_B3=1#开环 0 闭环 1
    comm_B4=0
    ChannelData = 0#0表示1路 1表示2路 2表示3路
    #发送数据为浮点数 声明下浮点数输出
    dll.XMT_COMMAND_SinglePoint.argtypes=[c_int,ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_double]  #定义传参类型
   # sendData = 5.7#发送数据值
    #dll.XMT_COMMAND_SinglePoint.restype = ctypes.c_int
    dll.XMT_COMMAND_SinglePoint(ctypes.c_int(0),ctypes.c_int(1),ctypes.c_int(comm_B3),ctypes.c_int(comm_B4),ctypes.c_int(ChannelData),ctypes.c_double(sendData))#发送10v电压                                                 
    print("第%d次:SendData=%f"%(i,sendData))
    
    print("call sleep")
    distime = 0.25
    sleep(distime)#sleep 5s
    print("sleep end distim=%f秒"%distime)
    comm_B3=6#开环 5 闭环 6
    comm_B4=0
    ChannelData = 0#表示1路 1表示2路 2表示3路
    ReadData = -10.0#发送数据值
    print("初始值：ReadData=%d"%ReadData)
    dll.XMT_COMMAND_ReadData.restype = ctypes.c_double#转化为返回值浮点数
    ReadData = dll.XMT_COMMAND_ReadData(0,1,comm_B3,comm_B4,ChannelData)#发送10v电压
    print("第:%d次,发送数据值:%.4fV,读取的数据值:ReadData=%.4fV"%(i,sendData,ReadData))
   
def SendThreeDataVolt(VoltOrMove_Data_0,VoltOrMove_Data_1,VoltOrMove_Data_2):   #同时发送三路电压数据 
    #//do 多路单点类 2 3  同时发送三路数据
    # DLL_XMT_USB_API   unsigned char XMT_COMMAND_MultSinglePoint(int usbDeviceNum,
    #	                unsigned char address,
    #					unsigned char Command_B3,
    #					unsigned char Command_B4,
    #					double VoltOrMove_Data_0,
    #					double VoltOrMove_Data_1,
    #					double VoltOrMove_Data_2
    #					);
    comm_B3 = 2#2是电压 3 是位移命令
    comm_B4 = 0
    sendData = VoltOrMove_Data_0
    sendData_2 = VoltOrMove_Data_1
    sendData_3 = VoltOrMove_Data_2
    dll.XMT_COMMAND_MultSinglePoint.argtypes=[ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_double,ctypes.c_double,ctypes.c_double]  #定义传参类型
    #dll.XMT_COMMAND_MultSinglePoint.restype = ctypes.c_int
    dll.XMT_COMMAND_MultSinglePoint(ctypes.c_int(0),ctypes.c_int(1),ctypes.c_int(comm_B3),ctypes.c_int(comm_B4),ctypes.c_double(sendData),ctypes.c_double(sendData_2),ctypes.c_double(sendData_3))
def SendThreeDataMove(VoltOrMove_Data_0,VoltOrMove_Data_1,VoltOrMove_Data_2):   #同时发送三路电压数据 
    #//do 多路单点类 2 3  同时发送三路数据
    # DLL_XMT_USB_API   unsigned char XMT_COMMAND_MultSinglePoint(int usbDeviceNum,
    #	                unsigned char address,
    #					unsigned char Command_B3,
    #					unsigned char Command_B4,
    #					double VoltOrMove_Data_0,
    #					double VoltOrMove_Data_1,
    #					double VoltOrMove_Data_2
    #					);
    comm_B3 = 3#2是电压 3 是位移命令
    comm_B4 = 0
    sendData = VoltOrMove_Data_0
    sendData_2 = VoltOrMove_Data_1
    sendData_3 = VoltOrMove_Data_2
    dll.XMT_COMMAND_MultSinglePoint.argtypes=[ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_double,ctypes.c_double,ctypes.c_double]  #定义传参类型
    #dll.XMT_COMMAND_MultSinglePoint.restype = ctypes.c_double
    dll.XMT_COMMAND_MultSinglePoint(ctypes.c_int(0),ctypes.c_int(1),ctypes.c_int(comm_B3),ctypes.c_int(comm_B4),ctypes.c_double(sendData),ctypes.c_double(sendData_2),ctypes.c_double(sendData_3))
####################################
#引导Dll 开始扫描设备 开启usb设备 发送ABC数据通过usb 


def fun_timer():
    global timer
    global exec_count
    print("Hello Timer!-%d"%exec_count)
    exec_count += 1
    # 15秒后停止定时器
    
    sendData = exec_count
    comm_B3=0#开环 0 闭环 1
    comm_B4=0
    ChannelData = 0#0表示1路 1表示2路 2表示3路
    #发送数据为浮点数 声明下浮点数输出
    dll.XMT_COMMAND_SinglePoint.argtypes=[c_int,ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_double]  #定义传参类型
    #dll.XMT_COMMAND_SinglePoint.restype = ctypes.c_double
    dll.XMT_COMMAND_SinglePoint(ctypes.c_int(0),ctypes.c_int(1),ctypes.c_int(comm_B3),ctypes.c_int(comm_B4),ctypes.c_int(ChannelData),ctypes.c_double(sendData))#发送10v电压                                                 


    if exec_count < 8:
        timer = threading.Timer(1, fun_timer)
        timer.start()
        

dll = ctypes.cdll.LoadLibrary('XMT_DLL_USB.dll')
#dll = cdll.LoadLibrary('P:\\labPython\\untitled1\\XMT_DLL_USB.dll')
#dll = cdll.LoadLibrary('XMT_DLL_USB.dll')
#dll = cdll.LoadLibrary('XMTDLLT.dll')
ret = dll.add(2, 4)
wt = 20
num=6    
print("Hello World XMTDemoret=%d"%ret)

#from ctypes import * 
#fileName="XMT_DLL_USB.dll" 
#func=cdll.LoadLibrary(fileName) 
#str = create_string_buffer(20) 
#n = func.add(2, 4);
#func.GetString(str) 

#print n 
#print str.raw 


#XMT_COMMAND_SinglePoint(int usbDeviceNum,
#	                unsigned char address,
#					unsigned char Command_B3,
#					unsigned char Command_B4,
#					unsigned char Channel_Num,
	#				double VoltOrMove_Data
#					); //
# i = ScanUsbDevice();//表示连接的usb的设备个数 为下一步连接usb做准备 
    


    
numDeviceusb=-1;
print("usbs设备初始数据:numDeviceusb=%d"%numDeviceusb)
numDeviceusb = dll.ScanUsbDevice();#//表示连接的usb的设备个数 为下一步连接usb做准备   
print("扫描usb设备数量:numDeviceusb=%d"%numDeviceusb)

tmpStateOfUsbDevie   = -1;
print("tmpStateOfUsbDevie=%d"%tmpStateOfUsbDevie )
tmpStateOfUsbDevie = dll.OpenUsbPython(numDeviceusb-1);#usb设备从0开始，需要usb设备数目减一；
print("tmpStateOfUsbDevie=%d"%tmpStateOfUsbDevie )

dll.SendABC(numDeviceusb-1);#发送测试

#########################
#定时器开启
exec_count = 0
timer = threading.Timer(1, fun_timer)
timer.start()


sendData = 0;
comm_B3=0#开环 0 闭环 1
comm_B4=0
ChannelData = 0#0表示1路 1表示2路 2表示3路
#发送数据为浮点数 声明下浮点数输出
dll.XMT_COMMAND_SinglePoint.argtypes=[c_int,ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_double]  #定义传参类型
sendData = 5.7#发送数据值
#dll.XMT_COMMAND_SinglePoint.restype = ctypes.c_double
dll.XMT_COMMAND_SinglePoint(ctypes.c_int(0),ctypes.c_int(1),ctypes.c_int(comm_B3),ctypes.c_int(comm_B4),ctypes.c_int(ChannelData),ctypes.c_double(sendData)) #发送10v电压                                                 
print("第一次:SendData=%f"%sendData)

print("call sleep")
distime = 0.5
sleep(distime)#sleep 0.5s
print("sleep end distime=%f秒"%distime)
comm_B3=5#开环 5 闭环 6
comm_B4=0
ChannelData = 0#0表示1路 1表示2路 2表示3路
ReadData = -10.0#发送数据值
print("初始值：ReadData=%d"%ReadData)
dll.XMT_COMMAND_ReadData.restype = ctypes.c_double#转化为返回值浮点数
ReadData = dll.XMT_COMMAND_ReadData(0,1,comm_B3,comm_B4,ChannelData)#发送10v电压
print("发送数据值:%.4fV,读取的数据值:ReadData=%.4fV"%(sendData,ReadData))

comm_B3=0#开环 0 闭环 1
comm_B4=0
ChannelData = 0#0表示1路 1表示2路 2表示3路
sendData =10.3;
dll.XMT_COMMAND_SinglePoint(ctypes.c_int(0),ctypes.c_int(1),ctypes.c_int(comm_B3),ctypes.c_int(comm_B4),ctypes.c_int(ChannelData),ctypes.c_double(sendData))#发送10v电压
print("第二次:SendData=%f"%sendData)


#读取电压或位移数据值 需要加适当延时
#XMT_COMMAND_ReadData(int usbDeviceNum,
#	                unsigned char address,
#					unsigned char Command_B3,
#					unsigned char Command_B4,
#					unsigned char Channel_Num
#					);
print("call sleep2")
distime = 0.5
sleep(distime)#sleep 5s
print("sleep end distim2=%f秒"%distime)


comm_B3=5#开环 5 闭环 6
comm_B4=0
ChannelData = 0#表示1路 1表示2路 2表示3路
ReadData = -10.0
print("初始值：ReadData=%d"%ReadData)
dll.XMT_COMMAND_ReadData.restype = ctypes.c_double#转化为返回值浮点数
ReadData = dll.XMT_COMMAND_ReadData(0,1,comm_B3,comm_B4,ChannelData)#发送10v电压
print("发送数据值:%.4fV,读取的数据值:ReadData=%.4fV"%(sendData,ReadData))


for i in range(0,2):
    SendVoltDataAndReadData(i)  
for j in range(0,2):
    SendVoltDataAndReadData(9-j)
     
#while(w<10):
#    SendVoltDataAndReadData(w)
#    print("发送数据值-while:%.4fV"%w)
#    w = w+1
    
    

    
 ####################################
#分散的读取数据   
ChannelDataInput = 0
SendDataInput = 0
RWData = -1
w=0
U=0
while(U<2):
      U= U + 1
      w = 0
      while(w<2):
         SendDataInput = w
         SendVolt(ChannelDataInput,SendDataInput)#发送电压数据函数 通道 0 对应1路 1对应二路 2对应三路
         #print("发送数据值-while:%.4fV"%w)
         #延时一定时间
         whTime=0.5
         sleep(whTime)
         #读取开环数据
         RWData = ReadChannelVoltData(ChannelDataInput)#读取通道对应的开环数据
         print("发送数据值-while:%.4fV,读取数据值%.4f"%(w,RWData))
         w = w+1
      print("发送数据值-whileU:%d"%(U))
SendDataInput = 0
SendVolt(ChannelDataInput,SendDataInput)#发送电压数据函数 通道 0 对应1路 1对应二路 2对应三路 
print("发送数据值-whileEnd:%.4fV"%SendDataInput) 
   
##########################################
#三路同时发送数据    
#    VoltOrMove_Data_0 = i
#    VoltOrMove_Data_1 = i
#    VoltOrMove_Data_2 = i
#    SendThreeDataVolt(VoltOrMove_Data_0,VoltOrMove_Data_1,VoltOrMove_Data_2)

   
hello()

























