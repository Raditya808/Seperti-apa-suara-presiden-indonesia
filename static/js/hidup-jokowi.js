
// for audio 
let music = document.getElementById('audio');

// for prabowo face 
let iconleader = document.getElementById('prabowo-image')

// menggunakan syntax play
// prabowo sound
function klik(){
  
        if(music.paused){
          music.play()
          iconleader.src = 'static/src/hidup-jokowi-sound/prabowo-face/2.png'
         
        }else{
          music.pause()
        }
    
}
