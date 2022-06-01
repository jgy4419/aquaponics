<template>
    <div id="container">
        <video autoplay="true" id="videoElement">
    
        </video>
    </div>
</template>

<script>
export default {
    mounted(){
        var video = document.querySelector("#videoElement");
 
if (navigator.mediaDevices.getUserMedia) {
  navigator.mediaDevices.getUserMedia({ video: true })
    .then(function (stream) {
      video.srcObject = stream;
    })
    .catch(function (err0r) {
      console.log("Something went wrong!", err0r);
    });
}
    } 
}
</script>
<style lang="scss" scoped>
#container {
    margin: 0px auto;
    width: 100vw;
    height: 50vh;
    #videoElement {
        border-radius: 20px;
        border: 5px solid rgb(232, 232, 232);
        width: 500px;
        height: 375px;
        background-color: #666;
    }
}
</style>