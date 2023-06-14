console.log('bueno')

// let socket = io('http://127.0.0.1:1337/static/socket.io.js')
var socket = io();
socket.on('connect', function() {
	socket.emit('my event', {data: 'I\'m connected!'});
});
