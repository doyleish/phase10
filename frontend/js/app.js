$(document).ready(function(){
    window.ac = -1
})

function new_game(){
    $.getJSON("/p10/api/new_game", function(data){
        window.game_id = data["return"]
        join_game(data["return"]);
    });
}

function join_game(game_id){
    $("#landing").css("display", "none");
    $("#game").css("display", "block");
    if (typeof game_id === "undefined"){
        game_id = $("#game_id").val();
    }
    $.getJSON("/p10/api/game_info/"+game_id, function(data){
        $('#game_title').text(data['title']);
        $('#ac').val(0);
    })
    setInterval(listener_loop, 3000);
}

function listener_loop() {
    console.log(window.ac);
    $.getJSON("/p10/api/ac/"+window.game_id, function(data){
        if(data["return"] > window.ac){
            console.log("full update here");
            window.ac = data["return"];
            full_update();
        }
    })
}

function full_update(){
    console.log("full update");
}
