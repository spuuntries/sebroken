<p align="center">
<b style="font-size:2em">An SEB file patcher.</b>
</br><img src="src/icons/config_icon.png" style="width:200px;">
</br><i>SEB Icon being "unlocked".</i>
</p>

# **What?**

`SEBroken` is a `.seb` file patcher, essentially, it allows you to modify certain parts of the file more easily.[^1]

## **What is an `SEB` file?**

SEB stands for [**Safe Exam Browser**](https://github.com/SafeExamBrowser).  
An SEB file is the configuration file for it, it has the extension of `.seb`.

The full file standard can be viewed [here](https://safeexambrowser.org/developer/seb-file-format.html), but basically, how a valid `.seb` file is created is by:

1. taking a [p-list](https://en.wikipedia.org/wiki/Property_list) XML file with the appropriate keys;
2. compressing the contents of it;
3. encrypting and prefixing it;
4. compressing it once more.

The `encryption` password is then used as the password that you enter to use the config file/enter the exam.

</br>

# **Why?**

<p style="font-size: .1em"><strike>My school</strike> <i>"A-certain-organization-that-I'm-currently-affiliated-with"</i> has announced that the standard that they are going to use for an upcoming <strike>final exams</strike> <i>"a competency examination"</i> is going to be changed from <b>Google Forms</b> to <b>Safe Exam Browser + Google Forms</b>.</p>  
*Cough* Why not :smile:

## **Wtf is that icon?**

`SEB + "Mind Broken" = SEBroken`, :pepega:

# **Running**
## **Simplified Instructions:**
Check out the advanced instructions (for development/linux) [here](#development).
### **1. Open the `.exe` file from [releases](releases/latest).**
You should now see the following:  
<img src="src/icons/running_ss.png" style="max-width: 500px; border-radius: 10px;">

### **2. Select the file you want to patch.** 
This ***has*** to be an [absolute path](https://www.computerhope.com/issues/ch001708.htm#windows).  
You can press the `Browse` button to open up a file selector.

### **3. Insert the exam password into the `password` field**
This is the encryption password, we won't be able to patch the file without it. 

### **4. (Optional) Insert a new admin password into the `authpassword` field**
If you're planning to do further modifications using the  configuration tool from SEB, you'll need to have access to the admin/quit password of the file.  
By default the password will be changed to `password`, but if you'd like, you could change it to anything else.  

By changing the configured hash, you'll be able to log in using the newly configured password.

----

#### **Additional notes**
In `Optional Arguments` you can change a few things to do more "advanced" patches.

----

</br>

# **Development**
> **NOTE: Launching via this method is not recommended, YMMV.**  
> There has been found multiple blocking installation issues with [Gooey](https://github.com/chriskiehl/Gooey), which is the library I used for GUI.  
> As such, if you do encounter any issues during installation, please do not consult me regarding it.   
</br>

When setting up the development environment, it's recommended to create a `virtualenv` first. This is to prevent dependency conflicts.  

Once you're booted into the `virtualenv`, install the requirements, and execute the `main.py` file to start up the GUI.  
(i.e. `python main.py`)


</br>

[^1]: Given that you know the `encryption` password, more info in [**here**](#what-is-an-seb-file).

----
### **For educators/teachers, AKA, an "FAQ":**
1. **This is intended for malicious purposes, isn't it?**  
Uh, *"no"*?  
A tool is a tool, how it's used is up to the wielder of the tool, I am not to be blamed if your students use this for malicious purposes.
2. **Okay, but what if they *do* use it for malicious purposes?**  
Well, for one, **"where there's a will, there's a way"**, this goes both ways, the proverb never mentions that that will has to be for good, nor bad.  
If your students are already coming into the exam with malintent, there really isn't much of anything that you can "do" to completely prevent it.
</br></br> 
Regardless, there *are* a few ways to "defend" against the use of this tool in your exams:  

    1. **Change the how you do your exams**  
    The exams that are "vulnerable" to this are exams that allow the use of, (a) individual devices; (b) manual loading of the SEB file.  
    To prevent "abuse" of this, all you need to really do is disallow/prevent any of those factors.  

    2. **Do a checksum check on the config file**  
    This is a slight bit more manual and "overkill" than the other method, but continuous monitoring really is the only "fool-proof" way to prevent abuse of tools like this.  
    Prior to entering SEB, check the hash of `.seb` file and compare it to your sample's, if they don't match then you can be certain that the file has been modified in some way or another.

</br>
<b style="font-size: 2em">"Where there's a will, there's a way."</b>