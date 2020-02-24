# scrapy-projects

Get [Scrapy](https://github.com/scrapy/scrapy)
```
% pip install scrapy
```

Clone this repo
```
% git clone https://github.com/lesservehicle/scrapy-projects.git
```

Change to a project directory. This one is for scraping statistics for a popular mobile game.

```
% cd scrapy-projects/ayumilegends
```

Take a look at the available spiders in the project
```
% scrapy list
champs
```

Run a crawl using the available spider and output the results to a CSV, suppressing log output
```
% scrapyscrapy crawl --nolog -o champs.csv -t csv champs
```
