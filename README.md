# Background
One of my favourite video games of all time is the massively popular MMORPG, [Runescape](http://www.runescape.com/). It's an adventure game where you can control a character to do many different things in a virtual world. One of the things that makes Runescape so unique is the fact that it has a whole virtual currency which players use to purchase items in the game. Much like the economy in real life, prices of items in the game are determined by supply and demand. There is a place in the game known as the Grand Exchange, where players can look at prices of items and put in items for sale/buy items. Much like the trading floor in real life, the grand exchange is a hotspot of economical activity in game, as it is where the majority of the wealth in the game changes hands. 

# This Project
In this project, my goal is quantitatively build a financial model of the Runescape economy, and autonomously trade/sell items in the game with the intention to generate a large amount of in-game currency. While a game’s economy is different from the real stock market, many financial principles apply, and the main goal of this project is to 1) learn the basics of quantitive finance and adapt them, 2) to use my knowledge of data science to process the massive amount of data the Runescape API provides, and 3) to learn more about libraries that will allow me to create an AI that will not be banned by the game bot detection system. 

In this project, Python and R will be used to process the data. Python will be used to create the model. A pseudo-java(using auto-it) will be used to create the bot that actually implements the model.

# Accessing the Runescape API
The first step is to take the data from the runescape website. Because there are only several relevant things, there are steps necessary in order to sift through the data. After going through all the data on the api, I realised that much of the data available on the site was unavailable through the API. As such, it became necessary to write additional code to manually sift through the website to obtain additional data, like volume of trading and different qualifiers about items.

# Building the quantitative model
Building the model itself is the most challenging part of the project. This will involve a deep understanding of the game economy and how it differs from the real economy, as different factors will affect the price of different items, even if the historical data would not normally suggest so. Additionally, the model will need to be adjusted over time for game events/updates.

# Building an AI to play the game and automatically trade
After building a model, the AI will be made to automatically trade. Net profit and losses will be recorded and analysed to edit the model, and backtesting will also be implemented to verify the model.
 
