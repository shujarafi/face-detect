install python.
install pyserial from pip install pyserial
install tweepy from pip
install arduino ide

search google and do above installations.

connect arduino

servo red->5v
      brown->gnd
      orange->pin 9

connect arduino  pc

run arduino ide (load SerialCallResponseASCII.ino given in folder)
select board -> arduino/genuino Mega or Mega 2560
select tools->port as com6.....
get (com6 com5 etc) from port -> this is wanted

//////////////////////////////////////////////////////////////////////////////////

a.py contains scripts which perform actions when you pressed keys in keybord.
 CHANGE THE FILE CONTENT COM6 as your port which find before.if your port is also com6 there is nothing to change just run
run this after main installations comlplete as -> python a.py


pythonserver.py is restful api.you can run this -> python pythonServer.py
use curl to send http requset (check google)
if you send a get request after running this that means authorized one come.servo will rotate.
if you send a post (empty body or somthing in body ok) request that means unauthorized one come -> this send a tweet

example post request -> curl -X POST -F 'your_name=bla_bla' http://localhost:8081   (this should be fired if unauthorized one detected)
example get request -> curl http://localhost:8081 

if unknown person detected twwet to the account -> manpinpon@gmail.com  password -> myaccount
subcribe by your mobile dend sms as tweets.


api req c py 3 c

poddak inna


pythonserver.py is the file act as a server(restful).run this as 


