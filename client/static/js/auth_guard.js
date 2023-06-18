const submit = document.getElementById('submit');
const username = document.getElementById('username');
const password = document.getElementById('password');
const auth_form = document.getElementsByClassName('auth-content')[0]
var socket = io();
socket.on('connect', function() {
	socket.emit('my event', {data: 'I\'m connected!'});
});

submit.addEventListener('click',()=>{
    if(username.value.length < 4 || password.value.length < 4){
        alert('The provided username / password needs to 4 or more characters');
        auth_form.reset();
        return;
    }
    //console.log("test");
    if(MODE == 'SIGN_IN'){
        socket.emit('login', username.value, password.value);
        socket.on('login_res', (res)=>{
            console.log(res);
            if(res.result == 'true'){
                localStorage.setItem("UUID", res.id)
                window.location.href = '/'
            }else{
                alert('Login failed');
                auth_form.reset();
                return;
            }
        })
    }
    else{
        const confirm_password = document.getElementById('confirm-password');
        if(confirm_password.value.length < 4){
            alert('Password missmatch');
            auth_form.reset();
            return;
        }
        socket.emit('register', username.value, password.value, confirm_password.value)
        socket.on('register_res', (res)=>{
            if(res.result == 'true'){
                window.location.href = '/auth?mode=SIGN_IN'
            }else{
                alert('Register failed');
                auth_form.reset();
                return;
            }
        })
    }
})