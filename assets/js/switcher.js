// Selecting all the required classes from HTML to change 
var body = document.body
var check = document.querySelector('#check')
var box = document.querySelector('.box')
var ball = document.querySelector('.ball')

// Adding an eventListener function to change color everytime var check is changed.(checked & unchecked)

check.addEventListener('change',function(){

  //   conditions to apply when checkbox is checked

  if(this.checked == true){
    box.setAttribute('style','background-color:white;')
    ball.setAttribute('style','transform:translatex(100%);')
    body.setAttribute('style','background-color:black; color:white;') 


  }

  //   conditions to apply when checkbox is unchecked

  if(this.checked == false){
    box.setAttribute('style','background-color:black; color:white;')
    ball.setAttribute('style','transform:translatex(0%);')
    body.setAttribute('style','background-color:white; color:black;')



  }
})
