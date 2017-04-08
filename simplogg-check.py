#!/usr/bin/python
# -*- coding: utf8 -*-

__author__ = "Davyd Maker"
__version__ = "1.1"

import requests

headers = {
    'User-Agent': 'Googlebot'
}

try:
	r = requests.get('http://simplo.gg/dash/',headers=headers)
except Exception as e:
	print('This site is currently unavailable.')
	exit()

web = r.text

r = web.split('<tbody>')
r = r[1].strip()
r = r.split('</tbody>')
r = r[0].strip()

qtdJogos = r.count('<tr>')

i = 0
while i < qtdJogos:
	j = r.split('</tr>')
	j = j[i].split('</td>')
	jKleft = j[1].split('<td>')
	j = j[0].split('<td>')
	jKleft = jKleft[1].strip().replace('<center>','').replace('</center>',' ')
	if int(jKleft) < 1:
		i += 1
		continue
	j = j[1].strip().replace('Free Steam Key','')
	print(j + jKleft + 'keys left')
	i += 1
