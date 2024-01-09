# cookie-clicker-bot

Work in progress.

## Description:
A bot powered by selenium web driver which interacts with a Cookie Clicker game. The bot runs for
5 minutes and checks if any 'Buildings' are available for purchase every 5 seconds. At the end of 
5 minutes the number of cookies per second is printed to the console. 

### Notes
- My naive approach is to always purchase the highest tier building available, since the higher tier
buildings give more cookies per second than lower tiers.

#### To Do:
- Access the 'Upgrades' section and if one is available for purchase, always purchase an upgrade
over an building.