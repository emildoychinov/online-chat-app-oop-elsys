const roomName = document.getElementById('username');
const roomMembers = document.getElementById('password');
const submit = document.getElementById('submit');
const user_id = localStorage.getItem('UUID');

if(!user_id){
    window.location.href = '/';
}

var socket = io();
	socket.on('connect', function() {
		socket.emit('my event', {data: 'I\'m connected!'});
	});

socket.emit('change_room', user_id);

submit.addEventListener('click', () =>{
    console.log('sex')
    var memberList = roomMembers.value.split(',');
    socket.emit('make_room', user_id, roomName.value, memberList);
});