#Runtime Configuration
This will easily create an Openshift diy-0.1 app with Python 3.5.1 & Django 1.9.7 & uWSGI in only 5 commands.

````shell
rhc create app -a <app_name> -t diy-0.1
cd app_name
````
The rhc tool doesn't always create the app folder for me and I've run into issues with it building now that I'm on an upgraded account. You can also make the DIY cartridge through the web, clone it to your local machine, and once you are in the git repo directory finish with the following commands.

````shell
git remote add upstream -m master git@github.com:CSUChico-CINS465/OpenshiftPython3.5DjangoDIY.git
git pull -s recursive -X theirs upstream master
git push
````

And watch the scripts do their thing.
