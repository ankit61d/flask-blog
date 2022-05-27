

function like(post_id, like_state){
    
    const likeButton = document.getElementById('like-button');
    console.log(likeButton)
    var myRequest = new XMLHttpRequest();

    myRequest.open('POST','http://127.0.0.1:5000/post/' + post_id + '/like');

    myRequest.onload = function(){
        console.log('my request loaded')
        if (like_state){
            console.log("true state, changing to like")
            likeButton.classList.remove("focus");
            likeButton.classList.remove("active");
            likeButton.setAttribute('aria-pressed', 'false');
            likeButton.setAttribute('value', 'Like');
            likeButton.setAttribute('onclick', "like("+ post_id +", false)");
        }else{
            console.log("false , now changing to Liked")
            likeButton.classList.add("focus");
            likeButton.classList.add("active");
            likeButton.setAttribute('aria-pressed','true');
            likeButton.setAttribute('value', 'Liked');
            likeButton.setAttribute('onclick', "like("+ post_id +", true)");
        }

    };

myRequest.send();
}