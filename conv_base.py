# -*- coding: utf-8 -*-

if __name__ == '__main__':
	print('S: こんにちは！お名前とお電話番号を教えてください。')
	while True:
		# input from User
		sent = input('U: ')
		if sent == 'ありがとう' or sent == 'Thanks' or sent == 'Thank you' or sent == 'ありがと':
			print('S: どういたしまして')

