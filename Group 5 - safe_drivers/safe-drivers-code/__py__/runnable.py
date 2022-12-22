import weather_condition as wc

ci = wc.random_city()
response = wc.url(ci)

wc.__main__(ci,response)