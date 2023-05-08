# Proccy-Clash
Simple project that enable to extract, study and handle the process running in you laptop. 
Permits operation as check memory, kill, gathering inlo, close groups of processes and blacklist and withelist a
variety of them.
It permits also some operations as open shells on the target laptop for more specific and jobs.

The project is just a 'have-fun' project. Im not trying to create a useful tool, a malware of any type. 
Im just having some fun studying what can I do with projects info. 

So don't use it in a bad way. Or, I mean. At least don't use that on me. Peace.  


## Setup
For a correct installation. Execute these commands.
```shell
python -m venv venv
source venv/Scripts/activate # on linux/macos change "Script" with "bin" with some versions
# venv/Scripts/activate on  windows
pip install -r requirements.txt
```

## Sections
The program is composed by various sections that permits you to navigate on the various functions.

### Extractor
Core of the program. It start the extraction of the existing processes and store them into a file 
```shell
$ python .\extractor.py <filename>  
```
The args following the function name are:
1. filename its not mandatory. In case of no file name it will be saved as p_temp_<date_hash>.json
2. after the execution the file will be located at res/in
3. filename of the process file. Must be specified without the extention (json default). 
4. Extracted processes will be stored into a json file in res/out folder as filename_result.json

### Visualizer 
Section used mostly for get the extracted process json and print it in a more precise way.
The initial Json produced from the extractor has typically a linear form as: 

| proc | #pid | #ppid | #domain | #username  | ...   |
|:----:|:----:|:-----:|:-------:|:----------:| :---: |
| mail | 301  |  283  | Unknown | ececchetti | ...   |

The Visualizer algorithm at first is able to extract it into a json array containing layered processes:
So from the first process (father) all the child processes nested inside. And the children of the children 
and so on...

Then after the algorithm process is possible to check the result.

Few different visualization are possible:
- --json : Print the process as raw json
- --table : Print the process as html table json

Its also possible to cleanup of the result, to store it locally or also mail the result to you google account.
(protecting it, encoding it or with a normal zip)
- --no-store: Drop the file at the end
- --store: Store the file at the end
- --mail: Zip and send by mail the extraction result
- --mail-protected: Zip and send result with result protected by psw

To add these features just add the string at the end of the instruction as:
```shell
$  python .\visualizer.py test_0 --mail
```

## Services
### Mailer
To setup this service we need to configure the smtp mail and psw.
So at first, enter the username of your mail google account account. At the moment is the only one supported.
To generate an application-specific password for your Google e-mail account, you can follow these steps:

Log in to your Google account
1. Select "Security" from the left-hand menu
2. Scroll down to the "Signing in to Google" section
3. Select "App passwords"
4. In the "Select app" drop-down menu, select "Mail"
5. In the "Select device" drop-down menu, select the appropriate device or "Other" if not listed
6. Click "Generate"
7. Copy the generated password and use it for SMTP authentication in your Python script.
Be sure not to share the generated password with others and use it only for SMTP authentication.
Token must be inserted in config/mail


## GUI
- nella cartella res/in/ ci metti il tuo file dei processi (ci sono altri file di esempio)
- vai sulla cartella con la console e usi il comando per runnare lo script:

```shell
    $ python .\main.py <json_processi>
```

 < json_processi> e' il nome del file dei processi che hai messo nelle res/in e non deve contenere l'estenzione. 

## TODO
- [ ] Hide/UnHide of the process table and children (with js scripts and a better table)
- [ ] Remove extension from filename when cal functions 
- [ ] Filter on extraction
- [ ] Filter on visualizer

## Input/Output and Folders
- All the print are done in the terminal. After it will be added a logger system also for the case where we need to 
store log results
- result of our calculation are stored in the res/out folder and data that we insert must me inserted in in folder. 
- For other specification check the help specific for the function you are using