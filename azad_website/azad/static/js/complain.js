let complains = document.querySelectorAll(".complain");
complains.forEach((complain)=>{
    if(complain.innerHTML.length>70){
        complain.innerHTML = (complain.innerHTML.substring(0, 50)+" ... "+complain.innerHTML.substring(complain.innerHTML.length-1, complain.innerHTML.length-40));
    }
    
})