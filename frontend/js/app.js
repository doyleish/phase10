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
    $.getJSON("/p10/api/join/"+window.game_id, function(data){
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
    update_game_info();
    update_players();
    update_hand();
}

function update_game_info(){
    console.log("game info update");
    $.getJSON("/p10/api/game_info/" + window.game_id, function(data){
        window.turn = data['turn'];
        window.round = data['round'];
        window.dealer = data['dealer'];
        window.title = data['title'];
    });
}


function update_players(){
    $.getJSON("/p10/api/players/" + window.game_id, function(data){
        console.log("player update");
        $("#playerbar").html("");
        $("#playerbar").text("");
        window.players = 0;
        for(var pl in data["return"]){
            window.players += 1;
            var ct = Handlebars.compile($("#player_template").html());
            $("#playerbar").html($("#playerbar").html()+ct(data["return"][pl]));
        }
        $("#player"+window.player_id).css("font-weight","bold");
        $("[id^=dealer]").css("display","none");
        $("#dealer"+window.dealer).css("display","inline-block");
    });
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

function deal_round(){
    if(window.dealer == window.player_id){
        $.getJSON("/p10/api/deal/" + window.game_id, function(data){
            console.log("deal");
        });
    }
}

