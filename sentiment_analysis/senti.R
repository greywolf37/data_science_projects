# Load packages
library(dplyr)
library(tidytext)
library(tidyr)
library(stringr)
library(janeaustenr)
library(ggplot2)
library(reshape2)
library(wordcloud)

setwd("C:/Users/Rubin Thomas/Desktop/DS_projects/sentiment_analysis")

# "afinn" for values from -5 to 5
get_sentiments("bing")

# loading janes book
tidy <- austen_books() %>%
  group_by(book) %>%
  mutate(linenumber = row_number(), 
         chapter = cumsum(str_detect(text, regex("^chapter [\\divxlc]", ignore_case = TRUE)))) %>%
  ungroup() %>%
  unnest_tokens(word, text)

# Positive sentiments
positive_senti <- get_sentiments() %>%
  filter(sentiment == "positive")

# Get just positive sentiment words
Emma_positive <- tidy %>%
  filter(book == 'Emma') %>%
  semi_join(positive_senti) %>%
  count(word, sort = TRUE)

# Sentiments in book  Emma
bing <- get_sentiments("bing")

Emma_sentiment <- tidy %>% 
  inner_join(bing) %>%
  filter(book == "Emma") %>%
  count(book = "Emma", index = linenumber %/% 80, sentiment) %>%
  spread(sentiment, n, fill = 0) %>%
  mutate(sentiment = positive - negative)

# Plotting sentiment over the book
ggplot(Emma_sentiment, aes(index, sentiment), fill=book) +
  geom_bar(stat = "identity", show.legend = TRUE) +
  facet_wrap(~sentiment, ncol = 2, scales = 'free_x')

# Finding most sentimental words
counting_words <- tidy %>%
  inner_join(bing) %>%
  count(word, sentiment, sort = TRUE)

counting_words %>%
  filter(n > 150) %>%
  mutate(n = ifelse(sentiment == 'negative', -n, n)) %>%
  mutate(word = reorder(word, n)) %>%
  ggplot(aes(word, n, fill= sentiment)) +
  geom_col() +
  coord_flip() +
  labs(y = 'Sentiment Score')

# Crating a word cloud
tidy %>%
  inner_join(bing) %>% 
  count(word, sentiment) %>% 
  acast(word ~ sentiment, value.var = 'n', fill = 0) %>% 
  comparison.cloud(color = c("red", "dark green"), max.words = 100)
  

  

