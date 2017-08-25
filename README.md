# annotatedDatasetBrazilianProtests
This page includes:
  One file with tweet IDs and the classification of the tweets as positive, negative or neutral.
    Each message was classified by 3 humans. Each human classification is in the file. Each line has the tweet ID, 
    the three human classification and a fifth and last column with an final classification. The last column presents the
    classification considering that: if two or more human agree with an classification, then the last column presents the class
    choosen by the majority; on the other side, if the three humans disagreed, then the message was considered neutral.

  The IDs enabling someone to retrieval the entirely tweet using the Twitter API. I have provided an script here if someone wishs.

  An Python script to retrieval of those messages using Twitter API.
    Install python 2.7.x on your computer (not tested with python 3.x).
    It will be necessary to include Twitter credentials. Use this link https://apps.twitter.com/ (be logged in).
    Include your credentials in the appropriate script location.
    Install mongoDB. It must be running during the script usage.
    You should especify the location where the data will be saved (database and collection).
    Take care to relate (link) the messages rightly with the classes defined to each of it.
