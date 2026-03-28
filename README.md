# For Jeff                          

ForJeff is an automatic selenium voting bot that attempts to rig radio show contests by voting for Slayer, instead of whatever menial trash reaches the top40 these days.




## Todo

- Add VPN support using openpyn
- Add support for nonocaptcha



## Updates since original commit

### v0.1
- Added the initial song selector and slayer randomizer. It's not completely working yet but getting close
- Added the name generator

### v0.2
- Added email Generator
- Small scroll changes to make sure elements can be found
- Seems to be working up until captcha


## Concept

In order to avoid detection, certain additional steps need to be applied. They are as follows

1. Randomize position of 'the' vote between the other required votes
2. Randomized set of most common (real) names of 'voters'
3. Use disposable email addresses
4. If necessary: use rotating proxies to make ips change
5. Captcha avoidance?
