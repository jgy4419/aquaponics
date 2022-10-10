export function scrollTop(element) {
    console.log(element);
    const mainDiv = document.querySelector(`.${element}`);
    mainDiv.scrollTop = 0;
}