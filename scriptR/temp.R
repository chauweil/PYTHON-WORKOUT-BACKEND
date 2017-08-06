library(jsonlite)

# url with some information about project in Andalussia
url <- 'file.json'

# read url and convert to data.frame
document <- fromJSON(txt=url)
plot(document$x,document$y,type="l")
