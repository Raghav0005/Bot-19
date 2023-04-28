# Bot-19
Hack the North 2021 Project

## Pictures
<img width="880" alt="Screen Shot 2023-02-19 at 12 04 23 PM" src="https://user-images.githubusercontent.com/58956834/219963165-9b627c8b-b7ca-4721-a191-09e5f9cf4ee0.png">

<img width="482" alt="Screen Shot 2023-02-19 at 12 08 15 PM" src="https://user-images.githubusercontent.com/58956834/219963279-b907e303-5e16-4432-8fef-f6aca7ad5ab9.png">

<img width="471" alt="Screen Shot 2023-02-19 at 12 09 19 PM" src="https://user-images.githubusercontent.com/58956834/219963402-acdca49e-e13b-44f8-b9db-cfb2fca0a658.png">

## Inspiration
COVID-19 has rapidly affected our day to day life, businesses, and also disrupted the world trade and movements. With such a drastic pause in our lives, we wanted to provide an easy to access COVID-19 data according to the user's needs, Covid-19 screening, new/headlines, facts, etc. for our discord users. Conducting searches on a web browser can be inconvenient and costs time. Thus, we wanted to create something that could provide important information fast without the need of opening a web-browser or visiting another hard-to-use statistical website. BOT-19 was designed to provide exactly that - fast and accurate information on the fly with simple commands. This discord bot uses APIs for COVID-19 statistics as well as news sources to extract data without requiring the user to visit these sites.

## What It Does
 BOT-19 provides a range of data: COVID-19 statistics for the entire world, for specific countries, or even specific Canadian provinces. In addition, it has a news/headline command that provides headline news on any topic of the user's choice, with or without relation to COVID-19. On top of that, the bot can also visualize COVID-19 data with a daily self-updating graph for easier communication. Furthermore, the bot can perform COVID-19 screening (with the help of the Ontario Ministry of Health guidelines) through interactive questions and answers.

## How We Built It
To perform such operations, an internal sophisticated language was our priority. Thus, we predominantly used the Python language/framework and its libraries to create Bot-19. This involved obtaining public API data sets and performing operations on them to convert them to JSON objects, that provides us readable data structures such as dictionaries and lists. Specifically, we used Postman's Covid-19 APIs and "newsapi.io" for fetching news/headlines relevant to the user's needs. We then implemented numerous commands to provide users with their desired information. Furthermore, the implementation of the Pandas and Madplotlib libraries in Python helped plot Covid-19 cases of selected countries in a visual format, with an API and data set that refreshes daily.

## Challenges We Ran Into
Initially, we worked together to understand the processes of JSON requests in Python and how to obtain data from APIs. With some determination and dedication and external research, we were successfully able to implement APIs into our code to be able to retrieve our desired data as per the user's request. Another challenge was regarding incorporating the graph into an Embed structure for an output to the user. Mutual collaboration and experimentation helped solve that problem.

## Accomplishments We Are Proud Of
We are proud of creating a project that allows an individual to educate themselves and know about the current events. Since COVID-19 has changed our whole lives, we believe it is eminently important for people to be updated with the information regarding COVID-19 so that they are able to observe possible trends, which will allow them to also take extra precautions. We built this bot with a multitude of features so that everyone is able to benefit from it, and learn something new. We are also proud of implementing technologies we had limited knowledge of, including APIs and different libraries.

## What We Learned
We learned about the use of APIs and how to effectively incorporate them with the use of different libraries such as the MATPLOTLIB for creating a live graph, while also practicing data implementation in the Python language. We also investigated different features of discord applications and how to create a bot application through a coding language we are familiar with.

## Future Aspirations
Firstly, we would like to expand our news database so we cover a wider range of topics. We want to create a more friendly user interface, and transition screening into a DM chat instead of in-server, while also developing more functions. Some examples include providing comparisons of different statistics. Moreover, we can also add a live graph for each of the countries showing their trends which will help the user visualize it better. Finally, we would like to host our discord bot, to allow for users to be able to use the bot in their own server.

## Technologies Used
- Python
- JSON
- Matplotlib
- REST API
- Pandas
- Discord.py
