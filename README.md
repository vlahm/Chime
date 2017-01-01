# **Chime**

### Set alarms and reminders from GNOME Terminal
### **Description**

Open a terminal window and call Chime with the
number of hours, minutes, and/or seconds to wait before it dings.
Optionally, set a reminder message.  The program can easily be made to work even
if you close its terminal.

### **Contents**
1. Requirements
2. Installation
3. Usage
  1. Basic (using `python` command from shell)
  2. Run from anywhere with alias
  3. Run from anywhere as daemon (independent of shell instance)
4.  Contact the author

---
### **1. Requirements**
Only works on Linux.  
Requires GNOME Terminal to be installed.  
Works with Python 2 or 3.

---
### **2. Installation**
All you need is: `pip install chime`

If for some reason that doesn't work (e.g. bell sound is not audible)...

1. Navigate to [https://github.com/vlahm/Chime/tree/master/Chime/dist](https://github.com/vlahm/Chime/tree/master/Chime/dist)
2. Right-click `chime-1.0.0.tar.gz` and save link to desired location.
3. Navigate to the folder where you saved the tarball, then execute:

  ```
  tar -xzvf chime-1.0.0.tar.gz  
  pip install chime-1.0.0/  
  ```
  (The slash is important in the above command.)

---
### **3. Usage**
Chime takes two arguments: a duration and an error message.  The duration is specified as a single string containing a number followed by ‘h’, ‘m’, or ‘s’, for ‘hours’, ‘minutes’, or ‘seconds’. You can also combine units, as in '1h20m3s'. The error message is a separate string, which is returned when the time is up.

#### 1. Basic (using `python` command from shell)
`python path/to/chime.py <duration> <reminder message>`  

Note that this usage may return benign error messages.
##### **_Examples:_**
`python chime.py 2m45s`  
`python ~/chime.py 1h5m 'get laundry'`
#### 2. Run from anywhere with alias
Add the following function to your `.bashrc` file:
```bash
function chime { 
    python path/to/chime.py $1 $2
}
```
Then execute from any terminal with, e.g. `chime 1h15m 'start dinner'`.
#### 3. Run from anywhere as daemon (disconnect from shell)
For full functionality (and suppression of potential noncritical error messages),
it is best to run Chime as a daemon process, which
places it in the "background" and allows you to close the terminal that
spawned it without terminating its process.

Add the following function to your `.bashrc` file.
You'll need to update the filepath for `chime.py`. You can put the output file
`nohup.py` in the same directory as `chime.py` or anywhere you like. Just note
that it's referred to twice in this function definition, and both will have to be
modified.
```bash
function chime { 
    nohup python example/path/chime.py $1 $2 > \
    example/path/nohup.out 2>/dev/null & disown $!
    sleep 1s
    tail --lines=1 example/path/nohup.out
}    
```
Then execute from any terminal with, e.g. `chime 1h15m 'start dinner'`.  
It will now be safe to exit the terminal.

---
### **4. Contact the author**
Mike Vlah: 
+ vlahm13@gmail[dot]com
+ [linkedin.com/in/michaelvlah](linkedin.com/in/michaelvlah)

