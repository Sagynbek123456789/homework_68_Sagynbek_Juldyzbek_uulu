function getCookie(name){
    let cookieValue = null;
    if (document.cookie && document.cookie !== ''){
        const cookies = document.cookie.split(';');
        for (let i =0; i<cookies.length; i++){
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length +1) ===(name + '=')){
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
                break
            }
        }
    }
    return cookieValue;
}



async function makeRequest(url, method= 'GET'){
    let headers = {};
    if (method !== "GET"){
        const csrftoken = getCookie('csrftoken');
        headers['X-CSRFToken'] = csrftoken
    }
    let response = await fetch(url, {method, headers});

    if (response.ok) {
        return await response.json();
    } else {
        let error = new Error (response.statusText);
        error.response = response;
        throw error;
    }
}

    async function onClick(e){
        e.preventDefault()
        let a = e.target;
        let url = a.href
        let method = 'POST';
        if (a.innerText === 'лайк'){
            a.innerText = 'анлайк';
            method = 'POST';
        }
        else {
            a.innerText = 'лайк';
            method = 'DELETE';
        }

        let response = await makeRequest(url, method);
        console.log(response);
        let span = document.getElementById(a.dataset['spanCountId']);
        span.innerText = response.count;
    }

    function onLoad(){
        let likes = document.getElementsByClassName('likes');
        for (let like of likes){
            like.addEventListener('click', onClick)
        }
    }
    window.addEventListener('load', onLoad);
