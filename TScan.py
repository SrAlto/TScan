#!/usr/bin/python
import socket
import requests
import re
import os
from time import sleep

print ("""
=======================
=    TSCAN V. 0.6     =
=======================

#> Robots/Sitemap.
#> Vulns SqlInjection GET/POST.
#> Proucura de arquivos maliciosos (SHELL).
#> Scanner WP/Joomla.
#> Admin Finder.
#> SqliBypass Test (Desenvolvimento...)

#> OBS: UM SCAN COMPLETO PODE DURAR 20 MINUTOS, POIS TEMOS MAIS DE 10.000 DIRETORIOS PARA TESTE.
#> EM BREVE MAIS VELOCIDADE NO SCAN.
""")

print("Coloque a barra logo ao final do site (www.site.com/)")
sitet = raw_input("Digite o site que sera verificado: ")
 
      
print ("==============================================================================")

print("Procurando robots.txt/sitemap.xml...")
print(" ")
robot = open('robot/wordlist.txt').readlines()
for linharobot in robot:
        respostarobot = requests.get(sitet+linharobot)
        codigorobot = respostarobot.status_code
        if codigorobot == 200:
           print sitet+linharobot
           sv = open('robot/subs.txt','a')
           sv.write(sitet+linharobot)
           sv.close()
print ("==============================================================================")
print ("Buscando urls com paramentros id=")

arquivosqli = open('sqli/wordlist.txt','r').readlines()
for linhaSqli in arquivosqli:
    retornoSqli = requests.get(sitet+linhaSqli).status_code
    respostaSqli = requests.get(sitet+linhaSqli+"'").text
    if retornoSqli == 200:
       if 'mysql_fetch_array()' in respostaSqli or 'You have an error in your SQL syntax' in respostaSqli or 'argument is not a valid' in respostaSqli or 'Fatal error' in respostaSqli:
           print("Url Vuln: "+sitet+linhaSqli)
           sva = open ('sqli/vuln.txt','a')
           sva.write(sitet+linhaSqli)
           sva.close() 
       else:
           print("Url sem vuln: "+sitet+linhaSqli)
           sva = open ('sqli/semvuln.txt','a')
           sva.write(sitet+linhaSqli)
           sva.close() 
print ("==============================================================================")
print (" ")
print ("Buscando falhas de Sqli Post")
arquivopost = open('sqli/wordlistp.txt','r').readlines()
for linhaPost in arquivopost:
    retornoPost = requests.get(sitet+linhaPost).status_code
    respostaPost = requests.get(sitet+linhaPost).text
    if retornoPost == 200:
       if 'mysql_fetch_array()' in respostaPost or 'You have an error in your SQL syntax' in respostaPost or 'Fatal Error' in respostaPost:
           print("Url Vuln: "+sitet+linhaPost)
           sve = open ('sqli/vulnpost.txt','a')
           sve.write(sitet+linhaPost)
           sve.close() 
       else:
           print("Url sem vuln: "+sitet+linhaPost)
           sve = open ('sqli/semvulnpost.txt','a')
           sve.write(sitet+linhaPost)
           sve.close() 
print ("==============================================================================")


print ("Vamos achar Plugins instalados Wordpress/Joomla... ")
print("Testado Wordpress...")
arquivowp = open('plugins/wordpress/wordpress.txt','r')
linhaswp = arquivowp.readlines()
for linhawp in linhaswp:
        respostawp = requests.get(sitet+linhawp)
        codigowp = respostawp.status_code
        if codigowp == 200:
            sv = open('plugins/wordpress/output.txt','a')
            sv.write(sitet+linhawp)
            print (sitet+linhawp)

print ("==============================================================================")       
print("Buscando shell upada nesse site...")
print(" ")
sleep(2)
print("Isso pode demorar uns 2 a 4 minutos")
arquivoshel = open('shell/wordlist.txt','r')
linhasshel= arquivoshel.readlines()
for linhashel in linhasshel:
        respostashel = requests.get(sitet+linhashel)
        codigoshel = respostashel.status_code
        if codigoshel == 200:
           svi = open('shell/shell.txt','a')
           print sitet+linhashel
print ("==============================================================================")
print (" ")
sleep(2)

print ("==============================================================================")
print ("Vamos achar o painel administrador... ")
print("Verificando 5.500 diretorios isso pode demorar... Aguarde.")
arquivo = open('dir/wordlist.txt','r')
linhas = arquivo.readlines()
for linha in linhas:
        resposta = requests.get(sitet+linha)
        codigo = resposta.status_code
        if codigo == 200:
            sv = open('dir/painel.txt','a')
            sv.write(sitet+linha)
            print (sitet+linha)
       
print(" ")
print ("==============================================================================")
print ("Caso nao tenha aparecido nenhum link acima possa ser que nao ha painel de adm.")
print ("==============================================================================")
sleep(2)

##print(" ")
#print ("O nosso SCAN achou o painel correto para o painel administrativo? Se sim [S], se nao[N]")
#sn = input("#>")
#if sn == S or s:
#    print ("Legal, vamos fazer teste de SqliBypass nesse painel...")
#    arquivobypass = open('dir/painel.txt', 'a')
#    linhas

       
print("FIM! TODOS OS RELATORIOS VOCE PODE ENCONTRAR NO ARQUIVO CHAMADO (output.txt)")
