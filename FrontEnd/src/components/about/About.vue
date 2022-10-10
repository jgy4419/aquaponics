<template>
    <div class="contain">
        <Section1/>
        <Section2/>
    </div>
</template>

<script>
import Section1 from './AboutSection1.vue';
import Section2 from './AboutSection2.vue';
export default {
    components: {
        Section1,
        Section2,
    }
}
</script>