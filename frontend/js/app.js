
function new_game(){
    $.getJSON("/p10/api/new_game", function(data){
        console.log(data['return']);
        
    })
}

function join_game(){
    $("#landing").css("display", "none");
    $("#game").css("display", "block");
}
