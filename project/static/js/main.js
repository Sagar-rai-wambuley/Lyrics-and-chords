    var mid_column = document.querySelector('.mid_column');
    var mid_column_header = document.querySelector('.mid_column_header');
    var mid_column_body = document.querySelector('.mid_column_body');
    var sagar_content = document.querySelector('#sagar_content')



    function startScroll() {
        setInterval(function () {
            window.scrollBy({ top: .5, behavior: "smooth" })
        }, 90);


    function startScrolltwoTimes() {
        setInterval(function () {
            window.scrollBy({ top: 1, behavior: "smooth" })
        }, 55);
        }
    document.querySelector('.scroll_sticky_predefined').addEventListener("click", function () {
        startScrolltwoTimes();
        })
    }

    function startScrolling() {
        setTimeout(startScroll, 7000);
        document.querySelector('header').style.display = "None"
        document.querySelector('.right_column').style.display = "None"
        document.querySelector('#scroll').classList.add('scroll_sticky_predefined')
        document.querySelector('#stop').classList.add('stop_sticky_predefined')
        document.querySelector('.lyrics_header').style.display = "None"
        document.querySelector('.content_hr').style.display = "None"
        document.querySelector('#scroll').innerHTML = "2x"
        document.querySelector('.about').style.display = "None"
        document.querySelector('.small_thumnail_name').style.display = "None"
        document.querySelector('.small_thumnail_subname').style.display = "None"
        document.querySelector('.toptitle').style.display = "None"
        document.querySelector('#small_thumnail_image').style.cssText = "display:none;"
        document.querySelector('#large_thumnail_image').style.display = "None"
        scroll_sticky_predefined.style.display = "None"

}
document.querySelector('.search_bar').addEventListener("click", function () {
    document.querySelector('.body').classList.add('.search_page');    
})





 
