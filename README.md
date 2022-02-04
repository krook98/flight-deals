# General info
Send your friends notifcations with best flight prices they desire!

### API Used
I use Sheety API to save data to Google Sheets document (https://sheety.co/)  
For searching flights I use Tequila API (https://tequila.kiwi.com/portal/docs/tequila_api/search_api)

### Technology
Python 3.9.10  
Google Sheets

### Setup
To run this project you might need your own API keys. Google, Sheety and Kiwi accounts are neccessary.    

### Launch
Firstly, you need to add your own API keys, emails, origin city. You set environment variables in terminal with:  <br/><br/>
`export 'YOUR_ENV_VAR_NAME'=value`  <br/><br/>
Then you can access it in code with:  <br/><br/>
`os.environ.get('YOU_ENV_VAR_NAME')`  <br/><br/>
Run app with:  <br/><br/>
`python3 main.py` 

