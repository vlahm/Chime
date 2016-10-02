# **IN PROGRESS**

# **Chime**

### Set alarms and reminders from GNOME Terminal
### **Description**

Open a terminal window and call Chime with the
number of hours, minutes, and/or seconds to wait before it dings.
Optionally, set a reminder message.  The program can be made to work even
if you close its terminal, though it will be cancelled if you log off or
shut down your computer.

### **Contents**
1. Installation
  1. Standard installation
  2. Conda installation (recommended)
2. How to use
  1. Basic (using `python` command from shell)
  2. Run from anywhere with alias
  3. Run from anywhere as daemon (independent of shell instance)
3.  Additional notes
4.  Contact the author

---
### **1. Installation**
#### 1. Standard installation


---
### **2. How to use**
#### 1. Basic (using `python` command from shell)
`python path/to/chime.py 
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
For full functionality, it is best to run Chime as a daemon process, which
places it in the "background" and allows you to close the terminal that
spawned it without terminating its process.

Add the following function to your `.bashrc` file.
You'll need to update the filepath for `chime.py`. You can put the output file
`nohup.py` in the same directory as `chime.py` or anywhere you like. Just note
that it's referred to twice in this function definition.
```bash
function chime { 
    nohup python example/path/chime.py $1 $2 > \
    example/path/nohup.out 2>/dev/null & disown $!
    sleep 1s
    tail --lines=1 example/path/nohup.out
}    
```
Then execute from any terminal with, e.g. `chime 1h15m 'start dinner'`.

---
### **7. Contact the author**
Mike Vlah: 
+ vlahm13@gmail[dot]com
+ [linkedin.com/in/michaelvlah](linkedin.com/in/michaelvlah)
