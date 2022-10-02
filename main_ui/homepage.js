$(document).ready(function() {
    init();
});

function init(){
    $("#v-pills-tab .nav-link").unbind("click.selected-tab",tabClick)
    $("#v-pills-tab .nav-link").bind("click.selected-tab",tabClick)
};

function tabClick(this){
    console.info($(this).attr("aria-controls"))
}