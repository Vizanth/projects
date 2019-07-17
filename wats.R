# Read and load text file in R

>library(readtext) #Load Required package >setwd("/Users/Desktop/RDirectory")

>TextData <- readtext("chat.txt")


>TextData <- as.data.frame(TextData)

# Remove punctuation, Numbers, special characters and other unwanted things and stem all the words.


>library(tm)


>mystopwords <- c("manish", "e18682","pm","am", "<", ">", stopwords("en")) #Define all the words which are not required

>CleanData <- tolower(TextData$text) #Turn the data into lower case

>CleanData <- removeWords(CleanData, mystopwords)


>CleanData <- removePunctuation(CleanData)


>CleanData <- removeNumbers(CleanData)

>CleanData <- stemmer(CleanData, rm.bracket = TRUE)

# Make a word-cloud with according to the frequency of the word used

>library(wordcloud)

>library(qdap)

>TextFrequency <- freq_terms(CleanData, at.least = 1)


>wordcloud(TextFrequency$WORD, TextFrequency$FREQ, colors = TextFrequency$FREQ, max.words = 200)


If we look at the wordcloud its clearly visible that hmm and okay are most frequently used words whereas hehe, babe, know and call are used repeatedly followed by other words based on their frequency of use.

# Sentiment Analysis 

>library(syuzhet)


>Sentiments <- get_nrc_sentiment(TextFrequency$WORD)


>Sentiments <- cbind("Words" = TextFrequency$WORD, Sentiments)


>SentimentsScore <- data.frame("Score" = colSums(Sentiments[2:11]))


>TotalSentiments <- cbind("Sentiments" = rownames(SentimentsScore), SentimentsScore)

>rownames(TotalSentiments) <- NULL

# Visualisation of the sentiments extracted from the texts

>library(ggplot2)


>ggplot(data = TotalSentiments, aes(x = Sentiments, y = Score)) + geom_bar(stat = "identity", aes(fill = Sentiments))



