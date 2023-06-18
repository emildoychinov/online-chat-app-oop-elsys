window.onload = function(){
	console.log('bueno')
	const room_container = document.getElementById('room-container');
	const user_id = localStorage.getItem("UUID");
	const send_button = document.getElementById('sendBtn');
	const message = document.getElementById('message');
	const chatbox = document.getElementsByClassName('chat-box')[0];
	if(!user_id){
		window.location.href=('/auth')
	}
	// let socket = io('http://127.0.0.1:1337/static/socket.io.js')
	var socket = io();
	socket.on('connect', function() {
		socket.emit('my event', {data: 'I\'m connected!'});
	});

	socket.emit('change_room', user_id);
	socket.emit('get_rooms', user_id);
	socket.on('user_rooms', (rooms) => {
		console.log(rooms);
		for (var room of rooms){
			var obj = JSON.parse(room);
			var room_button = document.createElement('h4');
			room_button.id = obj.id;
			room_button.className = 'room';
			room_button.textContent = obj.name;
			room_button.addEventListener("click", (e) => {	
				chatbox.innerHTML="";
				localStorage.setItem('ROOM', e.target.id);
				socket.emit('change_room', e.target.id);
				socket.emit('get_messages', e.target.id);
			})
			room_container.appendChild(room_button);
		}
	})
	

	send_button.addEventListener("click", () =>{
		var chatroom = localStorage.getItem('ROOM');
		console.log(chatroom);
		socket.emit('send_message', user_id, chatroom, message.value);
	})

	socket.on('display_message', (message) =>{
		var newMessage = document.createElement('div');
		newMessage.innerHTML = message.username + ': ' + message.content;
		newMessage.className = (message.user_id == user_id) ? 'sent' : 'msg';
		chatbox.appendChild(newMessage);
	})
	socket.on('messages', (messages) => {
		if(messages != undefined){
			for (var message of messages){
				var obj = JSON.parse(message);
				var newMessage = document.createElement('div');
				newMessage.innerHTML = obj.user + ': ' + obj.content;
				newMessage.className = (obj.user_id == user_id) ? 'sent' : 'msg';
				chatbox.appendChild(newMessage);
			}
		}
	})
}