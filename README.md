#Runtime Configuration
This will easily create an Openshift diy-0.1 app with Python 3.5.1 & Django 1.9.7 & uWSGI using PostgresSQL for it's backend in only a few commands.

````shell
rhc create app -a <app_name> -t diy-0.1
cd app_name
````

The rhc tool doesn't always create the app folder for me and I've run into issues with it building now that I'm on an upgraded account. You can also make the DIY cartridge through the web, clone it to your local machine, and once you are in the git repo directory finish with the following commands. Also at this point before you use the following commands, you should add a PostgresSQL 9.2 cartridge to your cartridge. You can do that with the command below or through the web portal.

````shell
rhc cartridge add -c postgresql-9.2 -a <app-name>
git remote add upstream -m master git@github.com:CSUChico-CINS465/Openshift_DIY_Latest_Python3_and_Django.git
git pull -s recursive -X theirs upstream master
git push
````

And watch the scripts do their thing. This will take a while and will result in a ton of text in your terminal window. If you want to reduce this you can make the compilation of Python3.5.1 silent by changing the lines in the *.openshift/action_hooks/pre_build* script that say ***make install*** to instead read as follows, as this will pipe this output to */dev/null* instead of to the terminal:

````shell
make install > /dev/null
````

Once the scripts are done, you should have a running Django webserver that's singular home view will display the system python version at your cartridge's web address.

This code was cobbled together from openshift code examples found at the following sites:

* http://www.indjango.com/deploying-django-app-on-openshift/
* https://bitbucket.org/diy/openshift-diy-py27-django
* https://github.com/Praisebetoscience/openshift-cartridge-python-3.5
* http://stackoverflow.com/questions/26871381/deploying-a-local-django-app-using-openshift
