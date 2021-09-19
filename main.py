import discord
import os
import time
import asyncio
import io
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure, check
import random
from datetime import datetime
import requests

# Other python files:
import graph

#^ basic imports for other features of discord.py and python ^

client = discord.Client()

client = commands.Bot(command_prefix='/')  #put your own prefix here


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Activity(
                                     type=discord.ActivityType.listening,
                                     name="\"Six Feet Apart\" by Luke Combs"))
    print("Bot is ready."
          )  #will print "bot online" in the console when the bot is online


@client.command()
async def hello(ctx):
    randomANS = [
        "Hey", "Nice to meet you", "Hello!", "Ola!", "Hi there!", "What's up?",
        "How is it going?", "Woah! Hello!"
        "Wassup Homie?", "How are you?", "It's a pleasure to assist you",
        "Howdy!", "G'day!", "What's new?"
    ]
    text = randomANS[random.randint(0, len(randomANS) - 1)]
    await ctx.send(text)


@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def graph(ctx):  # world stats, will work on other ones after this
    embed = discord.Embed(title="World Comparitive Statistics Graph",
                          color=0x552E12)

    g = discord.File("img.jpg")
    embed.set_image(url="attachment://img.jpg")

    await ctx.send(embed=embed, file=g)

@client.command()
async def facts(ctx):
    facts = [
        "Coronavirus can make babies seriously ill.",
        "People with type A blood may be more susceptible to infection.",
        "Some people with COVID-19 have digestive symptoms.",
        "Vaccination is very effective in preventing severe COVID-19.",
        "Most people who get COVID-19 will have a mild form of the illness and will be able to recover at home, without needing hospital treatment.",
        "People with underlying medical conditions (such as heart conditions or stroke) and associated risk factors are at higher risk of serious complications from COVID-19.",
        "Despite some reports, there is no scientific evidence to suggest that heart medications may increase your risk of COVID-19.",
        "Preventing heart conditions and stroke and managing your health is more critical than ever.",
        "Physical distancing does not mean social isolation.",
        "The novel coronavirus is SARS-CoV-2 and the disease is COVID-19.",
        "The first cases in the United States were mainly in people who traveled from China.",
        "The novel coronavirus spreads very easily from person to person.",
        " Social distancing and wearing a mask helps slow the spread of infection.",
        "COVID-19 symptoms range from mild to severe and it can be fatal.",
        "COVID-19 treatment includes FDA-approved antivirals and antibodies.",
        "There are three authorized COVID-19 vaccines.",
        "The source of the novel coronavirus is linked to animals.",
        "Coronavirus is a family of viruses, which can cause the common cold or more severe diseases such as severe acute respiratory syndrome, Middle East respiratory syndrome, and the coronavirus disease, COVID-19."
    ]
    # create new embed element
    embed = discord.Embed(title="COVID-19 Facts 😷", color=0x552E12)
    image_url = [
        "https://www.gov.mb.ca/asset_library/en/restartmb/covid-19-header.jpg",
        "https://www.un.org/sites/un2.un.org/files/covid19_response_logo_with_un_emblem_horizontal_april_2020.png",
        "https://moffitt.org/media/13017/covid-19-banner.jpg"
    ]

    rand_img = image_url[random.randint(0, len(image_url) - 1)]

    embed.set_image(url=rand_img)

    embed.add_field(name="Did you know?",
                    value=facts[random.randint(0,
                                               len(facts) - 1)],
                    inline=True)

    await ctx.send(embed=embed)


@client.command()
async def fastscreen(ctx):
    selfAssessmentQuestions = {
        "Are you fully vaccinated against Covid-19 or have been tested positive for Covid-19 and since been cleared in the last 90 days?":
        "Yes",
        "Do you feel any of these symptoms?     \
         \n- Sore throat \
         \n- Fever \
         \n- Dry cough \
         \n- Loss of taste or smell \
         \n- Headache":
        "No",
        "In the past 14 days, have you been in contact with anyone known to have previous exposure to Covid-19 (including friends and family)?":
        "No",
        "In the past 14 days, have you travelled outside  of Canada or been in contact with someone who has?\nAnd, have either you or the traveller you had contact with been directed to quarantine by CBSA/PHAC on your return to Canada?":
        "No"
    }

    notSafe = 0
    for question in selfAssessmentQuestions:
        msg1 = await ctx.send(question)
        # custom_emoji = get(ctx.message.server.emojis, name="custom_emoji")

        reaction, user = await client.wait_for('reaction_add', timeout=60.0)
        await ctx.send("You responded with {}".format(reaction.emoji))

        response = ""
        # Conditionals here:
        if str(reaction.emoji) == '👍':
            response = "Yes"
        elif str(reaction.emoji) == '👎':
            response = "No"
        else:
            await ctx.send(
                "You have reacted with an invalid emoii. This self-screen is no longer 😔valid. Please try again."
            )
            notSafe = -1
            break

        if response != selfAssessmentQuestions[question]:
            notSafe += 1

    if notSafe > 0:
        await ctx.send(
            "Based on your responses, you are showing symptoms of possibly having Covid-19. Please stay home today, isolate yourelf and contact a medical proffessional. Take care of yourself!"
        )
    elif notSafe == 0:
        await ctx.send(
            "Based on your answers, you are most likely are safe from Covid-19. However, remember to wear your mask, sanitize yourself and wash your hand consistently throughout your day. Have a great one!"
        )


@client.command()
async def stats(ctx, country="Canada"):
    url = "https://api.covid19api.com/summary"

    response = requests.get(url)
    final = response.json()

    image_urls = [
        "https://thumbs.dreamstime.com/b/covid-all-together-word-cloud-image-many-images-words-covid-all-together-word-cloud-image-182882717.jpg",
        "https://thumbs.dreamstime.com/b/covid-all-together-word-cloud-image-many-images-words-covid-all-together-word-cloud-image-182882723.jpg",
        "https://thumbs.dreamstime.com/b/covid-word-cloud-white-background-178214349.jpg",
        "https://healix.com/wp-content/uploads/2020/03/virus-4835301_1920-banner.jpg",
        "https://static.vecteezy.com/system/resources/previews/001/060/056/non_2x/covid-19-coronavirus-disease-banner-vector.jpg",
        "https://unicarechc.org/wp-content/uploads/2020/11/banner4.jpg",
        "https://thumbs.dreamstime.com/z/coronavirus-banner-background-copyspace-covid-epidemic-concept-vector-d-abstract-viruses-illustration-horizontal-blue-178235279.jpg",
        "https://thumbs.dreamstime.com/z/coronavirus-banner-background-copyspace-covid-epidemic-concept-vector-d-abstract-viruses-illustration-infection-horizontal-178730278.jpg"
    ]

    if (len(country) == 2):
        countrycode = country.upper()
        for set1 in final["Countries"]:
            if set1["CountryCode"] == countrycode:
                embed = discord.Embed(title=set1["Country"] + " Stats",
                                      color=0x552E12)
                embed.set_image(url=image_urls[random.randint(0, 3)])
                embed.add_field(name="Country",
                                value=set1["Country"],
                                inline=True)
                embed.add_field(name="Country Code",
                                value=set1["CountryCode"],
                                inline=True)
                embed.add_field(name="New Confirmed",
                                value=set1["NewConfirmed"],
                                inline=True)
                embed.add_field(name="Total Confirmed",
                                value=set1["TotalConfirmed"],
                                inline=True)
                embed.add_field(name="New Deaths",
                                value=set1["NewDeaths"],
                                inline=True)
                embed.add_field(name="Total Deaths",
                                value=set1["TotalDeaths"],
                                inline=True)
                embed.add_field(name="New Recovered",
                                value=set1["NewRecovered"],
                                inline=True)
                embed.add_field(name="Total Recovered",
                                value=set1["TotalRecovered"],
                                inline=True)
                await ctx.send(embed=embed)
    else:
        country = country.title()
        for set1 in final["Countries"]:
            if set1["Country"] == country:
                embed = discord.Embed(title=set1["Country"] + " Stats",
                                      color=0x552E12)
                embed.set_image(url=image_urls[random.randint(0, 3)])
                embed.add_field(name="Country",
                                value=set1["Country"],
                                inline=True)
                embed.add_field(name="Country Code",
                                value=set1["CountryCode"],
                                inline=True)
                embed.add_field(name="New Confirmed",
                                value=set1["NewConfirmed"],
                                inline=True)
                embed.add_field(name="Total Confirmed",
                                value=set1["TotalConfirmed"],
                                inline=True)
                embed.add_field(name="New Deaths",
                                value=set1["NewDeaths"],
                                inline=True)
                embed.add_field(name="Total Deaths",
                                value=set1["TotalDeaths"],
                                inline=True)
                embed.add_field(name="New Recovered",
                                value=set1["NewRecovered"],
                                inline=True)
                embed.add_field(name="Total Recovered",
                                value=set1["TotalRecovered"],
                                inline=True)
                await ctx.send(embed=embed)


@client.command()
async def prov(ctx, province="Ontario"):
    province = province.title()
    url = "https://api.covid19api.com/live/country/canada"
    response = requests.get(url)
    final = response.json()
    today = datetime.today().strftime('%Y-%m-%d')

    temp = []
    image_urls = [
        "https://www.acfcs.org/wp-content/uploads/2020/03/Virus-Roundup-One-Red-Horizontal-final-March-2020-1024x314.jpg",
        "https://www.actratoronto.com/wp-content/uploads/2021/04/HANDS-FACE-SPACE_040121.png",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4H6EW_Ovdk-w_oQ8rvfmen1Xl9mjHxlyo9SDgtTYmTXYxD3E59Z_HMT4MWHFUsRzVQ6s&usqp=CAU",
        "https://img.freepik.com/free-vector/covid-19-coronavirus-outbreak-banner-with-virus-cells_1017-24631.jpg?size=626&ext=jpg",
        "https://img.freepik.com/free-vector/covid-19-coronavirus-banner-with-virus-cells-design_1017-24549.jpg?size=626&ext=jpg",
        "https://cupe.ca/sites/cupe/files/node_representative_image/covid-19_image_final.jpg",
        "https://image.freepik.com/free-vector/coronavirus-cells-banner_1035-18753.jpg",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTnudcWDuxYGKFMgs58wGXqQtZ7OMHA1CEHr2G9xIGR3ptsKOrdZHT5EjpsHHBFjkpbjhk&usqp=CAU",
        "https://images.squarespace-cdn.com/content/v1/57d715c0bebafbf5c3eaf44b/1584465526130-VBL291FNUH859XB7NGJT/Coronavirus+Banner.png?format=1000w"
    ]

    for set1 in final:
        if set1["Date"] == today + "T00:00:00Z":
            temp.append(set1)

    for i in temp:
        if i["Province"] == province:
            embed = discord.Embed(title=i["Province"] + " Stats",
                                  color=0x552E12)
            embed.set_image(url=image_urls[random.randint(0, len(image_urls))])
            embed.add_field(name="Province", value=i["Province"], inline=True)
            embed.add_field(name="Confirmed",
                            value=i["Confirmed"],
                            inline=True)
            embed.add_field(name="Deaths", value=i["Deaths"], inline=True)
            embed.add_field(name="Recovered",
                            value=i["Recovered"],
                            inline=True)
            embed.add_field(name="Active", value=i["Active"], inline=True)
            await ctx.send(embed=embed)


# @client.command()
# async def casestotal(ctx, country="Canada"):
#   url = "https://api.covid19api.com/summary"

#   response = requests.get(url)
#   final = response.json()
#   for set1 in final["Countries"]:
#     if set1["Country"] == country:
#         await ctx.send(set1["TotalConfirmed"])

# @client.command()
# async def casestoday(ctx, country="Canada"):
#   url = "https://api.covid19api.com/summary"

#   response = requests.get(url)
#   final = response.json()
#   for set1 in final["Countries"]:
#     if set1["Country"] == country:
#         await ctx.send(set1["NewConfirmed"])

# @client.command()
# async def deathstotal(ctx, country="Canada"):
#   url = "https://api.covid19api.com/summary"

#   response = requests.get(url)
#   final = response.json()
#   for set1 in final["Countries"]:
#     if set1["Country"] == country:
#         await ctx.send(set1["TotalDeaths"])

# @client.command()
# async def deathstoday(ctx, country="Canada"):
#   url = "https://api.covid19api.com/summary"

#   response = requests.get(url)
#   final = response.json()
#   for set1 in final["Countries"]:
#     if set1["Country"] == country:
#         await ctx.send(set1["NewDeaths"])

# @client.command()
# async def recoverytoday(ctx, country="Canada"):
#   url = "https://api.covid19api.com/summary"

#   response = requests.get(url)
#   final = response.json()
#   for set1 in final["Countries"]:
#     if set1["Country"] == country:
#         await ctx.send(set1["NewRecovered"])

# @client.command()
# async def recoverytotal(ctx, country="Canada"):
#   url = "https://api.covid19api.com/summary"

#   response = requests.get(url)
#   final = response.json()
#   for set1 in final["Countries"]:
#     if set1["Country"] == country:
#         await ctx.send(set1["TotalRecovered"])


@client.command()
async def world(ctx):
    url = "https://api.covid19api.com/summary"

    response = requests.get(url)
    final = response.json()

    embed = discord.Embed(title="World Stats")
    embed.set_image(
        url=
        "https://www.bloomberg.com/graphics/2020-in-graphics/img/Coronavirus/Coronavirus4-fb.png"
    )

    embed.add_field(name="New Confirmed",
                    value=final["Global"]["NewConfirmed"],
                    inline=True)
    embed.add_field(name="Total Confirmed",
                    value=final["Global"]["TotalConfirmed"],
                    inline=True)
    embed.add_field(name="New Deaths",
                    value=final["Global"]["NewDeaths"],
                    inline=True)
    embed.add_field(name="Total Deaths",
                    value=final["Global"]["TotalDeaths"],
                    inline=True)
    await ctx.send(embed=embed)


@client.command()
async def news(ctx, topic="covid", country="ca", category="top"):

    url = "https://newsdata.io/api/1/news?apikey=" + os.getenv(
        "NEWSIO_KEY"
    ) + "&q=" + topic + "&country=" + country + "&category=" + category
    # print(url)

    response = requests.get(url)
    #print(response.status_code)

    data = response.json()

    link_arr = []

    # data = response.text
    for articles in data["results"]:
        link_arr.append(articles["link"])

    if len(link_arr) == 0:
        await ctx.send("No news found on this topic ;(")
    else:
        # dividing by two in order to try to get more relevent articles (not sure if actually does that)
        await ctx.send(link_arr[random.randint(0, len(link_arr) // 2 - 1)])


@client.command()
async def headlines(ctx, topic="covid", cnt=3, country="ca", category="top"):

    url = "https://newsdata.io/api/1/news?apikey=" + os.getenv(
        "NEWSIO_KEY"
    ) + "&q=" + topic + "&country=" + country + "&category=" + category
    # print(url)

    response = requests.get(url)
    #print(response.status_code)

    data = response.json()

    link_arr = []
    titles = []

    temp = 0
    for ind, articles in enumerate(data["results"]):
        cur_title = articles["title"]
        if temp == cnt:
            break
        if cur_title not in titles:
            temp += 1
            link_arr.append(articles)
            titles.append(cur_title)

    for i in range(cnt):
        embed = discord.Embed(title="News Headlines", color=0x552E12)
        img_url = link_arr[i]["image_url"]
        embed.add_field(name=link_arr[i]["title"],
                        value=link_arr[i]["link"],
                        inline=True)

        if img_url != None:
            embed.set_image(url=img_url)
        else:
            embed.set_image(
                url=
                "https://www.albertadoctors.org/images/ama-master/feature/Stock%20photos/News.jpg"
            )

        await ctx.send(embed=embed)


my_secret = os.environ['TOKEN']
client.run(my_secret)
