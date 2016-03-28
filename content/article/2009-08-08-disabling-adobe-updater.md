Title: Disabling adobe updater
Date: 2009-08-08 16:44
Author: Mukesh
Category: uncategorized
Slug: disabling-adobe-updater
Status: published

I love adobes photoshop, Deamvear and Acrobat reader and other
application which are as great as these, but one thing I dont like about
adobe that they start there auto update as soon you start there
application. and also there updater is resource hungry.

Being in India where Bandwidth is very precious, and where you get
charge on the usage of your bandwidth [ and I have very less  Download
limit :(  but good speed :) ], so when I started Acrobat reader to read
a document,  I dint notice that adobe updater also auto started. Due to
this I lost my precious download limit and then I decided to remove the
auto update.

After Googling  Little  I found the solution for this. here is a
solution for this.

> ##### **Turn off automatic updates on Windows OS** {#head1}
>
> If your computer is connected to the internet, then you can change the
> Adobe Updater preferences to not check for updates.
>
> To Change the Adobe Updater preferences, do the following:
>
> 1.  Start the AdobeUpdater.exe application from ...\\Program
>     Files\\Common Files\\Adobe\\Updater 5
> 2.  When the update screen appears, click the Preferences button
> 3.  Uncheck the Automatically Check for updates checkbox and click OK
>
> If your computer does not have an internet connection, then you can
> manually edit the AdobeUpdaterPreferences.dat file.
>
> To manually edit the AdobeUpdaterPreferences.dat file, do the
> following:
>
> 1.  Start the AdobeUpdater.exe application from ...\\Program
>     Files\\Common Files\\Adobe\\Updater 5
> 2.  When the Adobe Updater dialog appears stating that there is no
>     Internet connection, click Cancel
> 3.  Navigate to ...\\Documents and Settings\\[username]\\Local
>     Settings\\Application Data\\Adobe\\Updater5 on Windows XP or
>     ...\\[username]\\AppData\\Local\\Adobe\\Updater5 on Vista and open
>     AdobeUpdaterPrefs.dat in Notepad.
> 4.  If the *\<AutoCheck\>1\</AutoCheck\>* tag already exists, then
>     change the value from 1 to 0. Otherwise, add the line
>     *\<AutoCheck\>0\</AutoCheck\>* anywhere between the
>     *\<AdobeUpdater\>\</AdobeUpdater\>* tags.
> 5.  Close and save the AdobeUpdaterPrefs.dat file

and  [here](http://kb2.adobe.com/cps/402/kb402251.html) is a original
post from adobe  :) .
