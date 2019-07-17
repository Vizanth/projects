#Web Scraping
#Loading the rvest package
library(rvest)
#Specifying the url for desired website to be scraped
url <-"https://www.imdb.com/list/ls021077432/"
#Reading the HTML code from the website
wbp<-read_html(url)
print(wbp)
#Using CSS selectors to scrap the rankings section
ran_data_html<-html_nodes(wbp,'.text-primary')
rank<-html_node(wbp,".small")
rank
ran_data_html
#Converting the ranking data to text
r<-html_text(ran_data_html)


#Let's have a look at the rankings
#Data-Preprocessing: Converting rankings to numerical
r<-as.numeric(r)
#Let's have another look at the rankings
r
#Using CSS selectors to scrap the Movie genre section
gen<-html_nodes(wbp,'.genre')
gen
#Converting the genre data to text
gen_text<-html_text(gen)
gen_text
#Let's have a look at the runtime
run<-html_nodes(wbp,".runtime")
run

#Data-Preprocessing: removing \n
gen_text<-gsub(pattern = "\n",replacement = "",gen_text)
gen_text
#Data-Preprocessing: removing excess spaces
gen_text<-gsub(pattern = " ",replacement = "",gen_text)
gen_text
#taking only the first genre of each movie
gen_text<-gsub(pattern = ",.*",replacement = "",gen_text)

#Convering each genre from text to factor
gen_text<-as.factor(gen_text)
#Let's have another look at the genre data
run<-html_nodes(wbp,".runtime")
#Using CSS selectors to scrap the Movie runtime section

#Converting the runtime data to text
ry<-html_text(run)

#Let's have a look at the runtime
ry
#Data-Preprocessing: removing mins and converting it to numerical
ry<-gsub(pattern = "min",replacement = "",ry)
ry<-as.numeric(ry)
ry[15]=0
#Let's have another look at the runtime data

#Combining all the lists to form a data frame
#t<-as.list.data.frame(r,gen_text,ry)
t<-data.frame(SNO=r,Genre=gen_text,Runtime=ry)
head(t)
#Plot
library(ggplot2)
xy<-qplot(data=t,Runtime,fill=Genre,bins=30)
xy