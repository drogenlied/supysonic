# coding: utf-8

from flask import request
from web import app
from db import User

@app.route('/rest/getUser.view')
def user_info():
	username = request.args.get('username')
	if username is None:
		return request.error_formatter(10, 'Missing username')

	user = User.query.filter(User.name == username).first()
	if user is None:
		return request.error_formatter(0, 'Unknown user')

	return request.formatter({
		'user': {
			'username': user.name,
			'email': user.mail,
			'scrobblingEnabled': False,
			'adminRole': user.admin,
			'settingsRole': False,
			'downloadRole': False,
			'uploadRole': False,
			'playlistRole': False,
			'coverArtRole': False,
			'commentRole': False,
			'podcastRole': False,
			'streamRole': True,
			'jukeboxRole': False,
			'shareRole': False
		}
	})

