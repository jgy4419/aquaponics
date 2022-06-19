<template>
    <div>
        <Section1/>
        <Section2/>
        <Section3/>
    </div>
</template>

<script>
import Section1 from './MainSection1';
import Section2 from './MainSection2';
import Section3 from './MainSection3';
export default {
    components: {
        Section1,
        Section2,
        Section3
    },
    mounted(){
        setTimeout(() => {
            let mainText = document.querySelector('.mainText');
            let mainImg = document.querySelector(".mainImg");   
            mainText.classList.add('event');
            mainImg.classList.add("event");
        }, 300);
        
        let screenHeight = document.documentElement.scrollHeight;
        let contentBox = document.querySelector('.contentBox');
        let contentBox2 = document.querySelector('.contentBox2');

        document.addEventListener('scroll', function(){
            let currentScrollValue = document.documentElement.scrollTop;
            if(currentScrollValue > screenHeight / 1.5){
                contentBox2.classList.add('event');
            }else if(currentScrollValue > screenHeight / 5){
                contentBox.classList.add('event');
            }else{
                contentBox.classList.remove('event');
                contentBox2.classList.remove('event');
            }
        })
    }
}
</script>