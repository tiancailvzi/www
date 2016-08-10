# ping from different server to one server at the same time

import os
ip_list = ["172.30.188.197","172.30.188.201","172.30.188.202","172.30.188.182"]

def ping_start():
        for ip in ip_list :
                scr_cmd = "screen -L -t 111 -dm bash -c 'ping -c 50000 -f 172.30.174.1'"
                cmd = 'sshpass -p 123456 ssh root@%s -o StrictHostKeyChecking=no "%s"' %(ip,scr_cmd)
                os.system(cmd)
                print (cmd)


ping_start()

"""
1) sshpass
  sshpass -p password ssh usrname@ip -o StrictHostKeyChecking=no
  后面可跟command 但要 “”包起来
2) screen
3) os.system(cmd) cmd为shell命令  
os.popen(command[, mode[, bufsize]])
  os.system(command)

2.os.popen() 功能强于os.system() 返回值 , os.popen() 可以返回回显的内容，以文件描述符返回。
eg:
t_f = os.popen ("ping 192.168.1.1")
print t_f.read()

或者:
for line in os.popen("dir"):
    print line
    
4)subprocess
  import subprocess
  从Python 2.4开始，Python引入subprocess模块来管理子进程，
  以取代一些旧模块的方法：如 os.system、os.spawn*、os.popen*、popen2.*、commands.*
  不但可以调用外部的命令作为子进程，而且可以连接到子进程的input/output/error管道，获取相关的返回信息
  subprocess.call() 像system.os()
  父进程等待子进程完成
  返回退出信息(returncode，相当于Linux exit code)
  subprocess.check_call()
  父进程等待子进程完成
  返回0
  检查退出信息，如果returncode不为0，则举出错误subprocess.CalledProcessError
  ，该对象包含有returncode属性，可用try…except…来检查
  subprocess.check_output()
  父进程等待子进程完成
  返回子进程向标准输出的输出结果
  
subprocess.Popen() #Popen is a class 
与上面的封装不同，Popen对象创建后，主程序不会自动等待子进程完成。我们必须调用对象的wait()方法，父进程才会等待 (也就是阻塞block)，
child = subprcess.Popen()
child.wait() # to make sure parent process wait after child excute
"""
