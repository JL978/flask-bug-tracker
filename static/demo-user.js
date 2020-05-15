document.addEventListener('DOMContentLoaded', ()=>{

    const users = document.querySelector('#demo-users')
    // const content = document.querySelector('.form-conent')
    document.querySelector('#demo-button').onclick = function(){
        users.style.display = 'inherit';
        users.style.animationPlayState = 'running';
    //     // content.style.animationPlayState = 'running';
    //     form.addEventListener('animationend', function(){
    //         //form.style.animationPlayState = 'initial'
    //         content.style.display = 'hidden';
    //     })
    // }
})