$(document).ready(function(){
    window.ac = -1;
})

function new_game(){
    $.getJSON("/p10/api/new_game", function(data){
        window.game_id = data["return"];
        join_game(data["return"]);
    });
}

function join_game(game_id){
    $("#landing").css("display", "none");
    $("#game").css("display", "block");
    if (typeof game_id === "undefined"){
        window.game_id = $("#game_id").val();
        game_id = $("#game_id").val();
    }
    $.getJSON("/p10/api/join/"+game_id, function(data){
        window.player_id = data["return"];
    });
    $.getJSON("/p10/api/game_info/"+game_id, function(data){
        $('#game_title').text(data['title']);
        $('#ac').val(0);
    })
    window.hand = [];
    setInterval(listener_loop, 3000);
}

function listener_loop() {
    console.log(window.ac);
    $.getJSON("/p10/api/ac/"+window.game_id, function(data){
        if(data["return"] > window.ac){
            window.ac = data["return"];
            full_update();
        }
    })
}

function full_update(){
    update_hand();
    console.log("full update");
}

function update_hand(){
    $.getJSON("/p10/api/hand/" + window.game_id + "/" + window.player_id, function(data){
        console.log("hand update");
        $("#handblock").html("");
        $("#handblock").text("");
        for(var card in data["return"]){
            var ct = Handlebars.compile($("#card_template").html());
            $("#handblock").html($("#handblock").html()+ct(data["return"][card]));
        }
    });
}






