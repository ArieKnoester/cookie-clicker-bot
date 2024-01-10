# cookie-clicker-bot

## Description:
A bot powered by selenium web driver which interacts with a Cookie Clicker game. The bot runs for
5 minutes and checks if any 'Buildings' and 'Upgrades' are available for purchase every 5 seconds. 
At the end of 5 minutes the number of cookies per second is printed to the console. 

### Notes
My naive approach is to always purchase the highest tier building available, since the higher tier
buildings give more cookies per second than lower tiers. If an upgrade is available, always purchase
the upgrade over a building. With this approach, an upgrade will only be purchased if it is cheaper
than a building. This is not likely the most effective algorithm to maximize the number of cookies 
per second within a 5-minute runtime, however purchasing the first available 'Cursor' upgrade when this
condition was met almost doubled the cookies per second in my tests.
