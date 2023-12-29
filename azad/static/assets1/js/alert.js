close_alert=document.getElementById("icon");
alert = document.getElementById("alert");
close_alert.addEventListener("click", ()=>{
    
    alert.style.display="none";
})
setTimeout(()=>{
    alert.style.display='none';
}, 5000);
