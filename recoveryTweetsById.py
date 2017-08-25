# -*- coding: utf-8 -*-
import re
import urllib2
import oauth2 as oauth
import pymongo
import json
import time
import codecs
import sys

'''
    @author
        Tiago Cruz de França
    @since
        12-23-2015
    @version 
        1.0.0
    @see
        https://github.com/tcruzfranca/annotatedDatasetBrazilianProtests
        This is a specific version made for turn easy the retrival of tweets from the Brazilian protests Golden Dataset.
        For a more generic version for retrival of tweets by id, access https://github.com/tcruzfranca/scripts.

    License (BSD 2): Available in https://github.com/tcruzfranca/annotatedDatasetBrazilianProtests/blob/master/LICENSE.txt.
    
    description 
                This code is useful for retrieval tweets usin list of tweet's IDs. Such list must be a file in which each ID is in a different line.
                In the end of this file you can see the main function and the instructions for set correctly the configurations needed.
    
    Please access the git address and cite at least one: our paper or the git account if we want use this script.
'''
def logError(log, msg):
    log.write(msg+"\n")

'''
Save files. Just a utility function.
'''
def salvarArquivo(data, destino, log):
    #for registro in data:
    #print "escreveu no arquivo"
    data = json.loads(data)
    #print data
    for registro in data:
        try:
            #print "vaiEscreverNoArquivo"
            destino.write(json.dumps(registro)+"\n")
            #print "Escreveu"
            #destino.flush()
            #print "flush"
        except:
            msg = "Ao Salvar o Arquivo"
            logError(log, msg)
            print "Unexpected error:" + str(sys.exc_info()[0])
            
'''
    This function just receive a list of tweet IDs and send a requisition with the list of desired IDs.
'''
def pegarTweets(ids, destino, log):

    listaIds = ""
    URL = "https://api.twitter.com/1.1/statuses/lookup.json?id="
    for j in ids:
        listaIds += str(j)+","

    listaIds = listaIds[:-1]#remover ultima virgula
    URL += listaIds
    #print "vaiEnviarReqisição"
    response,data = client.request(URL,"GET")

    #print "enviouRequisiçãoVaiSalvar"
    salvarArquivo(data, destino,log)
    #print "Salvou"


'''
    Sets lists containing 100 tweets IDs for the requisition. The end list could be less than 100 IDs.
'''
def coletarTweetsAntigos(arqIDs, destino, log):
    ids = []

    for i in arqIDs:
        #i = i.replace("\n","")
        #i = i.replace("\r","")
        i = re.sub("[^0-9]","",i)


        ids.append(i)
        
            #URL = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=tcruzfranca&count=1"
        if len(ids) == 100:
            try:
                print "pegaTweets"
                pegarTweets(ids,destino,log)
                print "depoisPegarTweets"
                time.sleep(5)                        
            except:
                msg = "Erro ao coletar."                
                logErro(log,msg)
                print "Unexpected error:"+ str(sys.exc_info()[0])
                print "dormiu"
                time.sleep(60*15)
                pegarTweets(ids,destino,log)
            finally:
                ids = []

    else:
        pegarTweets(ids,destino, log)



if __name__ == "__main__":

    '''
        1.You must create Twitter oauth2 credentials. Those credentials are linked to your accont. So, you need to be logged.
          link for Twitter credentials: https://apps.twitter.com/
        2.Set the file of IDs
        3.Set the destination file where your tweets will be saved. Keep in mind, each tweet are a json representation.
        4.If you want, rename the log file.        
    '''

    #1. Coppy your respective credentials here.
    Consumer_key = "your consumer key"
    Consumer_secret = "your consumer secret"
    Access_token = "your access token"
    Access_token_secret = "your acess token secret"


    consumer = oauth.Consumer(key=Consumer_key, secret=Consumer_secret)
    access_token = oauth.Token(key=Access_token, secret=Access_token_secret)
    client = oauth.Client(consumer, access_token)

    #2. Set the file of IDs
    arq = open("GoldStandardDataSet.csv")
    #3. Set the destination File
    destino = codecs.open("destinationFile.json",'w',"utf-8")
    log = open("log.txt","a")
    coletarTweetsAntigos(arq, destino,log)

    arq.close()
    destino.close()
    log.close()
